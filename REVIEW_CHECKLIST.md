# Pull Request Review Checklist — E1, E2 and E3

**Project:** Lab Equipment Booking System  
**Repository:** https://github.com/aadhil-nisar/lab-equipment-booking-system  
**Updated for final E3 review:** 22 October 2026

This checklist defines how another team member reviews each Pull Request and records the **actual** review evidence. It supersedes the initial E1 draft. A successful CI run is not a substitute for an independent review.

## 1. Pull Request Information (complete for each new PR)

- **PR number:**
- **Title:**
- **Developer / author:**
- **Independent reviewer:**
- **Related GitHub Issue:**
- **Head branch:**
- **Base branch:** `main`
- **Review date:**
- **Latest commit SHA:**
- **CI run URL:**

## 2. Functional Correctness

- [ ] Changes match the Issue and acceptance criteria.
- [ ] Expected route and user-interface behavior works.
- [ ] Invalid inputs are rejected appropriately.
- [ ] The implemented business rules are followed.
- [ ] Existing FR-00–FR-04 behavior is not broken.
- [ ] Any changed booking-status transitions are documented.

## 3. Code Quality

- [ ] Code is readable and names are meaningful.
- [ ] Python and Flask conventions are followed.
- [ ] There are no unused imports, accidental files or conflict markers.
- [ ] Ruff passes on the current PR revision.
- [ ] Relevant code is not accidentally removed during merge conflict resolution.

## 4. Database and Integrity

- [ ] Models and relationships have appropriate fields and constraints.
- [ ] Valid changes persist correctly in SQLite.
- [ ] Invalid changes do not alter existing booking data.
- [ ] Booking IDs, equipment IDs and student IDs are handled safely.
- [ ] Deleting equipment with booking history is rejected.
- [ ] Database and local secrets are excluded from commits.

## 5. Authentication and Security

- [ ] Authentication is required for protected routes.
- [ ] Students cannot perform Staff-only actions (HTTP 403).
- [ ] Students see only their own booking records.
- [ ] User input is validated server-side.
- [ ] Passwords are hashed, not committed in plaintext.
- [ ] Mutating browser forms use POST and CSRF protection.
- [ ] No credentials, application secrets or private data appear in PR diffs.

## 6. Error Handling

- [ ] Invalid booking time or duration gives a clear error.
- [ ] Unknown record IDs return appropriate responses (e.g., HTTP 404).
- [ ] Unauthorized operations are blocked.
- [ ] Repeated decisions are blocked (HTTP 409).
- [ ] Invalid operations preserve existing data.

## 7. Testing and CI

- [ ] Relevant positive tests are included.
- [ ] Relevant negative and boundary tests are included.
- [ ] FR-03 BVA/EP and overlap policies are covered where relevant.
- [ ] Existing regression tests pass.
- [ ] Ruff passes.
- [ ] Coverage output is inspected, not guessed.
- [ ] **Latest PR commit** has successful GitHub Actions checks.
- [ ] Reviewer inspected the actual code and test diff.

## 8. FR-03 Booking Validation Review

- [ ] End must follow start.
- [ ] Start must be in the future.
- [ ] Duration is inclusive 30–240 minutes.
- [ ] Unavailable equipment is rejected.
- [ ] Student submission checks Pending and Approved overlaps.
- [ ] Rejected bookings do not block requests.
- [ ] Adjacent and different-equipment/date requests are permitted.
- [ ] Overlap tests exercise partial, full and exact overlaps.

## 9. FR-04 Staff Decision Review

- [ ] Staff Pending list and status history render correctly.
- [ ] Staff can Approve or Reject a valid Pending request.
- [ ] Student sees updated status in their own booking history.
- [ ] Students cannot invoke Staff decision endpoints.
- [ ] Only Pending requests can be decided.
- [ ] Approval revalidates time and equipment availability.
- [ ] Approval conflict check uses **Approved** bookings only and excludes the selected booking.
- [ ] At most one of two overlapping Pending requests can become Approved.
- [ ] A Rejected booking frees its time slot.
- [ ] Equipment with any booking history cannot be deleted.

## 10. Documentation and Before Merge

