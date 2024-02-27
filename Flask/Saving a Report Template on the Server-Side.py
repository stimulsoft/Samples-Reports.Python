import json
import os
from flask import Flask, request, url_for
from stimulsoft_reports import StiResult
from stimulsoft_reports.designer import StiDesigner
from stimulsoft_reports.events import StiReportEventArgs
from stimulsoft_reports.report import StiReport

app = Flask(__name__)

def saveReport(args: StiReportEventArgs):
    filePath = os.path.normpath(os.getcwd() + '\\static\\reports\\' + args.fileName + '2')
    try:
        with open(filePath, mode='w', encoding='utf-8') as file:
            jsonReport = json.dumps(args.report, indent = 4)
            file.write(jsonReport)
            file.close()
    except Exception as e:
        return StiResult.getError(str(e))

    return f'The report was successfully saved to a {args.fileName} file.'

@app.route('/', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()
    designer.onSaveReport += saveReport

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    designer.report = report

    return designer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)