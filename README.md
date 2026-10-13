
# Lab Equipment Booking System

## Project Overview

The Lab Equipment Booking System is a web-based application
developed for the Software Engineering Mini Project.

The system will allow students to request laboratory
equipment bookings and lab staff to manage equipment
and booking requests.

The project also demonstrates Software Engineering
practices including GitHub Issues, Projects, branches,
Pull Requests, peer reviews, automated testing and
Continuous Integration.

## Team Members and Module Allocation

| Member | GitHub Username | Module | Responsibility |
|---|---|---|---|
| Aadhil | aadhil-nisar | M5 | Approval, Integration and CI |
| Koparnika | koparnikasrikaran2002-gif | M1 | Accounts and Authentication |
| Sinthu | sinthu02 | M2 | Equipment Catalogue |
| Sumaiya | fathimasumaiya884-collab | M3 | Booking Form and Model |
| Vijaha | HasVij | M4 | Booking Validation and Tests |

## Coordination Roles

| Role | Assigned Member |
|---|---|
| Coordinator | Koparnika |
| QA Lead | Vijaha |
| GitHub/CI Lead | Aadhil |
| Review Lead | Sinthu |

## Functional Requirements

The functional requirements are recorded as GitHub Issues.

- FR-00: Accounts and Login
- FR-01: Equipment Catalogue
- FR-02: Booking Requests
- FR-03: Booking Validation
- FR-04: Booking Approval and Status

## Technology Stack

- Python 3.11 or newer
- Flask
- Flask-SQLAlchemy
- SQLite
- pytest
- pytest-cov
- Ruff
- Git and GitHub
- GitHub Actions
- GitHub Projects

## Project Structure

```text
lab-equipment-booking-system/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── equipment.py
│   └── templates/
│       └── index.html
├── tests/
│   ├── conftest.py
│   └── test_smoke.py
├── .gitignore
├── README.md
├── REVIEW_CHECKLIST.md
└── requirements.txt
```

## Installation and Setup

### 1. Clone the Repository

```powershell
git clone https://github.com/aadhil-nisar/lab-equipment-booking-system.git
cd lab-equipment-booking-system
```

### 2. Create a Virtual Environment

Windows PowerShell:

```powershell
py -m venv .venv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Run the Flask Application

```powershell
python -m flask --app app run
```

Open:

http://127.0.0.1:5000

The homepage should display the Lab Equipment Booking System.

## Database Setup

The application uses SQLite through Flask-SQLAlchemy.

The initial Equipment model contains:

- id
- name
- category
- description
- status

The database tables are initialized automatically
when the Flask application starts.

The local SQLite database is stored at:

instance/lab_equipment.db

The local database is excluded from Git using .gitignore.

## Automated Testing

The project uses pytest.

Run the tests:

```powershell
python -m pytest -v
```

The initial E1 test suite contains four tests:

1. Homepage responds successfully.
2. Invalid routes return HTTP 404.
3. Equipment database table is created.
4. Equipment data can be saved and retrieved.

### Coverage

Run:

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

This generates a terminal coverage report.

## Code Quality

Ruff is used for Python linting.

Run:

```powershell
python -m ruff check .
```

## Continuous Integration

GitHub Actions automatically runs on pushes
and Pull Requests.

Workflow file:

.github/workflows/ci.yml

The CI workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs Ruff.
5. Runs pytest with coverage.

All checks should pass before merging a Pull Request.

## GitHub Development Workflow

The team follows:

Issue -> Branch -> Code -> Test -> Pull Request
-> Peer Review -> CI -> Merge

Every development task should be linked to a GitHub Issue.

Team members should use their own branches and
GitHub accounts.

Pull Requests must be reviewed by another member.

The project uses REVIEW_CHECKLIST.md for reviews.

## GitHub Projects Board

The board contains five statuses:

- Backlog
- To do
- In progress
- In review
- Done

Functional requirement Issues remain in Backlog
until their implementation begins.

E1 tasks move to Done after successful completion
and merge.

## E1 Deliverables

E1 Evaluation: 14 October 2026

The E1 deliverables are:

- GitHub repository
- Team members and roles in README
- Requirements represented as GitHub Issues
- GitHub Projects board
- Running Flask application
- Basic SQLite/database setup
- GitHub Actions workflow
- Ruff and pytest running in CI
- Evidence of feature branches and reviewed PRs
- Draft REVIEW_CHECKLIST.md

The complete functional application is not expected at E1.

## Future Development

E2 Evaluation: 19 October 2026

Continue implementation of accounts, equipment catalogue,
booking requests and booking validation.

E3 Evaluation: 23 October 2026

Complete the application, integration, testing,
documentation and final review evidence.

## Security and Development Notes

- Do not commit passwords or secret credentials.
- Do not commit local SQLite database files.
- Do not commit Python virtual environments.
- Validate user input when implementing forms.
- Restrict Staff-only functionality appropriately.
- Review code and tests before merging.

## Current Project Status

E1 - Initial Flask, database, testing,
documentation and GitHub workflow setup.
