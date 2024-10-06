import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# ---- Setting up the tab ----
dizzys_trumpet = Image.open("images/Dizzys_trumpet.jpg")
st.set_page_config(page_title="Jazz", page_icon=dizzys_trumpet, layout="wide")

# ---- Using CSS ----
with open("style\style2.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# ---- Loading assets ----
miles_davis = Image.open("images/milesdavis2.jpg")
dizzy_gillespie = Image.open("images/dizzy.webp")
ella_fitzgerald = Image.open("images/ella_fitzgerald.jpg")
glenn_miller = Image.open("images/Glenn-miller-dba73f5.webp")
john_coltrane = Image.open("images/john_coltrane.jpg")
louis_armstrong = Image.open("images/Louis-Armstrong-GettyImages-964102851.jpg")

# ---- Header ----
title = st.markdown("<h1 style='text-align: center; font-size: 150px;'>Jazz</h1>", unsafe_allow_html=True)
st.subheader("\"Jazz stands for freedom. It's supposed to be the voice of freedom: Get out there and improvise, "
             "and take chances, and don't be a perfectionist - leave that to the classical musicians.\" -Dave Brubeck")
st.write("   ")
st.subheader("\"Boxing is like jazz. The better it is, the less people appreciate it.\" -George Foreman")
st.write("   ")
st.subheader("\"If you have to ask what jazz is, you'll never know.\" -Louis Armstrong")
st.write("   ")
st.subheader("\"Jazz is the last refuge of the untalented. Jazz musicians enjoy themselves more than anyone listening "
             "to them does.\" -Tony Wilson")
st.write("   ")
st.subheader("\"Jazz is a fighter. The word 'jazz' means to me, 'I dare you. Let's jump into the unknown!'\" -Wayne "
             "Shorter")
st.write("   ")
st.subheader("\"I only hope that one day, America will recognize what the rest of the world already has known, "
             "that our indigenous music - gospel, blues, jazz and R&B - is the heart and soul of all popular music; "
             "and that we cannot afford to let this legacy slip into obscurity, I'm telling you.\" -Quincy Jones")

# ---- Images ----
with st.container():
    st.write("   ")
    _, col2, _, = st.columns((1,2,1))
    with col2:
        st.image(miles_davis)

with st.container():
    st.write("   ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(dizzy_gillespie)
    with col2:
        st.image(ella_fitzgerald)
    with col3:
        st.image(glenn_miller)

with st.container():
    st.write("   ")
    col1, col2 = st.columns(2)
    with col1:
        st.image(john_coltrane)
    with col2:
        st.image(louis_armstrong)
# ---- 3 Columns: Learn, Listen and Make ----
with st.container():
    st.write("   ")
    col1, col2, col3 = st.columns(3)
    # LEARN
    with col1:
        st.markdown("<h1 style='text-align: center;'>Learn</h1>", unsafe_allow_html=True)

        # Jazz, Ellington, Basie, Mingus, Miller, Coltrane, Davis, Rich

        # Jazz
        st.write("Jazz")
        one, two, three = st.columns(3)
        with one:
            st.write("[Jazz History Tree](https://www.jazzhistorytree.com/)")
        with two:
            st.write("[Origins of Jazz](https://jazzobserver.com/the-origins-of-jazz/)")
        with three:
            st.write("[Jazz Britannica](https://www.britannica.com/art/jazz)")

        # Duke Ellington
        st.write("Duke Ellington")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/Duke_Ellington)")
        with two:
            st.write("[Britannica](https://www.britannica.com/biography/Duke-Ellington)")
        with three:
            st.write("[Kennedy Center](https://www.kennedy-center.org/education/resources-for-educators/classroom-resources/media-and-interactives/artists/ellington-duke/)")

        # Count Basie
        st.write("Count Basie")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/Count_Basie)")
        with two:
            st.write("[Count Basie Center for the Arts](https://thebasie.org/countbasiebio/)")
        with three:
            st.write("[Rutgers University bio](https://countbasie.rutgers.edu/biography/)")

        # Charles Mingus
        st.write("Charles Mingus")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/Charles_Mingus)")
        with two:
            st.write("[Official Website](https://www.charlesmingus.com/mingusbio)")
        with three:
            st.write("[NPR](https://www.npr.org/2022/04/21/1093614930/how-the-late-jazz-great-charles-mingus-is-being-remembered-100-years-later)")

        # Glen Miller
        st.write("Glen Miller")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/Glenn_Miller)")
        with two:
            st.write("[Official Website](https://glennmillerorchestra.com/history/)")
        with three:
            st.write("[Britannica](https://www.britannica.com/biography/Glenn-Miller)")

        # John Coltrane
        st.write("John Coltrane")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/John_Coltrane)")
        with two:
            st.write("[Official Website](https://www.johncoltrane.com/biography)")
        with three:
            st.write("[Senior's Thesis on Coltrane](https://coltrane.room34.com/)")

        # Miles Davis
        st.write("Miles Davis")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/Miles_Davis)")
        with two:
            st.write("[NEA](https://www.arts.gov/honors/jazz/miles-davis)")
        with three:
            st.write("[Timeline](https://www.milesdavis.com/timeline/)")

        # Buddy Rich
        st.write("Buddy Rich")
        one, two, three = st.columns(3)
        with one:
            st.write("[Wikipedia](https://en.wikipedia.org/wiki/Buddy_Rich)")
        with two:
            st.write("[Official Website](http://buddyrich.com/)")
        with three:
            st.write("[Flapper Press](https://www.flapperpress.com/post/unbeatable-the-life-and-drumming-of-buddy-rich)")


    with col2:
        st.markdown("<h1 style='text-align: center;'>Listen</h1>", unsafe_allow_html=True)

        # Ellington, Basie, Mingus, Miller, Coltrane, Davis, Rich

        # one, two, three, four = st.columns(4)
        # with one:
        # st.write("[Spotify](https://open.spotify.com/artist/4F7Q5NV6h5TSwCainz8S5A?autoplay=true)")
        # with two:
        # st.write("[Apple Music](https://music.apple.com/us/artist/duke-ellington/39525)")
        # with four:
        # st.write("[YouTube](https://www.youtube.com/results?search_query=duke+ellington)")

        # Duke Ellington
        st.write("Duke Ellington")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/4F7Q5NV6h5TSwCainz8S5A?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/duke-ellington/39525)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=Duke+Ellington)")

        # Count Basie
        st.write("Count Basie")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/2jFZlvIea42ZvcCw4OeEdA?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/count-basie/28327)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=Count+Basie)")

        # Charles Mingus
        st.write("Charles Mingus")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/1W8TbFzNS15VwsempfY12H?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/charles-mingus/478880)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=Charles+Mingus)")

        # Glen Miller
        st.write("Glen Miller")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/2aAHdB5HweT3mFcRzm0swc?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/glen-miller/1458900599)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=Glen+Miller)")

        # John Coltrane
        st.write("John Coltrane")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/2hGh5VOeeqimQFxqXvfCUf?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/john-coltrane/120199)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=John+Coltrane)")

        # Miles Davis
        st.write("Miles Davis")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/0kbYTNQb4Pb1rPbbaF0pT4?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/miles-davis/44984)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=Miles+Davis)")

        # Buddy Rich
        st.write("Buddy Rich")
        one, two, three = st.columns(3)
        with one:
            st.write("[Spotify](https://open.spotify.com/artist/1pVtwG5Up1OZOEpSHJ4AAs?autoplay=true)")
        with two:
            st.write("[Apple Music](https://music.apple.com/us/artist/buddy-rich/82499)")
        with three:
            st.write("[YouTube](https://www.youtube.com/results?search_query=Buddy+Rich)")
    # MAKE
    with col3:
        st.markdown("<h1 style='text-align: center;'>Make</h1>", unsafe_allow_html=True)

        # Musescore 4, Flat.io
        st.write("[Musescore(FREE)](https://musescore.org/en)")
        st.write("[Flat(FREE)](https://flat.io/)")
        st.write("[Noteflight(FREE & PREMIUM VERSION)](https://www.noteflight.com/)")
        st.write("[Sibelus(MONTHLY SUBSCRIPTION)](https://www.avid.com/sibelius)")