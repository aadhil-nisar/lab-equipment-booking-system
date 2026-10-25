# Pull Request Review Checklist — E1, E2 and E3
## Completed evidence-based register for **all 11 merged Pull Requests**

**Project:** Lab Equipment Booking System  
**Repository:** https://github.com/aadhil-nisar/lab-equipment-booking-system  
**Verification date:** 25 October 2026  
**Scope:** PR #8, #9, #11–#19 (all merged PRs found in the repository as of verification)  
**Latest verified `main` commit:** `e709b9fd27044bbfbd655abe007d5ed5f91be277`  
**Latest verified `main` CI:** [Run #40149580359](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/40149580359) — **Success**

> **Checklist interpretation:** `[x]` = an outcome evidenced by GitHub code/PR records, automated tests or successful CI. `[ ]` = unverified or an outstanding action. **N/A** = not applicable to that PR. This is a retrospective E3 evidence compilation, **not** a replacement for independent reviews recorded at the time of each PR. A green CI run does not constitute peer approval.

## 1. Pull Request Information — Entire Project Register

| PR | Feature | Developer | Recorded reviewer | Review result | CI at PR head | Merge |
|---|---|---|---|---|---|---|
| [#8](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/8) | Set up Flask SQLite database pytest Ruff and CI | Aadhil (`aadhil-nisar`) | Sinthu (`sinthu02`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/38456974242) | Merged |
| [#9](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/9) | Document E1 team roles and add review checklist | Koparnika (`koparnikasrikaran2002-gif`) | Vijaha (`HasVij`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/38459491742) | Merged |
| [#11](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/11) | Implement FR-00 student registration and authentication | Koparnika (`koparnikasrikaran2002-gif`) | Sumaiya (`fathimasumaiya884-collab`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39147200598) | Merged |
| [#12](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/12) | Implement FR-01 Equipment Catalogue with Staff CRUD and Tests | Sinthu (`sinthu02`) | Vijaha (`HasVij`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39149861449) | Merged |
| [#13](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/13) | E2: Add FR-00 and FR-01 Integration Tests | Aadhil (`aadhil-nisar`) | Vijaha (`HasVij`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39151942100) | Merged |
| [#14](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/14) | Implement FR-02 booking requests and tests | Sumaiya (`fathimasumaiya884-collab`) | Sinthu (`sinthu02`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39153897917) | Merged |
| [#15](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15) | E2: Implement Initial FR-03 Booking Validation and Automated Tests | Vijaha (`HasVij`) | Sumaiya (`fathimasumaiya884-collab`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39157863420) | Merged |
| [#16](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16) | Complete FR-03 overlapping booking validation and tests | Vijaha (`HasVij`) | Sumaiya (`fathimasumaiya884-collab`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39182464921) | Merged |
| [#17](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/17) | Implement FR-04 staff booking decisions and integration tests | Aadhil (`aadhil-nisar`) | Vijaha (`HasVij`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39654792218) | Merged |
| [#18](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/18) | Feature/fr 04 staff approval final | Aadhil (`aadhil-nisar`) | **None recorded** | **No review** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39656733361) | Merged |
| [#19](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/19) | docs: finalize E3 README and retrospective | Aadhil (`aadhil-nisar`) | Koparnika (`koparnikasrikaran2002-gif`) | **Approved** | [Success](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39898273936) | Merged |

Each PR has a **separate completed record in Section 16**, including:
PR number, title, author, reviewer, related Issue, head/base branches,
head SHA, CI run, changed files, evidence-supported checkboxes and
unverified/not-applicable checks.

## 2. Functional Correctness — Final Integrated Application

- [x] FR-00 Student registration, authentication and role restrictions are implemented, with tests.
- [x] FR-01 equipment list, category filter and Staff management are implemented, with tests.
- [x] FR-02 Student booking submissions, Pending status and personal booking history are implemented, with tests.
- [x] FR-03 future-time, duration, equipment-availability and overlap validation are implemented, with tests.
- [x] FR-04 Staff decisions and resulting booking statuses are implemented, with tests.
- [x] Automated integration/regression tests for FR-00–FR-04 pass on final `main`.
- [ ] A new, separate complete end-to-end **manual browser acceptance report** was not independently provided.

## 3. Code Quality

- [x] Source files are separated into Flask Blueprints, SQLAlchemy models, HTML templates and pytest files.
- [x] The current CI confirms `python -m ruff check .` passes.
- [x] Every listed PR has a successful GitHub Actions run associated with its PR-head SHA.
- [x] All listed PRs were merged into `main`.
- [ ] Exhaustive independent line-by-line review of every historic change and conflict resolution is not established by CI alone.

## 4. Database and Integrity

- [x] `User`, `Equipment` and `Booking` models are present in integrated source.
- [x] Student and equipment references are modeled in booking records.
- [x] The Booking model limits booking status to `Pending`, `Approved` and `Rejected`.
- [x] Tests verify that valid Staff decisions persist in SQLite.
- [x] Tests verify invalid Staff decisions do not change the booking status.
- [x] Removing equipment with booking history is blocked and covered by automated tests.
- [x] `.gitignore` excludes local SQLite databases, instance files and `.env` files.
- [ ] A full historical secret scan of every PR diff has not been independently documented.

## 5. Authentication and Security

- [x] Protected application routes use `@login_required`.
- [x] Students are blocked from Staff actions (HTTP 403), verified by tests.
- [x] Student booking lists are filtered by authenticated Student ID.
- [x] Public registration creates Student accounts rather than allowing arbitrary Staff creation.
- [x] User passwords are hashed through the User model.
- [x] Browser form mutations use POST and include CSRF protection.
- [ ] An external security audit or full credential-scanning report is not verified.

## 6. Error Handling

- [x] Invalid date/time/duration inputs are rejected by booking validation.
- [x] Unknown booking IDs return HTTP 404 in Staff decision tests.
- [x] Unauthorized Staff operations return HTTP 403 in automated tests.
- [x] Repeated decisions return HTTP 409 in automated tests.
- [x] Overlapping Approved bookings block conflicting approvals with HTTP 409.
- [x] Failed approval tests verify the persisted status is unchanged.

## 7. Testing and CI

- [x] Positive booking/authentication/equipment and Staff decision tests are included.
- [x] Negative, role-restriction and boundary tests are included.
- [x] FR-03 Boundary Value Analysis, Equivalence Partitioning and overlapping cases are documented/tested.
- [x] FR-04 approval/rejection, invalid decisions and conflicting Pending booking cases are tested.
- [x] Latest main-branch `pytest` run: **97 passed, 0 failed**.
- [x] Latest main-branch Ruff: **All checks passed!**
- [x] Latest main-branch statement coverage: **96%** (390 statements, 14 missed).
- [x] `app/booking_validation.py`: **100%** statement coverage in the verified latest report.
- [x] `app/routes/staff_bookings.py`: **100%** statement coverage in the verified latest report.
- [x] Every historical PR-head commit has a successful associated GitHub Actions run (links in Section 16).
- [ ] An original written independent reviewer inspection is **not recorded for PR #18**.

**Verified results:** [latest `main` CI #40149580359](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/40149580359) (25 October 2026).

## 8. FR-03 Booking Validation Review — Implemented on `main`

- [x] End time must follow start time.
- [x] Booking start must be in the future.
- [x] Duration is inclusive 30–240 minutes.
- [x] Equipment Out of service cannot be booked.
- [x] New Student submissions check overlapping Pending and Approved reservations.
- [x] Rejected bookings do not block new requests.
- [x] Adjacent bookings, different dates and different equipment are permitted.
- [x] Overlap tests include partial, exact, contained and boundary intersections.

**Primary PR evidence:** [#15](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15), [#16](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16).  
**Source/tests:** `app/booking_validation.py`, `tests/test_booking_validation.py`, `tests/test_booking_overlap.py`.

## 9. FR-04 Staff Decision Review — Implemented on `main`

- [x] Staff Pending request list and recent decision history have render/route tests.
- [x] Staff can approve or reject a valid Pending request.
- [x] Student booking history reflects Staff decisions.
- [x] Students cannot invoke Staff decision endpoints.
- [x] Only Pending bookings can be approved or rejected.
- [x] Approval revalidates time and current equipment availability.
- [x] Approval checks **Approved** booking overlaps only, excluding its own booking ID.
- [x] Test confirms only one of two existing overlapping Pending requests becomes Approved.
- [x] Rejection frees the booking slot.
- [x] Equipment with booking history cannot be deleted.
- [ ] PR #18's final follow-up changes have **no distinct submitted independent review**.

**Primary PR evidence:** [#17](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/17) (approved by Vijaha); [#18](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/18) (merged without a submitted review).  
**Source/tests:** `app/routes/staff_bookings.py`, `tests/test_staff_bookings.py`.

## 10. Documentation and Before-Merge Workflow

- [x] PRs #8–#19 on the register have actual GitHub branches, PR records and merges into `main`.
- [x] Each PR has a successful associated GitHub Actions run for its head SHA.
- [x] Ten of the eleven listed PRs have recorded independent **APPROVED** review submissions.
- [x] PR #19 adds `RETROSPECTIVE.md`, which is present on `main`.
- [x] `TESTING.md`, `REVIEW_CHECKLIST.md`, `.github/workflows/ci.yml`, and tests exist on `main`.
- [x] GitHub Issues #1–#5 are closed.
- [x] Git tag `v1.0` exists.
- [ ] PR #18 lacks independent submitted review evidence; do not call it approved.
- [ ] GitHub Projects board card positions were not independently confirmed.
- [ ] The current `README.md` needs correction: it currently starts with the **Testing Plan** content rather than the project README overview.
- [ ] The existing `v1.0` tag points to commit `7fccdb3`, not the latest `main`; it omits later documentation and commits.
- [ ] Lecturer E3 presentation/sign-off is not independently confirmed.

## 11. Review Decision — Historical Recorded Submissions

- [x] **Approved**, recorded on GitHub for PRs **#8, #9, #11, #12, #13, #14, #15, #16, #17 and #19**.
- [ ] **No independent approval**, recorded on GitHub for PR **#18**.
- [ ] The original reviews' written checklists were not all individually ticked (notably PR #17).
- [ ] **Request changes:** no recorded formal request-changes review was found in the examined PR review submissions; this is not evidence no informal corrective work occurred.

**Important:** This document does not create any new GitHub approvals. Recorded reviewer identities and dates appear in the individual PR records below.

## 12. Final Project PR and Peer-Review Register

The complete 11-PR register appears in Section 1, with **per-PR evidence and checklist in Section 16**. Every listed PR is merged.

**Review coverage:** 10 PRs with a submitted independent `APPROVED` review; PR #18 with no recorded submission.

## 13. Final Verified Automated QA Record

**Branch:** `main`  
**Latest CI run:** [#40149580359](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/40149580359)  
**Run date:** 25 October 2026  
**Head commit:** `e709b9fd27044bbfbd655abe007d5ed5f91be277`  
**Result:** Success

- [x] Main-branch CI successful.
- [x] Ruff all checks passed.
- [x] pytest **97 passed, 0 failed**.
- [x] Statement coverage **96%** (390 statements, 14 missed).
- [x] `app/booking_validation.py` **100%**.
- [x] `app/routes/staff_bookings.py` **100%**.
- [x] FR Issues #1–#5 closed.
- [x] All 11 historical PRs in the register merged.
- [x] `RETROSPECTIVE.md` present on `main`.
- [x] `v1.0` tag exists.
- [ ] `v1.0` is not aligned to the latest `main` commit.
- [ ] Final Project Board positions not independently confirmed.
- [ ] Separate submitted approval of PR #18 not recorded.
- [ ] Lecturer E3 demonstration/sign-off not verified.

## 14. Final Team Responsibilities

| Responsibility | Member |
|---|---|
| Team Coordinator and GitHub Projects tracking | Koparnika |
| Co-Coordinator and requirement/task tracking | Sumaiya |
| Review Lead and review checklist | Sinthu |
| QA Lead, BVA/EP and test evidence | Vijaha |
| FR-04 developer, system integration, GitHub/CI Lead | Aadhil |

## 15. Closing Notes

The source code for FR-00 to FR-04 is integrated and the latest automated CI is passing. This file documents the **actual per-PR review decisions** and evidence. It must not be represented as if one reviewer signed or individually checked all items for every PR.

Remaining project-quality actions: confirm Project Board status; correct the `README.md` content; consider release/tag policy for the already-published `v1.0`; and document PR #18's missing review accurately.

Related: [README.md](README.md) · [TESTING.md](TESTING.md) · [RETROSPECTIVE.md](RETROSPECTIVE.md)

---

## 16. Individual Pull Request Checklists — All PRs

### PR #8 — Set up Flask SQLite database pytest Ruff and CI

| Field | Verified value |
|---|---|
| Pull Request | [#8](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/8) |
| Developer / author | Aadhil (`aadhil-nisar`) |
| Independent reviewer | Sinthu (`sinthu02`) |
| Related Issue | [Issue #6](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/6) |
| Head branch | `setup/e1-flask-ci` |
| Base branch | `main` |
| Review / merge date | 13 October 2026 |
| Latest PR-head SHA | `c42aecd5f28fd09147597b8f3537825b1197cfb5` |
| PR-head CI | [Run #38456974242 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/38456974242) |
| Status | **Merged** |

**Changed files / key diff:** `.github/workflows/ci.yml`, `app/__init__.py`, `app/extensions.py`, `app/models/equipment.py`, `tests/conftest.py`, `tests/test_smoke.py`, `requirements.txt`, `.gitignore`.

**Completed evidence-backed checks**

- [x] Initial Flask application, SQLite setup, Equipment model and dependency files appear in the PR diff.
- [x] pytest smoke tests and Ruff/CI workflow are included in the submitted changes.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Sinthu submitted an **APPROVED** review, describing the project structure, SQLite configuration, tests and CI.
- [x] The PR was merged into `main`.
- [x] Independent **APPROVED** review by Sinthu (`sinthu02`).

**Open / not-applicable / clarification**

- FR-00–FR-04 feature-specific checks: **N/A** to this E1 foundation PR.
- [ ] A historical secret scan beyond the inspected repository configuration is not recorded.

**Historical review decision:** Approved by Sinthu (`sinthu02`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/8).

---

### PR #9 — Document E1 team roles and add review checklist

| Field | Verified value |
|---|---|
| Pull Request | [#9](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/9) |
| Developer / author | Koparnika (`koparnikasrikaran2002-gif`) |
| Independent reviewer | Vijaha (`HasVij`) |
| Related Issue | [Issue #7](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/7) |
| Head branch | `docs/e1-readme-review-checklist` |
| Base branch | `main` |
| Review / merge date | 13 October 2026 |
| Latest PR-head SHA | `3b9d170934f098ba58a0da6c58e216b181e02605` |
| PR-head CI | [Run #38459491742 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/38459491742) |
| Status | **Merged** |

**Changed files / key diff:** `README.md`, `REVIEW_CHECKLIST.md`.

**Completed evidence-backed checks**

- [x] The PR adds E1 project overview, team allocation, setup instructions and the review checklist.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Vijaha submitted an **APPROVED** review with written documentation feedback.
- [x] The documentation PR was merged into `main`.
- [x] Independent **APPROVED** review by Vijaha (`HasVij`).

**Open / not-applicable / clarification**

- Implementation-specific FR-03/FR-04 checks: **N/A** to this documentation PR.
- [ ] The present-day `README.md` appears to contain a copy of `TESTING.md`; this is a **later repository-quality issue**, not an unrecorded defect in the E1 review.

**Historical review decision:** Approved by Vijaha (`HasVij`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/9).

---

### PR #11 — Implement FR-00 student registration and authentication

| Field | Verified value |
|---|---|
| Pull Request | [#11](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/11) |
| Developer / author | Koparnika (`koparnikasrikaran2002-gif`) |
| Independent reviewer | Sumaiya (`fathimasumaiya884-collab`) |
| Related Issue | [Issue #1](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/1) |
| Head branch | `feature/FR-00-auth` |
| Base branch | `main` |
| Review / merge date | 18 October 2026 |
| Latest PR-head SHA | `bd2010ba0ea396eb4ed567e937a706f1cfc95634` |
| PR-head CI | [Run #39147200598 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39147200598) |
| Status | **Merged** |

**Changed files / key diff:** `app/routes/auth.py`, `app/models/user.py`, `app/commands.py`, `app/templates/auth/login.html`, `app/templates/auth/register.html`, `tests/test_auth.py`.

**Completed evidence-backed checks**

- [x] Student registration, login/logout, role handling, Staff-creation CLI and authentication tests are in the PR.
- [x] Passwords are hashed and protected routes use Flask-Login; role checks reject unauthorized Students.
- [x] Registration input validation and CSRF-aware browser forms are part of the feature.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Sumaiya submitted an **APPROVED** review with detailed comments about the auth implementation and tests.
- [x] The PR was merged into `main`.
- [x] Independent **APPROVED** review by Sumaiya (`fathimasumaiya884-collab`).

**Open / not-applicable / clarification**

- FR-03/FR-04 rules: **N/A** to the original FR-00 feature PR.
- [ ] No separate manual screen-by-screen acceptance report was confirmed for this exact PR revision.

**Historical review decision:** Approved by Sumaiya (`fathimasumaiya884-collab`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/11).

---

### PR #12 — Implement FR-01 Equipment Catalogue with Staff CRUD and Tests

| Field | Verified value |
|---|---|
| Pull Request | [#12](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/12) |
| Developer / author | Sinthu (`sinthu02`) |
| Independent reviewer | Vijaha (`HasVij`) |
| Related Issue | [Issue #2](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/2) |
| Head branch | `feature/FR-01-equipment-catalogue` |
| Base branch | `main` |
| Review / merge date | 18 October 2026 |
| Latest PR-head SHA | `e67f910063bc7a921e10bab20d8d57fbacb86c05` |
| PR-head CI | [Run #39149861449 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39149861449) |
| Status | **Merged** |

**Changed files / key diff:** `app/routes/equipment.py`, `app/templates/equipment/catalogue.html`, `app/templates/equipment/form.html`, `tests/test_equipment.py`, `TESTING.md`.

**Completed evidence-backed checks**

- [x] Equipment listing, category filter, Staff-only CRUD and allowed equipment statuses are implemented.
- [x] Input validation and authorization tests are included.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Vijaha submitted an **APPROVED** review with recorded FR-01 review observations.
- [x] The PR was merged into `main`.
- [x] Independent **APPROVED** review by Vijaha (`HasVij`).

**Open / not-applicable / clarification**

- [ ] The historical-booking deletion guard was integrated later in PR #17; do **not** attribute that later guard to the original PR #12.
- FR-03/FR-04 decision checks: **N/A** to PR #12.

**Historical review decision:** Approved by Vijaha (`HasVij`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/12).

---

### PR #13 — E2: Add FR-00 and FR-01 Integration Tests

| Field | Verified value |
|---|---|
| Pull Request | [#13](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/13) |
| Developer / author | Aadhil (`aadhil-nisar`) |
| Independent reviewer | Vijaha (`HasVij`) |
| Related Issue | [Issue #10](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/10) |
| Head branch | `feature/e2-integration` |
| Base branch | `main` |
| Review / merge date | 18 October 2026 |
| Latest PR-head SHA | `99eefa274c88a8574978d8ea73ef8cf963c6619b` |
| PR-head CI | [Run #39151942100 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39151942100) |
| Status | **Merged** |

**Changed files / key diff:** `tests/test_e2_integration.py`.

**Completed evidence-backed checks**

- [x] The PR adds an automated Student-registration/login-to-catalogue integration test.
- [x] The test checks Student access to the catalogue and denies unauthorized equipment management.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Vijaha submitted a formal **APPROVED** review; the review text largely describes what to check.
- [x] The PR was merged into `main`.
- [x] Independent **APPROVED** review by Vijaha (`HasVij`).

**Open / not-applicable / clarification**

- Production code changes and FR-03/FR-04 checks: **N/A** to this test-only PR.
- [ ] The approval text is not detailed proof that each requested verification was individually documented.

**Historical review decision:** Approved by Vijaha (`HasVij`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/13).

---

### PR #14 — Implement FR-02 booking requests and tests

| Field | Verified value |
|---|---|
| Pull Request | [#14](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/14) |
| Developer / author | Sumaiya (`fathimasumaiya884-collab`) |
| Independent reviewer | Sinthu (`sinthu02`) |
| Related Issue | [Issue #3](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/3) |
| Head branch | `feature/FR-02-booking-requests` |
| Base branch | `main` |
| Review / merge date | 18 October 2026 |
| Latest PR-head SHA | `1e47565667aa14b4da91f7c39aa5dd6ab59a0da7` |
| PR-head CI | [Run #39153897917 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39153897917) |
| Status | **Merged** |

**Changed files / key diff:** `app/models/booking.py`, `app/routes/booking.py`, `app/templates/booking/new.html`, `app/templates/booking/mine.html`, `tests/test_booking.py`.

**Completed evidence-backed checks**

- [x] Booking model associates Student and Equipment and stores date/time/status.
- [x] Student submission creates Pending bookings and My Requests filters by authenticated Student.
- [x] Role restrictions and booking form tests are included.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Sinthu submitted an **APPROVED** review and the PR was merged.
- [x] Independent **APPROVED** review by Sinthu (`sinthu02`).

**Open / not-applicable / clarification**

- [ ] Complete duration/overlap validation was delivered later in PRs #15/#16; it must not be attributed to PR #14 alone.
- [ ] The submitted review text includes template-style placeholders; verify the exact statements rather than claiming every item was explicitly signed off.

**Historical review decision:** Approved by Sinthu (`sinthu02`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/14).

---

### PR #15 — E2: Implement Initial FR-03 Booking Validation and Automated Tests

| Field | Verified value |
|---|---|
| Pull Request | [#15](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15) |
| Developer / author | Vijaha (`HasVij`) |
| Independent reviewer | Sumaiya (`fathimasumaiya884-collab`) |
| Related Issue | [Issue #4](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/4) |
| Head branch | `feature/FR-03-initial-validation` |
| Base branch | `main` |
| Review / merge date | 18 October 2026 |
| Latest PR-head SHA | `087c585bf18def89336d25227fb213f4dec64635` |
| PR-head CI | [Run #39157863420 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39157863420) |
| Status | **Merged** |

**Changed files / key diff:** `app/booking_validation.py`, `app/routes/booking.py`, `tests/test_booking_validation.py`, `TESTING.md`.

**Completed evidence-backed checks**

- [x] Checks require end after start, future start and 30–240-minute inclusive duration.
- [x] Initial FR-03 validation is integrated with Student booking submission.
- [x] Positive, negative and boundary-value tests are included and described.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Sumaiya submitted a detailed **APPROVED** review; the PR was merged.
- [x] Independent **APPROVED** review by Sumaiya (`fathimasumaiya884-collab`).

**Open / not-applicable / clarification**

- [ ] Overlapping-booking detection was completed in subsequent PR #16; **not** part of the completed scope of PR #15.
- FR-04 Staff decision policy: **N/A** to this initial validation PR.

**Historical review decision:** Approved by Sumaiya (`fathimasumaiya884-collab`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15).

---

### PR #16 — Complete FR-03 overlapping booking validation and tests

| Field | Verified value |
|---|---|
| Pull Request | [#16](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16) |
| Developer / author | Vijaha (`HasVij`) |
| Independent reviewer | Sumaiya (`fathimasumaiya884-collab`) |
| Related Issue | [Issue #4](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/4) |
| Head branch | `feature/FR-03-overlap-validation` |
| Base branch | `main` |
| Review / merge date | 21 October 2026 |
| Latest PR-head SHA | `d6c94487f8dcb546e80eab644e3318a1b25e6f5f` |
| PR-head CI | [Run #39182464921 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39182464921) |
| Status | **Merged** |

**Changed files / key diff:** `app/booking_validation.py`, `app/routes/booking.py`, `tests/test_booking_overlap.py`, `TESTING.md`.

**Completed evidence-backed checks**

- [x] The conflict query checks same equipment, same date and intersecting start/end times.
- [x] Pending and Approved bookings block overlapping Student requests; Rejected bookings do not.
- [x] Adjacent slots, different dates and different equipment are allowed.
- [x] Overlap test values include full, partial, exact and boundary cases.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Sumaiya submitted an **APPROVED** review with a detailed overlap-test checklist; PR merged.
- [x] Independent **APPROVED** review by Sumaiya (`fathimasumaiya884-collab`).

**Open / not-applicable / clarification**

- [ ] The Staff-specific Approved-only conflict policy was finalized in PRs #17/#18; distinguish it from the Student submission behavior.
- [ ] An exhaustive independent security/secret-scan report was not available.

**Historical review decision:** Approved by Sumaiya (`fathimasumaiya884-collab`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16).

---

### PR #17 — Implement FR-04 staff booking decisions and integration tests

| Field | Verified value |
|---|---|
| Pull Request | [#17](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/17) |
| Developer / author | Aadhil (`aadhil-nisar`) |
| Independent reviewer | Vijaha (`HasVij`) |
| Related Issue | [Issue #5](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/5) |
| Head branch | `feature/FR-04-staff-approval` |
| Base branch | `main` |
| Review / merge date | 21 October 2026 |
| Latest PR-head SHA | `7fe814255d8f380773a4d28b4a9bc69e0e927663` |
| PR-head CI | [Run #39654792218 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39654792218) |
| Status | **Merged** |

**Changed files / key diff:** `app/routes/staff_bookings.py`, `app/templates/staff/bookings.html`, `tests/test_staff_bookings.py`, `app/__init__.py`, `app/booking_validation.py`, `app/routes/equipment.py`, `app/templates/auth/staff.html`, `app/templates/index.html`.

**Completed evidence-backed checks**

- [x] Staff-only Pending dashboard and Approve/Reject routes are included.
- [x] Decisions use POST, validate pending status, recheck availability and booking slot, and persist statuses.
- [x] Approval conflict check excludes the selected booking and filters existing **Approved** bookings.
- [x] Tests cover successful decisions, Student access (403), repeat decisions (409), overlap denial, and equipment-history deletion guard.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Vijaha submitted an **APPROVED** review; the PR was merged into `main`.
- [x] Independent **APPROVED** review by Vijaha (`HasVij`).

**Open / not-applicable / clarification**

- [ ] The original Vijaha review body contains unchecked template boxes. The GitHub approval is verified, but those individual checklist boxes are **not** proven personally ticked.
- [ ] PR #18 follow-up changes were not independently approved in their own PR.

**Historical review decision:** Approved by Vijaha (`HasVij`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/17).

---

### PR #18 — Feature/fr 04 staff approval final

| Field | Verified value |
|---|---|
| Pull Request | [#18](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/18) |
| Developer / author | Aadhil (`aadhil-nisar`) |
| Independent reviewer | **None recorded** |
| Related Issue | [Issue #5](https://github.com/aadhil-nisar/lab-equipment-booking-system/issues/5) |
| Head branch | `feature/FR-04-staff-approval-final` |
| Base branch | `main` |
| Review / merge date | 21 October 2026 (merged; no review date) |
| Latest PR-head SHA | `4380a9246b66aacf17b4f3ee685a1f6a2f580e45` |
| PR-head CI | [Run #39656733361 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39656733361) |
| Status | **Merged** |

**Changed files / key diff:** `app/booking_validation.py`, `app/routes/staff_bookings.py`, `tests/test_staff_bookings.py`.

**Completed evidence-backed checks**

- [x] The PR changes Staff approval conflict logic, booking validation integration and FR-04 tests.
- [x] The PR-head GitHub Actions run succeeded.
- [x] The PR was merged into `main` on 21 October 2026.
- [x] The final integrated `main` regression and coverage run is passing.
- [ ] No independent submitted PR review found.

**Open / not-applicable / clarification**

- [ ] **No independent submitted `APPROVED`/`REQUEST_CHANGES` review exists for this PR.**
- [ ] A later CI success or Vijaha's review of PR #17 is **not** a separate review of PR #18.
- [ ] If desired, record a clearly labeled post-merge review of the final code; do not present it as pre-merge approval.

**Historical review decision:** Not approved on GitHub (no review submission). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/18).

---

### PR #19 — docs: finalize E3 README and retrospective

| Field | Verified value |
|---|---|
| Pull Request | [#19](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/19) |
| Developer / author | Aadhil (`aadhil-nisar`) |
| Independent reviewer | Koparnika (`koparnikasrikaran2002-gif`) |
| Related Issue | Documentation PR; no linked Issue verified |
| Head branch | `docs/e3-final-submission` |
| Base branch | `main` |
| Review / merge date | 23 October 2026 |
| Latest PR-head SHA | `eb15c0ee14f4ee5bf5d45208c17761a20a16cc1d` |
| PR-head CI | [Run #39898273936 — **Success**](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39898273936) |
| Status | **Merged** |

**Changed files / key diff:** `RETROSPECTIVE.md`.

**Completed evidence-backed checks**

- [x] `RETROSPECTIVE.md` was added and now exists on `main`.
- [x] The PR-head GitHub Actions run succeeded.
- [x] Koparnika submitted **APPROVED** and the PR was merged into `main`.
- [x] Independent **APPROVED** review by Koparnika (`koparnikasrikaran2002-gif`).

**Open / not-applicable / clarification**

- [ ] Although the PR title mentions README, the actual changed-files list contains **only `RETROSPECTIVE.md`**.
- [ ] The approval was submitted with no detailed review comment; do not infer line-by-line review outcomes.
- [ ] The current `README.md` appears to duplicate the testing document; correct it in a separate reviewed PR if the submitted README must explain the project.

**Historical review decision:** Approved by Koparnika (`koparnikasrikaran2002-gif`). **PR result:** Merged. [View evidence](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/19).

---

