from flask import Blueprint, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Editing_a_Report_Template_in_the_Designer = app = Blueprint('Editing_a_Report_Template_in_the_Designer', __name__)

@app.route('/Editing_a_Report_Template_in_the_Designer', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    designer.report = report

    return designer.getFrameworkResponse()
