from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer, enums

Changing_the_Viewer_Theme = app = Blueprint('Changing_the_Viewer_Theme', __name__)

@app.route('/Changing_the_Viewer_Theme', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.options.appearance.backgroundColor = 'black'
    viewer.options.appearance.theme = enums.StiViewerTheme.OFFICE_2022_BLACK_GREEN
    viewer.options.toolbar.displayMode = enums.StiToolbarDisplayMode.SEPARATED

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()