- [ ] PR description explains what changed and why.
- [ ] Issue is linked; `Closes #N` is used only for fully completed work.
- [ ] README and TESTING docs are updated where needed.
- [ ] Reviewer posts a written, evidence-based comment.
- [ ] Reviewer selects **Approve** or **Request changes**.
- [ ] Developer addresses any requested changes in the same PR.
- [ ] Current CI is successful and conflicts are resolved.
- [ ] Merge targets `main` and is confirmed by GitHub.
- [ ] Issue / GitHub Project status is updated after merge.

## 11. Review Decision Template

**Choose one after inspection:**

- [ ] **Approve** — All blocking issues are resolved and CI is successful.
- [ ] **Request changes** — Issues listed below must be fixed.
- [ ] **Comment only** — Feedback submitted; not an approval.

**Reviewer name:**  
**Review date:**  
**Test evidence:**  
**CI evidence URL:**  
**Findings:**  
**Corrective action / follow-up:**

**Reminder:** Do not tick items that have not been checked. A PR author cannot substitute as their own independent reviewer.

## 12. Final Project PR and Peer-Review Register

The following status is verified from the GitHub PR and review records as of 22 October 2026.

| PR | Feature | Developer | Submitted reviewer result | Merge status |
|---|---|---|---|---|
| [#8](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/8) | E1 Flask, SQLite, pytest, Ruff, CI | Aadhil | See historical PR | Merged |
| [#9](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/9) | E1 README / review checklist | Koparnika | See historical PR | Merged |
| [#11](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/11) | FR-00 Accounts and Login | Koparnika | **Approved — Sumaiya** | Merged |
| [#12](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/12) | FR-01 Equipment Catalogue | Sinthu | **Approved — Vijaha** | Merged |
| [#13](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/13) | E2 integration | Aadhil | **Approved — Vijaha** | Merged |
| [#14](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/14) | FR-02 Booking Requests | Sumaiya | **Approved — Sinthu** | Merged |
| [#15](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/15) | FR-03 initial validation | Vijaha | **Approved — Sumaiya** | Merged |
| [#16](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/16) | FR-03 overlap validation | Vijaha | **Approved — Sumaiya** | Merged |
| [#17](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/17) | FR-04 Staff approval initial integration | Aadhil | **Approved — Vijaha** | Merged |
| [#18](https://github.com/aadhil-nisar/lab-equipment-booking-system/pull/18) | FR-04 final branch and conflict resolution | Aadhil | **No submitted independent review recorded for #18** | Merged |

### Review evidence clarification for PR #18

The approval on PR #17 is genuine and can be presented as Vijaha's review of that earlier FR-04 change. PR #18 was merged and the final CI passed, but it has **no separate submitted review** in GitHub's review records. Do not describe PR #18 as formally approved by Vijaha. If the coursework requires explicit final-revision review evidence, ask an independent team member to inspect the merged code and document a **post-merge audit** on an Issue or a new review-only PR; label it accurately as post-merge follow-up, not as a pre-merge approval.

## 13. Final Verified Automated QA Record

**Branch:** `main`  
**GitHub Actions:** https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39657131371  
**Run date:** 21 October 2026  
**Result:** Success

- [x] Final CI successfully completed on `main`.
- [x] Ruff reported **All checks passed!**.
- [x] pytest reported **97 passed, 0 failed**.
- [x] pytest-cov reported **96%** statement coverage.
- [x] `app/booking_validation.py` reached **100%** statement coverage in that run.
- [x] `app/routes/staff_bookings.py` reached **100%** statement coverage in that run.
- [x] Issues #1–#5 are Closed.
- [x] PRs #16, #17 and #18 are Merged.
- [ ] Separate independent PR #18 review record (not found at verification time).
- [ ] Final GitHub Project board card positions independently confirmed.
- [ ] Lecturer E3 presentation/sign-off recorded (scheduled for 23 October 2026).

These checked items record **verified evidence**, not assumptions based solely on a checklist.

## 14. Final Team Responsibilities

| Responsibility | Owner |
|---|---|
| Team coordination and Project board | Koparnika |
| Co-coordination and requirement tracking | Sumaiya |
| Review process and checklist | Sinthu |
| BVA/EP, test plan and QA sign-off | Vijaha |
| FR-04 development, integration, CI and merges | Aadhil |

## 15. Closing Notes

The required application features are integrated on `main`, with a passing final automated CI run. Preserve PR URLs, Issues, final testing numbers and screenshots for the E3 review. No outstanding review or demonstration evidence should be described as already completed unless independently confirmed.

Related documents: [README.md](README.md) · [TESTING.md](TESTING.md).
