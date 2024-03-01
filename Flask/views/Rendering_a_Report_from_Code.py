from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport

Rendering_a_Report_from_Code = app = Blueprint('Rendering_a_Report_from_Code', __name__)


@app.route('/Rendering_a_Report_from_Code', methods = ['GET', 'POST'])
def index():
    # Creating a report object and defining JavaScript events
    report = StiReport()
    report.onAfterRender += 'afterRender'

    # If the request processing was successful, you need to return the result to the client side
    if report.processRequest(request):
        return report.getFrameworkResponse()
    
    # Loading a report by URL and calling the report build
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    # Getting the necessary JavaScript code and HTML part of the report generator
    js = report.javascript.getHtml()
    html = report.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the report are displayed
    return render_template('Rendering_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
