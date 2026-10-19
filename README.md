Lab Equipment Booking System

Software Engineering Mini Project

Repository: https://github.com/aadhil-nisar/lab-equipment-booking-system

Current Evaluation: E2 — Intermediate Review
Evaluation Date: Monday, 19 October 2026
E2 Status: Development requirements completed; final demonstration and documentation verification

1. Project Overview

The Lab Equipment Booking System is a web-based application developed using Python, Flask and SQLite.

The application allows:

Students to register and log in.

Students to view and filter laboratory equipment.

Students to submit equipment booking requests.

Students to view their own booking requests and booking statuses.

Staff to log in and manage the equipment catalogue.

Staff-only actions to be protected using role-based access control.

New equipment booking requests are initially marked as Pending.

The project also demonstrates Software Engineering practices, including GitHub Issues, GitHub Projects, branches, Pull Requests, peer reviews, automated testing, code-quality checks and Continuous Integration.

Evaluation Milestones

Evaluation

Date

Requirements

E1 — Initial Review

14 October 2026

Project setup, repository, team roles, Flask, SQLite, testing and CI

E2 — Intermediate Review

19 October 2026

FR-00, FR-01, FR-02, initial FR-03 validation progress, automated tests, CI and peer reviews

E3 — Final Review

23 October 2026

Complete FR-03, FR-04 booking approval, further integration and final testing

E2 Completion Summary:

FR-00 Accounts and Login — Implemented and merged.

FR-01 Equipment Catalogue — Implemented and merged.

FR-02 Booking Requests — Implemented and merged.

FR-03 Initial Booking Validation — Implemented and merged for E2.

Automated tests — Implemented.

GitHub Actions CI — Configured and running successfully.

GitHub peer reviews — Completed for the merged E2 Pull Requests.

The remaining overlapping-booking validation and Staff approval functionality are part of E3.

2. Team Members and Module Allocation

Member

GitHub Username

Registration Number

Module

Responsibility

Aadhil

aadhil-nisar

ASP/2023/061

M5

Booking Approval, Integration and CI

Koparnika

koparnikasrikaran2002-gif

ASP/2023/082

M1

Accounts and Authentication (FR-00)

Sinthu

sinthu02

ASP/2023/163

M2

Equipment Catalogue (FR-01)

Sumaiya

fathimasumaiya884-collab

ASB/2023/0085

M3

Booking Requests (FR-02)

Vijaha

HasVij

ASB/2023/087

M4

Booking Validation and Tests (FR-03)

Coordination Roles

Role

Member

Responsibility

Coordinator

Koparnika

Team coordination, deadlines, GitHub Issues and Projects

Co-Coordinator

Sumaiya

Support task tracking, communication and progress monitoring

QA Lead

Vijaha

Test design, BVA/EP, validation and test evidence

GitHub / CI Lead

Aadhil

Integration, GitHub Actions, PR coordination and merges

Review Lead

Sinthu

Coordinate peer reviews and maintain review practices

Each team member contributes through development, testing, peer review, integration or coordination.

3. Functional Requirements and Current Scope

Requirement

Description

Issue

Responsible

E2 Status

FR-00

Accounts and Login

#1

Koparnika

Completed and merged

FR-01

Equipment Catalogue

#2

Sinthu

Completed and merged

FR-02

Booking Requests

#3

Sumaiya

Completed and merged

FR-03

Booking Validation

#4

Vijaha

Initial E2 validation merged; E3 overlap work remaining

FR-04

Booking Approval and Status

#5

Aadhil

Planned for E3

Current Implementation Status

FR-00, FR-01 and FR-02 are implemented and merged into main.

FR-03 initial E2 validation is also merged. It currently includes:

End time must be after start time.

Booking must start in the future.

Minimum booking duration of 30 minutes.

Maximum booking duration of 4 hours.

Rejection of unavailable equipment.

Automated boundary and form-validation tests.

