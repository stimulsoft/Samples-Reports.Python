from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

class IndexHandler(RequestHandler):
    def get(self):
        designer = StiDesigner()

        if designer.processRequest(self.request):
            return designer.getFrameworkResponse(self)
        
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        designer.report = report

        js = designer.javascript.getHtml()
        html = designer.getHtml()

        self.render('Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.html', designerJavaScript = js, designerHtml = html)
    
    def post(self):
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
