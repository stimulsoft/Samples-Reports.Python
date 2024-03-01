from flask import Blueprint, request, url_for
from stimulsoft_reports.events import StiDataEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Using_Parameters_in_SQL_Query = app = Blueprint('Using_Parameters_in_SQL_Query', __name__)


# The function will be called before requesting data from the database
def beginProcessData(args: StiDataEventArgs):
    
    # Here you can check any connection, data source and query parameters and change them
    # Any changes will not be sent to the client side
    if args.dataSource == 'customers' and len(args.parameters) > 0:
        args.parameters['Country'].value = 'Germany'


@app.route('/Using_Parameters_in_SQL_Query', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object and defining Python events
    viewer = StiViewer()
    viewer.onBeginProcessData += beginProcessData

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object and loading a report by URL
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleListSQLParameters.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
