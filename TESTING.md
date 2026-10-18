# E2 Testing Plan and Evidence

**Project:** Lab Equipment Booking System
**Coursework:** Software Engineering Mini Project
**Evaluation:** E2 — Intermediate Review, Monday 19 October 2026
**Repository:** https://github.com/aadhil-nisar/lab-equipment-booking-system
**Evidence status:** This file is a testing plan and results log. Update the *Actual result* and evidence links after running tests; do not mark unverified checks as passed.

## 1. Testing Responsibilities

| Team member | GitHub username | Module / testing responsibility |
|---|---|---|
| Koparnika | `koparnikasrikaran2002-gif` | FR-00 Accounts and Login; Coordinator; maintain the GitHub Project board |
| Sinthu | `sinthu02` | FR-01 Equipment Catalogue; Review Lead |
| Sumaiya | `fathimasumaiya884-collab` | FR-02 Booking Requests; Co-Coordinator |
| Vijaha | `HasVij` | FR-03 Booking Validation; QA Lead; BVA and EP test design |
| Aadhil | `aadhil-nisar` | Integration, CI, final checks and merge coordination |

### Review assignments

| Change | Developer | Reviewer | Review evidence |
|---|---|---|---|
| FR-00 | Koparnika | Sumaiya | PR #11; inspect its review history |
| FR-01 | Sinthu | Vijaha | PR #12; inspect its review history |
| FR-02 | Sumaiya | Sinthu | PR #14; inspect its review history |
| FR-03 E2 progress | Vijaha | Sumaiya | Add PR number and review URL when opened |
| E2 integration | Aadhil | Independent team reviewer | PR #13; inspect its review history |

PR links:
- FR-00: https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/11
- FR-01: https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/12
- FR-02: https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/14
- E2 integration: https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/13

## 2. E2 Scope and Current Implementation

| Requirement | Expected E2 demonstration | Repository state checked 18 Oct 2026 |
|---|---|---|
| FR-00 | Registration, login/logout, Student/Staff roles, access control | Implementation present on `main` |
| FR-01 | Equipment listing/filtering and Staff CRUD | Implementation present on `main` |
| FR-02 | Student booking form, Pending requests, own-request list | Implementation present on `main` |
| FR-03 | Initial validation rules, BVA/EP and tests | Issue #4 open; standalone E2 validator/tests not yet found on `main` |
| FR-04 | Staff approval/rejection | E3 scope; not required as a complete E2 feature |

**Important:** Source code being present does not prove that a test passed or that the reviewer approved it. Record command output and GitHub Actions evidence separately.

## 3. Test Environment and Commands

**Supported development environment:** Python 3.11+, Flask, Flask-SQLAlchemy, SQLite, pytest, pytest-cov and Ruff.
**Test database:** Tests use an in-memory SQLite database via `tests/conftest.py`.
**CSRF:** Disabled only in test-client configuration; real browser POST forms use CSRF tokens.

From the repository root in VS Code PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run each module individually:

```powershell
python -m pytest tests/test_auth.py -v
python -m pytest tests/test_equipment.py -v
python -m pytest tests/test_booking.py -v
```

After `tests/test_booking_validation.py` has been added to the current branch, also run:

```powershell
python -m pytest tests/test_booking_validation.py -v
```

Run the complete test suite, lint and coverage:

```powershell
python -m pytest -v
python -m ruff check .
python -m pytest --cov=app --cov-report=term-missing
```

**Record results:**

| Check | Actual result | Evidence (terminal output / link) |
|---|---|---|
| FR-00 pytest | Not recorded | Add evidence |
| FR-01 pytest | Not recorded | Add evidence |
| FR-02 pytest | Reported passing locally; attach latest output | Add evidence |
| FR-03 pytest | Pending E2 implementation | Add evidence |
| Full pytest suite | Not recorded | Add evidence |
| Ruff | Not recorded | Add evidence |
| Coverage percentage | Not recorded | Add percentage and output |
| GitHub Actions on latest PR | Not recorded | Add workflow/checks URL |

