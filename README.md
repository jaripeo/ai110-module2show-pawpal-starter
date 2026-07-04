# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

🐾 Daily Care Plan for Jordan's Pets 🐾
----------------------------------------
[HIGH] Mochi: Morning Walk (30 min) - daily
[HIGH] Mochi: Heartworm Medication (5 min) - monthly
[MEDIUM] Luna: Laser Pointer Play (15 min) - daily
----------------------------------------

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov

```

To verify the system's core behaviors, run the automated test suite using pytest:

```bash
# Run the full test suite:
python -m pytest

```


Sample test output:

C:...\codepath\ai110-module2show-pawpal-starter>python -m pytest
========================================== test session starts ==========================================
platform win32 -- Python 3.9.13, pytest-8.4.2, pluggy-1.6.0
rootdir: C:...\codepath\ai110-module2show-pawpal-starter
collected 5 items                                                                                        

tests\test_pawpal.py .....                                                                         [100%]

=========================================== 5 passed in 0.09s ===========================================



## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.


| Feature | Method(s) | Notes |
| :--- | :--- | :--- |
| **Task sorting** | `Scheduler.sort_by_time()` | Uses `sorted()` with a lambda function and `datetime.strptime` to arrange tasks chronologically by "HH:MM". |
| **Filtering** | `Scheduler.filter_tasks()` | Iterates through pet tasks to exclude items already marked `is_completed=True`. |
| **Conflict handling** | `Scheduler.detect_conflicts()` | Uses a dictionary to track scheduled times, returning warning strings if exact start times overlap. |
| **Recurring tasks** | `Scheduler.complete_and_reschedule()` | Automatically instantiates a new `Task` object using `timedelta(days=1)` when a daily task is completed. |

📸 Demo Walkthrough

**How to use PawPal+:**
1. **Initialize Profile:** Upon loading the app, enter the Owner's name and the Pet's core details.
2. **Schedule Tasks:** Use the input form to add care activities, specifying the exact start time, priority, duration, and recurrence frequency (e.g., Daily).
3. **Generate Plan:** Click "Generate Plan" to trigger the `Scheduler`. The system will filter out completed tasks, sort the remaining ones chronologically, and render them in a clean table.
4. **Conflict Resolution:** If two tasks are scheduled at the exact same time, the UI will intercept the conflict and display a prominent warning banner above the schedule so the owner can adjust their day.

**Sample CLI Output (`main.py` verification):**
```text
🐾 Daily Care Plan for Dave Rodriguez's Pets 🐾
--------------------------------------------------
⚠️ CONFLICT: 'Give Medication' and 'Morning Walk' are both scheduled at 08:00!
-------------------------------------------------- Mochi: Morning Walk (30 min) [HIGH] Luna: Give Medication (5 min) [HIGH] Luna: Laser Pointer Play (15 min) [MEDIUM] Mochi: Evening Feeding (15 min) [HIGH]
--------------------------------------------------