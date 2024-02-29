from flask import Blueprint, request, render_template, url_for
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

Using_a_Handler_in_a_Separate_Function = app = Blueprint('Using_a_Handler_in_a_Separate_Function', __name__)

mainHandler = StiHandler('/Using_a_Handler_in_a_Separate_Function/handler')

@app.route('/Using_a_Handler_in_a_Separate_Function')
def index():
    viewer = StiViewer()
    viewer.handler = mainHandler
    viewer.options.appearance.fullScreenMode = True

    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render_template('Using_a_Handler_in_a_Separate_Function.html', viewerJavaScript = js, viewerHtml = html)

@app.route('/Using_a_Handler_in_a_Separate_Function/handler', methods = ['GET', 'POST'])
def handler():
    mainHandler.processRequest(request)
    return mainHandler.getFrameworkResponse()
