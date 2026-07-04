from pawpal_system import Task, Pet

def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    task = Task(title="Feed Pet", duration_minutes=10, priority="high")
    assert task.is_completed is False  # Should start as False
    
    task.mark_complete()
    assert task.is_completed is True   # Should change to True

def test_pet_add_task():
    """Verify that adding a task increases the pet's task count."""
    pet = Pet(name="Buddy", species="Dog")
    assert len(pet.tasks) == 0  # Should start empty
    
    new_task = Task(title="Brush Fur", duration_minutes=15, priority="low")
    pet.add_task(new_task)
    
    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Brush Fur"