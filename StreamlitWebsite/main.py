import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/459a6abc-2736-4b7e-b3f7-04b5da81996d/tmQhyAzmgc.json")
img_contact_form = Image.open("images/tiktok_rizz_party_meme.jpg")
img_lottie_animation = Image.open("images/what-is-the-deal-with-the-lebron-sunshine-meme-and-why-does-v0-ldwzfUTARVtIF3FzcdMDwu3KUwgOiVHhVFCveI9saWA.webp")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Brian :wave:")
st.title("A student at Lakota East High School")
st.write("I am passionate about computer science")
st.write("[Learn More >](https://www.linkedin.com/in/brian-nyachia-a00b86266/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I’m a senior in high school that is highly interested in computer science, and wants to become a software engineer in future. 
            As of now I’ve become proficient in Java but I’m planning on learning other languages like Python, JavaScript, HTML, CSS, and Swift
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/channel/UCmmFRQGpp278At2Q7xdliQg)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Flies are the easiest way to do it
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video..](https://www.youtube.com/watch?v=4Ox-vYu9Ee8)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=lvqvIi3XgcE&list=PLMs3SNJIf3cJYkIvKur6xIO3GalO51u6d&index=829)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ - CHANGE EMAIL ADDRESS
    contact_form = """
    <form action="https://formsubmit.co/nyachia94@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
