import json
import os
from flask import Flask, request, render_template, url_for
from stimulsoft_reports import StiResult
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer
from stimulsoft_reports.viewer.enums import StiToolbarDisplayMode
from stimulsoft_reports.designer import StiDesigner

app = Flask(__name__)

def saveReport(args: StiReportEventArgs):
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename = 'reports/' + args.fileName))
    try:
        with open(filePath, mode='w', encoding='utf-8') as file:
            jsonReport = json.dumps(args.report, indent = 4)
            file.write(jsonReport)
            file.close()
    except Exception as e:
        return StiResult.getError(str(e))

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onDesignReport += 'viewerDesign'
    viewer.options.appearance.fullScreenMode = True
    viewer.options.toolbar.showDesignButton = True
    viewer.options.toolbar.displayMode = StiToolbarDisplayMode.SEPARATED

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render_template('Working with onDesign and onExit events.html', componentJavaScript = js, componentHtml = html)

@app.route('/designer', methods = ['GET', 'POST'])
def designer():
    designer = StiDesigner()
    designer.onExit += 'designerExit'
    designer.onSaveReport += saveReport
    designer.options.appearance.fullScreenMode = True
    designer.options.toolbar.showFileMenuExit = True

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    designer.report = report

    js = designer.javascript.getHtml()
    html = designer.getHtml()

    return render_template('Working with onDesign and onExit events.html', componentJavaScript = js, componentHtml = html)

if __name__ == '__main__':
    app.run(debug=True, port=8040)