import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kurt's Code Corner", page_icon="images\\favicon.png", layout="wide")

with open("style.css", "r") as css_file:
    css = css_file.read()


st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown("<h1>Kurt's Code Corner</h1>",unsafe_allow_html=True)
st.markdown("<h2>A blogsite project</h2>",unsafe_allow_html=True)


selected = option_menu(
    menu_title=None,
    options=["Home","Content","About Me"],
    icons=["house","camera","person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "#fafafa",},
            "icon": {"color": "orange", "font-size": "30px"}, 
            "nav-link": {"font-size": "30px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#a34534"},
        }
    )

if selected == "Home":
    
    Home1,Home2 = st.columns(2)

    with Home1:
        st.markdown("<h1>This website is a programming project developed by Kurt Ronnel B. Chua</h1>",unsafe_allow_html=True)
    with Home2:
        st.markdown("""<img id="KPhoto" src="https://scontent.fmnl8-3.fna.fbcdn.net/v/t39.30808-6/320781449_545114937233508_2340515307354402763_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEqZ9ssVdWb7nxABUUCUYpfIxQhh9vEWiUjFCGH28RaJbkCDJtUJy0XXuGd0S8ezpExR6u6QDklm94B17oc36ZN&_nc_ohc=Qq6AvUFXM4AAX_spXsN&_nc_ht=scontent.fmnl8-3.fna&cb_e2o_trans=t&oh=00_AfC0b_UuUWWbtYw6m4uIfxPxkCS2og2jEc4Jykkhvt5Qag&oe=656BD784">""",unsafe_allow_html=True)
        
    
        
if selected == "Content":
    
    st.markdown("<h1>My Socials</h1>",unsafe_allow_html=True)
    
    facebook, github, stack_overflow = st.columns(3)

    with facebook:
        st.markdown("""<a href="https://www.facebook.com/kurtronnel.chua.7"><img id="FBPhoto" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Facebook_logo_36x36.svg/480px-Facebook_logo_36x36.svg.png"></a>""",unsafe_allow_html=True)

    with github:
        st.markdown("""<a href="https://github.com/wafoolz12"><img id="GHPhoto" src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"></a>""",unsafe_allow_html=True)

        

    with stack_overflow:
        st.markdown("""<a href="https://stackoverflow.com/users/22993346/kurt-chua"><img id="SOPhoto" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Stack_Overflow_icon.svg/768px-Stack_Overflow_icon.svg.png"></a>""",unsafe_allow_html=True)

    st.markdown("<h1>Contact Me!</h1>",unsafe_allow_html=True)

    


    st.markdown("""
                
    <form action="https://formsubmit.co/chuakurt24@gmail.com" method="POST">
            <input type="text" name="name" placeholder="your name" required>
            <input type="email" name="email" placeholder="your email" required>
            <textarea name="message" placeholder="your message"></textarea>
            <button type="submit">Send</button>
    </form>
                """,unsafe_allow_html=True)



if selected == "About Me":
    
    st.markdown("<h1>Things about me</h1>",unsafe_allow_html=True)
    
    Description1, Photo1 = st.columns(2)

    with Description1:
        
        st.markdown("""

        <p id="Bio1"><span style="font-weight: bold"><u>Introduction</u></span><br><br>Hello my name is Kurt Ronnel B. Chua and I am a student studying for a degree on Bachelor of Science in Computer Engineering at SNSU(Surigao Del Norte State University).
                    You might be asking right now, why did you choose such a course? well, it is because I have a passion for computers, technology, and what not. But
                    what I really enjoy the most on that aspect is software development. I first got introduced to programming back in 2020 when my cousin would always talk about
                    his game development ventures, I would always find it interesting just how passionately he talked about his coding projects, so I became curious, and then
                    asked him to teach me. And all is history.</p>
                    
    """, unsafe_allow_html=True)
        
    with Photo1:
        st.markdown("""<img id="TypeMan" src="https://media.tenor.com/M-WzFWCPVHsAAAAC/guy-typing-typing.gif">""",unsafe_allow_html=True)

    Photo2, Description2 = st.columns(2)

    with Photo2:
        st.markdown("""<img id="Flappy" src="https://media0.giphy.com/media/euuaA2cwLEUuI/giphy.gif">""",unsafe_allow_html=True)

    with Description2:

        st.markdown("""

        <p id="Bio2"><span style="font-weight: bold"><u>Past Projects</u></span><br><br>After being taught the basics and fundamentals of
                    programming, I worked on a few projects. Mostly games, I started with the scratch game engine because back then, we found type coding intimidating and preferred using
                    drag drop. I made a few games but they were pretty awful, but I did make a rocket game that I am pretty proud of. And as time went on, I started using bigger game engines
                    like Unity. I made a flappy bird knockoff with it.</p>
                    
    """, unsafe_allow_html=True)

    Description3, Photo3 = st.columns(2)

    with Description3:
        
        st.markdown("""

        <p id="Bio3"><span style="font-weight: bold"><u>College Life</u></span><br><br>And now brings us to the present. Today, I am currently studying Computer Engineering at Surigao Del Norte State
                    University, SNSU for short, and I have so far really learned a lot when it comes to programming. I've learned languages like C, C++, and Python, currently using python, and I hope
                    to be able to learn more languages in the near future like JavaScript, Java, C#, etc. So far I've been doing ok, and I hope to make it through the first semester, although Calculus is pretty difficult, I may be able to pull
                    through.</p>
                    
    """, unsafe_allow_html=True)


    with Photo3:
            st.markdown("""<img id="College" src="https://www.vrogue.co/top-featureds-media.giphy.com/media/114QbccJsc5cis/giphy.gif">""",unsafe_allow_html=True)

    



