from flask import Flask, request, url_for
from stimulsoft_reports.events import StiExportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

def beginExportReport(args: StiExportEventArgs):
    args.fileName = 'MyExportedFileName.' + args.fileExtension

    if args.format == StiExportFormat.PDF:
        args.settings['creatorString'] = 'My Company Name (c) YEAR'
        args.settings['allowEditable'] = False

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onBeginExportReport += beginExportReport

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)