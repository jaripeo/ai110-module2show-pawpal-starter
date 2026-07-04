import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

st.divider()

# --- STEP 2: MANAGE APPLICATION MEMORY ---
# Initialize our backend objects in session state so they survive page reloads
if "owner" not in st.session_state:
    default_owner = Owner(name="Jordan")
    default_pet = Pet(name="Mochi", species="dog")
    default_owner.add_pet(default_pet)
    st.session_state.owner = default_owner

st.subheader("Quick Demo Inputs")

# Update the objects based on UI inputs
owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
pet_name = st.text_input("Pet name", value=st.session_state.owner.pets[0].name)
species = st.selectbox("Species", ["dog", "cat", "other"], index=0)

# Sync UI changes back to the objects
st.session_state.owner.name = owner_name
st.session_state.owner.pets[0].name = pet_name
st.session_state.owner.pets[0].species = species

st.markdown("### Tasks")
st.caption(f"Add a task for {st.session_state.owner.pets[0].name}.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

# --- STEP 3: WIRING UI ACTIONS TO LOGIC ---
if st.button("Add task"):
    # Create a real Task object from our backend logic
    new_task = Task(title=task_title, duration_minutes=int(duration), priority=priority)
    
    # Add it to the pet's task list using the backend method
    st.session_state.owner.pets[0].add_task(new_task)
    st.success(f"Added to {st.session_state.owner.pets[0].name}'s profile!")

# Display current tasks dynamically from the backend objects
current_tasks = st.session_state.owner.pets[0].tasks
if current_tasks:
    st.write(f"Current tasks for {st.session_state.owner.pets[0].name}:")
    # Convert objects to a format st.table can easily read
    display_tasks = [{"Title": t.title, "Duration (min)": t.duration_minutes, "Priority": t.priority} for t in current_tasks]
    st.table(display_tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button will call your scheduling logic to generate a plan.")

if st.button("Generate schedule"):
    # We will wire this up fully in Phase 4, but let's test the connection!
    scheduler = Scheduler(available_time_minutes=120)
    
    # Call the generate_daily_plan method from pawpal_system.py
    schedule_output = scheduler.generate_daily_plan(st.session_state.owner)
    
    st.text(schedule_output)