Remaining E3 functionality:

Overlapping-booking detection and final integration.

Staff approval and rejection of booking requests.

Approval-time booking validation.

Additional integration and regression tests.

4. Technology Stack

Technology

Purpose

Python

Programming language

Flask

Web application framework

SQLite

Database

Flask-SQLAlchemy

Database models and queries

Flask-Login

Login sessions and authentication

Werkzeug

Password hashing

Flask-WTF

CSRF protection

HTML and CSS

User interface

pytest

Automated testing

pytest-cov

Test coverage

Ruff

Python code-quality checking

Git

Version control

GitHub

Repository and team collaboration

GitHub Issues

Requirement and task tracking

GitHub Projects

Project workflow board

GitHub Actions

Continuous Integration

Dependencies are maintained in requirements.txt.

5. Project Structure

lab-equipment-booking-system/
|
|-- .github/
|   |-- workflows/
|       |-- ci.yml
|
|-- app/
|   |-- __init__.py
|   |-- commands.py
|   |-- extensions.py
|   |-- booking_validation.py
|   |
|   |-- models/
|   |   |-- __init__.py
|   |   |-- user.py
|   |   |-- equipment.py
|   |   |-- booking.py
|   |
|   |-- routes/
|   |   |-- __init__.py
|   |   |-- auth.py
|   |   |-- equipment.py
|   |   |-- booking.py
|   |
|   |-- templates/
|       |-- index.html
|       |-- auth/
|       |   |-- register.html
|       |   |-- login.html
|       |   |-- staff.html
|       |-- equipment/
|       |   |-- catalogue.html
|       |   |-- form.html
|       |-- booking/
|           |-- new.html
|           |-- mine.html
|
|-- tests/
|   |-- conftest.py
|   |-- test_smoke.py
|   |-- test_auth.py
|   |-- test_equipment.py
|   |-- test_booking.py
|   |-- test_booking_validation.py
|   |-- test_e2_integration.py
|
|-- .gitignore
|-- README.md
|-- REVIEW_CHECKLIST.md
|-- TESTING.md
|-- requirements.txt

E2 validation module: app/booking_validation.py

E2 validation tests: tests/test_booking_validation.py

The E3 overlap-validation tests are developed separately in the FR-03 feature branch and are not part of the merged E2 implementation.

6. Installation and Local Setup

The following instructions use Windows PowerShell in VS Code.

Step 1 — Clone the Repository

git clone https://github.com/aadhil-nisar/lab-equipment-booking-system.git
cd lab-equipment-booking-system

If the repository is already cloned, check your local work before updating:

git status --short
git branch --show-current

Once unfinished changes are safely committed or saved, update main:

git switch main
git pull --ff-only origin main

Step 2 — Create a Virtual Environment

py -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1

Step 3 — Install Dependencies

python -m pip install -r requirements.txt

Step 4 — Set a Local Secret Key

$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")

Never commit secret keys or passwords to GitHub.

Step 5 — Run the Application

python -m flask --app app run --port 5001

Open:

http://127.0.0.1:5001

For development on the default port:

python -m flask --app app run --debug

Default URL:

http://127.0.0.1:5000

Step 6 — Check Application Routes

In a second terminal:

python -m flask --app app routes

Expected routes include:

/auth/register

/auth/login

/auth/logout

/auth/staff

/equipment/

/equipment/new

/bookings/new

/bookings/

7. Database Setup and Models

The application uses SQLite and Flask-SQLAlchemy.

The application factory initializes the database tables using db.create_all().

Local database path:

instance/lab_equipment.db

The database file is excluded from version control.

Important: Do not delete the local database during the demonstration because it contains accounts, equipment and booking records.

User Model — FR-00

File: app/models/user.py

Field

Description

id

Unique user identifier

username

Unique login username

email

Email address

password_hash

Secure password hash

role

Student or Staff

Equipment Model — FR-01

