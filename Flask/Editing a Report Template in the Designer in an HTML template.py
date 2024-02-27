from flask import Flask, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()

    if designer.processRequest(request):
        return designer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    designer.report = report

    js = designer.javascript.getHtml()
    html = designer.getHtml()

    return render_template('Editing a Report Template in the Designer in an HTML template.html', designerJavaScript = js, designerHtml = html)

if __name__ == '__main__':
    app.run(debug=True, port=8040)