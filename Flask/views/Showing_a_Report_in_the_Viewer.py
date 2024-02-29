from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Showing_a_Report_in_the_Viewer = app = Blueprint('Showing_a_Report_in_the_Viewer', __name__)

@app.route('/Showing_a_Report_in_the_Viewer', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()
