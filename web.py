import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("To-Do or Not To-Do")
#st.subheader("Track your  tasks!")
st.write("Increase your productivity and track your tasks with this simple to-do app.")
st.text_input(label="", 
                placeholder="Add a task...", 
                on_change=add_todo, 
                key="new_todo")

for index, todo in enumerate(todos):
    count = todo.index
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

#need to run "pip freeze > requirements.txt" after testing streamlit is funcitoning
#then upload to github