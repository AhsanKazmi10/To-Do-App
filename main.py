import streamlit as st

# App Title with Icon
st.set_page_config(page_title="To-Do List App", page_icon="✅")
st.title("📝 To-Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar Heading with Icon
st.sidebar.header("⚡ Manage Your Tasks")

# Add Task Input
new_task = st.sidebar.text_input("➕ Add a new task", placeholder="Enter your task here...")

# Add Task Button
if st.sidebar.button("📌 Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success("✅ Task added successfully!")
    else:
        st.warning("⚠️ Task cannot be empty!")

# Display Tasks
st.header("📝 Your To-Do List")

if not st.session_state.tasks:
    st.info("🎯 No tasks yet! Start by adding a task from the sidebar.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Checkbox for marking task completion
        completed = col1.checkbox(f"✅ {task['task']}", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Edit button with state management
        if f"edit_mode_{index}" not in st.session_state:
            st.session_state[f"edit_mode_{index}"] = False

        if col2.button("✏️", key=f"edit_{index}"):
            st.session_state[f"edit_mode_{index}"] = True

        if st.session_state[f"edit_mode_{index}"]:
            new_task_text = st.text_input("Edit Task", task["task"], key=f"edit_text_{index}")
            if st.button("💾 Save", key=f"save_{index}"):
                if new_task_text.strip():
                    st.session_state.tasks[index]["task"] = new_task_text
                    st.session_state[f"edit_mode_{index}"] = False
                    st.rerun()  # ✅ Updated from st.experimental_rerun()

        # Delete button
        if col3.button("🗑️", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.rerun()  # ✅ Updated from st.experimental_rerun()

# Clear All Tasks Button
if st.button("⚠️ Clear All Tasks"):
    st.session_state.tasks = []
    st.success("🧹 All tasks deleted successfully!")
    st.rerun()  # ✅ Updated from st.experimental_rerun()

# Footer
st.markdown("---")
st.caption("🚀 Stay organized & productive with this simple To-Do List App.")
