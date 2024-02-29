from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Registering_a_Data_from_Code = app = Blueprint('Registering_a_Data_from_Code', __name__)

@app.route('/Registering_a_Data_from_Code', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onBeginProcessData += 'beginProcessData'

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render_template('Registering_a_Data_from_Code.html', viewerJavaScript = js, viewerHtml = html)