## 4. FR-00 — Accounts and Authentication

**Owner:** Koparnika
**Test file:** `tests/test_auth.py`

| ID | Test case | Expected result | Actual result |
|---|---|---|---|
| AUTH-01 | Register with valid Student details | Account created; password hashed | Not recorded |
| AUTH-02 | Attempt public registration with Staff role | Account remains Student | Not recorded |
| AUTH-03 | Invalid username, email or password | Registration rejected | Not recorded |
| AUTH-04 | Duplicate username/email | Registration rejected | Not recorded |
| AUTH-05 | Correct username/password | Login successful | Not recorded |
| AUTH-06 | Incorrect password | Login rejected | Not recorded |
| AUTH-07 | Logout | Session ends; public homepage shown | Not recorded |
| AUTH-08 | Anonymous access to Staff page | Redirect to Login | Not recorded |
| AUTH-09 | Student opens Staff page | HTTP 403 | Not recorded |
| AUTH-10 | Manually created Staff account | Staff login and Staff page work | Not recorded |

**Manual checks:** Verify Register, Login, Logout and the Staff page in the browser. Never place real passwords or application secrets in screenshots or this file.

## 5. FR-01 — Equipment Catalogue

**Owner:** Sinthu
**Reviewer:** Vijaha
**Test file:** `tests/test_equipment.py`

| ID | Test case | Expected result | Actual result |
|---|---|---|---|
| EQ-01 | Anonymous catalogue access | Redirect to Login | Not recorded |
| EQ-02 | Student catalogue access | HTTP 200 | Not recorded |
| EQ-03 | Filter by category | Only matching equipment displayed | Not recorded |
| EQ-04 | Empty catalogue | “No equipment found” displayed | Not recorded |
| EQ-05 | Student attempts to add equipment | HTTP 403; no record saved | Not recorded |
| EQ-06 | Student attempts to edit equipment | HTTP 403; no change | Not recorded |
| EQ-07 | Student attempts to delete equipment | HTTP 403; record retained | Not recorded |
| EQ-08 | Staff creates equipment | Record saved | Not recorded |
| EQ-09 | Staff edits equipment | Record updated | Not recorded |
| EQ-10 | Staff deletes equipment | Record removed | Not recorded |
| EQ-11 | Invalid name/category/description/status | HTTP 400; no invalid record saved | Not recorded |
| EQ-12 | DELETE route requested via GET | HTTP 405 | Not recorded |
| EQ-13 | Unknown equipment ID | HTTP 404 | Not recorded |

**Manual checks:** Login as Staff to add, edit, filter and delete a disposable equipment record. Login as Student to confirm read-only access and a 403 response to `/equipment/new`.

## 6. FR-02 — Booking Requests

**Owner:** Sumaiya
**Reviewer:** Sinthu
**Test file:** `tests/test_booking.py`

| ID | Test case | Expected result | Actual result |
|---|---|---|---|
| BOOK-01 | Anonymous opens booking form | Redirect to Login | Not recorded |
| BOOK-02 | Student opens booking form | HTTP 200 and equipment list | Not recorded |
| BOOK-03 | Valid booking submission | Booking stored in SQLite | Not recorded |
| BOOK-04 | Booking status supplied by Student | Server stores Pending, not an injected status | Not recorded |
| BOOK-05 | Student opens own booking list | Own requests and status displayed | Not recorded |
| BOOK-06 | Student opens list with only another Student's booking | Other Student's booking hidden | Not recorded |
| BOOK-07 | End time before start time | HTTP 400; no booking | Not recorded |
| BOOK-08 | Out-of-service equipment | HTTP 400; no booking | Not recorded |
| BOOK-09 | Staff tries to submit Student request | HTTP 403 | Not recorded |

