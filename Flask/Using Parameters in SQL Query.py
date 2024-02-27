from flask import Flask, request, url_for
from stimulsoft_reports.events import StiDataEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

def beginProcessData(args: StiDataEventArgs):
    if args.dataSource == 'customers' and len(args.parameters) > 0:
        args.parameters['Country'].value = 'Germany'

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onBeginProcessData += beginProcessData

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleListSQLParameters.mrt'))
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)