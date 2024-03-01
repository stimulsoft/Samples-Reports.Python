from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Showing_a_Report_in_the_Viewer = app = Blueprint('Showing_a_Report_in_the_Viewer', __name__)


@app.route('/Showing_a_Report_in_the_Viewer', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object
    viewer = StiViewer()

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
