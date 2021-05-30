import streamlit as st
from execbox import execbox

st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/balloon_1f388.png",
    width=100,
)
"""
# So you heard about Streamlit...

Hey! 👋 My name is Johannes. 
When you read this, someone probably told you about Streamlit and how great it is. 
But you may have no idea how Streamlit or coding in Python works. This guide is just for 
you. It teaches you how to build beautiful web apps with Streamlit in 3 simple lessons. 
This guide is:

- **interactive:** you will code directly in here, no installation required
- **project-based:** in each lesson, we will build one full Streamlit app
- **built with Streamlit 😉**
"""

st.write("")

"""
## Lesson 1: Saying hello 👋

We'll start with the most basic example in every coding tutorial: Printing out 
"Hello World!". First, we need to tell the computer that we want to use the Streamlit 
library. 

Type `import streamlit as st` in the box below, then hit **CMD** + **ENTER** on 
your keyboard:

"""

text = execbox(autorun=True)

if text == "import streamlit as st":
    """
    Great! There's two parts to this command:

    - `import streamlit` makes the computer import the Streamlit library
    - `as st` tells the computer that from now on, we will not write `streamlit` anymore
      but just `st` (which save us a tiny bit of time 😉)

    Let's move on. To print out "Hello World!", just type `st.write("Hello World!")` in
    the box below (in a new line below the import statement):
    """

    text = execbox("import streamlit as st", autorun=True)

    if text == 'import streamlit as st\nst.write("Hello World!")':
        """
        Cool but doesn't look mindblowing yet, right? Let's make it a bit prettier.
        Replace `st.write` with `st.title` and turn `"Hello World!"` into
        `"Hello Streamlit! 🎈"` (you can copy/paste the balloon emoji into the editor if
        you don't know how to write it on your computer).
        """

        text = execbox('import streamlit as st\nst.write("Hello World!")', autorun=True)

        if text == 'import streamlit as st\nst.title("Hello Streamlit! 🎈")':
            st.balloons()
            """
            ---

            Wuhuuu!!! Congrats on your first little Streamlit app! Fantastic job, you 
            are ready to move on to lesson 2.
            """
