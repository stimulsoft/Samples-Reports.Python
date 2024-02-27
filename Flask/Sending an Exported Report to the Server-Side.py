import os
from flask import Flask, request, url_for
from stimulsoft_reports.events import StiExportEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

def endExportReport(args: StiExportEventArgs):
    filePath = os.path.normpath(os.getcwd() + url_for('static', filename='reports/' + args.fileName))
    with open(filePath, mode='wb') as file:
        file.write(args.data)
        file.close()
    return f'The exported report was successfully saved to a {args.fileName} file.'

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onEndExportReport += endExportReport

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)