from flask import Flask, request, render_template, url_for
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)
mainHandler = StiHandler('/handler')

@app.route('/')
def index():
    viewer = StiViewer()
    viewer.handler = mainHandler
    viewer.options.appearance.fullScreenMode = True

    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render_template('Using a Handler in a Separate Function.html', viewerJavaScript = js, viewerHtml = html)

@app.route('/handler', methods = ['GET', 'POST'])
def handler():
    mainHandler.processRequest(request)
    return mainHandler.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)