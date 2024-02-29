from flask import Blueprint, request, render_template
from stimulsoft_reports.designer import StiDesigner

Registering_Data_when_Creating_a_New_Report = app = Blueprint('Registering_Data_when_Creating_a_New_Report', __name__)

@app.route('/Registering_Data_when_Creating_a_New_Report', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()
    designer.onCreateReport += 'createReport'
    designer.options.appearance.fullScreenMode = True

    if designer.processRequest(request):
        return designer.getFrameworkResponse()

    js = designer.javascript.getHtml()
    html = designer.getHtml()

    return render_template('Registering_Data_when_Creating_a_New_Report.html', designerJavaScript = js, designerHtml = html)
