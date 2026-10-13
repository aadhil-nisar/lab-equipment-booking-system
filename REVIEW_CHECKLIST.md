
# Pull Request Review Checklist

## Lab Equipment Booking System

This document provides the review checklist for all
Pull Requests in the Lab Equipment Booking System.

Every Pull Request must be reviewed by another
team member before merging into main.

This is the initial E1 draft checklist.

## 1. Pull Request Information

- PR Number:
- PR Title:
- PR Author:
- Reviewer:
- Related GitHub Issue:
- Review Date:

## 2. Functional Correctness

- [ ] The changes match the linked Issue.
- [ ] Required functionality works correctly.
- [ ] Input validation is appropriate.
- [ ] Business rules are followed.
- [ ] Existing functionality is not broken.

## 3. Code Quality

- [ ] Code is readable and understandable.
- [ ] Names are meaningful.
- [ ] Python and Flask conventions are followed.
- [ ] Unnecessary imports and files are removed.
- [ ] Ruff checks pass.

## 4. Database Review

- [ ] Database models contain correct fields.
- [ ] Appropriate data types are used.
- [ ] Primary keys are defined correctly.
- [ ] Required fields and constraints are checked.
- [ ] Database operations behave as expected.
- [ ] Local database files are not committed.

## 5. Security Review

- [ ] No passwords or secret keys are committed.
- [ ] Sensitive data is protected.
- [ ] Authentication is used where necessary.
- [ ] Staff-only actions have role restrictions.
- [ ] User inputs are validated.

## 6. Error Handling

- [ ] Invalid inputs are handled appropriately.
- [ ] Errors do not crash the application unexpectedly.
- [ ] Error messages are clear and understandable.

## 7. Testing Review

- [ ] Relevant automated tests are included.
- [ ] Existing tests still pass.
- [ ] Positive test cases are considered.
- [ ] Negative test cases are considered.
- [ ] pytest runs successfully.
- [ ] Test coverage is reviewed.
- [ ] GitHub Actions CI passes.

## 8. Documentation Review

- [ ] README is updated if necessary.
- [ ] The Pull Request description is clear.
- [ ] The related Issue is linked.
- [ ] Changes are understandable to reviewers.

## 9. Review Decision

Select one:

- [ ] Approve
- [ ] Request changes
- [ ] Comment only

### Reviewer Comments

Write review comments here.

### Reviewer Name

### Review Date

## 10. Before Merging

- [ ] Peer review is completed.
- [ ] Requested corrections are addressed.
- [ ] Latest CI checks pass.
- [ ] The target branch is main.
- [ ] The related GitHub Issue is linked.
- [ ] GitHub Projects status is updated.

## Team Review Guidelines

- PR authors must not approve their own work.
- Reviewers should inspect actual code changes.
- Comments should be clear and constructive.
- Developers should fix problems on the same branch.
- Changes should not be merged with failing CI.
- Completed E1 tasks should be moved to Done.

## E1 Pull Request Review Assignment

| PR | Author | Reviewer |
|---|---|---|
| PR 1 - Flask, Database, Tests and CI | Aadhil | Sinthu |
| PR 2 - README and Review Checklist | Koparnika | Vijaha |

## Note

This checklist will be refined during E2 and E3
as additional application functionality is implemented.
