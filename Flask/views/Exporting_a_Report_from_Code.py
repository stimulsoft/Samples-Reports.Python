from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat

Exporting_a_Report_from_Code = app = Blueprint('Exporting_a_Report_from_Code', __name__)

@app.route('/Exporting_a_Report_from_Code')
def index():
    return render_template('Exporting_a_Report_from_Code.html')

@app.route('/Exporting_a_Report_from_Code/export', methods = ['GET', 'POST'])
def export():
    report = StiReport()

    if report.processRequest(request):
        return report.getFrameworkResponse()

    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    requestFormat = request.args.get('format')
    exportFormat = StiExportFormat.DOCUMENT
    if requestFormat == 'pdf':
        exportFormat = StiExportFormat.PDF
    elif requestFormat == 'excel':
        exportFormat = StiExportFormat.EXCEL
    elif requestFormat == 'html':
        exportFormat = StiExportFormat.HTML

    report.exportDocument(exportFormat)

    js = report.javascript.getHtml()
    html = report.getHtml()

    return render_template('Exporting_a_Report_from_Code.html', reportJavaScript = js, reportHtml = html)
