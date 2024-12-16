from flask import Blueprint, render_template
from stimulsoft_reports import StiNodeJs

Configuring_and_Installing_Node_js = app = Blueprint('Configuring_and_Installing_Node_js', __name__)


@app.route('/Configuring_and_Installing_Node_js', methods = ['GET', 'POST'])
def index():
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
    return render_template('Server_Side_Message.html', title = title, message = message)

    