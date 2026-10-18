

\# E2 Testing Plan and Evidence



\## Project



Lab Equipment Booking System



\## Evaluation



E2 - Intermediate Review

19 October 2026



\## Test Responsibilities



| Member | Responsibility |

|---|---|

| Koparnika | FR-00 Authentication |

| Sinthu | FR-01 Equipment Catalogue |

| Sumaiya | FR-02 Booking Requests |

| Vijaha | FR-03 Validation and QA |

| Aadhil | Integration and CI |



\## FR-01 Automated Testing



Test file: `tests/test\_equipment.py`



Run:



```powershell

python -m pytest tests/test\_equipment.py -v

```



Run the complete suite:



```powershell

python -m pytest -v

```



\## FR-01 Test Cases



| Test | Expected Result | Actual Result |

|---|---|---|

| Anonymous catalogue access | Redirect to Login | Not run |

| Student catalogue access | HTTP 200 | Not run |

| Category filtering | Only matching items | Not run |

| Empty catalogue | No equipment found | Not run |

| Student add request | HTTP 403 | Not run |

| Student edit request | HTTP 403 | Not run |

| Student delete request | HTTP 403 | Not run |

| Staff create | Record saved | Not run |

| Staff edit | Record updated | Not run |

| Staff delete | Record removed | Not run |

| Invalid input | HTTP 400, no save | Not run |

| Delete using GET | HTTP 405 | Not run |

| Invalid equipment ID | HTTP 404 | Not run |



Replace "Not run" with Pass or Fail after

executing each test.



\## Code Quality



Command:



```powershell

python -m ruff check .

```



Result: Not run



\## Full Test Suite



Command:



```powershell

python -m pytest -v

```



Result: Not run



\## Coverage



Command:



```powershell

python -m pytest --cov=app --cov-report=term-missing

```



Coverage result: Not recorded



\## Manual Testing



Staff login:

Result: Not run



Equipment creation:

Result: Not run



Equipment update:

Result: Not run



Equipment deletion:

Result: Not run



Student view and filter:

Result: Not run



Student role restriction:

Result: Not run



\## GitHub Actions



PR number: Pending



CI result: Pending



CI evidence: Add PR Actions/checks URL.



\## FR-01 Review Record



Developer: Sinthu

Reviewer: Vijaha



Review date: Pending

Review outcome: Pending

Review comments: To be recorded in the PR review.



\## Integration Notes



FR-00 must remain working after FR-01.



FR-02 will use Equipment records.



FR-03 validation and integration tests will

be expanded by the responsible team members.



