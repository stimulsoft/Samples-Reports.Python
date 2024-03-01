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
    # Creating a viewer object and defining Python events
    viewer = StiViewer()
    viewer.onOpenedReport += openedReport

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # Creating a report object and loading a report by URL
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
