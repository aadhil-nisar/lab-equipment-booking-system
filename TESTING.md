# Testing Plan, Test Cases and Evidence — E1 to E3

**Project:** Lab Equipment Booking System  
**Coursework:** Software Engineering Mini Project  
**Repository:** https://github.com/aadhil-nisar/lab-equipment-booking-system  
**E2 Review:** 19 October 2026  
**E3 Final Review:** 23 October 2026  
**Evidence verified:** 22 October 2026, using the latest successful `main` GitHub Actions run dated 21 October 2026.

## Final Verified Results

| Measure | Final merged `main` result |
|---|---|
| Automated tests | **97 passed, 0 failed** |
| Test runtime on CI | **10.68 seconds** (pytest step) |
| Ruff | **All checks passed!** |
| Statement coverage | **96%** |
| Measured Python statements | **390** |
| Executed statements | **376** |
| Missing statements | **14** |
| CI conclusion | **Success** |
| CI link | [Run #39657131371](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39657131371) |
| Branch checked | `main` |

These are actual post-merge GitHub Actions log results, including FR-03 E3 and FR-04. The team's earlier local run was 79 passed and 96% coverage, before the complete E3 overlap-test set was included on `main`.

**Meaning:** 97/97 discovered tests passed in this CI run and 376/390 measured statements were executed. This does **not** establish that every possible behavior is correct.

## 1. Testing Responsibilities and Peer Review

| Member | GitHub | Testing / coordination responsibility |
|---|---|---|
| Koparnika | `koparnikasrikaran2002-gif` | FR-00 accounts; Coordinator and GitHub board |
| Sinthu | `sinthu02` | FR-01 catalogue; Review Lead |
| Sumaiya | `fathimasumaiya884-collab` | FR-02 requests; Co-Coordinator |
| Vijaha | `HasVij` | FR-03 validation, BVA/EP, QA Lead |
| Aadhil | `aadhil-nisar` | FR-04 decisions, integration, CI and regression |

### Verified Pull Requests

| Requirement | Developer | Review evidence | PR and status |
|---|---|---|---|
| FR-00 | Koparnika | Sumaiya: Approved | [#11](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/11), merged |
| FR-01 | Sinthu | Vijaha: Approved | [#12](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/12), merged |
| FR-02 | Sumaiya | Sinthu: Approved | [#14](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/14), merged |
| FR-03 E2 | Vijaha | Sumaiya: Approved | [#15](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15), merged |
| FR-03 E3 | Vijaha | Sumaiya: Approved | [#16](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16), merged |
| E2 integration | Aadhil | Vijaha: Approved | [#13](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/13), merged |
| FR-04 initial | Aadhil | Vijaha: Approved | [#17](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/17), merged |
| FR-04 follow-up | Aadhil | **No submitted review recorded on #18** | [#18](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/18), merged |

For full details, see [REVIEW_CHECKLIST.md](REVIEW_CHECKLIST.md). PR #18's lack of a separate review should not be hidden by the passing tests or the approval on PR #17.

## 2. Scope and Acceptance Criteria

| Requirement | Core verification | Repository status |
|---|---|---|
| FR-00 | Register, login/logout, Staff role restrictions, password hashing | Implemented; Issue #1 closed |
| FR-01 | Catalogue, filter, Staff-only CRUD, invalid input | Implemented; Issue #2 closed |
| FR-02 | Student request, Pending status, Student privacy | Implemented; Issue #3 closed |
| FR-03 | Date/time/duration and overlap checks | Implemented; Issue #4 closed |
| FR-04 | Staff approval/rejection, status persistence, revalidation | Implemented; Issue #5 closed |

### Booking conflict policy

- When **creating a Student request**, existing Pending or Approved bookings for the same equipment/date that overlap are blockers.
- When **approving an existing request**, the application checks conflicts against **Approved** bookings only. This allows Staff to choose one of two overlapping Pending bookings already in the database; it will prevent both from becoming Approved.
- Rejected bookings do not block new requests.
- Adjacent slots are not overlapping, because conflict requires `existing.start < new.end` and `existing.end > new.start`.
- Different dates or different equipment do not conflict.

### Complete Business Rules — FR-00 to FR-04

**Project:** Lab Equipment Booking System  
**Purpose:** Document the business rules implemented across all five functional requirements.  
**Implementation:** Flask, Python, SQLite and SQLAlchemy.  
**Verification:** pytest automated tests and GitHub Actions.

The following 60 rules describe the application's implemented validation, authorization, equipment management, booking and approval behavior.

#### FR-00 — Accounts and Authentication

**Responsible member:** Koparnika  
**Implementation:** `app/routes/auth.py`, `app/models/user.py`, `app/commands.py`  
**Tests:** `tests/test_auth.py`

| Rule ID | Business rule |
|---|---|
| BR-00-01 | Usernames must contain 3–80 characters, using lowercase letters, numbers or underscores. Input is trimmed and converted to lowercase. |
| BR-00-02 | Email addresses must follow the accepted email format and contain no more than 120 characters. |
| BR-00-03 | Account passwords must contain at least 8 characters. |
| BR-00-04 | Password and confirmation password must match during registration. |
| BR-00-05 | Two users cannot register with the same username. |
| BR-00-06 | Two users cannot register with the same email address. |
| BR-00-07 | Public registration always creates a Student account, regardless of any submitted role value. |
| BR-00-08 | Passwords must be stored as secure hashes, not plaintext. |
| BR-00-09 | Login is permitted only when the username exists and the password is correct. |
| BR-00-10 | Invalid credentials must not authenticate the user. |
| BR-00-11 | Staff accounts are provisioned through the `create-staff` command. Staff-only pages must reject Student access with HTTP 403. |

**Example:** A Student cannot create a Staff account by changing the registration form's `role` field.

#### FR-01 — Equipment Catalogue and Management

**Responsible member:** Sinthu  
**Implementation:** `app/routes/equipment.py`, `app/models/equipment.py`  
**Tests:** `tests/test_equipment.py`, `tests/test_staff_bookings.py`

| Rule ID | Business rule |
|---|---|
| BR-01-01 | Only authenticated users can access the Equipment Catalogue. |
| BR-01-02 | Users can view equipment and filter the catalogue by category. |
| BR-01-03 | Only Staff can add new equipment. |
| BR-01-04 | Only Staff can edit equipment details. |
| BR-01-05 | Only Staff can delete equipment. |
| BR-01-06 | Equipment names must contain 1–120 characters after trimming whitespace. |
| BR-01-07 | Equipment categories must contain 1–80 characters after trimming whitespace. |
| BR-01-08 | Equipment descriptions cannot exceed 2,000 characters. |
| BR-01-09 | Equipment status must be either `Available` or `Out of service`. |
| BR-01-10 | Invalid equipment details must be rejected without saving incorrect changes. |
| BR-01-11 | Equipment with any existing booking history cannot be deleted, even when those bookings are Rejected. |

**Example:** Staff cannot delete a microscope that has an existing booking record. The system returns HTTP 409 Conflict.

#### FR-02 — Student Booking Requests

**Responsible member:** Sumaiya  
**Implementation:** `app/routes/booking.py`, `app/models/booking.py`  
**Tests:** `tests/test_booking.py`

| Rule ID | Business rule |
|---|---|
| BR-02-01 | Only authenticated Students can create equipment booking requests. Staff accounts cannot submit Student booking requests. |
| BR-02-02 | A booking request must contain a valid, positive equipment ID. |
| BR-02-03 | The selected equipment must exist in the database. |
| BR-02-04 | Students can submit requests only for equipment currently marked Available. |
| BR-02-05 | Booking dates and times must follow the accepted date and time formats. |
| BR-02-06 | Booking requests must satisfy the date, time and duration validation rules in FR-03. |
| BR-02-07 | New booking requests must be rejected when they overlap existing Pending or Approved bookings for the same equipment and date. |
| BR-02-08 | Every successful new request must start as Pending. The Student ID must come from the authenticated account; Students cannot assign themselves an Approved status. |
| BR-02-09 | Students can view their own booking history but cannot view other Students' booking records through the My Bookings page. |

**Example:** After a Student submits a valid booking, the system stores the request with status `Pending`.

#### FR-03 — Booking Validation

**Responsible member:** Vijaha  
**Implementation:** `app/booking_validation.py`, `app/routes/booking.py`  
**Tests:** `tests/test_booking_validation.py`, `tests/test_booking_overlap.py`

| Rule ID | Business rule |
|---|---|
| BR-03-01 | Booking end time must be later than start time. |
| BR-03-02 | Booking start date and time must be in the future. |
| BR-03-03 | The minimum booking duration is 30 minutes, inclusive. |
| BR-03-04 | The maximum booking duration is 240 minutes (4 hours), inclusive. |
| BR-03-05 | Booking requests for Out-of-service equipment must be rejected. |
| BR-03-06 | Overlap detection must compare bookings for the same equipment. |
| BR-03-07 | Overlap detection must compare bookings on the same date. |
| BR-03-08 | Two bookings overlap when `existing.start_time < requested.end_time` and `existing.end_time > requested.start_time`. |
| BR-03-09 | Existing Pending bookings block overlapping new Student requests. |
| BR-03-10 | Existing Approved bookings block overlapping new Student requests. |
| BR-03-11 | Rejected bookings do not block new booking requests. |
| BR-03-12 | Adjacent time slots are permitted. Bookings for different equipment or dates do not conflict. |

**Boundary Value Analysis (BVA)**

| Duration | Expected |
|---|---|
| 29 minutes | Reject |
| 30 minutes | Accept |
| 31 minutes | Accept |
| 239 minutes | Accept |
| 240 minutes | Accept |
| 241 minutes | Reject |

These values test the minimum and maximum duration boundaries.

**Overlap example**

Existing booking: 09:00–10:00

| New booking | Expected |
|---|---|
| 08:00–09:00 | No conflict |
| 08:59–09:30 | Conflict |
| 09:00–10:00 | Conflict |
| 09:30–10:30 | Conflict |
| 09:59–11:00 | Conflict |
| 10:00–11:00 | No conflict |
| 08:00–11:00 | Conflict |

The time intervals above are assessed on the same date and for the same equipment.

#### FR-04 — Staff Booking Approval and Status

**Responsible member:** Aadhil  
**Implementation:** `app/routes/staff_bookings.py`  
**Tests:** `tests/test_staff_bookings.py`  
**Pull Requests:** #17 and #18

| Rule ID | Business rule |
|---|---|
| BR-04-01 | Users must be authenticated before accessing Staff booking management. |
| BR-04-02 | Only users with the Staff role can approve, reject or manage booking decisions. Students receive HTTP 403. |
| BR-04-03 | The Staff dashboard displays Pending requests in date/time order and up to 30 recent Approved or Rejected bookings. |
| BR-04-04 | Approval and rejection operations must use HTTP POST requests rather than GET. |
| BR-04-05 | Booking decision requests with unknown booking IDs must return HTTP 404. |
| BR-04-06 | Only Pending bookings can be approved or rejected. Repeated decisions must be blocked with HTTP 409. |
| BR-04-07 | Before approval, the selected equipment must still exist and have Available status. |
| BR-04-08 | Before approval, booking dates, times and durations must be revalidated against FR-03 rules. |
| BR-04-09 | During Staff approval, overlapping bookings with Approved status block the decision. Other Pending requests do not automatically block approval. |
| BR-04-10 | The selected booking ID must be excluded from its own conflict check. |
| BR-04-11 | If an Approved-booking conflict exists, the approval must return HTTP 409 and leave the request Pending. |
| BR-04-12 | Successful approval must change the booking status to Approved and commit the change to SQLite. |
| BR-04-13 | Successful rejection must change the status to Rejected and save it. Rejected bookings retain their history, free the time slot, and the updated status is visible in the Student's booking history. |

**Example — Double-booking prevention**

Two existing Pending bookings request the same microscope on the same future date:

- Booking A: 09:00–10:00
- Booking B: 09:30–10:30

Staff approves Booking A.

Expected result:

- Booking A becomes Approved.
- Booking B remains Pending.
- Approving Booking B is blocked with HTTP 409 because it overlaps Booking A.

This rule is tested by:

`test_staff_can_choose_one_of_two_pending_overlaps`

**Main implementation:**

`has_booking_conflict()` is called with `exclude_booking_id=booking.id` and `blocking_statuses=("Approved",)` before changing the booking status.

#### Cross-Module Business Rules

**Responsible members:** Entire development team

| Rule ID | Business rule |
|---|---|
| BR-CM-01 | User roles must be restricted to Student and Staff, as enforced by the database model. |
| BR-CM-02 | Booking statuses must be restricted to Pending, Approved and Rejected, as enforced by the database model. |
| BR-CM-03 | Protected operations must enforce server-side authorization, and mutating browser forms use POST and CSRF protection. |
| BR-CM-04 | Invalid operations must not incorrectly modify persisted data. Automated tests verify this for the relevant booking and equipment operations. |

#### Business Rule Verification

Business rules are verified through the automated tests in:

- `tests/test_auth.py` — Authentication and role rules.
- `tests/test_equipment.py` — Equipment management rules.
- `tests/test_booking.py` — Student booking rules.
- `tests/test_booking_validation.py` — Booking duration and date rules.
- `tests/test_booking_overlap.py` — Overlap and booking-status policies.
- `tests/test_staff_bookings.py` — Staff approval, rejection and conflict rules.

**Latest verified automated QA evidence (25 October 2026):**

- 97 tests passed.
- 0 failed.
- Ruff passed.
- 96% statement coverage.

**GitHub Actions run:** https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/40149580359

**Note:** These rules document current application behavior. Automated test success does not replace independent review or prove protection against every possible concurrent booking scenario.

## 3. Environment, Commands and Results

**Framework:** Flask / Flask-SQLAlchemy / Flask-Login / Flask-WTF.  
**Test framework:** pytest and pytest-cov.  
**Lint:** Ruff.  
**CI Python:** 3.11.  
**Test database:** in-memory SQLite from `tests/conftest.py`.  
**CSRF:** disabled only for test-client requests; real browser forms keep CSRF protection.

### Commands — Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest tests/test_auth.py -v
python -m pytest tests/test_equipment.py -v
python -m pytest tests/test_booking.py -v
python -m pytest tests/test_booking_validation.py -v
python -m pytest tests/test_booking_overlap.py -v
python -m pytest tests/test_staff_bookings.py -v
python -m pytest tests/test_e2_integration.py -v
python -m pytest tests/test_smoke.py -v
python -m pytest -v
python -m ruff check .
python -m pytest --cov=app --cov-report=term-missing
```

For a detailed local coverage view:

```powershell
python -m pytest --cov=app --cov-report=term-missing --cov-report=html:htmlcov --cov-report=json:coverage.json
Start-Process .\htmlcov\index.html
python -m pytest --collect-only -q
```

Do not commit generated coverage output or the local SQLite database.

### Results register

| Check | Verified automated evidence |
|---|---|
| Full pytest regression | 97 passed, 0 failed — final `main` CI |
| Ruff lint | All checks passed — final `main` CI |
| Coverage | 96% — final `main` CI |
| FR-00 to FR-04 | Included in passing regression suite |
| FR-03 overlap tests | `tests/test_booking_overlap.py` included in passing suite |
| FR-04 approval tests | `tests/test_staff_bookings.py` included in passing suite |
| Browser manual tests | Team demonstrated functionality during development; retain dated screenshots/notes if required for formal sign-off |
| Latest CI | https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39657131371 |

## 4. FR-00 — Accounts and Authentication

**Owner:** Koparnika · **Reviewer:** Sumaiya · **Test file:** `tests/test_auth.py`.

| ID | Test case | Expected outcome |
|---|---|---|
| AUTH-01 | Valid Student registration | Student created; hashed password |
| AUTH-02 | Public registration attempts Staff role | Account remains Student |
| AUTH-03 | Invalid username/email/password | Rejected |
| AUTH-04 | Duplicate username/email | Rejected |
| AUTH-05 | Correct credentials | Login successful |
| AUTH-06 | Incorrect password | Login rejected |
| AUTH-07 | Logout | Session ended |
| AUTH-08 | Anonymous opens Staff page | Redirect to login |
| AUTH-09 | Student opens Staff page | HTTP 403 |
| AUTH-10 | Staff CLI registration and login | Staff authenticated; Dashboard accessible |

**Automated result:** Included in 97 passing CI tests.  
**Manual demo:** Register/login/logout as Student, then access `/auth/staff` as Student and as Staff. Keep real credentials out of evidence screenshots.

## 5. FR-01 — Equipment Catalogue

**Owner:** Sinthu · **Reviewer:** Vijaha · **Test file:** `tests/test_equipment.py`.

| ID | Test case | Expected outcome |
|---|---|---|
| EQ-01 | Anonymous opens catalogue | Redirect to login |
| EQ-02 | Student opens catalogue | HTTP 200 |
| EQ-03 | Filter by category | Matching equipment shown |
| EQ-04 | Empty catalogue | Appropriate empty-state message |
| EQ-05 | Student creates equipment | HTTP 403 |
| EQ-06 | Student edits equipment | HTTP 403 |
| EQ-07 | Student deletes equipment | HTTP 403 |
| EQ-08 | Staff creates equipment | Saved |
| EQ-09 | Staff edits equipment | Updated |
| EQ-10 | Staff deletes unused equipment | Deleted |
| EQ-11 | Invalid equipment values | Rejected without invalid save |
| EQ-12 | GET request to delete endpoint | HTTP 405 |
| EQ-13 | Unknown equipment ID | HTTP 404 |
| EQ-14 | Delete equipment with booking history | HTTP 409; equipment and booking retained |

**Automated result:** Included in passing CI suite; EQ-14 is also exercised in `tests/test_staff_bookings.py`.  
**Manual demo:** Staff CRUD/category filter; Student read-only access. Use an unused sample item for deletion.

## 6. FR-02 — Booking Requests

**Owner:** Sumaiya · **Reviewer:** Sinthu · **Test file:** `tests/test_booking.py`.

| ID | Test case | Expected outcome |
|---|---|---|
| BOOK-01 | Anonymous opens request form | Redirect to login |
| BOOK-02 | Student opens request form | HTTP 200 |
| BOOK-03 | Valid future request | Booking stored |
| BOOK-04 | Student injects Approved status | Server stores Pending |
| BOOK-05 | Student views own requests | Own history and statuses |
| BOOK-06 | Another Student has a booking | Other Student's booking hidden |
| BOOK-07 | End time before start | Request rejected |
| BOOK-08 | Out-of-service equipment | Request rejected |
| BOOK-09 | Staff submits Student request | HTTP 403 |

**Automated result:** Included in passing CI suite.  
**Manual demo:** Student submits a valid future booking, confirms Pending status, and later checks Approved/Rejected decision.

## 7. FR-03 — Booking Validation (BVA and EP)

**Owner:** Vijaha · **Reviewer:** Sumaiya.  
**Files:** `app/booking_validation.py`, `tests/test_booking_validation.py`, `tests/test_booking_overlap.py`.  
**E2 PR:** #15, merged · **E3 PR:** #16, merged.

### 7.1 Duration and date rules

- Start must be in the future.
- End must follow start.
- Duration must be at least **30 minutes** and at most **4 hours**, inclusive.
- Equipment must exist and be Available.

### 7.2 Boundary Value Analysis (BVA)

Use a booking date sufficiently in the future.

| ID | Start | End | Duration | Expected |
|---|---|---|---|---|
| BVA-01 | 09:00 | 09:29 | 29 min | Reject: below minimum |
| BVA-02 | 09:00 | 09:30 | 30 min | Accept |
| BVA-03 | 09:00 | 09:31 | 31 min | Accept |
| BVA-04 | 09:00 | 12:59 | 239 min | Accept |
| BVA-05 | 09:00 | 13:00 | 240 min | Accept |
| BVA-06 | 09:00 | 13:01 | 241 min | Reject: above maximum |
| BVA-07 | 09:00 | 09:00 | Zero min | Reject: end not after start |
| BVA-08 | 11:00 | 10:00 | Negative interval | Reject |
| BVA-09 | Yesterday | — | Past start | Reject |
| BVA-10 | Same day at/before now | — | Past or current start | Reject |

### 7.3 Equivalence Partitioning (EP)

| ID | Input class | Expected |
|---|---|---|
| EP-01 | Valid future duration and Available equipment | Accept; Pending |
| EP-02 | Duration shorter than 30 minutes | Reject |
| EP-03 | Duration over four hours | Reject |
| EP-04 | End time not after start | Reject |
| EP-05 | Past start | Reject |
| EP-06 | Out-of-service equipment | Reject |
| EP-07 | Unknown equipment | Reject |
| EP-08 | Overlap with Pending reservation on Student submission | Reject |
| EP-09 | Overlap with Approved reservation on Student submission | Reject |
| EP-10 | Overlap only with Rejected reservation | Allow |
| EP-11 | Adjacent interval | Allow |
| EP-12 | Different equipment/date | Allow |

### 7.4 Overlap boundary cases

Existing booking **09:00–10:00** on the same date/equipment:

| New interval | Overlap? |
|---|---|
| 08:00–09:00 | No — adjacent before |
| 08:59–09:30 | Yes — starts before |
| 09:00–10:00 | Yes — exact |
| 09:30–10:30 | Yes — partial overlap |
| 09:59–11:00 | Yes — ends later |
| 10:00–11:00 | No — adjacent after |
| 08:00–11:00 | Yes — contains existing |

These cases are covered by the dedicated FR-03 overlap test suite. All E3 tests are included in the successful final CI run.

## 8. FR-04 — Staff Approval and Status

**Owner:** Aadhil · **QA reviewer on PR #17:** Vijaha.  
**Files:** `app/routes/staff_bookings.py`, `app/templates/staff/bookings.html`, `tests/test_staff_bookings.py`.  
**Merged PRs:** #17 and #18.

| ID | Scenario | Expected outcome |
|---|---|---|
| STAFF-01 | Staff opens dashboard | Pending requests displayed |
| STAFF-02 | Anonymous user visits Staff routes | Redirect to login |
| STAFF-03 | Student views or posts Staff decision | HTTP 403; no status change |
| STAFF-04 | Staff approves valid Pending booking | Approved, saved and visible to Student |
| STAFF-05 | Staff rejects Pending booking | Rejected, saved and visible to Student |
| STAFF-06 | Rejected booking occupies former slot | New request can use that slot |
| STAFF-07 | Staff repeats same decision | HTTP 409 |
| STAFF-08 | Approve after Rejected | HTTP 409 |
| STAFF-09 | Approve Out-of-service equipment | Blocked, status remains Pending |
| STAFF-10 | Approve expired booking | Blocked, status remains Pending |
| STAFF-11 | Approve overlapping existing Approved booking | Blocked |
| STAFF-12 | Two already-Pending overlaps | Staff may approve one, not both |
| STAFF-13 | Unknown booking ID | HTTP 404 |
| STAFF-14 | Use GET for approve/reject | HTTP 405 |
| STAFF-15 | Delete equipment with booking history | HTTP 409; history retained |

### Distinct validation policies at request and approval stages

`has_booking_conflict(..., blocking_statuses=("Pending", "Approved"))` is the default for Student request submission. Staff approval calls `has_booking_conflict(..., exclude_booking_id=booking.id, blocking_statuses=("Approved",))` to make a decision among legacy/competing Pending requests. This prevents the mutual-blocking problem found during manual testing.

**Automated result:** The final CI includes and passes `tests/test_staff_bookings.py`.

## 9. Manual E3 Demonstration and Acceptance Checklist

This is a **manual** evidence checklist. A passing automated suite does not automatically mean that a particular live demonstration was recorded. Complete the *Observed / evidence* column during rehearsal or evaluation.

| Demo action | Expected | Observed / evidence |
|---|---|---|
| Register Student | Student account created | Record screenshot or date |
| Student logs in | Student homepage | Record |
| Staff logs in | Staff Dashboard | Record |
| Student opens Staff URL | 403 | Record |
| Staff creates and filters equipment | Catalogue updated | Record |
| Student requests future slot | Pending | Record |
| Student requests too-short or too-long slot | Rejected | Record |
| Student requests existing active slot | Conflict rejected | Record |
| Staff approves valid Pending request | Approved | Record |
| Staff rejects another request | Rejected | Record |
| Student sees decision | Status displayed | Record |
| Staff tries to approve expired booking | Blocked | Record |
| Staff tries to approve already-Approved conflict | Blocked | Record |
| Show CI and coverage | 97 passed, Ruff passed, 96% | [CI evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39657131371) |

Use dates after the current day; avoid putting passwords, real secrets or personal account data in screenshots.

## 10. Coverage Report — Verified `main` CI

The following values are from the **21 October 2026** GitHub Actions log:

| Application file | Statements | Missed | Coverage |
|---|---:|---:|---:|
| `app/__init__.py` | 31 | 0 | 100% |
| `app/booking_validation.py` | 26 | 0 | 100% |
| `app/commands.py` | 28 | 5 | 82% |
| `app/extensions.py` | 14 | 2 | 86% |
| `app/models/__init__.py` | 4 | 0 | 100% |
| `app/models/booking.py` | 13 | 0 | 100% |
| `app/models/equipment.py` | 8 | 0 | 100% |
| `app/models/user.py` | 18 | 0 | 100% |
| `app/routes/__init__.py` | 0 | 0 | 100% |
| `app/routes/auth.py` | 61 | 2 | 97% |
| `app/routes/booking.py` | 56 | 4 | 93% |
| `app/routes/equipment.py` | 77 | 1 | 99% |
| `app/routes/staff_bookings.py` | 54 | 0 | 100% |
| **TOTAL** | **390** | **14** | **96%** |

**Executed statements:** 390 − 14 = **376**.  
**Source:** https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39657131371

High coverage supports confidence but cannot prove that all paths, concurrency conditions or real-world outcomes are correct.

## 11. GitHub Actions, Review and Project Evidence

**Workflow:** `.github/workflows/ci.yml`  
**Process:** Issue → Branch → Code → Tests → PR → Review → CI → Merge → Board update.

### CI result

- Date: **21 October 2026** (UTC).
- Branch: `main`.
- Result: **Success**.
- Ruff: **All checks passed!**
- pytest: **97 passed in 10.68s**.
- Coverage: **96%**.
- Link: https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39657131371

### GitHub Issues

All five functional requirement Issues (#1–#5) are **closed**. This verifies Issue status; individual Project board cards should still be checked for their Done column.

### Peer review nuance

PRs #11–#17 have the approved reviews listed above. For **PR #18**, the repository shows successful merging and CI but **no submitted independent review on #18**. An independent post-merge audit comment may be added as follow-up evidence; it should not be described as pre-merge approval.

## 12. Known Limitations and Future QA

- The development server is not production hosting.
- Booking dates/times follow the server's local clock; define a timezone for production.
- Test coverage is 96%; 14 application statements were not executed in the reported suite.
- Concurrent approval changes are not guaranteed atomic across separate Staff workers; production would need stronger database-level transaction protections.
- Manual demonstration screenshots/signatures need to be captured where the university requires separate proof.
- The PR #18 review-evidence gap should be documented transparently rather than marked completed.

## 13. Final E3 QA Sign-Off

| Requirement or check | Responsible | Status / evidence |
|---|---|---|
| FR-00 implementation and tests | Koparnika | Merged; passing CI |
| FR-01 implementation and tests | Sinthu | Merged; passing CI |
| FR-02 implementation and tests | Sumaiya | Merged; passing CI |
| FR-03 BVA/EP and overlap validation | Vijaha | PRs #15/#16 merged; passing CI |
| FR-04 Staff approval and status | Aadhil | PRs #17/#18 merged; passing CI |
| Full regression suite | Aadhil / Vijaha | **97 passed, 0 failed** |
| Ruff | Aadhil | **All checks passed** |
| Coverage | Vijaha / Aadhil | **96%** (390 statements, 14 missing) |
| GitHub Actions `main` | Aadhil | **Success** — run #39657131371 |
| Peer-review evidence | Review Lead Sinthu | #11–#17 approved as recorded; #18 separate review not recorded |
| Issue closure | Koparnika / Sumaiya | #1–#5 closed |
| Manual E3 demonstration | All five members | Scheduled/record separately |

**Final QA conclusion:** All five functional modules are merged and the final verified GitHub Actions run passed its Ruff and 97 automated tests, with 96% statement coverage. Final demonstration attendance and any further assessment sign-off are distinct from successful automated verification.

**QA Lead:** Vijaha  
**Integration Lead:** Aadhil  
**Final CI evidence date:** 21 October 2026  
**Scheduled E3 review:** 23 October 2026
