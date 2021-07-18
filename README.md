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

## Architecture

### Risk Assessment

A screenshot of my risk assessment document can be found below.

![Risk Assessment](https://i.imgur.com/jBcHTP3.png)

**Update**: After discussing with my mentor, I have decided to make my project simpler due to the risk of potentially not being able to finish in time. This risk has been added on to the risk assessment. The current plan is to revisit this risk assessment after a initial prototype of my project, to change the product to adapt to the risks.

The full Risk Assessment document can be found [here](https://docs.google.com/spreadsheets/d/18LOucbo6bNB233hZN950s-zoDuAG8sb8tvt1NYHw6a0/edit?usp=sharing).

### Project Tracking

My Project will be tracked using Jira. Here is my initial diagram that I plan to update as I progress in my project

![Jira Board](https://i.imgur.com/J6FbtIT.png)

### Entity Relationship Diagram

My inital ER diagram is shown below, with changes expected to be implemented as my project progresses.

![ER Diagram](https://i.imgur.com/QPFhp07.png)

The current structure is one to many relatioship between "User Profile" and "Game Records" as a user can have many games on record. Then we have a one to many relationship between "Game Records" and "Heroes" as a game usually has 10 different hero IDs. Having this relationship allows users to find their game records, as well as the heroes they have played (with/against).

I have altered my ER diagram to adjust for the change made in my approach to the project

![ER Diagram2](https://i.imgur.com/TkUyLNV.png)

If I have sufficient time in the project, then I will implement further features on to the ER chart, and possibly another table.

### CI Pipeline
