# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design has four core classes to keep the data and logic sepearted from each other. They classes are: Owner, Pet, Task, and Scheduler. Below I describe each of the classes. 

Owner: Represents the application user. It stores the owner's name and maintains a list of their Pet objects, acting as the top entity.

Pet: Holds basic details about the animal (name, species) and manages a list of Task objects specifically related to their care.

Task: A data structure representing a care activity. It tracks the title, the duration it takes (in minutes), and its priority level.

Scheduler: The class that controls the system. It handles the constraints (like maximum available time) and contains the logic to filter, sort, and output a prioritized daily plan.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, the design changed significantly during the implementation phase. In Phase 4, I had to expand the Task class to include new attributes: start_time, frequency, is_completed, and due_date. This change was necessary to move beyond a simple data container and actually support the new "smart" scheduling features, such as sorting tasks chronologically and using the datetime module to automatically reschedule recurring daily tasks.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler currently considers completion status (filtering), chronological time (sorting), and overlapping schedules (conflict detection). I decided that filtering out completed tasks and sorting the remaining ones by start_time mattered most because a pet owner fundamentally needs a clean, chronological timeline to follow throughout the day. Flagging exact time conflicts was prioritized next to ensure the owner doesn't accidentally double-book their routine.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is using a "lightweight" conflict detection algorithm that only checks for exact start_time matches, rather than calculating overlapping durations.

This tradeoff is reasonable because pet care tasks are often fluid (like starting a 10-minute feeding at 08:00 and a 5-minute medication at 08:05 isn't a strict failure like a double-booked meeting). It keeps the code simpler, avoids importing complex interval-tree libraries, and still gives the user the necessary "heads up" warning without crashing the program.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used my AI coding assistant primarily as an architectural sounding board and a syntax resource. It was highly effective for translating abstract concepts (like UML diagrams) into structural Python dataclasses, and for finding specific library functions I needed, such as using `datetime.strptime` for chronological sorting and `timedelta` for recurring task dates.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

During the implementation of the conflict detection algorithm, the initial AI suggestion included a complex interval-tree approach to calculate overlapping minute durations. I rejected this because it was overly complex for a simple pet scheduler. Instead, I guided the AI to write a lightweight dictionary-based solution that only checks for exact `start_time` matches, which I verified by writing a specific pytest case.

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested basic state changes (verifying that mark_complete() correctly toggles status and that adding a task updates a pet's list) alongside the smart algorithmic behaviors: sorting correctness, daily recurrence logic (ensuring a new task is generated exactly one day in the future), and conflict detection (verifying duplicate times trigger a warning). These tests were critical to verify that the "brain" of the application was completely reliable in the CLI before connecting it to the Streamlit UI.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am highly confident in the scheduler's current capabilities because all core logic paths and primary edge cases (like out-of-order task entry and duplicate time slots) pass the automated pytest suite. If I had more time, the next edge cases I would test include date rollovers for recurring tasks (e.g., what happens when a daily task is completed on February 28th or December 31st) and handling user inputs with invalid time string formats.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with successfully bridging the CLI backend logic to the Streamlit frontend. Ensuring the Streamlit session state correctly held the `Owner` object without wiping the data on every render was a major win for the app's usability.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the UI by adding interactive checkboxes next to each task in the Streamlit table so the user could trigger the `complete_and_reschedule()` logic directly from the browser, rather than just generating the plan.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

Being the "lead architect" with AI means you cannot just copy and paste; you have to enforce system boundaries. The AI will write whatever code you ask for, but as the human, I had to ensure the `Scheduler` wasn't suddenly storing pet data, keeping the separation of concerns intact.