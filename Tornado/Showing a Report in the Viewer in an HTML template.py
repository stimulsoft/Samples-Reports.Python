import asyncio, os
from tornado.web import Application, RequestHandler, url
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer

class MainHandler(RequestHandler):
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

        self.render('Showing a Report in the Viewer in an HTML template.html', viewerJavaScript = js, viewerHtml = html)

class WebApplication(Application):
	def __init__(self):
		handlers = [
			url(r'/', MainHandler)
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), 'templates'),
			static_path=os.path.join(os.path.dirname(__file__), 'static')
		)
		Application.__init__(self, handlers, **settings)

async def main():
	app = WebApplication()
	app.listen(8040)
	print('Starting development server at http://127.0.0.1:8040/')
	await asyncio.Event().wait()

if __name__ == '__main__':
	asyncio.run(main())