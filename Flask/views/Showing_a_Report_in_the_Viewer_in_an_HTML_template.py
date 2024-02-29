from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Showing_a_Report_in_the_Viewer_in_an_HTML_template = app = Blueprint('Showing_a_Report_in_the_Viewer_in_an_HTML_template', __name__)

@app.route('/Showing_a_Report_in_the_Viewer_in_an_HTML_template', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.options.appearance.scrollbarsMode = True
    viewer.options.width = '1000px'
    viewer.options.height = '600px'

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render_template('Showing_a_Report_in_the_Viewer_in_an_HTML_template.html', viewerJavaScript = js, viewerHtml = html)
