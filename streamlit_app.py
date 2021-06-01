import functools
import streamlit as st
from execbox import execbox

import ui

st.set_page_config(
    page_title="So you heard about Streamlit...", page_icon="🎈", layout="wide"
)

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

# TODO: Make this look like layout="centered".
_, center, _ = st.beta_columns([0.22, 0.56, 0.22])
with center:
    st.image(
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/balloon_1f388.png",
        width=100,
    )
    st.write(
        f"""
        # So you heard about Streamlit...

        Hey! 👋 
        When you read this, someone probably told you about [Streamlit](https://streamlit.io/) 
        and how great it is. But you may have no idea how Streamlit works or how to code 
        in Python. This guide is just for you. It teaches you how to build beautiful web 
        apps with Streamlit in 3 simple lessons. This guide is:
        
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
    ui.space(2)


def lesson1_step1(my_exercise_box):
    st.write(
        """
        We'll start with the most basic example in every coding tutorial: Printing out
        "Hello World!". First, we need to tell the computer that we want to use the Streamlit
        library.

        Type `import streamlit as st` in the box below (the command is evaluated while 
        you type, so don't worry if errors pop up while typing):
        """
    )
    given = ""
    expected = "import streamlit as st"
    my_exercise_box(given, expected)
    st.write(
        """
        Great! Streamlit is ready to be used now. There's two parts to this command:

        - `import streamlit` makes the computer import the Streamlit library
        - `as st` tells the computer that from now on, we will not write `streamlit` anymore
        but just `st` (which save us a tiny bit of time 😉)
        """
    )


def lesson1_step2(my_exercise_box):
    st.write(
        """
        Let's move on. To print out "Hello World!", just type `st.write("Hello World!")` in
        the box below (in a new line below the import statement):
        """
    )
    given = "import streamlit as st"
    expected = 'import streamlit as st\nst.write("Hello World!")'
    my_exercise_box(given, expected)
    st.write(
        """
        See this "Hello World!" on the right side? 👉 That's the output of the `st.write`command!! 
        """
    )


def lesson1_step3(my_exercise_box):
    st.write(
        """
        It works but doesn't look very impressive yet, right? Let's make it a bit prettier.
        
        Replace `st.write` with `st.title` and turn `"Hello World!"` into
        `"Hello Streamlit! 🎈"` (you can copy/paste the balloon emoji into the editor if
        you don't know how to write it on your computer).
        """
    )
    given = 'import streamlit as st\nst.write("Hello World!")'
    expected = 'import streamlit as st\nst.title("Hello Streamlit! 🎈")'
    my_exercise_box(given, expected)
    st.write(
        """
        Way better! 😍
        """
    )


def lesson1_step4(my_exercise_box):
    st.write(
        """
        Almost there! Let's add a short description below the title to finish up.
        
        Use the `st.write` command again and pass in the text `"This is my very first app."`
        (again, in a new line below your existing code).
        """
    )
    given = 'import streamlit as st\nst.title("Hello Streamlit! 🎈")'
    expected = 'import streamlit as st\nst.title("Hello Streamlit! 🎈")\nst.write("This is my very first app.")'
    my_exercise_box(given, expected)
    st.balloons()
    st.write(
        """
        Wuhuuu!!! Congrats on your first little Streamlit app! Fantastic job, 
        you are ready for lesson 2 (cute animals are waiting there 🤗🐶). 
        Just select it at the top of the page.
        """
    )


def lesson2_step1(my_exercise_box):
    st.write(
        """
        In this lesson, we'll build a more advanced Streamlit app: It will show the user
        some pictures of their favorite animal. 
        
        Let's start with what you are already familiar with. In the box below, import 
        the Streamlit library (`import streamlit as st`) and give the app the title 
        `"Your favorite animal 🐶🐱🐥"`, using `st.title`.
        """
    )
    given = ""
    expected = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")'
    my_exercise_box(given, expected)
    st.write("Nice! Good job on remembering lesson 1.")


def lesson2_step2(my_exercise_box):
    st.write(
        """
        Before showing the animal pics, let's be polite and ask the user for their name.
        For this, we'll use our first Streamlit **widget**. Widgets are interactive elements
        where the user can input some data. Streamlit has a bunch of built-in widgets 
        (e.g. for text, numbers, dates, checkboxes, file uploads, ...), and you can 
        even [build your own widgets](https://docs.streamlit.io/en/stable/streamlit_components.html)! 
        
        To get the user name, we will use a text input widget. Below the existing code, 
        write `st.text_input("What's your name?")`.
        """
    )
    given = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")'
    expected = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nst.text_input("What\'s your name?")'
    my_exercise_box(given, expected)
    st.write(
        "Looks good! Unfortunately, nothing happens when you enter your name in the gray text field 😔"
    )


def lesson2_step3(my_exercise_box):
    st.write(
        """
        We need to do two things to change this:
        
        1. Get the user input from the text field. In the box below, change the last 
        line to `name = st.text_input("What\'s your name?")`. This will store the 
        user input in the **variable** `name`. 
        2. Greet the user. We will use the `st.write` command for this, which you 
        already know from lesson 1. Add it below the other code and pass the 
        following value to it, which we will explain in a second: `f"Hey {name}!"`
        """
    )
    given = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nst.text_input("What\'s your name?")'
    expected = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?")\nst.write(f"Hey {name}!")'
    my_exercise_box(given, expected)
    st.write(
        "Go try it out! Enter your name in the text field on the right, press Enter, and see what happens..."
    )
    # TODO: Explain f-string.


def lesson2_step4(my_exercise_box):
    st.write(
        """
        Super cool, right? But there's one thing we can improve: When the user hasn't
        entered their name yet, the app still shows "Hey !" below the text field. Let's 
        remove this.
        
        We will use an **if clause** for this. In this case, we just want to check 
        if `name` contains a value and only show the greeting when it does. Luckily for 
        us, this is very easy in Python. Just replace the last line of your code by:

        ```
        if name:
            st.write(f"Hey {name}!")
        ```
        """
    )
    given = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?")\nst.write(f"Hey {name}!")'
    expected = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?")\nif name:\n    st.write(f"Hey {name}!")'
    my_exercise_box(given, expected)
    st.write(
        """
        Try it out again! Now the greeting will only appear after you entered your name.
        In general, all indented code below an `if` clause (as the `st.write` command in 
        this case) will only be executed when the `if` clause is true (more on this later!). 
        """
    )


def lesson2_step5(my_exercise_box):
    st.write(
        """
        Ok, time for animals! First, we want to ask the user what their favorite animal
        is. For this, we'll use yet another widget: A select box.
        
        Below your code, add `animal = st.selectbox("What's you favorite?", ["dog", "cat", "chick"])`.
        Make sure it is indented again, so it only shows up after the user entered their 
        name (and the `if` clause is true).
        """
    )
    given = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?")\nif name:\n    st.write(f"Hey {name}!")'
    expected = 'import streamlit as st\nst.title("Your favorite animal 🐶🐱🐥")\nname = st.text_input("What\'s your name?")\nif name:\n    st.write(f"Hey {name}!")\n    animal = st.selectbox("What\'s you favorite?", ["dog", "cat", "chick"])'
    my_exercise_box(given, expected)
    st.write(
        """
        
        """
    )


def exercise_box(body, expected_body, *args, **kwargs):
    """Shows an execbox which returns True when the user inputs the `expected_body`."""
    # TODO: Add some more magic to disregard blank lines etc.
    # TODO: Use button instead of checkbox.
    # TODO: Maybe add some delay after typing has finished before executing or at least
    #   showing error messages, so the user is not confused by error messages.
    solved = execbox(body, *args, **kwargs) == expected_body
    if not solved:
        skipped = st.checkbox("Skip", key="skip_" + body)
        if st.checkbox("Show solution"):
            st.code(expected_body)
        if not skipped:
            st.stop()


if lesson_name == "Lesson 1":
    ui.colored_header("Lesson 1: Saying hello 👋", "violet-70")
    steps = [lesson1_step1, lesson1_step2, lesson1_step3, lesson1_step4]
elif lesson_name == "Lesson 2":
    ui.colored_header("Lesson 2: Animal pics 🐶", "blue-70")
    steps = [lesson2_step1, lesson2_step2, lesson2_step3, lesson2_step4, lesson2_step5]

for i, step in enumerate(steps):
    col1, col2 = st.beta_columns(2)
    with col1:
        my_exercise_box = functools.partial(
            exercise_box, output_container=col2, autorun=True
        )
        step(my_exercise_box)
    if i < len(steps) - 1:
        st.write("---")
