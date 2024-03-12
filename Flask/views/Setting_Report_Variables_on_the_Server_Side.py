from datetime import datetime
from flask import Blueprint, request, url_for
from stimulsoft_reports.events import StiVariablesEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Setting_Report_Variables_on_the_Server_Side = app = Blueprint('Setting_Report_Variables_on_the_Server_Side', __name__)


# The function will be called before building the report when preparing the values of variables
def prepareVariables(args: StiVariablesEventArgs):

    # You can set the values of the report variables, the value types must match the original types
    # If the variable contained an expression, the already calculated value will be passed
    if len(args.variables) > 0:
        args.variables['Name'].value = 'Maria'
        args.variables['Surname'].value = 'Anders'
        args.variables['Email'].value = 'm.anders@stimulsoft.com'
        args.variables['Address'].value = 'Obere Str. 57, Berlin'
        args.variables['Sex'].value = False
        args.variables['BirthDay'].value = datetime(1982, 3, 20, 0, 0, 0)


@app.route('/Setting_Report_Variables_on_the_Server_Side', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()

    # Defining viewer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    viewer.onPrepareVariables += prepareVariables

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleVariables.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
