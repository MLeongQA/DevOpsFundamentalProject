# DevOpsFundamentalProject

## Contents

## Introduction

### Objective

The objective of this project is as follows:
>To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

I am expected to implement the following:
- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.

- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.

- Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board

- Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.

- A functioning front-end website and integrated API's, using Flask.
Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

### My Proposition

For this project, I have decided to create a record keeping site for the popular MOBA game "Dota 2", where users will be able to create a profile and upload their match data that they have played. Users will be able to view their own game records, as well as others and update or delete certain game records or game data.

An outline of the CRUD implementation is as follows:

**Create**
- User Profile
  - User ID
  - Username/Tag
  - Region
  - Rank 
- Game Records
  - Game ID
  - User ID
  - Hero ID
  - Duration
  - Win/Loss
  - (Potentially additional data such as Networth or K/D/A)
- Heroes
  - Hero ID
  - Hero Name
  - Attribute
  - Roles

**Read/Update/Delete**
- User Profiles
- Game Records
- Hero Records

**Update**: This has been updated after discussion to remove the Heros table and come back to it as a future development point.

## Architecture

### Risk Assessment

A screenshot of my risk assessment document can be found below.

![Risk Assessment](https://i.imgur.com/jBcHTP3.png)

**Update**: After discussing with my mentor, I have decided to make my project simpler due to the risk of potentially not being able to finish in time. This risk has been added on to the risk assessment. The current plan is to revisit this risk assessment after a initial prototype of my project, to change the product to adapt to the risks.

The full Risk Assessment document can be found [here](https://docs.google.com/spreadsheets/d/18LOucbo6bNB233hZN950s-zoDuAG8sb8tvt1NYHw6a0/edit?usp=sharing).

### Project Tracking

My Project will be tracked using Trello. This is due to the fact that Trello is free, a easy to understand and present but also has a lot of depth from the various features it provides.

Here is the initial diagram that I plan to update as I progress in my project

![Jira Board](https://i.imgur.com/4Lrzm7l.png)

I have divided my trello board into multiple lists to categorise each task and be able to see the task progress.

- **Project Resources**: A list of handy resources for my project that can be quickly accessed.
- **User Stories**: A collection of stories to document the requirements of my project
- **To Do**: A list of tasks that are required to be initalised.
- **In Progress**: A list of tasks that have been started and requires completion
- **Testing**: A list of code related tasks that require testing.
- **Review**: A list of tasks that require reviewing before being authorised to be completed
- **Completed**: A list of tasks that have been completed.

The full trello board can be found [here](https://trello.com/b/USnsQD0E/devops-project-board)

### Entity Relationship Diagram

My inital ER diagram is shown below, with changes expected to be implemented as my project progresses.

![ER Diagram](https://i.imgur.com/QPFhp07.png)

The current structure is one to many relatioship between "User Profile" and "Game Records" as a user can have many games on record. Then we have a one to many relationship between "Game Records" and "Heroes" as a game usually has 10 different hero IDs. Having this relationship allows users to find their game records, as well as the heroes they have played (with/against).

**Update**: I have altered my ER diagram to adjust for the change made in my approach to the project

![ER Diagram2](https://i.imgur.com/TkUyLNV.png)

If I have sufficient time in the project, then I will implement further features on to the ER chart, and possibly another table.

### Analysis of Testing

I've decided to use a series of Unit tests and integration tests for my application. Trello was used to keep track of functionality that required unit/integration tests, to ensure that I reached 100% coverage for my application. More information on each specific testing can be found below.

### CI Pipeline

![CI Pipeline Diagram](https://i.imgur.com/kUqBXb6.png)

The above diagram shows my continuous integration pipeline to promote rapid development and automation to save time. All code is pushed onto github, which Jenkins can then fetch and can run the implemented integration tests. Trello is used for project tracking to ensure tasks are finished on time, and Selenium is used to run integration tests for my application. 

**Jenkins Build Script**

I have broken the build script down into three stages:

1. Installation of relevant modules for the virtual environment.

```
#!/bin/sh
sudo apt-get install python3 python3-pip python3-venv chromium-browser -y wget unzip -y

version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip
```

2. Setting up the virtual environment with python-venv.

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

3. Initiating the unit and integration tests.

```
python3 -m pytest --cov=application --cov-report term-missing --disable-warnings
```


## Development

### Unit Testing

Unit Testing was used to test the back-end of my application, to ensure routes were working + data was being manipulated correctly. Each functionality of my app was divided into seperate classes and functions, and assertions were used to ensure that the correct response was produced for each action. Tests are automatically run after every git push using Jenkins webhooks and a coverage report is produced using JaCoCo, which is set up to fail the build, if the coverage degrades more than a specified threshold.

![Coverage](https://i.imgur.com/DT1LrkO.png)

Unit tests and integration tests can be run manually by using the three steps in the Jenkins build script highlighted above. 

![Coverage2](https://i.imgur.com/wxpbymr.png)

### Integration Testing

Integration testing was used to test the front-end of my application, to ensure that the forms were correctly interacting with each other. Selenium was used to simulate a user on my application, and test each functionality of the site by interacting with forms, links and buttons.

![Coverage2](https://i.imgur.com/wxpbymr.png)

Any failures in the integration testing would be highlighted on the coverage report. 

### Front-end Development

## Evaluation 

### Ideas for Potential Improvements

- Implement a third heroes database that can be related to games.
- Implement a many to many relationship between players and games instead of a one to many.
- Implement a auto increment feature for mmr.
- Implement filters to allow for broader searches for player profiles/games.

### Authors/Contributors

Mikito Leong

### Acknowledgements

- Oliver Nichols
- Ryan Wright
- Victoria Sacre
