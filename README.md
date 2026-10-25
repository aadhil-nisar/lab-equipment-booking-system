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

| Member | Registration Number | GitHub Username | Testing / Coordination Responsibility |
|---|---|---|---|
| Aadhil | ASP/2023/061 | `aadhil-nisar` | FR-04 decisions, integration, CI and regression |
| Koparnika | ASP/2023/082 | `koparnikasrikaran2002-gif` | FR-00 accounts; Coordinator and GitHub board |
| Sinthu | ASP/2023/163 | `sinthu02` | FR-01 catalogue; Review Lead |
| Sumaiya | ASB/2023/085 | `fathimasumaiya884-collab` | FR-02 requests; Co-Coordinator |
| Vijaha | ASB/2023/087 | `HasVij` | FR-03 validation, BVA/EP, QA Lead |

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
