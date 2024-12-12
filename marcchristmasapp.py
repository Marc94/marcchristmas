import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="Merry Christmas!", page_icon="🎄")

# Title and header
st.title("🎄 Merry Christmas! 🎅")
st.header("Welcome to the Christmas Spirit App!")

# Display Christmas greeting
st.subheader("A Festive Season of Joy, Peace, and Love!")
st.write("Let's make this Christmas more fun and interactive!")

# Display a random Christmas quote
christmas_quotes = [
    "May your days be merry and bright!",
    "Wishing you a magical Christmas season!",
    "Merry Christmas and Happy New Year!",
    "May the joy and peace of Christmas be with you all through the New Year.",
    "Christmas is not a time nor a season, but a state of mind."
]

st.write("### Christmas Quote of the Day:")
st.write(f"**{random.choice(christmas_quotes)}**")

# Christmas wish feature
st.write("### Send Your Christmas Wish!")
name = st.text_input("What's your name?")

if name:
    wish = st.text_area("Write your Christmas wish:")
    if st.button("Send Wish"):
        st.write(f"🎄 Merry Christmas, {name}! 🎅")
        st.write(f"Your Wish: {wish}")
        st.balloons()  # Fun animation on button click!

# Display Christmas music (optional)
music_link = "https://www.youtube.com/watch?v=8jD9nFc-aBQ"  # A Christmas music link
st.write("🎶 Listen to some Christmas music while you are here! 🎶")
st.markdown(f"[Click here for some Christmas music]( {music_link} )")
