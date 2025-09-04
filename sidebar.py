import random
import streamlit as st
from assets.prompts import lv1_instrucstion_prompting,lv1_zeroshot_cot
class draw_sidebar():
    def __init__(self):
        self.initialize_state()
        
    def initialize_state(self):
        if "level_1_upgrade_applied" not in st.session_state:
            st.session_state.level_1_upgrade_applied = None
        if "show_level_up_prompt" not in st.session_state:
            st.session_state.show_level_up_prompt = True
        
    def ui_sidebar(self):
        with st.sidebar:
            st.markdown("<h3 style='text-align: center;'>I'm here to help you</h3>", unsafe_allow_html=True)
    def logic_sidebar(self):
        with st.sidebar:
            st.write("Do you want to level up your prompting skill?")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Yes", key="yes_button"):
                    st.session_state.level_1_upgrade_applied = True
                    st.session_state.show_level_up_prompt = False
                    st.rerun()
            with col2:
                if st.button("No", key="no_button"):
                    st.session_state.level_1_upgrade_applied = False
                    st.session_state.show_level_up_prompt = False 
                    st.rerun()
                    
        return self
    def level_checking(self):
        if st.session_state.level_1_upgrade_applied is True:
            prompt_functions = [lv1_instrucstion_prompting, lv1_zeroshot_cot]
            random_function = random.choice(prompt_functions)
            with st.sidebar:
                st.write(random_function())
        elif st.session_state.level_1_upgrade_applied is False:
            with st.sidebar:
                st.write("That's fine, no pressure! 😉")  


    