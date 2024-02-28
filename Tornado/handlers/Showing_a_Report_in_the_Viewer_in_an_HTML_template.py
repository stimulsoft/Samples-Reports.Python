from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

class ViewerHandler(RequestHandler):
    def get(self):
        viewer = StiViewer()
        viewer.options.appearance.scrollbarsMode = True
        viewer.options.width = '1000px'
        viewer.options.height = '600px'

        if viewer.processRequest(self.request):
            return viewer.getFrameworkResponse(self)
        
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        viewer.report = report

        js = viewer.javascript.getHtml()
        html = viewer.getHtml()

        self.render('Showing_a_Report_in_the_Viewer_in_an_HTML_template.html', viewerJavaScript = js, viewerHtml = html)
    
    def post(self):
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)
