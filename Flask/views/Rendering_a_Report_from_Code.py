from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport

Rendering_a_Report_from_Code = app = Blueprint('Rendering_a_Report_from_Code', __name__)

@app.route('/Rendering_a_Report_from_Code', methods = ['GET', 'POST'])
def index():
    report = StiReport()
    report.onAfterRender += 'afterRender'

    if report.processRequest(request):
        return report.getFrameworkResponse()
    
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    js = report.javascript.getHtml()
    html = report.getHtml()

    return render_template('Rendering_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
