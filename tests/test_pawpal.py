from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler

# --- Phase 2 Tests ---

def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    task = Task(title="Feed Pet", duration_minutes=10, priority="high")
    assert task.is_completed is False
    task.mark_complete()
    assert task.is_completed is True

def test_pet_add_task():
    """Verify that adding a task increases the pet's task count."""
    pet = Pet(name="Buddy", species="Dog")
    new_task = Task(title="Brush Fur", duration_minutes=15, priority="low")
    pet.add_task(new_task)
    assert len(pet.tasks) == 1

# --- Phase 5: Smart Algorithm Tests ---

def test_sorting_correctness():
    """Verify tasks are returned in chronological order."""
    scheduler = Scheduler(available_time_minutes=120)
    
    # Create an evening task and a morning task
    task1 = Task(title="Evening Walk", duration_minutes=10, priority="low", start_time="18:00")
    task2 = Task(title="Morning Feeding", duration_minutes=10, priority="high", start_time="08:00")

    # Pass them into the sorter out of order
    unsorted_tasks = [("Dog", task1), ("Dog", task2)]
    sorted_tasks = scheduler.sort_by_time(unsorted_tasks)

    # The first item in the sorted list should now be the Morning task
    assert sorted_tasks[0][1].title == "Morning Feeding"
    assert sorted_tasks[1][1].title == "Evening Walk"

def test_recurrence_logic():
    """Confirm that marking a daily task complete creates a new task for the following day."""
    scheduler = Scheduler(available_time_minutes=120)
    pet = Pet(name="Buddy", species="Dog")
    task = Task(title="Walk", duration_minutes=30, priority="high", frequency="daily")
    pet.add_task(task)

    # Complete the task, which should trigger the automatic reschedule
    scheduler.complete_and_reschedule(pet, task)

    # The pet should now have 2 tasks (the old completed one, and the new one for tomorrow)
    assert len(pet.tasks) == 2
    assert pet.tasks[0].is_completed is True
    assert pet.tasks[1].is_completed is False
    
    # Verify the new task's due date is exactly 1 day from today
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)

def test_conflict_detection():
    """Verify that the Scheduler flags duplicate times."""
    scheduler = Scheduler(available_time_minutes=120)
    
    # Create two tasks at the exact same start time (08:00)
    task1 = Task(title="Walk", duration_minutes=30, priority="high", start_time="08:00")
    task2 = Task(title="Meds", duration_minutes=5, priority="high", start_time="08:00")

    tasks_to_check = [("Buddy", task1), ("Luna", task2)]
    conflicts = scheduler.detect_conflicts(tasks_to_check)

    # The system should return exactly 1 warning about the 08:00 conflict
    assert len(conflicts) == 1
    assert "CONFLICT" in conflicts[0]