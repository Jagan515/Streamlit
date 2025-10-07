import streamlit as st
from chapter_1 import run_chapter_1
from chapter_2 import run_chapter_2
from chapter_3 import run_chapter_3
from chapter_4 import run_chapter_4
from chapter_5 import run_chapter_5

st.title("📚 Streamlit Project Launcher (Cloud-Friendly)")

chapter_map = {
    "Chapter 1": run_chapter_1,
    "Chapter 2": run_chapter_2,
    "Chapter 3": run_chapter_3,
    "Chapter 4": run_chapter_4,
    "Chapter 5": run_chapter_5,
}

selected_chapter = st.selectbox("Select Chapter", list(chapter_map.keys()))

if st.button("Run Selected Chapter"):
    st.info(f"Running {selected_chapter}...")
    chapter_map[selected_chapter]()  # call the function
    
 # Note: Remove run_chapter_number to work properly.