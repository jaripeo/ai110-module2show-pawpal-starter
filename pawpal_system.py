from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta, date  # <-- Added 'date' here

@dataclass
class Task:
    """Represents a single pet care activity."""
    title: str
    duration_minutes: int
    priority: str
    start_time: str = "00:00"  # Format HH:MM
    frequency: str = "once"    # 'once', 'daily', 'weekly'
    is_completed: bool = False
    due_date: date = field(default_factory=date.today)  # <-- Changed this line

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.is_completed = True

@dataclass
class Pet:
    """Represents a pet and holds their specific care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a new task to the pet's task list."""
        self.tasks.append(task)

@dataclass
class Owner:
    """Represents the user and holds their pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a new pet to the owner's profile."""
        self.pets.append(pet)

class Scheduler:
    """Handles the algorithmic logic for generating care plans."""
    def __init__(self, available_time_minutes: int):
        self.available_time_minutes = available_time_minutes

    def filter_tasks(self, owner: Owner, pet_name: Optional[str] = None, is_completed: Optional[bool] = None) -> List[tuple]:
        """Filters tasks by pet name and/or completion status."""
        filtered = []
        for pet in owner.pets:
            if pet_name and pet.name != pet_name:
                continue
            for task in pet.tasks:
                if is_completed is not None and task.is_completed != is_completed:
                    continue
                filtered.append((pet.name, task))
        return filtered

    def sort_by_time(self, tasks: List[tuple]) -> List[tuple]:
        """Sorts a list of (pet_name, task) tuples chronologically by HH:MM."""
        return sorted(tasks, key=lambda item: datetime.strptime(item[1].start_time, "%H:%M"))

    def detect_conflicts(self, tasks: List[tuple]) -> List[str]:
        """A lightweight check that flags tasks scheduled for the exact same start_time."""
        warnings = []
        seen_times = {}
        for pet_name, task in tasks:
            if task.start_time in seen_times:
                warnings.append(f"⚠️ CONFLICT: '{task.title}' and '{seen_times[task.start_time]}' are both scheduled at {task.start_time}!")
            else:
                seen_times[task.start_time] = task.title
        return warnings

    def complete_and_reschedule(self, pet: Pet, task: Task) -> None:
        """Marks a task complete and automatically generates the next occurrence if recurring."""
        task.mark_complete()
        
        if task.frequency == "daily":
            new_task = Task(
                title=task.title,
                duration_minutes=task.duration_minutes,
                priority=task.priority,
                start_time=task.start_time,
                frequency=task.frequency,
                due_date=task.due_date + timedelta(days=1)
            )
            pet.add_task(new_task)

    def generate_daily_plan(self, owner: Owner) -> str:
        """Generates a formatted string of the daily schedule with smart sorting and warnings."""
        # 1. Filter to only get incomplete tasks
        pending_tasks = self.filter_tasks(owner, is_completed=False)
        
        # 2. Sort them chronologically
        sorted_tasks = self.sort_by_time(pending_tasks)
        
        # 3. Check for conflicts
        conflicts = self.detect_conflicts(sorted_tasks)

        if not sorted_tasks:
            return "No tasks scheduled for today! Relax."

        schedule_output = f"🐾 Daily Care Plan for {owner.name}'s Pets 🐾\n"
        schedule_output += "-" * 50 + "\n"
        
        # Print Warnings
        for warning in conflicts:
            schedule_output += f"{warning}\n"
            
        if conflicts:
            schedule_output += "-" * 50 + "\n"
            
        # Print Sorted Schedule
        for pet_name, task in sorted_tasks:
            schedule_output += f"[{task.start_time}] {pet_name}: {task.title} ({task.duration_minutes} min) [{task.priority.upper()}]\n"
            
        schedule_output += "-" * 50
        return schedule_output