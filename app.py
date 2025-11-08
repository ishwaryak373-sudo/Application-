import streamlit as st

st.set_page_config(page_title="Simple Todo App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("✅ Simple To-Do App")

new_task = st.text_input("Enter a task")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task)
        st.success("Task added!")
    else:
        st.warning("Task is empty")

st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks added yet")

else:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([6,1])
        col1.write(f"{i+1}. {t}")
        if col2.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
