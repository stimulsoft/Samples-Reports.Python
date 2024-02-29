import json
import os
from flask import Blueprint, request, url_for
from stimulsoft_reports import StiResult
from stimulsoft_reports.designer import StiDesigner
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport

Saving_a_Report_Template_on_the_Server_Side = app = Blueprint('Saving_a_Report_Template_on_the_Server_Side', __name__)

def saveReport(args: StiReportEventArgs):
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename = 'reports/' + args.fileName))
    try:
        with open(filePath, mode='w', encoding='utf-8') as file:
            jsonReport = json.dumps(args.report, indent = 4)
            file.write(jsonReport)
            file.close()
    except Exception as e:
        return StiResult.getError(str(e))

    return f'The report was successfully saved to a {args.fileName} file.'

@app.route('/Saving_a_Report_Template_on_the_Server_Side', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()
    designer.onSaveReport += saveReport

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    designer.report = report

    return designer.getFrameworkResponse()
