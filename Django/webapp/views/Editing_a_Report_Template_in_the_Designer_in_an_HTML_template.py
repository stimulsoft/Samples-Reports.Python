from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.designer import StiDesigner

def index(request):
	designer = StiDesigner()

	if designer.processRequest(request):
		return designer.getFrameworkResponse()
	
	report = StiReport()
	reportUrl = static('reports/SimpleList.mrt')
	report.loadFile(reportUrl)
	designer.report = report

	js = designer.javascript.getHtml()
	html = designer.getHtml()

	return render(request, 'Editing_a_Report_Template_in_the_Designer_in_an_HTML_template.html', {'designerJavaScript': js, 'designerHtml': html})
