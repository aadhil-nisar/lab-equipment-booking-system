# Lab Equipment Booking System

**Software Engineering Mini Project**
**Repository:** https://github.com/aadhil-nisar/lab-equipment-booking-system

## 1. Project Overview

The **Lab Equipment Booking System** is a Flask-based web application that lets Students browse laboratory equipment, submit booking requests, and track their requests. Lab Staff can maintain the equipment catalogue. Staff booking approvals and complete booking-conflict validation are planned for the final evaluation.

The project also demonstrates software engineering practices: requirements as GitHub Issues, a GitHub Projects board, feature branches, pull requests (PRs), peer reviews, automated tests, code-quality checks, continuous integration (CI), and team collaboration.

### Evaluation milestones

| Evaluation | Date | Scope |
|---|---|---|
| E1 — Initial Review | 14 October 2026 | Repository, team roles, Issues/board, Flask and SQLite foundation, tests, CI, and review checklist |
| E2 — Intermediate Review | 19 October 2026 | Working FR-00, FR-01, FR-02; initial FR-03 validation/testing progress; reviewed PRs and CI |
| E3 — Final Review | 23 October 2026 | Complete FR-03, FR-04 Staff approval, integration, testing, and final documentation |

## 2. Team Members and Module Allocation

| Member | GitHub username | Registration number | Module | Responsibility |
|---|---|---|---|---|
| Aadhil | `aadhil-nisar` | ASP/2023/061 | M5 | Booking Approval, Integration and CI |
| Koparnika | `koparnikasrikaran2002-gif` | ASP/2023/082 | M1 | Accounts and Authentication (FR-00) |
| Sinthu | `sinthu02` | ASP/2023/163 | M2 | Equipment Catalogue (FR-01) |
| Sumaiya | `fathimasumaiya884-collab` | ASB/2023/0085 | M3 | Booking Form and Model (FR-02) |
| Vijaha | `HasVij` | ASB/2023/087 | M4 | Booking Validation and Tests (FR-03) |

### Coordination roles

| Role | Member | Responsibility |
|---|---|---|
| Coordinator | **Koparnika** | Coordinate deadlines, team progress, Issues and GitHub Projects |
| Co-Coordinator | **Sumaiya** | Support coordination, requirement tracking and task updates |
| QA Lead | **Vijaha** | Coordinate test design, execution, defect reports and quality checks |
| GitHub / CI Lead | **Aadhil** | Maintain integration, GitHub repository workflow and GitHub Actions |
| Review Lead | **Sinthu** | Coordinate peer reviews and use of `REVIEW_CHECKLIST.md` |

All five members are responsible for meaningful development, testing, review, coordination, or integration contributions and for recording evidence in GitHub.

## 3. Functional Requirements and Current Scope

