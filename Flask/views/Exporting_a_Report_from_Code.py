from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat

Exporting_a_Report_from_Code = app = Blueprint('Exporting_a_Report_from_Code', __name__)


@app.route('/Exporting_a_Report_from_Code')
def index():
    # Rendering an HTML template
    return render_template('Exporting_a_Report_from_Code.html')


@app.route('/Exporting_a_Report_from_Code/export', methods = ['GET', 'POST'])
def export():
    # Creating a report object
    report = StiReport()

    # If the request processing was successful, you need to return the result to the client side
    if report.processRequest(request):
        return report.getFrameworkResponse()

    # Loading a report by URL and calling the report build
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    # Getting the export format passed in the GET request parameters
    requestFormat = request.args.get('format')
    exportFormat = StiExportFormat.DOCUMENT
    if requestFormat == 'pdf':
        exportFormat = StiExportFormat.PDF
    elif requestFormat == 'excel':
        exportFormat = StiExportFormat.EXCEL
    elif requestFormat == 'html':
        exportFormat = StiExportFormat.HTML

    # Calling a report export to a specified format
    report.exportDocument(exportFormat)

    # Getting the necessary JavaScript code and HTML part of the report generator
    js = report.javascript.getHtml()
    html = report.getHtml()

    # Rendering an HTML template, inside which JavaScript and HTML code of the report are displayed
    return render_template('Exporting_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
