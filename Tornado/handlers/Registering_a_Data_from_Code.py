from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

class ViewerHandler(RequestHandler):
    def get(self):
        viewer = StiViewer()
        viewer.onBeginProcessData += 'beginProcessData'
        
        if viewer.processRequest(self.request):
            return viewer.getFrameworkResponse(self)
        
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        viewer.report = report

        js = viewer.javascript.getHtml()
        html = viewer.getHtml()

        self.render('Registering_a_Data_from_Code.html', viewerJavaScript = js, viewerHtml = html)
    
    def post(self):
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
