import streamlit as st

if 'points' not in st.session_state:
    st.session_state.points = 0
if 'generated' not in st.session_state:
    st.session_state.generated = False

def setGenerated():
    st.session_state.generated = True

def add_points():
    st.session_state.points = st.session_state.points + 1

st.header('Baro :blue[App] :sunglasses:')

st.text_input("Enter your goal prompt", value="I want to be able to run for Dhiraagu Full Marathon", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, disabled=True, label_visibility="visible")

if st.button("Generate Milestones", type="primary", on_click=setGenerated) or st.session_state.generated == True:
    st.markdown(":clock5: :orange[Daily] Run 5K everyday")
    st.markdown(":seedling: :violet[Milestone] Complete a 20K run")
    st.markdown(":trophy: :green[Final Milestone] Run for Dhiraagu Full Marathon")
    st.button(":+1: complete daily goal", type="secondary", on_click=add_points)


st.markdown(f":point_right: :blue[Daily] {st.session_state.points}",)

st.divider()

if (st.session_state.points > 5):
    st.markdown(":hot_pepper: :blue[Yayy you won a trip to Bali!! Sponsored by Dhiraagu]")

if (st.session_state.points > 10):
    st.markdown(":three_button_mouse: :blue[You won an award! Suppperrr Clicckerr!!]")
