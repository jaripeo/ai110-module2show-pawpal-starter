from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    jordan = Owner(name="Jordan")
    mochi = Pet(name="Mochi", species="Dog")
    luna = Pet(name="Luna", species="Cat")
    jordan.add_pet(mochi)
    jordan.add_pet(luna)

    # Added OUT OF ORDER to test the sorting algorithm
    mochi.add_task(Task(title="Evening Feeding", duration_minutes=15, priority="high", start_time="18:00", frequency="daily"))
    mochi.add_task(Task(title="Morning Walk", duration_minutes=30, priority="high", start_time="08:00", frequency="daily"))
    
    # Scheduled at 08:00 to trigger the Conflict Detector
    luna.add_task(Task(title="Give Medication", duration_minutes=5, priority="high", start_time="08:00", frequency="daily"))
    luna.add_task(Task(title="Laser Pointer Play", duration_minutes=15, priority="medium", start_time="12:30"))

    scheduler = Scheduler(available_time_minutes=120)
    
    # Print the full schedule (Tests filtering, sorting, and conflicts)
    print(scheduler.generate_daily_plan(jordan))
    
    # Test Recurring Logic
    print("\n--- Testing Recurring Logic ---")
    morning_walk = mochi.tasks[1]
    print(f"Before completion: Mochi has {len(mochi.tasks)} tasks.")
    
    scheduler.complete_and_reschedule(mochi, morning_walk)
    
    print(f"After completion: Mochi has {len(mochi.tasks)} tasks.")
    print(f"New task due date: {mochi.tasks[-1].due_date} (Status: Completed={mochi.tasks[-1].is_completed})")

if __name__ == "__main__":
    main()