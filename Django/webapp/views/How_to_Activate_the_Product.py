from django.templatetags.static import static
from stimulsoft_reports import StiLicense
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.viewer import StiViewer


def index(request):
    # Creating a viewer object
    viewer = StiViewer()
    viewer.javascript.appendHead('<link rel="shortcut icon" href="' + static('favicon.ico') + '" type="image/x-icon">')

    # If the request processing was successful, you need to return the result to the client side
    if viewer.processRequest(request):
        return viewer.getFrameworkResponse()
    
    # You can use one of the methods below to register your license key
    # StiLicense.setFile(static('private/license.key'))
    # StiLicense.setKey('6vJhGtLLLz2GNviWmUTrhSqnO...')
    
    # Creating a report object
    report = StiReport()

    # Loading a report by URL
    # This method does not load the report object on the server side, it only generates the necessary JavaScript code
    # The report will be loaded into a JavaScript object on the client side
    reportUrl = static('reports/SimpleList.mrt')
    report.loadFile(reportUrl)

    # Assigning a report object to the viewer
    viewer.report = report

    # Displaying the visual part of the viewer as a prepared HTML page
    return viewer.getFrameworkResponse()
