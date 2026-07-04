from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    """Represents a single pet care activity."""
    title: str
    duration_minutes: int
    priority: str  # Expected values: 'low', 'medium', 'high'

@dataclass
class Pet:
    """Represents a pet and holds their specific care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a new task to the pet's task list."""
        pass

@dataclass
class Owner:
    """Represents the user and holds their pets."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a new pet to the owner's profile."""
        pass

class Scheduler:
    """Handles the algorithmic logic for generating care plans."""
    def __init__(self, available_time_minutes: int):
        self.available_time_minutes = available_time_minutes

    def generate_daily_plan(self, owner: Owner) -> List[Task]:
        """
        Generates a prioritized list of tasks that fit within the available time.
        """
        pass