import streamlit as s
import functions as fun


def add_todo():
    todo = s.session_state['todo']
    print(todo)
    todos = fun.get_todos()
    todos.append(todo + "\n")
    fun.save(todos)
    s.session_state['todo'] = ""


s.title("Todo App")
s.subheader("I am building a world class todo app which can be accessible across the world!!")
s.write("""
# My First App Hello *World*
""")

todos = fun.get_todos()


def check():
    print("clicked")


for idx, todo in enumerate(todos):
    checked = s.checkbox(todo, key=todo)
    if checked:
        todos.pop(idx)
        fun.save(todos)
        del s.session_state[todo]
        s.experimental_rerun()

s.text_input(label="", placeholder="Add new todo.....", on_change=add_todo, key='todo')

s.session_state
