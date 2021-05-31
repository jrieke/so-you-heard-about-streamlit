import streamlit as st
from execbox import execbox

import ui

st.set_page_config(page_title="So you heard about Streamlit...", page_icon="🎈")

# Make radio buttons horizontal.
st.write(
    """
    <style>
        .main * div.row-widget.stRadio > div {
            flex-direction:row
        }
    </style>
    """
    "",
    unsafe_allow_html=True,
)

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/balloon_1f388.png",
    width=100,
)
st.write(
    f"""
    # So you heard about Streamlit...

    Hey! 👋 
    When you read this, someone probably told you about Streamlit and how great it is.
    But you have no idea how Streamlit works or how to code in Python. This guide is
    just for you. It teaches you how to build beautiful web apps with Streamlit in 3
    simple lessons. This guide is:
    
    - <span style="color: {ui.color('violet-80')}">**interactive:** you will code directly in here, no installation required</span>
    - <span style="color: {ui.color('blue-80')}">**project-based:** in each lesson, we will build one full Streamlit app</span>
    - <span style="color: {ui.color('green-90')}">**for newcomers:** no Python or coding knowledge required</span>
    - <span style="color: {ui.color('red-90')}">**built with Streamlit:** because what else? 😉</span>
    
    """,
    unsafe_allow_html=True,
)


lesson_name = st.radio(
    "Jump to",
    ["Lesson 1", "Lesson 2", "Lesson 3", "Lesson 4"],
)

st.write(
    '<p align="right">Happy Streamliting!<br><i>Johannes (<a href="https://twitter.com/jrieke">@jrieke</a>)</i></p>',
    unsafe_allow_html=True,
)


def lesson1_step1():
    ui.colored_header("Lesson 1: Saying hello 👋", "violet-70")
    st.write(
        """
        We'll start with the most basic example in every coding tutorial: Printing out
        "Hello World!". First, we need to tell the computer that we want to use the Streamlit
        library.

        Type `import streamlit as st` in the box below, then click on the **APPLY** 
        button:
        """
    )
    text = execbox(autorun=True)
    return text == "import streamlit as st"


def lesson1_step2():

    st.write(
        """
        Great! Streamlit is ready to be used now. There's two parts to this command:

        - `import streamlit` makes the computer import the Streamlit library
        - `as st` tells the computer that from now on, we will not write `streamlit` anymore
        but just `st` (which save us a tiny bit of time 😉)

        Let's move on. To print out "Hello World!", just type `st.write("Hello World!")` in
        the box below (in a new line below the import statement):
        """
    )
    text = execbox("import streamlit as st", autorun=True)
    return text == 'import streamlit as st\nst.write("Hello World!")'


def lesson1_step3():
    st.write(
        """
        See this "Hello World" above? ☝️ That's the output of the `st.write`command!! 
        It works but doesn't look mindblowing yet, right? Let's make it a bit prettier.
        
        Replace `st.write` with `st.title` and turn `"Hello World!"` into
        `"Hello Streamlit! 🎈"` (you can copy/paste the balloon emoji into the editor if
        you don't know how to write it on your computer).
        """
    )
    text = execbox('import streamlit as st\nst.write("Hello World!")', autorun=True)
    return text == 'import streamlit as st\nst.title("Hello Streamlit! 🎈")'


def lesson1_step4():
    st.balloons()
    st.write(
        """
        Wuhuuu!!! Congrats on your first little Streamlit app! Fantastic job, you 
        are ready for lesson 2 – just select it at the top of the page.
        """
    )
    st.write("")
    # return st.button("Continue")


def lesson2_step1():
    ui.colored_header("Lesson 2: Animal pics 🐶", "blue-70")
    st.write(
        """
        In this lesson, we'll build a more advanced Streamlit app: It will show the user
        some pictures of their favorite animal. 
        
        Let's start with what you are already familiar with. In the box below, import 
        the Streamlit library (`import streamlit as st`) and give the app the title 
        `"Your favorite animal 🐶🐱🐥"`, using `st.title`.
        """
    )
    text = execbox(autorun=True)
    return text == 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")'


def lesson2_step2():
    st.write(
        """
        Nice! Good job on remembering lesson 1.
        
        Before showing the animal pics, let's be polite and ask the user for their name.
        For this, we'll use our first Streamlit **widget**. Widgets are interactive elements
        where the user can input some data. Streamlit has a bunch of built-in widgets 
        (e.g. for text, numbers, dates, checkboxes, file uploads, ...), and you can 
        even [build your own widgets](https://docs.streamlit.io/en/stable/streamlit_components.html)! 
        
        To get the user name, we will use a text input widget. Below the existing code, 
        write `st.text_input("What's your name?")`.
        """
    )
    text = execbox(
        'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")', autorun=True
    )
    return (
        text
        == 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nst.text_input("What\'s your name?", key="sd")'
    )


def lesson2_step3():
    st.write(
        """
        This looks good but nothing is happening yet, when you enter your name in the 
        text field. We need to do two things to change this:
        
        1. Get the user input from the text field. In the box below, change the last 
           line to `name = st.text_input("What\'s your name?")`. This will store the 
           user input in the **variable** `name`. 
        2. Greet the user. We will use the `st.write` command for this, which you 
           already know from lesson 1. Add it below the other code and pass the 
           following value to it, which we will explain in a second: `f"Hey {name}!"`
        """
    )
    text = execbox(
        'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nst.text_input("What\'s your name?")',
        autorun=True,
    )
    return (
        text
        == 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?")\nst.write(f"Hey {name}!")'
    )


def lesson2_step4():
    st.write(
        """
        Go try it out! Enter your name in the text field above and see what happens.
        """
    )
    text = execbox(
        'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?", key="sfjljlsd")\nst.write(f"Hey {name}!")',
        autorun=True,
    )
    return (
        text
        == 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nst.text_input("What\'s your name?", key="sd")'
    )


lessons = {
    "Lesson 1": [lesson1_step1, lesson1_step2, lesson1_step3, lesson1_step4],
    "Lesson 2": [lesson2_step1, lesson2_step2, lesson2_step3, lesson2_step4],
}

steps = lessons[lesson_name]
for i, step in enumerate(steps):
    if not step():
        break
    if i < len(steps) - 1:
        st.write("---")
