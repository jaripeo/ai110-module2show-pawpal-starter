import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- MANAGE APPLICATION MEMORY ---
if "owner" not in st.session_state:
    default_owner = Owner(name="Dave Rodriguez")
    default_pet = Pet(name="Mochi", species="dog")
    default_owner.add_pet(default_pet)
    st.session_state.owner = default_owner

st.subheader("Profile")
col_o, col_p, col_s = st.columns(3)
with col_o:
    owner_name = st.text_input("Owner", value=st.session_state.owner.name)
with col_p:
    pet_name = st.text_input("Pet name", value=st.session_state.owner.pets[0].name)
with col_s:
    species = st.selectbox("Species", ["dog", "cat", "other"], index=0)

# Sync UI changes back to the objects
st.session_state.owner.name = owner_name
st.session_state.owner.pets[0].name = pet_name
st.session_state.owner.pets[0].species = species

st.divider()

st.markdown(f"### Add a Task for {st.session_state.owner.pets[0].name}")

col1, col2 = st.columns(2)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
    start_time = st.time_input("Start Time").strftime("%H:%M")
with col2:
    duration = st.number_input("Duration (min)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"], index=1)

if st.button("Add task", type="primary"):
    new_task = Task(title=task_title, duration_minutes=int(duration), priority=priority, start_time=start_time, frequency=frequency)
    st.session_state.owner.pets[0].add_task(new_task)
    st.success(f"Added '{task_title}' to the schedule!")

st.divider()

st.subheader("Today's Smart Schedule")
if st.button("Generate Plan"):
    scheduler = Scheduler(available_time_minutes=120)
    
    # 1. Filter and Sort
    pending_tasks = scheduler.filter_tasks(st.session_state.owner, is_completed=False)
    sorted_tasks = scheduler.sort_by_time(pending_tasks)
    
    # 2. Check for Conflicts
    conflicts = scheduler.detect_conflicts(sorted_tasks)
    for warning in conflicts:
        st.warning(warning, icon="⚠️")
        
    # 3. Display Data
    if sorted_tasks:
        display_data = []
        for pet, task in sorted_tasks:
            display_data.append({
                "Time": task.start_time,
                "Pet": pet,
                "Task": task.title,
                "Duration": f"{task.duration_minutes}m",
                "Priority": task.priority.upper(),
                "Repeats": task.frequency
            })
        st.table(display_data)
    else:
        st.info("No tasks scheduled for today! Relax.")