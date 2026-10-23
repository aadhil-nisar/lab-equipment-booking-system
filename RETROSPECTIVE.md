# RETROSPECTIVE.md

# Lab Equipment Booking System — Project Retrospective

**Coursework:** Software Engineering Mini Project  
**Final Evaluation:** 23 October 2026  
**Team:** Aadhil, Koparnika, Sinthu, Sumaiya and Vijaha

## 1. Project Summary

The Lab Equipment Booking System was developed using Flask, Python and SQLite.

The project implements five functional requirements:

- FR-00 — Accounts and Login
- FR-01 — Equipment Catalogue
- FR-02 — Booking Requests
- FR-03 — Booking Validation
- FR-04 — Booking Approval and Status

The team used GitHub Issues, Projects, branches, Pull Requests, peer reviews, pytest, pytest-cov, Ruff and GitHub Actions.

## 2. What Went Well

### Teamwork and Module Allocation

The work was divided into five functional modules, each with a responsible developer.

This helped members focus on their features while coordinating integration through GitHub.

### Automated Testing

The team used automated tests during development to identify regressions and validate functionality.

The final verified GitHub Actions run on 22 October 2026 reported:

| Metric | Result |
|---|---|
| Automated tests | 97 passed |
| Failed tests | 0 |
| Statement coverage | 96% |
| Ruff | Passed |
| GitHub Actions | Success |

### Version Control and Continuous Integration

GitHub Issues were used to track requirements. Feature branches and Pull Requests provided a record of development.

GitHub Actions helped detect problems before and after integration.

## 3. Challenges Encountered

### Merge Conflicts

Changes to shared files caused merge conflicts during integration.

The team resolved the conflicts by examining both versions, preserving required functionality and rerunning automated tests.

**Lesson learned:** Coordinate edits to shared files and integrate changes regularly.

### Booking Conflict Validation

The booking workflow initially had a situation where two overlapping Pending requests could prevent each other from being approved.

The final policy distinguishes between new booking submissions and Staff approval decisions.

Student submissions are checked against Pending and Approved reservations. Staff approval is checked against existing Approved reservations.

**Lesson learned:** Business rules should be clarified and tested before integrating modules.

### Regression Testing

Changes to templates and functionality affected existing automated tests during development.

These problems were detected using pytest and corrected.

**Lesson learned:** Run the complete regression suite after modifying shared application files.

## 4. What Could Be Improved

- Clarify integration-dependent business rules earlier.
- Avoid unnecessary changes to shared files.
- Update documentation continuously rather than near submission.
- Schedule peer reviews before the final merge.
- Reserve additional time for manual testing.
- Use a clear final-release checklist.

## 5. Individual Contributions

| Team Member | Main Contribution |
|---|---|
| Koparnika | FR-00 Accounts and Login, coordination, GitHub Project tracking |
| Sinthu | FR-01 Equipment Catalogue, review coordination |
| Sumaiya | FR-02 Booking Requests, co-coordination and FR-03 peer reviews |
| Vijaha | FR-03 Booking Validation, BVA/EP testing and QA |
| Aadhil | FR-04 Staff Approval, final integration, CI and merging |

## 6. Improvements for Future Projects

In a future project, the team would:

1. Agree on detailed acceptance criteria before development.
2. Add tests alongside each new feature.
3. Integrate smaller changes more frequently.
4. Review each Pull Request before merging.
5. Maintain documentation during every evaluation.
6. Allow more time for final testing and demonstrations.

## 7. Conclusion

The project provided practical experience in developing a Flask application using a team-based Software Engineering workflow.

The team implemented FR-00 to FR-04 and demonstrated automated testing, code quality checks and continuous integration.

The project strengthened understanding of requirement allocation, database applications, validation, version control, peer reviews and collaborative problem-solving.

---

**QA Evidence:** GitHub Actions run [#39727210976](https://github.com/aadhil-nisar/lab-equipment-booking-system/actions/runs/39727210976)

**Retrospective confirmation:** All five members should review this document and confirm that its reflections accurately describe their experience.
