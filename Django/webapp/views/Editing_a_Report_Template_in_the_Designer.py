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

	return designer.getFrameworkResponse()
