import streamlit as st
from datetime import date

st.set_page_config(page_title="🍕 Food Lover App", layout="centered")

st.title("🍕🍜 Food Lover App 🍲")

# --- Step 1: User Name ---
name = st.text_input("Enter your name")
if not name:
    st.warning("Please enter your name to start ordering!")

# --- Step 2: Main Dish Selection ---
if name:
    main_dish = st.radio(
        "Pick your main dish: ", 
        ["Pizza", "Momos", "Chaap", "Chinese"]
    )

    # --- Step 3: Style/Flavor ---
    # used www.pexels.com for free images
    if main_dish == "Pizza":
        style = st.selectbox("Choose Pizza type: ", ["Margherita", "Pepperoni", "Veggie", "Cheese Burst"])
        image_url = "https://render.fineartamerica.com/images/rendered/default/metal-print/8/8/break/images/artworkimages/medium/1/pepperoni-pizza-james-w-johnson.jpg"
    elif main_dish == "Momos":
        style = st.selectbox("Choose Momos type: ", ["Steamed", "Fried", "Tandoori"])
        image_url = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/momos-dumplings-from-nepal-with-a-dip-manuel-krug.jpg"
    elif main_dish == "Chaap":
        style = st.selectbox("Choose Chaap style: ", ["Soya Chaap", "Paneer Chaap", "Spicy Chaap"])
        image_url = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/chukunder-chaap-vegetarian-beet-meatball-nitin-kapoor.jpg"
    else:
        style = st.selectbox("Choose Chinese dish: ", ["Noodles", "Fried Rice", "Manchurian", "Chow Mein"])
        image_url = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/china-noodles-.jpg"

    st.image(image_url, width=100)

    # --- Step 4: Additional Options ---
    extra_cheese = st.checkbox("Add Extra Cheese (Pizza only)")
    spicy = st.checkbox("Make it Spicy 🌶️")
    spice_level = st.slider("Choose spice level 🌶️", 0, 5, 3)
    quantity = st.number_input("How many plates?", min_value=1, max_value=10, step=1)
    delivery_date = st.date_input("Select delivery date", min_value=date.today())

    # --- Step 5: Place Order ---
    if st.button("Place Order"):
        if quantity < 1:
            st.error("Please select at least 1 plate!")
        elif not style:
            st.error("Please select a style/flavor!")
        else:
            st.success(f"Thank you {name}! Your order of {quantity} {main_dish} ({style}) is confirmed for {delivery_date}.")
            
            # --- Step 6: Dish-based Animations ---
            if main_dish == "Pizza":
                st.balloons()
            elif main_dish == "Momos":
                st.snow()
            elif main_dish == "Chaap":
                st.snow()
            else:  # Chinese
                st.balloons()
                st.snow()
            
            # Show extra options
            if extra_cheese:
                st.write("Extra Cheese added 🧀")
            if spicy:
                st.write("Your food will be extra spicy 🌶️")
            st.write(f"Spice level: {spice_level}")