**Manual checks:** Submit a valid booking from a Student account; confirm the selected equipment, date, start/end time and Pending status in `/bookings/`. Login as a different Student to check privacy.

## 7. FR-03 — Initial Booking Validation (E2)

**Developer:** Vijaha (`HasVij`)
**Reviewer:** Sumaiya (`fathimasumaiya884-collab`)
**Related issue:** https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/4
**Planned test file:** `tests/test_booking_validation.py`
**Issue state:** Open; **do not use** `Closes #4` in the E2-only PR.

### E2 validation rules

- Preserve the existing end-time-after-start-time check.
- Enforce a minimum duration of **30 minutes** (inclusive).
- Enforce a maximum duration of **4 hours** (inclusive).
- Reject requests that start in the past.
- Preserve the existing rejection of out-of-service equipment.
- Provide understandable validation errors without creating invalid bookings.

**Not yet implemented in the checked `main` branch:** Vijaha's new duration/past-date validator and the dedicated validation tests. Do not mark them Pass until the code is present and checked. Overlapping booking detection and Staff approval revalidation are scheduled for E3.

### 7.1 Boundary Value Analysis (BVA)

Use a booking date sufficiently in the future when testing durations.

| ID | Start time | End time | Duration | Expected | Actual |
|---|---|---|---|---|---|
| BVA-01 | 09:00 | 09:29 | 29 min | Reject — below minimum | Not recorded |
| BVA-02 | 09:00 | 09:30 | 30 min | Accept — minimum boundary | Not recorded |
| BVA-03 | 09:00 | 09:31 | 31 min | Accept | Not recorded |
| BVA-04 | 09:00 | 12:59 | 239 min | Accept | Not recorded |
| BVA-05 | 09:00 | 13:00 | 240 min | Accept — maximum boundary | Not recorded |
| BVA-06 | 09:00 | 13:01 | 241 min | Reject — above maximum | Not recorded |

**Current-time boundary:** A start time equal to or earlier than the server's current time must be rejected; a future start time is a candidate for acceptance if all other rules pass.

### 7.2 Equivalence Partitioning (EP)

| ID | Input class | Example | Expected | Actual |
|---|---|---|---|---|
| EP-01 | Valid booking | Future date, 09:00–10:00, Available item | Accept; Pending | Not recorded |
| EP-02 | Too short | 09:00–09:20 | Reject | Not recorded |
| EP-03 | Too long | 09:00–14:00 | Reject | Not recorded |
| EP-04 | Invalid time ordering | 11:00–10:00 | Reject | Not recorded |
| EP-05 | Past start time | Yesterday, 09:00–10:00 | Reject | Not recorded |
| EP-06 | Equipment unavailable | Out of service | Reject | Not recorded |
| EP-07 | Unknown equipment | ID 999999 | Reject | Not recorded |
| EP-08 | Overlapping booking | 09:30–10:30 versus existing 09:00–10:00 | **E3 design only** | Not implemented |
| EP-09 | Adjacent booking | 10:00–11:00 after 09:00–10:00 | **E3 policy/test** | Not implemented |

### 7.3 Automated E2 validation test evidence

Once Vijaha adds the test file:

```powershell
python -m pytest tests/test_booking_validation.py -v
python -m pytest -v
python -m ruff check .
python -m pytest --cov=app --cov-report=term-missing
```

| Evidence | Actual result | Link or notes |
|---|---|---|
| FR-03 test file added | Pending | Add commit/PR link |
| Boundary tests | Not recorded | Add passing/failed count |
| Flask form validation tests | Not recorded | Add passing/failed count |
| Full regression suite | Not recorded | Add output |
| Ruff | Not recorded | Add output |
| Coverage | Not recorded | Add percentage |
| GitHub Actions | Pending PR | Add check URL |

### 7.4 Remaining E3 work

