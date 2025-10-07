import streamlit as st
import subprocess
import webbrowser
import os
import sys
import socket

st.title("📚 Smart Streamlit Project Launcher")

# --- Helper function to find a free port ---
def find_free_port():
    s = socket.socket()
    s.bind(('', 0))  # OS assigns a free port
    port = s.getsockname()[1]
    s.close()
    return port

# --- Track running chapters ---
if "running_chapters" not in st.session_state:
    st.session_state.running_chapters = {}

# --- List your chapter scripts ---
chapters = ["chapter-1.py", "chapter-2.py", "chapter-3.py"]

# --- Select chapter ---
selected_chapter = st.selectbox("Select Chapter to Run", chapters)

# --- Run button ---
if st.button("Run Selected Chapter"):
    if os.path.exists(selected_chapter):
        # Check if already running
        if selected_chapter in st.session_state.running_chapters:
            port = st.session_state.running_chapters[selected_chapter]
            st.info(f"{selected_chapter} is already running on port {port}")
            webbrowser.open(f"http://localhost:{port}")
        else:
            try:
                port = find_free_port()
                # Launch Streamlit app
                subprocess.Popen(
                [sys.executable, "-m", "streamlit", "run", selected_chapter, "--server.port", str(port)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True)

            except Exception as e:
                st.error(f"Error launching the chapter: {e}")
    else:
        st.error(f"File {selected_chapter} not found!")

# --- Show running chapters ---
if st.session_state.running_chapters:
    st.subheader("Running Chapters")
    for chap, port in st.session_state.running_chapters.items():
        st.write(f"{chap} ➡ http://localhost:{port}")
