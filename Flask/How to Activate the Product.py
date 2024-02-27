from flask import Flask, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    """Please use one of the methods below to register your license key"""
    #viewer.license.setFile(url_for('static', filename='private/license.key'))
    #viewer.license.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)