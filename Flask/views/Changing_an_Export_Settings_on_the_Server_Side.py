from flask import Blueprint, request, url_for
from stimulsoft_reports.events import StiExportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat
from stimulsoft_reports.viewer import StiViewer
import datetime

Changing_an_Export_Settings_on_the_Server_Side = app = Blueprint('Changing_an_Export_Settings_on_the_Server_Side', __name__)


# The function will be called before exporting the report
def beginExportReport(args: StiExportEventArgs):

    # You can change the file name of the exported report
    args.fileName = 'MyExportedFileName.' + args.fileExtension

    # You can change export settings, the set of settings depends on the export type
    if args.format == StiExportFormat.PDF:
        args.settings['creatorString'] = 'My Company Name (c) YEAR'
        args.settings['allowEditable'] = False


@app.route('/Changing_an_Export_Settings_on_the_Server_Side', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object and defining Python events
    viewer = StiViewer()
    viewer.onBeginExportReport += beginExportReport

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
