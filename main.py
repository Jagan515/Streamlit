import streamlit as st  
import pandas as pd
import numpy as np
st.title("Hello World")
st.header("Welcome to my app")
st.subheader("This is a subheader")
st.write("This is my first Streamlit app")
st.text("This is some text")

st.markdown("This is **bold** text and this is *italic* text")

st.latex(r"E=mc^2")

st.code("print('Hello, World!')", language='python')

st.caption("This is a caption")

st.json({"name": "John", "age": 30, "city": "New York"}) 

st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})

st.table({"Column A": ["A", "B", "C"], "Column B": ["D", "E", "F"]})

st.metric(label="Speed", value="120 km/h", delta="10 km/h")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.title("📍 Lovely Professional University Location")

# LPU coordinates
data = pd.DataFrame({
    'lat': [31.252232],
    'lon': [75.703115]
})

st.map(data, zoom=14)
st.progress(70)
st.spinner("Loading...")
# st.balloons()
st.button("Click Me")

st.checkbox("Check Me")

st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])

st.selectbox("Select an option", ["Option A", "Option B", "Option C"])

st.multiselect("Select multiple options", ["Choice 1", "Choice 2", "Choice 3"])

st.slider("Select a value", 0, 100, 50)

st.text_input("Enter some text")

st.text_area("Enter a longer text")

st.number_input("Enter a number", min_value=0, max_value=100, value=50)

st.date_input("Select a date")

st.time_input("Select a time")

st.file_uploader("Upload a file")

st.color_picker("Pick a color")

# side bar use prefix sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.header("Sidebar Header")
st.sidebar.subheader("Sidebar Subheader")
st.sidebar.code("print('Hello from the sidebar!')", language='python')
st.sidebar.text("This is some sidebar text")

st.sidebar.checkbox("Sidebar Checkbox")
st.snow()

