from tornado.web import RequestHandler
from stimulsoft_reports import StiHandler
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

class IndexHandler(RequestHandler):
    def get(self):
        viewer = StiViewer()

        if viewer.processRequest(self.request):
            return viewer.getFrameworkResponse(self)
        
        """Please use one of the methods below to register your license key"""
        #viewer.license.setFile(url_for('static', filename='private/license.key'))
        #viewer.license.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
        
        report = StiReport()
        reportUrl = self.static_url('reports/SimpleList.mrt')
        report.loadFile(reportUrl)
        viewer.report = report

        return viewer.getFrameworkResponse(self)

    def post(self):
        handler = StiHandler()
        if handler.processRequest(self.request):
            return handler.getFrameworkResponse(self)