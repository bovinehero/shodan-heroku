# Shodan CLI Tool

(Developer: Gary Grant)

![Mockup image](docs/images/git-header.png)

[Live Site](https://bhero-shodan.herokuapp.com/) is hosted on heroku as a node.js app running python 3 code.

[Google Sheet](https://docs.google.com/spreadsheets/d/1M0zQoGMlJFKAZRlaijUbdoycJxjvHleksSBca_8Yu3w/edit#gid=387475559) to store results

## About

As part of professional services pentration testers utilise Open-source intelligence (OSINT) gathering on public facing endpoints to learn as much as they can about target environments.
Often the tools used by testers are independent of one another and require translating of results into a common data format that is more easily digestible by the buisness.
This presented a gap I gap where I could explore using python to reach a remote endpoint and provide data to report in a csv friendly format.

For my submission for PP3 in the Code Institute Full Stack Developer Course I developed a proof of concept command line tool to interact with the shodan search engine API and read/write data to Google Sheets.

> [Shodan](https://www.shodan.io/) is the first public search engine for Internet-connected devices and offers users a way to discover how exposed different endpoints are to attack.

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Manual](#user-manual)
    4. [User Stories](#user-stories)
3. [Design](#design)
    1. [Design Considerations](#design-considerations)
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    5. [Imagery](#imagery)
    4. [Structure](#structure)
    5. [Workflow](#workflow)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
5. [Features](#features)
    1. [Future Implementations](#future-implementations)
    2. [Accessibility Features](#accessibility-features)
6. [Testing](#testing)
    1. [Python Validation](#python-validation)
    2. [Testing User Stories](#testing-user-stories)
8. [Bugs](#bugs)
9. [Deployment & Local Development](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Project Goals 

### User Goals
+ Discover the capabilities of the tool
+ Recieve instructions on how to use the tool
+ Discover if the Shodan dB knows about my iP addresses

### Owner Goals
+ Create an application that allows users to query the shodan API within the limits of the free tier
+ Enable users to record results of their scan for future reporting.
+ Present the solution in a web based format (heroku)

## User Experience

### Target Audience

Security enthusiasts/professionals interested in reporting on the status of their external infrastructure or penetration testers looking for low hanging fruit targets.

### User Requirements and Expectations

+ A simple, error-free experience
+ Straightforward navigation
+ Ability to store/review results

### User Manual

On initial load the application will query Google Sheets and the SHodan API to try and ensure remote endpoints are set up as expected.

An error may throw here if permissions are not set correctly on your files or the API key is incorrect.

Please follow steps in [Deployment & Local Development](#deployment) to troubleshoot this.

Once ready the app will present the user with the following text:

``` sh
[+] Please enter the IP Address for Shodan to Query
[+] Use help command for more info
[+] Enter command or IP Address:
```

Here the user can input one of several special commands:

`help`: displays a list of commands the user can execute along with helpful information about how to use the search functionality
`info`: Returns a summary of shodan's capabilities based on your API key. You can then view the services and protocols by entering a 'Y' or 'y' when prompted.
`summary report`: Reaches out to your google sheet and returns all the data in json form.
`clear report`: Reaches out to your google sheet, deletes the worksheet and re-creates a blank worksheet.

Any other input is treated as an IP, if the user's input passes the app's validation check the string is forwarded to shodan where either the API will respond to the user's IP or deliver an error message explaining why no data has been returned.

The most common issue will be the IP not showing up in the shodan dB, the following IPs are known to have worked:

+ 8.8.8.8
+ 162.243.69.95
+ 171.248.148.180
+ 31.199.40.207
+ 8.8.4.4
+ 174.142.208.197
+ 86.110.30.26
+ 149.22.187.117
+ 176.96.154.158
+ 151.252.83.215
+ 209.222.212.30
+ 180.69.12.106


### User Stories

1. As a User, I would like to be able to search if the Shodan API has record of an IP I want to scan
2. As a User, I would like instructions on how to use this tool
3. As a User, I would like to view what services the shodan API scans
4. As a User, I woud like to view the protocols shodan searches for
5. As a User, I would like to be able to save my scan results
6. As a User, I would like to retrieve my saved scan results
7. As a User, I would like to be able to start a new report when I'm done with the old one
8. As an Owner, I want users to have a positive experience whilst using the app
9. As an Owner, I want users to easily discover how to use the app
10. As an Owner, I want the user to get feedback in case of wrong input
11. As an Owner, I want data entry to be validated, to guide the user on how to correctly format the input
12. As an Owner, I want the user to be notified on start up if the app is going to fail due to missing upstream/downstream  
13. As an Owner, I want users to be able to use this tool within the limits of the API key and reasonable Google Storage limits


## Design

As a basic terminal app the need for graphical design is limited, readability and ease of use are paramount.
The graded submission required hosting a terminal implementation within a node.js web app making it the primary area to explore a little creativity.

### Design Considerations

The orginal concept for the project was to provide a scanning tool that leverages the shodan API to activley scan any endpoint on the internet and then allow storage of the results in a summary fashion in a Google Spreadsheet.

After playing with a PoC for a while it became evident that due to the nature of the public way in which the submissions are graded there were a few immediate considerations I needed to address.

1. Vulnerability Scanning is not legal without the site owner's permission and disruptive scanning can cause a Denial of Service (DoS) to their owner.
2. Any Scans performed by this tool would utilise a private API key which would link to my account potentially making me liable for damages. For the submission only the search shodan's dB for existing results was implemented, as Shodan already has the results
3. Multiple users means multiple report sheets/workbooks, while in a local single user environment this is fine a publicly hosted solution (like in heroku) could be abused and tally up significant cost to me, thus storage restrictions were implemented.
4. The remote hosting solution meant that I needed a remote endpoint to write results to, thus local dB solutions like tinydB and sqlite would not be practical without increasing comlexity.

Although points 2 & 3 could be remedied via a Secure User Management system with a backing dB, a relational databse's incorporation is beyond the scope of this project.

### Colour

As a basic terminal app the need for graphical design is limited, readability and ease of use are paramount.
The graded submission required hosting a terminal implementation within a node.js web app making it the primary area to explore a little creativity.

Base white text on a black background was selected for the terminal colours, the only colour edits to the html template was to change the initial red colouration to purple to better fit withinthe shodan background image discussed below. 

### Fonts

The terminal provided by the heroku app was a little limited with regards to shell features, I stuck with the default font provided.
This means that when running locally users will benefit from the customisations in their own environment.

As a hacker's tool I elected to follow the terminal messaging convention in the orginal [metasploit framework](https://www.metasploit.com/) in order to assist the user in differentiating the different message types on screen. 

+ [+] Execution occured as planned or input required
+ [-] Verbose message that an error has taken place because of design limitation
+ [!] Informational statement 


### Imagery

For the site's background I used the Shodan AI Image from system shock 2 [presspack](https://igdb.se/games/system-shock-2/presskit). 
As the upstream API's name was inspired by the game's main antogonist I felt this was a fitting homage to it's history.

### Structure

After a preliminary status check the app launches into a while loop that awaits user input to execute on a special command or search shodan's dB for an IP Address.

The input runs against a validation function to check if an IP address is entered and then queries the Shodan API. 

Any other input, except terminal special functions will return the user back to this state.

In addition the special commands will always return their user back to this state once completed.

### Workflow

The Flowchart below shows the initial concept for the site. 
<br>
<details>
<summary>Flowchart </summary>
<br>
<img alt="Flowchart image for app" src="docs/images/shodan-db-search-white.png">
</details>

Persistent data for the app is managed in Google Sheets

## Technologies Used

### Languages

App Functionality is all written in Python 3

HTML, CSS and JavaScript were used to create the website in heroku.

### Frameworks and Tools

[Github](https://github.com/) - To save and store the files for the website and for version control.

[Heroku Apps](https://dashboard.heroku.com/apps) (Node.js) - to host the site 

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - troubleshooting and testing features as well as implement responsive styling

[GitPod](https://www.gitpod.io/) - for active development 

[Code Institute Python Development Template](https://github.com/Code-Institute-Org/python-essentials-template) - for setting up the initial development environment

[ezgif](https://ezgif.com/) image/media conversion to webp and gif for documentation

### Libraries

#### Python3 Libraries
+ json - used to handle json file to dictionary and vice versa.
+ re - used in input validation for IP Addresses.
+ time - used to delay output to screen.
+ os - used to pick up env variable files

#### Third Party Libraries
+ [shodan](https://pypi.org/project/shodan/) - used to query shodan web services.
+ [gspread](https://pypi.org/project/gspread/) - add and manipulate data in Google Sheets.
+ [google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/) - used to set up the authentification needed to access the Google API and Google Sheets. 

## Features

+ First Run Load in Checks
  + Checks Google Sheet to check worksheet set up, creating it if required
  + Reaches out to Shodan API to check the API capabilites and display them to the user
  + Provides a whimsical message from shodan "Make yourself comfortable, Hacker. Stay a while."
    + User Stories Covered: 3, 4, 8, 12, 13
    + Screenshot. <br> ![Load In Check](docs/images/feature-load-in-check.png)

+ Main Menu:
  + Provides the main interface where the user can execute searches (via IP)
  + Allows user to call help, info, clear report and summary commands
    + User Stories Covered: 8, 10, 11 
    + Screenshot. <br> ![Main Menu Prompt](docs/images/feature-main-menu.png)

+ Help Command:
  + Shows details about the info, clear report and summary commands
  + Displays an example of how to query the Shodan API via IP
    + User Stories Covered: 2, 8, 9
    + Screenshot. <br> ![Help Command](docs/images/feature-help-command.png)

+ Info Command:
  + Performs a call to Shodan to retreive the user's current API capabilities 
  + Provides a live summary of the user's capabilities based on the their plan
  + Can print out the protocols Shodan looks for with a description of each
  + Can print out the services and port pairing it checks by default for vulnerabilities
  + Uses same logic as the first run load in checks feature, but applies interactivity based on the function not being executed on launch.
    + User Stories Covered: 3, 4
    + Screenshot. <br> ![Info Command](docs/images/feature-info-command.png)

+ IP Search:
  + Validates an IP Address is valid
  + Queries Shodan for details on it
  + Displays a summary for the user
    + User Stories Covered: 1
    + Screenshot. <br> ![IP Search](docs/images/feature-ip-search.png)

+ Save Search to Workbook:
  + Checks Google sheets to determine if data can be saved - outputs message if it cannot
  + Saves/Appends the result to the worksheet in Google Sheets
    + User Stories Covered: 5, 13
    + Screenshot. <br> ![Save Scan in Terminal](docs/images/feature-save-result.png)
    + Screenshot. <br> ![Save Scan Results Sheet](docs/images/feature-save-result-sheet.png)

+ Display Summary Report
  + Reaches our to Google Sheets to fetch saved information
  + Displays the results in JSON format
    + User Stories Covered: 6
    + Screenshot. <br> ![Display the results in JSON](docs/images/feature-summary.png)

+ Clear Report:
  + Reaches our to Google Sheets to delete saved information
  + Creates a new clean, formatted worksheet within safe parameters for usage.
  + Uses same logic as the first run load in checks feature.
    + User Stories Covered: 7, 13
    + Screenshot. <br> ![Clear Report in terminal](docs/images/feature-clear-report.png)
    + Screenshot. <br> ![Clean Report WorkSheet](docs/images/feature-clear-report-sheet.png)

### Future Implementations

The potential scope for this tool is far reaching, but development was hindered by concerns I had in user mangement, access controls and timing constraints due to work commitments.
As a result scope was deliberately tight in order to deliver core functionality, additional feature implementations I'd like to explore would be around:

+ Integration to a web app for reporting, geo mapping and User Access Controls
+ Reporting Automation - emails, summaries etc.
+ more API functionality - Live Scans, Vuln assessments, Domain names as targets
+ create/modify reports for individual users
+ test coverage with pytest/unittest
+ Add in update/delete by row functionality to Google Sheets
+ add more summary report data format options (csv, yaml etc.)
+ More first deploy automation to make tool setup cleaner
+ More Error Handling to account for remote connections
+ Better Upstream API checking and reporting on status
+ dB integration instead of google sheets to allow better results management
+ Random Shodan Quote for message of the day when app is started.

## Testing

### Python Validation

PEP8 Linting was implemented to test python code format via the pylint plugin in Visual Studio Code.

PEP8 Results - No Errors Found

![pylint results](docs/images/pylint-results.png)

> the gitpod errors are environmental and not related to python

### Automated Testing

After building the base project I experimented with using pytest to perform some automated testing. While all the tests passed the test suite is predominantly limited to `test_shodan_helper.py`.

The structure of the code in `run.py` would require the set up of a testing env to execute on as the tests impact the production set up. I did not anticipate this during development and failed to allocate sufficient time to develop this. 

I used the following code to test the app:

``` sh
pip install pytest
pytest -qvl test_run.py
pytest -qvl test_shodan_helper.py
```

![pytest results](docs/images/testing-pytest.png)

As a result of my oversight manual testing would take up most of the responsibility.

### Testing user stories

1. As a __User__, I would like to be able to search if the Shodan API has record of an IP I want to scan

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| IP Search | From Main Menu input any valid IP address | Input should be sent to shodan with an error message or data retrieved presented to user.  | Works as expected |

<br>
<details>
<summary>IP Search</summary>
<br>
<img alt="IP Search Results" src="docs/images/testing-ip-search.gif">
</details>
<br>

2. As a __User__, I would like instructions on how to use this tool

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Help Command | From Main Menu input "help" | App should present user with help message  | Works as expected |

<br>
<details>
<summary>Help Command</summary>
<br>
<img alt="Help Command Results" src="docs/images/testing-help-command.gif">
</details>
<br>

3. As a __User__, I would like to view what services the shodan API scans

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| First Run Load in Checks | Executes when app is reloaded | Checks shodan and google sheets are responsive and displays capability summary and storage readiness  | Works as expected |
| Info Command | From Main Menu input "help", then "Y" | Displays a summary of capability then prints out services one by one  | Works as expected |

<br>
<details>
<summary>First Run Load in Checks</summary>
<br>
<img alt="First Run Load in Checks Results" src="docs/images/testing-first-run-load-in-checks.gif">
</details>
<br>
<details>
<summary>Info Command No Display</summary>
<br>
<img alt="Info Command Results" src="docs/images/testing-info-command-no.gif">
</details>
<br>
<details>
<summary>Info Command Display Services</summary>
<br>
<img alt="Info Command Results" src="docs/images/testing-info-command-display-services.gif">
</details>
<br>

4. As a __User__, I woud like to view the protocols shodan searches for

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| First Run Load in Checks | Executes when app is reloaded | Checks shodan and google sheets are responsive and displays capability summary and storage readiness  | Works as expected |
| Info Command | From Main Menu input "help", then any key except "Y", then "Y" | Displays a summary of capability then prints out protocols one by one  | Works as expected |

<br>
<details>
<summary>First Run Load in Checks</summary>
<br>
<img alt="First Run Load in Checks Results" src="docs/images/testing-first-run-load-in-checks.gif">
</details>
<br>
<details>
<summary>Info Command No Display</summary>
<br>
<img alt="Info Command Results" src="docs/images/testing-info-command-no.gif">
</details>
<br>
<details>
<summary>Info Command Display Protocols</summary>
<br>
<img alt="Info Command Results" src="docs/images/testing-info-command-display-protocols.gif">
</details>
<br>

5. As a __User__, I would like to be able to save my scan results

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Save Search to Non Full Workbook | After successful IP search, press "y" | Data saved to spreadsheet and confirmation displayed to user  | Works as expected |
| Save Search to Full Workbook | After successful IP search, press "y" | Data is not saved to spreadsheet and warning displayed to user | Works as expected |

<br>
<details>
<summary>Save to Non Full Workbook</summary>
<br>
<img alt="Save to Non Full Workbook Results" src="docs/images/testing-save-to-workbook.gif">
</details>
<br>
<details>
<summary>Save to Full Workbook</summary>
<br>
<img alt="Save to Empty Workbook Results" src="docs/images/testing-save-to-full-workbook.gif">
</details>
<br>

6. As a __User__, I would like to retrieve my saved scan results

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Display Summary Report | From Main Menu input "summary report" | Contents of worksheet displaed to user in JSON format  | Works as expected |

<br>
<details>
<summary>Display Summary Report</summary>
<br>
<img alt="Display Summary Report Results" src="docs/images/testing-display-summary.gif">
</details>
<br>

7. As a __User__, I would like to be able to start a new report when I'm done with the old one

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Clear Report | From Main Menu input "clear report"  | clears data from spreadsheet and notifies user  | Works as expected |

<br>
<details>
<summary>Clear Report</summary>
<br>
<img alt="Clear Report Results" src="docs/images/testing-clear-report.gif">
</details>
<br>

8. As an __Owner__, I want users to have a positive experience whilst using the app

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| First Run Load in Checks | Executes when app is reloaded | Checks shodan and google sheets are responsive and displays capability summary and storage readiness  | Works as expected |
| Main Menu | Input commands and hit return | Input commands should be validated and execute as per special command or be checked against shodan for results.  | Works as expected |
| Help Command | From Main Menu input "help" | App should present user with help message  | Works as expected |

<br>
<details>
<summary>First Run Load in Checks</summary>
<br>
<img alt="First Run Load in Checks Results" src="docs/images/testing-first-run-load-in-checks.gif">
</details>
<br>
<details>
<summary>Main Menu</summary>
<br>
<img alt="Main Menu Results" src="docs/images/testing-main-menu.gif">
</details>
<br>
<details>
<summary>Help Command</summary>
<br>
<img alt="Help Command Results" src="docs/images/testing-help-command.gif">
</details>
<br>

9. As an __Owner__, I want users to easily discover how to use the app

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Help Command | From Main Menu input "help" | App should present user with help message  | Works as expected |

<br>
<details>
<summary>Help Command</summary>
<br>
<img alt="Help Command Results" src="docs/images/testing-help-command.gif">
</details>
<br>

10. As an __Owner__, I want the user to get feedback in case of wrong input

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Input commands and hit return | Input commands should be validated and execute as per special command or be checked against shodan for results.  | Works as expected |

<br>
<details>
<summary>Main Menu</summary>
<br>
<img alt="Main Menu Results" src="docs/images/testing-main-menu.gif">
</details>
<br>

11. As an __Owner__, I want data entry to be validated, to guide the user on how to correctly format the input

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Menu | Input commands and hit return | Input commands should be validated and execute as per special command or be checked against shodan for results.  | Works as expected |

<br>
<details>
<summary>Main Menu</summary>
<br>
<img alt="Main Menu Results" src="docs/images/testing-main-menu.gif">
</details>
<br>

12. As an __Owner__, I want the user to be notified on start up if the app is going to fail due to missing upstream/downstream  

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| First Run Load in Checks | Executes when app is reloaded | Checks shodan and google sheets are responsive and displays capability summary and storage readiness  | Works as expected |

<br>
<details>
<summary>First Run Load in Checks</summary>
<br>
<img alt="First Run Load in Checks Results" src="docs/images/testing-first-run-load-in-checks.gif">
</details>
<br>

13. As an __Owner__, I want users to be able to use this tool within the limits of the API key and reasonable Google Storage limits

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| First Run Load in Checks | Executes when app is reloaded | Checks shodan and google sheets are responsive and displays capability summary and storage readiness  | Works as expected |
| Save Search to Full Workbook | After successful IP search, press "y" | Data is not saved to spreadsheet and warning displayed to user | Works as expected |
| Clear Report | From Main Menu input "clear report"  | clears data from spreadsheet and notifies user  | Works as expected |

<br>
<details>
<summary>First Run Load in Checks</summary>
<br>
<img alt="First Run Load in Checks Results" src="docs/images/testing-first-run-load-in-checks.gif">
</details>
<br>
<details>
<summary>Save to Empty Workbook</summary>
<br>
<img alt="Save to Empty Workbook Results" src="docs/images/testing-save-to-workbook.gif">
</details>
<br>
<details>
<summary>Save to Full Workbook</summary>
<br>
<img alt="Save to Empty Workbook Results" src="docs/images/testing-save-to-full-workbook.gif">
</details>
<br>
<details>
<summary>Clear Report</summary>
<br>
<img alt="Clear Report Results" src="docs/images/testing-clear-report.gif">
</details>
<br>

## Bugs

Every time the Y was selected the report was overwritten, fixed by removing kickstart logic to external function and the controls to validate user input logic

Following PEP formatting I introduced a lot of whitespace issues like so:
![Whitespace Bug](docs/images/bug-whitespace.png)
These were remediated by reducing the whitespace from code like:

``` py
  #...
            print('[-] Either ask admin to increase capacity \
            or clear report data')

  #...
```

to

``` py
  #...
            print('[-] Either ask admin to increase capacity \
or clear report data')

  #...
```

## Deployment & Local Development

All of the following steps require a logged in github account


### How to Fork
To fork this repository:

1. Go to the repository for this project.
2. Click the Fork button in the top right corner.

### Deployment

> TODO: update this

A custom Heroku app was used to deploy the demo website, however deploying the code for local use can be accomplished by can be accomplished by cloning the release branch: 

``` sh
git clone --branch release git@github.com:bovinehero/shodan-heroku.git
```

in your python 3 env (use venv as required), move to the directory that you have cloned the code to and run:

``` sh
pip install -r requirements.txt
```

This will download the required 3rd party packages from your a remote repo (PyPi has the required libraries).

Next create `secrets.json` with your API key from SHODAN.io

``` json
{
  "SHODAN_API_KEY" : "YOUR API KEY"
}
```

Next create a Google IAM service account and a workbook called `shodan` in Google Sheets.

The `gspread_secrets.json` is the key details for your service_account in json format, the email value for the __client_email__ key should be given editor permissions to your `shodan` workbook.

``` json
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": "",
}
```

Start the app with:

``` sh
python run.py
```

As this is the first run of the app, set up the workbook by running the `clear report` command in the tool.

This will set up the backend for use.

### How to Clone
To clone this repository (with the heroku dependencies):

1. Go to the repository for this project and select the main branch.
2. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
3. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
4. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Credits

### Content
Text Content for the website was written by the Crytek Employees and was ourced from the store [Page](https://eu-shop.crytek.com/games/hunt-showdown).
Block quotes for testimonials are cited within the web documents.

### Media
Images from the System Shock 2 [presspack](https://igdb.se/games/system-shock-2/presskit)

## Acknowledgments
I would like to acknowledge the following people who helped me along the way in completing my first CI project:

Nightdive Studios - Creator System Shock 2 for inspiring the cration of the shodan tool and presspack.

Shodan.io - Creator of the Shodan API and datastores that were used to collect the search data

My In House Red Team - (You know who you are!) for inspiring the use case for the project

Mo Shami - for being the mentor that set me on the right path and provided me with mid and final feedback prioir to submission.