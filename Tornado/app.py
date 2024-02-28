import asyncio, os
from tornado.web import Application, RequestHandler, url
from handlers import Showing_a_Report_in_the_Viewer, Showing_a_Report_in_the_Viewer_in_an_HTML_template
from handlers import Editing_a_Report_Template_in_the_Designer, Editing_a_Report_Template_in_the_Designer_in_an_HTML_template
from handlers import Exporting_a_Report_from_Code, Registering_a_Data_from_Code

class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')

class WebApplication(Application):
	def __init__(self):
		handlers = [
			url(r'/', IndexHandler),
			url(r'/Showing_a_Report_in_the_Viewer', Showing_a_Report_in_the_Viewer.ViewerHandler, name="Showing_a_Report_in_the_Viewer"),
			url(r'/Showing_a_Report_in_the_Viewer_in_an_HTML_template', Showing_a_Report_in_the_Viewer_in_an_HTML_template.ViewerHandler, name="Showing_a_Report_in_the_Viewer_in_an_HTML_template"),
			url(r'/Editing_a_Report_Template_in_the_Designer', Editing_a_Report_Template_in_the_Designer.DesignerHandler, name="Editing_a_Report_Template_in_the_Designer"),
			url(r'/Editing_a_Report_Template_in_the_Designer_in_an_HTML_template', Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.DesignerHandler, name="Editing_a_Report_Template_in_the_Designer_in_an_HTML_template"),
			url(r'/Exporting_a_Report_from_Code', Exporting_a_Report_from_Code.IndexHandler, name="Exporting_a_Report_from_Code"),
			url(r'/Exporting_a_Report_from_Code/export', Exporting_a_Report_from_Code.ExportHandler, name="Exporting_a_Report_from_Code_Export"),
			url(r'/Registering_a_Data_from_Code', Registering_a_Data_from_Code.ViewerHandler, name="Registering_a_Data_from_Code")
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