| Requirement | Description | Issue | Owner | Status / evaluation scope |
|---|---|---|---|---|
| FR-00 | Accounts and Login | [#1](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/1) | Koparnika | Implemented and merged for E2 |
| FR-01 | Equipment Catalogue | [#2](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/2) | Sinthu | Implemented and merged for E2 |
| FR-02 | Booking Requests | [#3](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/3) | Sumaiya | Implemented and merged for E2 |
| FR-03 | Booking Validation | [#4](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/4) | Vijaha | Initial E2 validation/test design in progress; full completion in E3 |
| FR-04 | Booking Approval and Status | [#5](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/5) | Aadhil | E3 work; not yet implemented |

**Status note:** This README distinguishes functionality already merged into `main` from planned E2/E3 work. The main branch currently includes basic FR-02 validation (valid input format, existing/available equipment, and end time after start time). The full 30-minute minimum, four-hour maximum, past-booking, and overlap checks are tracked through FR-03; do not claim those are all active until the relevant PRs have been merged and verified.

## 4. Technology Stack

- **Language:** Python 3.11 or newer
- **Web framework:** Flask
- **Database / ORM:** SQLite and Flask-SQLAlchemy
- **Authentication:** Flask-Login; Werkzeug password hashing
- **Form security:** Flask-WTF CSRF protection
- **Testing:** pytest and pytest-cov
- **Linting:** Ruff
- **Version control:** Git and GitHub
- **CI:** GitHub Actions
- **Project management:** GitHub Issues and GitHub Projects

Exact dependency constraints are maintained in `requirements.txt`.

## 5. Project Structure

```text
lab-equipment-booking-system/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py               # Flask application factory
│   ├── commands.py               # Manual Staff creation command
│   ├── extensions.py             # Database, login and CSRF extensions
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                # Student / Staff accounts
│   │   ├── equipment.py           # Equipment records
│   │   └── booking.py             # Student booking requests
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py                # Register, login, logout, Staff page
│   │   ├── equipment.py           # Catalogue and Staff CRUD
│   │   └── booking.py             # Submit and view Student bookings
│   └── templates/
│       ├── index.html
│       ├── auth/
│       │   ├── register.html
│       │   ├── login.html
│       │   └── staff.html
│       ├── equipment/
│       │   ├── catalogue.html
│       │   └── form.html
│       └── booking/
│           ├── new.html
│           └── mine.html
├── tests/
│   ├── conftest.py
│   ├── test_smoke.py
│   ├── test_auth.py
│   ├── test_equipment.py
│   ├── test_booking.py
│   └── test_e2_integration.py
├── .gitignore
├── README.md
├── REVIEW_CHECKLIST.md
├── TESTING.md
└── requirements.txt
```

**FR-03 in-progress files:** Vijaha's E2 work may add `app/booking_validation.py` and `tests/test_booking_validation.py`. Include these in the structure above **only after** that PR is merged into `main`.

## 6. Installation and Local Setup

Instructions below use **Windows PowerShell** in VS Code.

### Step 1 — Clone the repository

```powershell
git clone https://github.com/aadhil-nisar/lab-equipment-booking-system.git
cd lab-equipment-booking-system
```

If the project is already cloned, enter the folder and update `main` instead:

```powershell
git switch main
git pull --ff-only origin main
```

Before switching branches, check `git status --short` and resolve any local changes. Do not discard teammates' work.

### Step 2 — Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If `.venv` already exists, only activate it.

### Step 3 — Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4 — Set a local Flask secret key

Set a fresh secret in the current PowerShell session:

```powershell
$env:SECRET_KEY = (python -c "import secrets; print(secrets.token_hex(32))")
```

Use the same environment variable value across server restarts if you want existing login sessions to remain valid. Never commit secret values or passwords to GitHub. The application generates a key if none is provided, but keeping a stable local key is more convenient for development.

### Step 5 — Start the application

```powershell
python -m flask --app app run --debug
```

Open: http://127.0.0.1:5000/

If port 5000 is already in use:

```powershell
python -m flask --app app run --debug --port 5001
```

Then use `http://127.0.0.1:5001/` and replace port 5000 with 5001 in the URLs below. `--debug` is for local development only.

### Step 6 — Verify registered routes

In a second terminal with the environment activated:

```powershell
python -m flask --app app routes
```

## 7. Database Setup and Models

The application uses SQLite through Flask-SQLAlchemy and initializes registered tables when Flask starts using `db.create_all()`.

The local database is normally stored at:

```text
instance/lab_equipment.db
```

The `instance/` folder and SQLite database files are excluded from Git. **Do not delete the database casually**: it contains local accounts, equipment and bookings. `create_all()` creates missing tables; it does **not** migrate existing table schemas.

### User model — FR-00

| Field | Purpose |
|---|---|
| `id` | Unique account identifier |
| `username` | Unique username |
| `email` | Unique email address |
| `password_hash` | Hashed password, never plaintext |
| `role` | `Student` or `Staff` |

### Equipment model — FR-01

| Field | Purpose |
|---|---|
| `id` | Unique equipment identifier |
| `name` | Required name, up to 120 characters |
| `category` | Required category, up to 80 characters |
| `description` | Description; form limits input to 2,000 characters |
| `status` | `Available` or `Out of service` |

### Booking model — FR-02

| Field | Purpose |
|---|---|
| `id` | Unique booking identifier |
| `student_id` | Foreign key to the requesting User |
| `equipment_id` | Foreign key to Equipment |
| `booking_date` | Requested date |
| `start_time` | Requested start time |
| `end_time` | Requested end time |
| `status` | `Pending`, `Approved` or `Rejected` |

New requests are always created as **Pending**. The model can store Approved and Rejected values for future FR-04 functionality, but Staff approval/rejection routes are not yet implemented.

**Integration limitation:** FR-01 currently permits Staff to delete equipment. Because FR-02 bookings reference Equipment rows, the team must add an agreed protection/deactivation rule before deleting equipment linked to bookings. Avoid deleting referenced equipment during demonstrations.

## 8. FR-00 — Accounts and Authentication

**Owner:** Koparnika (`koparnikasrikaran2002-gif`)
**Issue:** [#1](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/1)

Implemented functionality:

- Public Student registration (public registration cannot assign the Staff role).
- Login and logout using Flask-Login sessions.
- Secure password hashing with Werkzeug.
- Student and Staff roles.
- Staff-only access enforcement; unauthorized Students receive HTTP 403.
- CSRF-protected registration, login and logout forms.

### Account URLs

| Page | Route |
|---|---|
| Student registration | `/auth/register` |
| Login | `/auth/login` |
| Logout | `/auth/logout` (POST) |
| Staff dashboard | `/auth/staff` |

### Create a Staff account manually

Staff accounts **must not** be created through public registration. Run:

```powershell
python -m flask --app app create-staff
```

Enter the username, email and password when prompted. Choose a unique username/email and a password of at least eight characters. Do not publish the password or store it in README, Issues, PR comments or screenshots.

Run FR-00 tests:

```powershell
python -m pytest tests/test_auth.py -v
```

## 9. FR-01 — Equipment Catalogue

**Owner:** Sinthu (`sinthu02`)
**Issue:** [#2](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/2)

Implemented functionality:

- Authenticated Students and Staff can browse equipment.
- Category filtering.
- Staff-only equipment creation, editing and deletion.
- Name/category/description validation.
- Equipment status: Available or Out of service.
- Server-side authorization checks, not just hidden buttons.

### Equipment routes

| Feature | Route | Allowed user |
|---|---|---|
| View/filter equipment | `/equipment/` | Logged-in Student or Staff |
| Add equipment | `/equipment/new` | Staff |
| Edit equipment | `/equipment/<id>/edit` | Staff |
| Delete equipment | `/equipment/<id>/delete` (POST) | Staff |

A Student trying a Staff-only URL receives HTTP 403. A user who is not logged in is redirected to login.

Run FR-01 tests:

```powershell
python -m pytest tests/test_equipment.py -v
```

## 10. FR-02 — Booking Requests

**Owner:** Sumaiya (`fathimasumaiya884-collab`)
**Issue:** [#3](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/3)

Implemented functionality:

- Logged-in Students choose available equipment.
- Students enter a booking date, start time and end time.
- Booking records are linked to the logged-in Student and the selected Equipment.
- Every new booking is saved with Pending status.
- Students can view **only their own** booking requests.
- Anonymous users are redirected to login; Staff cannot use Student booking routes.
- Basic form checks reject invalid date/time input, missing equipment, equipment marked Out of service, and end times not after start times.

### Booking routes

| Feature | Route | Allowed user |
|---|---|---|
| New booking request | `/bookings/new` | Student |
| My booking requests | `/bookings/` | Student |

### Example Student workflow

1. Register or log in at `/auth/login`.
2. Open `/equipment/` to view the catalogue.
3. Select **Request Equipment** on the homepage, or go to `/bookings/new`.
4. Choose an Available item and enter the date, start and end times.
5. Submit the request.
6. View it at `/bookings/` with **Pending** status.

Run FR-02 tests:

```powershell
python -m pytest tests/test_booking.py -v
```

## 11. FR-03 — Booking Validation: E2 Progress and E3 Completion

**Owner:** Vijaha (`HasVij`)
**Issue:** [#4](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/4)

FR-02 already checks time ordering and Equipment service status. The remaining FR-03 validation work is tracked separately, and Issue #4 remains open until the complete requirement is implemented and tested.

### E2 targets

- Prepare a test design using **Boundary Value Analysis (BVA)** and **Equivalence Partitioning (EP)**.
- Implement and test selected time validations, including the proposed 30-minute minimum, four-hour maximum and past-booking checks.
- Record positive/negative tests and evidence in `TESTING.md`.
- Demonstrate work in progress with a feature branch, PR and CI evidence.

### Duration boundaries for test design

| Case | Duration | Expected when FR-03 rules are active |
|---|---|---|
| BVA-01 | 29 minutes | Reject |
| BVA-02 | 30 minutes | Accept |
| BVA-03 | 31 minutes | Accept |
| BVA-04 | 239 minutes | Accept |
| BVA-05 | 240 minutes | Accept |
| BVA-06 | 241 minutes | Reject |

### Remaining E3 scope

- Prevent booking time slots in the past.
- Enforce both duration boundaries throughout the application.
- Detect overlapping requests according to agreed status/conflict rules.
- Integrate validation with Staff decisions.
- Add comprehensive boundary, equivalence, negative and integration tests.

**Important:** Do not mark Issue #4 Done just because the initial E2 validation PR is merged. Keep it open and **In progress** for E3 work. The E2 PR should say `Part of #4`, **not** `Closes #4`.

The planned tests may run with the following command **after** the files have been added to the relevant branch:

```powershell
python -m pytest tests/test_booking_validation.py -v
```

## 12. FR-04 — Booking Approval and Status: E3

**Owner:** Aadhil (`aadhil-nisar`)
**Issue:** [#5](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/5)

Planned functionality:

- Staff view Pending booking requests.
- Staff approve or reject requests.
- Status changes are saved as Approved or Rejected.
- Students can view their resulting status.
- Approval actions are restricted to Staff.
- Booking-conflict checks are integrated with approval.
- Automated tests cover authorization and status changes.

**Status:** Planned for E3; not yet available on `main`.

## 13. Automated Testing and Coverage

Tests use pytest with fixtures defined in `tests/conftest.py`. The configured test database uses **SQLite in memory** and disables CSRF **only for automated Flask test-client requests**. CSRF remains enabled for normal browser requests.

### Run individual test suites

```powershell
python -m pytest tests/test_smoke.py -v
python -m pytest tests/test_auth.py -v
python -m pytest tests/test_equipment.py -v
python -m pytest tests/test_booking.py -v
python -m pytest tests/test_e2_integration.py -v
```

### Run all tests

```powershell
python -m pytest -v
```

### Generate a coverage report

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

### Check Python code quality

```powershell
python -m ruff check .
```

Use `TESTING.md` to record **actual** test results, boundary/equivalence cases, manual test evidence, coverage percentage, failed tests and defect resolutions. Do not invent a pass count or coverage figure.

## 14. Continuous Integration (GitHub Actions)

Workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

GitHub Actions runs for pushes and pull requests. The existing workflow:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs dependencies from `requirements.txt`.
4. Runs `python -m ruff check .`.
5. Runs `python -m pytest --cov=app --cov-report=term-missing`.

PRs must have green checks on the latest commit before being merged. If CI fails, open the failed job logs, fix the cause on the feature branch, push again and wait for the rerun.

## 15. GitHub Issues, Branches, PRs and Peer Reviews

### Standard contribution workflow

1. Open the assigned Issue and confirm acceptance criteria.
2. Update the Issue's GitHub Project status to **In progress**.
3. Pull the latest `main` and create a feature branch.
4. Implement the change and write automated tests.
5. Run pytest, Ruff and coverage locally.
6. Update relevant documentation and `TESTING.md`.
7. Review `git status --short` and staged diff before committing.
8. Push to GitHub and open a PR targeting `main`.
9. Link the Issue and request a **different** team member as reviewer.
10. Reviewer checks **Files changed**, leaves a **written PR review note**, and Approves or Requests changes according to `REVIEW_CHECKLIST.md`.
11. Resolve review feedback and confirm latest CI is green.
12. Aadhil coordinates merge/integration; update the Project board and Issue state.

### Example Git commands

```powershell
git status --short
git switch main
git pull --ff-only origin main
git switch -c feature/FR-XX-description
# Make changes and run tests
git status --short
git add <specific-file-paths>
git --no-pager diff --cached --stat
git diff --cached --check
git commit -m "Implement FR-XX feature and tests"
git push -u origin feature/FR-XX-description
```

Replace the example branch and file placeholders; do not paste `<specific-file-paths>` literally into PowerShell. Avoid committing `.venv/`, `instance/`, `*.db`, `.env`, passwords or local test/coverage caches.

### Module PR review assignments

| Work | Developer | Reviewer | Integration |
|---|---|---|---|
| E1 Flask/database/tests/CI | Aadhil | Sinthu | Aadhil |
| E1 README/review checklist | Koparnika | Vijaha | Aadhil |
| FR-00 | Koparnika | Sumaiya | Aadhil |
| FR-01 | Sinthu | Vijaha | Aadhil |
| FR-02 | Sumaiya | Sinthu | Aadhil |
| FR-03 E2 initial validation | Vijaha | Sumaiya | Aadhil |
| FR-04 E3 | Aadhil | Another non-author team member | Team |

Every reviewer should leave a dated summary in the GitHub PR review with the checked functionality, test/CI evidence, issues found and decision. The **PR conversation is the review record**; do not overwrite README or the review checklist for each individual review.

For completed functional requirements, the PR description can include `Closes #N` so GitHub closes the Issue when merged. For **partial FR-03 E2 progress**, link `Part of #4` instead so the Issue stays open.

### GitHub Projects board

The board uses:

`Backlog → To do → In progress → In review → Done`

- **In progress:** Member is implementing or fixing the task.
- **In review:** A PR is open and awaiting review/CI.
- **Done:** Work is approved, checks pass and the PR is merged.
- **FR-03 exception:** After partial E2 work is merged, return Issue #4 to **In progress** until E3 completion.

**Coordination:** Koparnika maintains the board with Sumaiya's co-coordinator support.

## 16. E2 Evaluation Demonstration Plan (Approximately 15 Minutes)

| Approx. time | Presenter | Demonstration |
|---|---|---|
| 1 min | Koparnika | Project overview, Issues, team roles and board |
| 3 min | Koparnika | FR-00 Student registration/login/logout and Staff restriction |
| 3 min | Sinthu | FR-01 catalogue, filter and Staff add/edit controls |
| 3 min | Sumaiya | FR-02 Student request, Pending status and own-bookings view |
| 2 min | Vijaha | FR-03 initial validation design, boundary tests and progress |
| 2 min | Aadhil | pytest, Ruff, coverage, GitHub Actions and reviewed PR evidence |
| 1 min | Team | Integration summary, limitations and E3 plan |

Prepare test accounts and sample equipment **locally** in advance; do not share passwords. Use a separate test account for Student and Staff. If FR-03 validation code is still under review, distinguish its feature-branch demonstration from merged `main` functionality.

### Evidence to have ready

- Functional demo of FR-00, FR-01 and FR-02.
- GitHub Issues and Project board status.
- Feature branches, PRs and **written reviewer notes**.
- GitHub Actions results for the latest merged changes.
- pytest/Ruff/coverage output.
- `TESTING.md` with BVA/EP plan and actual results.
- Clear explanation of E3 remaining work.

## 17. Security, Data Integrity and Development Notes

- Never commit passwords, secret keys or real user credentials.
- Store passwords as hashes, not plaintext.
- Enforce Student/Staff restrictions on the **server**, not only by hiding links.
- Keep CSRF enabled for browser forms; tests use an isolated test configuration.
- Confirm booking ownership using the logged-in session, not editable form input.
- Validate incoming equipment, dates, times and status values server-side.
- Protect bookings when changing/deleting referenced equipment during future integration.
- Do not use the Flask debug server for production deployment.
- Perform code review and resolve CI errors before merging.

## 18. Current Project Status

**E1:** Completed — Flask and SQLite foundation, tests, CI, documentation and GitHub workflow established.

**E2:** FR-00, FR-01 and FR-02 have been implemented and merged. Initial FR-03 validation development/testing and final intermediate-review preparation are in progress.

**E3:** Finish FR-03 overlap/conflict validation, implement FR-04 approval/rejection, close remaining integration gaps, and complete final testing and documentation.

For up-to-date progress, use the [repository](https://github.com/aadhil-nisar/lab-equipment-booking-system), [Issues](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues), [Pull Requests](https://github.com/aadhil-nisar/lab-equipment-booking-system/pulls), and `TESTING.md` rather than relying on this snapshot alone.
