from flask import Flask, request, url_for
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer
import os

app = Flask(__name__)

def openedReport(args: StiReportEventArgs):
    # You can change any fields of the report object passed in the args
    args.report['ReportAlias'] = 'Report Alias from Server-Side'

    # Or you can upload a new one
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename = 'reports/SimpleList.mrt'))
    with open(filePath, mode='r', encoding='utf-8') as file:
        args.report = file.read()
        file.close()


@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onOpenedReport += openedReport

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)