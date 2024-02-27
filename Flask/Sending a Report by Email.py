from flask import Flask, request, url_for
from stimulsoft_reports.events import StiEmailEventArgs
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

app = Flask(__name__)

def emailReport(args: StiEmailEventArgs):
    args.settings.fromAddr = 'mail.sender@stimulsoft.com'
    args.settings.host = 'smtp.stimulsoft.com'
    args.settings.port = 456
    args.settings.login = '********'
    args.settings.password = '********'
    return 'The Email has been sent successfully.'

@app.route('/', methods = ['GET', 'POST'])
def index():
    viewer = StiViewer()
    viewer.options.toolbar.showSendEmailButton = True
    viewer.onEmailReport += emailReport

    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    report = StiReport()
    report.loadFile(url_for('static', filename='reports/SimpleList.mrt'))
    viewer.report = report

    return viewer.getFrameworkResponse()

if __name__ == '__main__':
    app.run(debug=True, port=8040)