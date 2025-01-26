import streamlit as st
from streamlit import session_state as ss

def draw_sidebar():
    # Apply custom CSS for aligning the bottom section
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                display: flex;
                flex-direction: column;
                height: 100vh;
                justify-content: space-between;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        # Top section with main logo
        st.image("img/Composer_Studio.png", use_container_width=True)
        st.markdown("---")  # Horizontal line for separation

        if 'page' not in ss:
            ss.page = 'Crews'

        # Navigation section
        pages_with_icons = {
            'Crews': '👥 Troupes',
            'Agents': '🤖 Agents',
            'Tasks': '📋 Tasks',
            'Tools': '🛠️ Tools',
            'Kickoff!': '🚀 Kickoff!',
            'Import/export': '📂 Import/Export'
        }
        selected_page = st.radio(
            'Navigate', 
            list(pages_with_icons.keys()), 
            index=list(pages_with_icons.keys()).index(ss.page),
            format_func=lambda x: pages_with_icons[x], 
            label_visibility="collapsed"
        )
        if selected_page != ss.page:
            ss.page = selected_page
            st.rerun()

        # Bottom section with secondary logo
        st.markdown("---")  # Horizontal line for separation
        try:
            st.image("img/RHCAI_Logo_Dark.png", use_container_width=True)
        except FileNotFoundError:
            st.error("Image not found: img/RHCAI_Logo_Dark.png")
