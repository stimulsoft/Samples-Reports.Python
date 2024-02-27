from datetime import datetime
from flask import Flask, request, url_for
from stimulsoft_reports.events import StiVariablesEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

def prepareVariables(args: StiVariablesEventArgs):
    if len(args.variables) > 0:
        args.variables['Name'].value = 'Maria'
        args.variables['Surname'].value = 'Anders'
        args.variables['Email'].value = 'm.anders@stimulsoft.com'
        args.variables['Address'].value = 'Obere Str. 57, Berlin'
        args.variables['Sex'].value = False
        args.variables['BirthDay'].value = datetime(1982, 3, 20, 0, 0, 0)

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onPrepareVariables += prepareVariables

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)