- Decide whether Pending booking requests reserve a slot or only Approved bookings block it.
- Implement overlapping-booking detection consistent with that policy.
- Test partial, exact, contained and adjacent-time overlaps.
- Recheck booking validity at Staff approval time.
- Integrate with FR-04 approval/rejection and complete regression testing.
- Keep Issue #4 open until all acceptance criteria are satisfied.

## 8. Manual E2 Demonstration Checklist

| Demonstration | Expected evidence | Result |
|---|---|---|
| Student registers and logs in | Homepage shows Student session | Not recorded |
| Staff logs in | Staff-only page accessible | Not recorded |
| Staff creates equipment | Item appears in catalogue | Not recorded |
| Student filters catalogue | Correct equipment category listed | Not recorded |
| Student submits request | Request appears as Pending | Not recorded |
| Student opens My Booking Requests | Only own requests are shown | Not recorded |
| Student attempts Staff equipment action | HTTP 403 | Not recorded |
| Invalid short duration (after FR-03 E2 merge) | Form displays validation error | Not recorded |
| Invalid long duration (after FR-03 E2 merge) | Form displays validation error | Not recorded |
| Past booking (after FR-03 E2 merge) | Form displays validation error | Not recorded |

**Evidence location:** Add screenshot filenames, PR links or demonstration notes here. Avoid screenshots exposing credentials.

## 9. GitHub Actions, PR Review and Project Board

The repository's CI workflow is `.github/workflows/ci.yml`; it installs project requirements, runs Ruff and runs pytest with coverage. Review the **latest commit's** Checks/Actions status before merging each PR.

Review process: **Issue → Branch → Code → Tests → PR → Written peer review → Green CI → Merge → Board update**.

For each PR, the reviewer should:

1. Inspect **Files changed** and follow `REVIEW_CHECKLIST.md`.
2. Verify authorization, database behavior, invalid-input paths and regression tests.
3. Leave a written note identifying findings and checks performed.
4. Submit **Approve** or **Request changes**; the author must address requested changes on the same branch.
5. Allow Aadhil to merge only after approval and current CI passes.

| Requirement | Issue | Board status after E2 completion |
|---|---|---|
| FR-00 | #1 | Done after verified merge |
| FR-01 | #2 | Done after verified merge |
| FR-02 | #3 | Done after verified merge |
| FR-03 | #4 | **In progress** after initial E2 PR merges; continue in E3 |
| FR-04 | #5 | Backlog / To do for E3 |

**FR-03 E2 PR link:** Not yet recorded
**FR-03 reviewer comment/link:** Not yet recorded
**FR-03 latest CI result:** Not yet recorded
**FR-03 E2 merge date:** Not yet recorded

## 10. Known Limitations and Follow-Up

- **Overlap validation:** Not yet implemented as part of completed FR-03 functionality.
- **Staff approval/rejection:** Planned for FR-04 in E3; E2 requests remain Pending.
- **Deleting booked equipment:** FR-01 deletion behavior must be reviewed once bookings reference equipment records, to avoid losing historical associations or database errors.
- **Timezone:** Current booking form interprets times using the server's local clock; production deployment needs an explicit timezone policy.
- **Test results and coverage:** Fill in actual outputs before presenting this document as evidence. Do not claim a result simply because a test is listed.

## 11. Final E2 QA Sign-Off

| Item | Responsible | Status / evidence |
|---|---|---|
| FR-00 manual and automated evidence | Koparnika | Pending documentation |
| FR-01 manual and automated evidence | Sinthu | Pending documentation |
| FR-02 manual and automated evidence | Sumaiya | Pending documentation |
| Initial FR-03 BVA/EP and tests | Vijaha | In progress |
| Overall regression, Ruff and coverage | Aadhil + Vijaha | Pending latest recorded output |
| Written PR reviews | Assigned reviewers | Verify on linked PRs |
| Project statuses and issue links | Koparnika | Verify board after each merge |

**QA Lead:** Vijaha
**Integration Lead:** Aadhil
**Sign-off date and verified results:** To be completed after the final E2 checks.
