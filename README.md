
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

| Member | GitHub Username | REG No | Module | Responsibility |
|---|---|---|---|---|
| Aadhil | aadhil-nisar | ASP/2023/061 | M5 | Approval, Integration and CI |
| Koparnika | koparnikasrikaran2002-gif | ASP/2023/082 | M1 | Accounts and Authentication |
| Sinthu | sinthu02 | ASP/2023/163 | M2 | Equipment Catalogue |
| Sumaiya | fathimasumaiya884-collab | ASB/2023/0085 | M3 | Booking Form and Model |
| Vijaha | HasVij | ASB/2023/087 | M4 | Booking Validation and Tests |

## Coordination Roles

| Role | Assigned Member | Responsibility |
|---|---|---|
| Coordinator | Koparnika | Manage team activities, deadlines and GitHub Projects |
| Co-Coordinator | Sumaiya | Assist with team coordination, requirements Issues and task tracking |
| QA Lead | Vijaha | Coordinate testing and quality assurance |
| GitHub/CI Lead | Aadhil | Manage GitHub repository and CI workflow |
| Review Lead | Sinthu | Coordinate peer reviews and maintain the review checklist |

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


## E2 - Accounts and Authentication

FR-00 provides:

- Student registration
- Login and logout
- Hashed password storage
- Student and Staff roles
- Staff-only access restrictions
- Automated authentication tests

### Student Registration

Run Flask and open:

http://127.0.0.1:5000/auth/register

Public registration creates Student accounts only.

### Login

http://127.0.0.1:5000/auth/login

### Staff Account Setup

Staff accounts are created through a terminal command:

```powershell
python -m flask --app app create-staff
```

Follow the interactive prompts for username, email
and password.

Do not put Staff passwords in the README or GitHub.

### Local Secret Key

For a stable development session, configure SECRET_KEY
as an environment variable before starting Flask.

Example using Windows PowerShell:

```powershell
$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")
```

### Authentication Tests

```powershell
python -m pytest tests/test_auth.py -v
```

### E2 Scope


## E2 - Accounts and Authentication

FR-00 provides:

- Student registration
- Login and logout
- Hashed password storage
- Student and Staff roles
- Staff-only access restrictions
- Automated authentication tests

### Student Registration

Run Flask and open:

http://127.0.0.1:5000/auth/register

Public registration creates Student accounts only.

### Login

http://127.0.0.1:5000/auth/login

### Staff Account Setup

Staff accounts are created through a terminal command:

```powershell
python -m flask --app app create-staff
```

Follow the interactive prompts for username, email
and password.

Do not put Staff passwords in the README or GitHub.

### Local Secret Key

For a stable development session, configure SECRET_KEY
as an environment variable before starting Flask.

Example using Windows PowerShell:

```powershell
$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")
```

### Authentication Tests

```powershell
python -m pytest tests/test_auth.py -v
```

### E2 Scope

FR-00 provides working accounts and role restrictions.

Equipment management and booking features are integrated
through the other E2 modules.


## E2 - FR-01 Equipment Catalogue

**Module Owner:** Sinthu (`sinthu02`)

### Features

FR-01 implements:

- Equipment listing for authenticated users.
- Category filtering.
- Staff-only equipment creation.
- Staff-only equipment editing.
- Staff-only equipment deletion.
- Equipment status: Available or Out of service.
- Server-side input validation and role restrictions.

### Equipment Fields

| Field | Description |
|---|---|
| ID | Automatically generated identifier |
| Name | Required, maximum 120 characters |
| Category | Required, maximum 80 characters |
| Description | Optional text, maximum 2000 characters in forms |
| Status | Available or Out of service |

### Access Control

| Action | Student | Staff |
|---|---|---|
| View catalogue | Yes | Yes |
| Filter category | Yes | Yes |
| Add equipment | No | Yes |
| Edit equipment | No | Yes |
| Delete equipment | No | Yes |

Users must log in before accessing the catalogue.

### Run the Equipment Catalogue

Start Flask:

```powershell
python -m flask --app app run
```

Log in and open:

http://127.0.0.1:5000/equipment/

Staff accounts are created using:

```powershell
python -m flask --app app create-staff
```

### Automated Tests

Run FR-01 tests:

```powershell
python -m pytest tests/test_equipment.py -v
```

Run all tests:

```powershell
python -m pytest -v
```

Run Ruff:

```powershell
python -m ruff check .
```

Run coverage:

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

### GitHub Information

- Requirement: FR-01
- Issue: #2
- Implementation owner: Sinthu
- Reviewer: Vijaha
- Integration: Aadhil

### Integration Note

FR-02 Booking Requests will use the existing
Equipment database records.

The Equipment model is preserved from E1.
Deletion rules for equipment linked to bookings
must be reviewed when FR-02 is integrated.


## Future Development

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
