from django.shortcuts import render
from django.templatetags.static import static
from stimulsoft_reports import StiNodeJs


def index(request):
    # Defining the HTML page title
    title = 'Configuring and Installing Node.js'

    # Creating a Node.js object
    nodejs = StiNodeJs()

    # Setting the path to the executable files of the already installed Node.js
    # nodejs.binDirectory = 'C:\\Program Files\\nodejs'
    # nodejs.binDirectory = '/usr/bin/nodejs'

    # Setting the path to the working directory where Node.js packages will be deployed.
    # By default, the current Python script execution directory is used.
    # nodejs.workingDirectory = ''

    # Installing the Node.js package from the official website, may take some time.
    # If the installation fails, the function will return False
    result = nodejs.installNodeJS()

    # Installing or updating product packages to the current version, may take some time.
    if result:
        result = nodejs.updatePackages()

    # Installation status or error text from Node.js engine.
    message = 'The installation was successful.' if result else nodejs.error

    # Rendering an HTML template with a text message as the server response.
    return render(request, 'Server_Side_Message.html', {'title': title, 'message': message})
