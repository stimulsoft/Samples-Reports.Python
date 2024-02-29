from flask import Blueprint, request, url_for
from stimulsoft_reports.events import StiDataEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Using_Parameters_in_SQL_Query = app = Blueprint('Using_Parameters_in_SQL_Query', __name__)

def beginProcessData(args: StiDataEventArgs):
    if args.dataSource == 'customers' and len(args.parameters) > 0:
        args.parameters['Country'].value = 'Germany'

@app.route('/Using_Parameters_in_SQL_Query', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onBeginProcessData += beginProcessData

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleListSQLParameters.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()
