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
    # Creating a viewer object
    viewer = StiViewer()

    # Defining viewer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    viewer.onBeginProcessData += beginProcessData

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleListSQLParameters.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
