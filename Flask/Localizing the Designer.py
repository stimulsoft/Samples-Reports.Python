from flask import Flask, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()
    designer.options.localization = 'de.xml'

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    designer.report = report

    return designer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)