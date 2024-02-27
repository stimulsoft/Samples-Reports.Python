from flask import Flask, request, render_template, url_for
from stimulsoft_reports.report import StiReport

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    report = StiReport()
    report.onAfterRender += 'afterRender'

    if report.processRequest(request):
        return report.getFrameworkResponse()
    
    reportUrl = url_for('static', filename = 'reports/SimpleList.mrt')
    report.loadFile(reportUrl)
    report.render()

    js = report.javascript.getHtml()
    html = report.getHtml()

    return render_template('Rendering a Report from Code.html', reportJavaScript = js, reportHtml = html)

if __name__ == '__main__':
    app.run(debug=True, port=8040)