from flask import Flask, request, render_template, url_for
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    designer = StiDesigner()
    designer.onCreateReport += 'createReport'
    designer.options.appearance.fullScreenMode = True

    if designer.processRequest(request):
        return designer.getFrameworkResponse()

    js = designer.javascript.getHtml()
    html = designer.getHtml()

    return render_template('Registering Data when Creating a New Report.html', designerJavaScript = js, designerHtml = html)

if __name__ == '__main__':
    app.run(debug=True, port=8040)