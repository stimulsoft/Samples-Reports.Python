from flask import Blueprint, request, url_for
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer
import os

Opening_the_Report_in_the_Viewer_and_Changing_it_on_the_Server_Side = app = Blueprint('Opening_the_Report_in_the_Viewer_and_Changing_it_on_the_Server_Side', __name__)


# The function will be called after the report is opened before it is assigned to the viewer
def openedReport(args: StiReportEventArgs):

    # You can change any fields of the report object passed in the args
    args.report['ReportAlias'] = 'Report Alias from Server-Side'

    # Or you can upload a new one
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename = 'reports/SimpleList.mrt'))
    with open(filePath, mode='r', encoding='utf-8') as file:
        args.report = file.read()
        file.close()


@app.route('/Opening_the_Report_in_the_Viewer_and_Changing_it_on_the_Server_Side', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()
    viewer.javascript.appendHead('<link rel="shortcut icon" href="' + url_for('static', filename = 'favicon.ico') + '" type="image/x-icon">')

    # Defining viewer events
    # When assigning a function name as a string, it will be called on the JavaScript client side
    # When assigning a function itself, it will be called on the Python server side
    viewer.onOpenedReport += openedReport

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
