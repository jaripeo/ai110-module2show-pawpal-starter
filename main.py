from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    # 1. Create an Owner
    jordan = Owner(name="Jordan")

    # 2. Create at least two Pets
    mochi = Pet(name="Mochi", species="Dog")
    luna = Pet(name="Luna", species="Cat")

    jordan.add_pet(mochi)
    jordan.add_pet(luna)

    # 3. Add at least three Tasks
    mochi.add_task(Task(title="Morning Walk", duration_minutes=30, priority="high"))
    mochi.add_task(Task(title="Heartworm Medication", duration_minutes=5, priority="high", frequency="monthly"))
    luna.add_task(Task(title="Laser Pointer Play", duration_minutes=15, priority="medium"))

    # 4. Generate and print the schedule
    scheduler = Scheduler(available_time_minutes=120)
    print(scheduler.generate_daily_plan(jordan))

if __name__ == "__main__":
    main()