File: app/models/equipment.py

Field

Description

id

Unique equipment identifier

name

Equipment name

category

Equipment category

description

Equipment details

status

Available or Out of service

Booking Model — FR-02

File: app/models/booking.py

Field

Description

id

Unique booking identifier

student_id

Student who submitted the booking

equipment_id

Requested equipment

booking_date

Requested date

start_time

Booking start time

end_time

Booking end time

status

Pending, Approved or Rejected

New bookings are saved with Pending status.

Approved and Rejected are supported by the data model, but Staff approval and rejection actions are reserved for FR-04.

8. FR-00 — Accounts and Authentication

Developer: Koparnika
Reviewer: Sumaiya
Issue: #1
Merged PR: #11

Implemented Features

Student registration.

Username and password authentication.

Secure password hashing.

Login and logout functionality.

Student and Staff roles.

Staff-only dashboard.

Role-based access control.

CSRF-protected forms.

Application URLs

Feature

Route

Register

/auth/register

Login

/auth/login

Logout

/auth/logout

Staff Dashboard

/auth/staff

Create a Staff Account

Staff accounts are created using the Flask CLI:

python -m flask --app app create-staff

Follow the terminal prompts.

Public Student registration cannot create Staff accounts.

Role Restriction

A logged-in Student opening:

http://127.0.0.1:5001/auth/staff

receives:

403 Forbidden

Automated Tests

python -m pytest tests/test_auth.py -v

E2 Status: Completed and merged.

9. FR-01 — Equipment Catalogue

Developer: Sinthu
Reviewer: Vijaha
Issue: #2
Merged PR: #12

Implemented Features

Display laboratory equipment.

Filter equipment by category.

Display availability status.

Staff adds equipment.

Staff edits equipment.

Staff deletes equipment.

Students have read-only catalogue access.

Unauthorized equipment-management requests are rejected.

Application Routes

Feature

Route

Permission

Equipment Catalogue

/equipment/

Student and Staff

Add Equipment

/equipment/new

Staff

Edit Equipment

/equipment/<id>/edit

Staff

Delete Equipment

/equipment/<id>/delete

Staff, POST only

Student Access Restriction

A Student opening:

http://127.0.0.1:5001/equipment/new

receives:

403 Forbidden

Automated Tests

python -m pytest tests/test_equipment.py -v

E2 Status: Completed and merged.

Integration note: Avoid deleting equipment that already has associated booking records. Protection for historical booking references requires further integration review.

10. FR-02 — Booking Requests

Developer: Sumaiya
Reviewer: Sinthu
Issue: #3
Merged PR: #14

Implemented Features

Student booking request form.

Selection of available equipment.

Booking date selection.

Start-time and end-time selection.

Booking storage in SQLite.

Automatic Pending status.

Student booking history.

Students can view only their own bookings.

Staff cannot submit Student booking requests.

Booking Routes

Feature

Route

Submit Booking

/bookings/new

My Booking Requests

/bookings/

Student Booking Workflow

Log in using a Student account.

Open Equipment Catalogue.

Click Request Equipment.

Select Available equipment.

Choose a future booking date.

Enter start and end times.

Submit Booking Request.

Open My Booking Requests.

Confirm the new booking status is Pending.

Automated Tests

python -m pytest tests/test_booking.py -v

E2 Status: Completed and merged.

11. FR-03 — Booking Validation

Developer: Vijaha
Reviewer: Sumaiya
Issue: #4
E2 Merged PR: #15

E2 Implementation Status

The initial FR-03 validation implementation is completed and merged into main.

Files added:

app/booking_validation.py
tests/test_booking_validation.py

Implemented Validation Rules

Booking must start in the future.

End time must be after start time.

Minimum booking duration is 30 minutes.

Maximum booking duration is 4 hours.

Equipment must exist and be available.

Invalid requests must not create booking records.

The minimum and maximum duration boundaries are inclusive.

