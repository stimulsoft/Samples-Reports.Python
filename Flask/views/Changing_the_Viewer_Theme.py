from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer, enums

Changing_the_Viewer_Theme = app = Blueprint('Changing_the_Viewer_Theme', __name__)


@app.route('/Changing_the_Viewer_Theme', methods = ['GET', 'POST'])
def index():
    # Creating a viewer object and defining options (setting the theme, background color, toolbar mode)
    viewer = StiViewer()
    viewer.options.appearance.theme = enums.StiViewerTheme.OFFICE_2022_BLACK_GREEN
    viewer.options.appearance.backgroundColor = 'black'
    viewer.options.toolbar.displayMode = enums.StiToolbarDisplayMode.SEPARATED

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
