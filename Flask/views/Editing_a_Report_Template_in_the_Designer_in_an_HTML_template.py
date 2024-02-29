from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

Editing_a_Report_Template_in_the_Designer_in_an_HTML_template = app = Blueprint('Editing_a_Report_Template_in_the_Designer_in_an_HTML_template', __name__)

@app.route('/Editing_a_Report_Template_in_the_Designer_in_an_HTML_template', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    designer.report = report

    js = designer.javascript.getHtml()
    html = designer.getHtml()

    return render_template('Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.html', designerJavaScript = js, designerHtml = html)