Boundary Value Analysis (BVA)

Boundary Value Analysis tests values below, at and above a defined limit.

Test ID

Start Time

End Time

Duration

Expected

BVA-01

09:00

09:29

29 minutes

Reject

BVA-02

09:00

09:30

30 minutes

Accept

BVA-03

09:00

09:31

31 minutes

Accept

BVA-04

09:00

12:59

239 minutes

Accept

BVA-05

09:00

13:00

240 minutes

Accept

BVA-06

09:00

13:01

241 minutes

Reject

These tests use a future booking date.

Equivalence Partitioning (EP)

Equivalence Partitioning divides inputs into categories with similar expected behavior.

Test ID

Input Category

Expected

EP-01

Valid future booking

Accept

EP-02

Booking shorter than 30 minutes

Reject

EP-03

Booking longer than 4 hours

Reject

EP-04

End time before start time

Reject

EP-05

Past booking date

Reject

EP-06

Out-of-service equipment

Reject

EP-07

Unknown equipment

Reject

Automated Validation Tests

Run:

python -m pytest tests/test_booking_validation.py -v

Test coverage includes:

Duration boundary checks.

Future-date validation.

Invalid time ordering.

Validation through the Flask booking form.

Confirmation that valid bookings receive Pending status.

Confirmation that rejected requests are not saved.

GitHub Evidence

Merged FR-03 E2 PR:

https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15

Developer: Vijaha
Reviewer: Sumaiya

Remaining E3 Work

Complete overlapping-booking detection.

Verify partial and exact time overlaps.

Verify adjacent bookings.

Integrate final validation with Staff approval decisions.

Complete remaining tests and integration.

The overlapping-booking feature is being developed through:

Open E3 PR #16:
https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16

PR #16 is not yet merged into main.

Issue #4 must remain Open / In progress until the full FR-03 requirement is completed.

E2 Status: Initial FR-03 validation completed and merged.

12. FR-04 — Booking Approval and Status

Developer: Aadhil
Issue: #5

Target: E3 — Final Evaluation

Planned Features

Staff view Pending booking requests.

Staff approve or reject requests.

Booking status changes are saved in SQLite.

Students can view the updated booking status.

Students cannot approve or reject bookings.

Booking conflicts are checked before approval.

Automated tests verify approval, rejection and access control.

Booking Status Values

Status

Meaning

Pending

Waiting for Staff decision

Approved

Accepted by Staff

Rejected

Declined by Staff

Current Status: Planned for E3; Staff approval and rejection have not yet been implemented on the merged E2 branch.

13. Automated Testing and Coverage

The project uses pytest for automated tests.

Tests use an isolated SQLite in-memory database through tests/conftest.py.

CSRF protection is disabled only for automated test-client requests. Normal browser forms retain CSRF protection.

FR-00 — Authentication Tests

python -m pytest tests/test_auth.py -v

FR-01 — Equipment Tests

python -m pytest tests/test_equipment.py -v

FR-02 — Booking Tests

python -m pytest tests/test_booking.py -v

FR-03 — Validation Tests

python -m pytest tests/test_booking_validation.py -v

E2 Integration Tests

python -m pytest tests/test_e2_integration.py -v

Smoke Tests

python -m pytest tests/test_smoke.py -v

Run All Automated Tests

python -m pytest -v

Run Ruff

python -m ruff check .

Generate Test Coverage

python -m pytest --cov=app --cov-report=term-missing

Coverage identifies which portions of application code are executed during automated tests.

The actual test count and coverage percentage should be recorded in TESTING.md after running the commands.

Combined Testing Commands

python -m pytest tests/test_auth.py -v
python -m pytest tests/test_equipment.py -v
python -m pytest tests/test_booking.py -v
python -m pytest tests/test_booking_validation.py -v
python -m pytest tests/test_e2_integration.py -v
python -m pytest -v
python -m ruff check .
python -m pytest --cov=app --cov-report=term-missing

