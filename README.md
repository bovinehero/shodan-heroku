# Shodan CLI Tool

(Developer: Gary Grant)

![Mockup image](docs/images/git-header.png)

[Live Site](https://bhero-shodan.herokuapp.com/) is hosted on heroku as a node.js app running python 3 code.

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Client Goals](#client-goals)
2. [User Experience](#user-experience)
    1. [Key Information on the Site](#key-information-on-the-site)
    2. [Target Audience](#target-audience)
    3. [User Requirements and Expectations](#user-requirements-and-expectations)
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
+ Goal One
+ Goal Two

### Client Goals
+ Goal One
+ Goal Two

## User Experience



### Key Information on the Site


### Target Audience


### User Requirements and Expectations


### User Stories


## Design

### Design Considerations


### Colour


### Fonts

USED MSF messaging standard

### Imagery

Shodan Image from system shock 2 press pack

### Structure


### Workflow

The Flowchart below shows the initial concept for the site. 
<br>
<details>
<summary>Flowchart </summary>
<br>
<img alt="Flowchart image for app" src="docs/images/shodan-db-search-white.png">
</details>

## Technologies Used

### Languages

App Functionality is all written in Python 3

HTML, CSS and JavaScript were used to create the website.

### Frameworks and Tools

[Github](https://github.com/) - To save and store the files for the website and for version control.

[Heroku Apps](https://dashboard.heroku.com/apps) (Node.js) - to host the site 

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - troubleshooting and testing features as well as implement responsive styling

[GitPod](https://www.gitpod.io/) - for active development 

[Code Institute Python Development Template](https://github.com/Code-Institute-Org/python-essentials-template) - for setting up the initial development environment

[ezgif](https://ezgif.com/) image conversion to webp


## Features
Summary of site.

+ Feature 1:

  + Summary of feature
    + User Stories Covered: X
    + Scrrenshot. <br> ![nav menu closed](docs/images/feature-feature1.png)

+ Feature 2:

  + Summary of feature
    + User Stories Covered: X
    + Scrrenshot. <br> ![nav menu closed](docs/images/feature-feature2.png)

+ Feature 3:

  + Summary of feature
    + User Stories Covered: X
    + Scrrenshot. <br> ![nav menu closed](docs/images/feature-feature3.png)

+ Feature 4:

  + Summary of feature
    + User Stories Covered: X
    + Scrrenshot. <br> ![nav menu closed](docs/images/feature-feature4.png)


### Future Implementations

+ Live Scans.
+ Reporting Automation - emails, summaries etc.
+ more API functionality
+ create/modify reports for individual users

## Testing

### Python Validation

PEP8 Linting was implemented to test python code format.

PEP8 Results - No Errors Found

X Warnings displayed

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Warning | Feature name / line | Descrition | Comments |


### Testing user stories

1. As a __Test Persona__, I would like to do some stuff.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Fature | Steps | Expectations  | Works as expected |


<br>
<details>
<summary>Story Results</summary>
<br>
<img alt="X Test Results" src="docs/images/testing-story1.gif">
</details>

## Bugs

### Big Bug One

Bug summary

Steps to replicate

[ref](https://developer.mozilla.org/en-US/docs/Web/CSS/:autofill)

## Deployment & Local Development

All of the following steps require a logged in github account


### How to Fork
To fork this repository:

1. Go to the repository for this project.
2. Click the Fork button in the top right corner.

### Deployment

> TODO: update this

A custom Heroku app was used to deploy the demo website, however deploying the code for use can be accomplished by can be accomplished by cloning the release branch: 

``` sh
git clone <url>
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

### Code Used


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