import streamlit as st
from streamlit_local_storage import LocalStorage
localS = LocalStorage()

def main():
    st.title("Text Boxes with Local Storage")

    # Retrieve stored values
    
    text1 = localS.getItem("text1")
    text2 = localS.getItem("text2")
    text3 = localS.getItem("text3")
    text4 = localS.getItem("text4")

    col1, col2 = st.columns(2)

    with col1:
        text1 = st.text_area("Text Box 1", text1,height=300)
        text3 = st.text_input("Text Box 3", text3)

    with col2:
        text2 = st.text_input("Text Box 2", text2)
        text4 = st.text_input("Text Box 4", text4)

    if st.button("Save"):
        localS.setItem("text1", text1)
        localS.setItem("text2", text2)
        localS.setItem("text3", text3)
        localS.setItem("text4", text4)
        st.success("Text saved successfully!")

if __name__ == "__main__":
    main()