14. Continuous Integration — GitHub Actions

The repository uses GitHub Actions for Continuous Integration.

Workflow file:

.github/workflows/ci.yml

CI Pipeline

When code is pushed or a Pull Request is opened, GitHub Actions runs the configured workflow.

The workflow:

Checks out the repository.

Sets up Python 3.11.

Installs dependencies.

Runs Ruff.

Runs pytest with coverage.

Displays the job result.

CI Commands

python -m ruff check .
python -m pytest --cov=app --cov-report=term-missing

GitHub Actions Evidence

Actions page:

https://github.com/aadhil-nisar/lab-equipment-booking-system/actions

Verified successful main workflow:

https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39183895215

This verifies that the configured CI workflow completed successfully on that main revision.

Any newer commits or Pull Requests should be checked separately for their latest CI results.

15. GitHub Issues, Branches, Pull Requests and Peer Reviews

Development Workflow

The team follows this development process:

Issue → Branch → Code → Tests → Pull Request → Peer Review → CI → Merge → Project Board Update

Development Steps

Create or open the assigned GitHub Issue.

Read its description, tasks and acceptance criteria.

Assign the responsible team member.

Move the Issue to In progress.

Create a separate feature branch.

Implement the required functionality.

Add automated tests.

Run pytest and Ruff.

Push the branch to GitHub.

Create a Pull Request targeting main.

Assign a different team member as reviewer.

Reviewer checks the changes and leaves written feedback.

Confirm GitHub Actions CI passes.

Merge the approved Pull Request.

Update the Issue and Project Board.

E2 Pull Requests and Reviews

Work

Developer

Reviewer

Pull Request

Status

FR-00

Koparnika

Sumaiya

#11

Merged

FR-01

Sinthu

Vijaha

#12

Merged

FR-02

Sumaiya

Sinthu

#14

Merged

FR-03 E2

Vijaha

Sumaiya

#15

Merged

E2 Integration

Aadhil

Vijaha

#13

Merged

E3 Development

Work

Responsible

Pull Request

Status

FR-03 Overlap Validation

Vijaha

#16

Open, not merged

FR-04 Staff Approval

Aadhil

Not yet recorded

Planned

Peer Review Requirements

Before approving a PR, the reviewer should check:

Correct functionality.

Code quality.

Authentication and authorization.

Database behavior.

Error handling.

Automated tests.

Integration with existing modules.

Successful CI results.

Reviewers should leave a written review note and approve or request changes.

The review guidelines are documented in:

REVIEW_CHECKLIST.md

GitHub Projects Board

The team uses the following workflow:

Backlog → To do → In progress → In review → Done

Backlog: Work planned for a future evaluation.

To do: Work ready to begin.

In progress: Development is underway.

In review: Pull Request is awaiting review.

Done: Work completed, reviewed and integrated.

The coordinator is Koparnika, supported by Sumaiya.

FR-03 Issue #4 remains In progress because its final E3 work is not complete.

16. E2 Evaluation Demonstration Plan

Evaluation Date: 19 October 2026
Duration: Approximately 15 minutes

Time

Responsible

Demonstration

1 minute

Koparnika

Project introduction, team roles and requirements

3 minutes

Koparnika

FR-00 Accounts and Login

3 minutes

Sinthu

FR-01 Equipment Catalogue

3 minutes

Sumaiya

FR-02 Booking Requests

2 minutes

Vijaha

FR-03 validation progress, BVA and EP tests

2 minutes

Aadhil

Automated tests, coverage, Ruff and GitHub Actions

1 minute

Team

GitHub collaboration and remaining E3 work

FR-00 Demonstration

Register Student.

Login.

Show Student role.

Show 403 on Staff-only URL.

Login as Staff.

Show Staff Dashboard.

Logout.

FR-01 Demonstration

Login as Staff.

