import time
import streamlit as st
import pyautogui

# Streamlit App Title
st.set_page_config(page_title="Desktop Automation Tool",page_icon="🤖",layout="wide")

# Sidebar for Task Selection
with st.sidebar:
    st.header("Task Selection")
    task = st.selectbox(
        "Select a Task",
        [
            "Move Mouse",
            "Click Mouse",
            "Type Text",
            "Take Screenshot",
            "Drag and Drop"
        ]
    )

# Function for perform automation tasks
def perform_task(task):
    try:
        # if user select Mouse MOve from the dropdown
        if task == "Move Mouse":
            st.subheader("Move Mouse")
            x = st.number_input("Enter X coordinate", value=100, step=10)
            y = st.number_input("Enter Y coordinate", value=100, step =10)
            duration = st.number_input("Duration (seconds)", value=1.0, step=1.0)
            if st.button("Move Mouse"):
                pyautogui.moveTo(x, y, duration=duration)
                st.success(f"Moved mouse to ({x}, {y}) in {duration} seconds.")

        # if user select Click Mouse from the dropdown 
        elif task == "Click Mouse":
            st.subheader("Click Mouse")
            button = st.radio("Select Mouse Button", ["left", "right", "middle"])
            clicks = st.number_input("Number of Clicks", value=1, min_value=1)
            if st.button("Click Mouse"):
                pyautogui.click(button=button, clicks=clicks)
                st.success(f"Clicked {button} button {clicks} times.")

        # if user select Type Text from the dropdown
        elif task == "Type Text":
            st.subheader("Type Text")
            text = st.text_input("Enter text to type")
            delay = st.number_input("Delay between keys (seconds)", value=0.1)
            if st.button("Type Text"):
                pyautogui.write(text, interval=delay)
                st.success(f"text typed: {text}")

        # if user select Take Screenshot from the dropdown
        elif task == "Take Screenshot":
            st.subheader("Take Screenshot")
            if st.button("Capture Screenshot"):
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                st.image("screenshot.png", caption="Desktop Screenshot", use_column_width=True)
                st.success("Screenshot captured and saved.")

        # if user select Drag and Drop from the dropdown
        elif task == "Drag and Drop":
            st.subheader("Drag and Drop")
            start_x = st.number_input("Start X coordinate", value=100)
            start_y = st.number_input("Start Y coordinate", value=100)
            end_x = st.number_input("End X coordinate", value=300)
            end_y = st.number_input("End Y coordinate", value=300)
            if st.button("Drag and Drop"):
                pyautogui.moveTo(start_x, start_y, duration=1)
                pyautogui.dragTo(end_x, end_y, duration=1)
                st.success(f"Dragged from ({start_x}, {start_y}) to ({end_x}, {end_y}).")

    except Exception as e:
        st.error(f"Error during automation: {str(e)}")


st.title("Desktop Automation Tool 🤖")
st.write("Perform desktop automation tasks using this tool.")

perform_task(task)


st.subheader("Instructions")
st.write("""
1. **Move Mouse**: Move the mouse cursor to specific coordinates.
2. **Click Mouse**: Perform mouse clicks (left, right, or middle).
3. **Type Text**: Simulate keyboard input.
4. **Take Screenshot**: Capture the screenshot.
5. **Drag and Drop**: Drag the mouse from one location to another locatio\n.
""")