from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

class DesignerHandler(RequestHandler):
    def get(self):
        designer = StiDesigner()

        if designer.processRequest(self.request):
            return designer.getFrameworkResponse(self)
        
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        designer.report = report

        return designer.getFrameworkResponse(self)
    
    def post(self):
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)

