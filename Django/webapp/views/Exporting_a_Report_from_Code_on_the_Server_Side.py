from django.contrib.staticfiles import finders
from django.shortcuts import render
from stimulsoft_reports.report import StiReport
from stimulsoft_reports.report.enums import StiEngineType, StiExportFormat


def index(request):
    # Defining the HTML page title
    title = 'Exporting a Report from Code on the Server-Side'

    # Creating a report object
    report = StiReport()

    # Setting the server-side rendering mode
    report.engine = StiEngineType.SERVER_NODE_JS

    # If the request processing was successful, you need to return the result to the client side
    if report.processRequest(request):
        return report.getFrameworkResponse()
    
    # Loading a report by URL
    # This method loads a report file and stores it as a compressed string in an object.
    # The report will be loaded from this string into a JavaScript object when using Node.js
    reportPath = finders.find('reports/SimpleList.mrt')
    report.loadFile(reportPath)

    # Building a report
    # The report is not built using Python code.
    # This method will prepare JavaScript code and pass it to Node.js, which will build a report and return the finished document.
    result = report.render()

    if result:
        # After successfully building a report, calling the document export method. Export is also performed using Node.js engine.
        # This method will return the byte data of the exported document, or save it to a file.
        buffer = report.exportDocument(StiExportFormat.HTML)
        
        # buffer = report.exportDocument(StiExportFormat.PDF)

        # filePath = finders.find('reports') + '/SimpleList.pdf'
        # result = report.exportDocument(StiExportFormat.PDF, filePath)
        # message = result
        
        message = f'The exported document takes {len(buffer)} bytes.'
        message += '<br><br><br>' + buffer.decode('utf-8')
    else:
        # If there is a build error, you can display the error text.
        message = report.nodejs.error
    
    # Rendering an HTML template with a text message as the server response.
    return render(request, 'Server_Side_Message.html', {'title': title, 'message': message})
