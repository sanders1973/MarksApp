import streamlit as st
from streamlit_local_storage import get_local_storage, set_local_storage

def main():
    st.title("Text Boxes with Local Storage")

    # Retrieve stored values
    text1 = get_local_storage("text1", "")
    text2 = get_local_storage("text2", "")
    text3 = get_local_storage("text3", "")
    text4 = get_local_storage("text4", "")

    col1, col2 = st.columns(2)

    with col1:
        text1 = st.text_input("Text Box 1", text1)
        text3 = st.text_input("Text Box 3", text3)

    with col2:
        text2 = st.text_input("Text Box 2", text2)
        text4 = st.text_input("Text Box 4", text4)

    if st.button("Save"):
        set_local_storage("text1", text1)
        set_local_storage("text2", text2)
        set_local_storage("text3", text3)
        set_local_storage("text4", text4)
        st.success("Text saved successfully!")

if __name__ == "__main__":
    main()
