from flask import Flask, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.onBeginProcessData += 'beginProcessData'

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    viewer.report = report

    js = viewer.javascript.getHtml()
    html = viewer.getHtml()

    return render_template('Registering a Data from Code.html', viewerJavaScript = js, viewerHtml = html)

if __name__ == '__main__':
    app.run(debug=True, port=8040)