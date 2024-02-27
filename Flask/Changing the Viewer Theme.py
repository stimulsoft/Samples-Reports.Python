from flask import Flask, request, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer, enums

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.options.appearance.backgroundColor = 'black'
    viewer.options.appearance.theme = enums.StiViewerTheme.OFFICE_2022_BLACK_GREEN
    viewer.options.toolbar.displayMode = enums.StiToolbarDisplayMode.SEPARATED

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)