Open Equipment Catalogue.

Add equipment.

Edit equipment.

Change availability status.

Filter equipment by category.

Demonstrate Student read-only permissions.

FR-02 Demonstration

Login as Student.

Open Request Equipment.

Select Available equipment.

Select a future date and valid time.

Submit booking.

Show Pending status.

Open My Booking Requests.

FR-03 Demonstration

Reject end time before start time.

Reject 29-minute duration.

Accept 30-minute duration.

Accept 4-hour duration.

Reject 4-hour-1-minute duration.

Reject past bookings.

Show BVA and EP design in TESTING.md.

Show automated tests.

Automated Testing and CI

python -m pytest -v
python -m ruff check .
python -m pytest --cov=app --cov-report=term-missing

Show successful GitHub Actions results and reviewed PRs.

Evidence Required

Running Flask application.

Completed FR-00, FR-01 and FR-02 functionality.

Initial FR-03 validation.

Automated tests.

Test coverage report.

Ruff result.

GitHub Actions success.

GitHub Issues.

GitHub Project Board.

Merged Pull Requests.

Peer reviews.

README.md.

TESTING.md.

REVIEW_CHECKLIST.md.

17. Security, Data Integrity and Development Notes

The project includes the following development and security practices:

User passwords are stored using secure hashing.

Authentication uses Flask-Login.

Staff-only routes are restricted.

Student ownership is checked on booking requests.

CSRF protection is enabled for browser forms.

Invalid booking times are rejected.

Equipment availability is validated.

Booking records are linked to database users and equipment.

Automated tests use a separate in-memory database.

Secret keys and passwords must not be committed.

Pull Requests undergo peer review.

GitHub Actions checks code quality and automated tests.

Current Limitations

Full overlapping-booking detection is still being developed in E3.

Staff approval and rejection are not yet available in the merged E2 application.

Deleting equipment with booking history requires additional safeguards.

Booking times use the server's local time; a production system should define an explicit timezone policy.

The Flask development server is not intended for production deployment.

These limitations are recorded as future integration work rather than being presented as completed E2 functionality.

18. Current Project Status

E1 — Completed

The team completed:

GitHub repository setup.

Team roles and task allocation.

Flask application setup.

SQLite database models.

GitHub Issues and Projects.

Testing configuration.

Ruff configuration.

GitHub Actions CI.

README and review documentation.

Initial peer-review workflow.

E2 — Completed Development Scope

The team completed and merged:

FR-00 Accounts and Login — PR #11.

FR-01 Equipment Catalogue — PR #12.

FR-02 Booking Requests — PR #14.

Initial FR-03 Booking Validation — PR #15.

E2 Integration Tests — PR #13.

The application supports Student and Staff authentication, equipment management, Student booking requests, initial booking validation and automated testing.

GitHub Actions has successfully executed the configured CI checks on main.

E3 — Remaining Development

The team will continue with:

Final FR-03 overlapping-booking validation.

FR-04 Staff approval and rejection.

Approval-time validation.

Additional integration and regression tests.

Final documentation and review.

FR-03 E3 development PR: #16 — Open.

FR-04 Issue: #5 — Open.

Project Links

GitHub Repository:
https://github.com/aadhil-nisar/lab-equipment-booking-system

GitHub Issues:
https://github.com/aadhil-nisar/lab-equipment-booking-system/issues

Pull Requests:
https://github.com/aadhil-nisar/lab-equipment-booking-system/pulls

GitHub Actions:
https://github.com/aadhil-nisar/lab-equipment-booking-system/actions

Testing Documentation:
TESTING.md

Review Guidelines:
REVIEW_CHECKLIST.md

Project: Lab Equipment Booking System
Coursework: Software Engineering Mini Project
Team Members: Aadhil, Koparnika, Sinthu, Sumaiya and Vijaha
E2 Review: 19 October 2026
E3 Review: 23 October 2026
