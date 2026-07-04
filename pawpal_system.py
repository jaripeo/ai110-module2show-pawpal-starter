from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a single pet care activity."""
    title: str
    duration_minutes: int
    priority: str  # Expected values: 'low', 'medium', 'high'
    frequency: str = "daily"
    is_completed: bool = False

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
    """Retrieves and organizes tasks across all pets for a daily plan."""
    def __init__(self, available_time_minutes: int):
        self.available_time_minutes = available_time_minutes

    def get_all_pending_tasks(self, owner: Owner) -> List[tuple]:
        """
        Retrieves all incomplete tasks from the owner's pets.
        Returns a list of tuples containing (pet_name, Task).
        """
        all_tasks = []
        for pet in owner.pets:
            for task in pet.tasks:
                if not task.is_completed:
                    all_tasks.append((pet.name, task))
        return all_tasks

    def generate_daily_plan(self, owner: Owner) -> str:
        """Generates a formatted string of the daily schedule."""
        pending_tasks = self.get_all_pending_tasks(owner)
        
        if not pending_tasks:
            return "No tasks scheduled for today! Relax."

        schedule_output = f"🐾 Daily Care Plan for {owner.name}'s Pets 🐾\n"
        schedule_output += "-" * 40 + "\n"
        
        for pet_name, task in pending_tasks:
            schedule_output += f"[{task.priority.upper()}] {pet_name}: {task.title} ({task.duration_minutes} min) - {task.frequency}\n"
            
        schedule_output += "-" * 40
        return schedule_output