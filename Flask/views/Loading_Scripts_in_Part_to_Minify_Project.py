from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Loading_Scripts_in_Part_to_Minify_Project = app = Blueprint('Loading_Scripts_in_Part_to_Minify_Project', __name__)

@app.route('/Loading_Scripts_in_Part_to_Minify_Project', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    designer.javascript.reportsSet = False
    designer.javascript.blocklyEditor = False
    designer.javascript.reportsChart = True
    designer.javascript.reportsExport = True
    designer.javascript.reportsImportXlsx = False
    designer.javascript.reportsMaps = False
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    designer.report = report

    return designer.getFrameworkResponse()
