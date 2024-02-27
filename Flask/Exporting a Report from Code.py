from flask import Flask, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiExportFormat

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Exporting a Report from Code.html')

@app.route('/export', methods = ['GET', 'POST'])
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

    return report.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)