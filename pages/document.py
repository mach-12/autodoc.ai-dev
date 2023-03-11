import streamlit as st
import streamlit.components.v1 as components

# import gh_md_to_html
from backend.prompts import buildDoc 

def main():
    st.set_page_config(
        page_title="AUTODOC.AI"
    )

    # Define title and image
    title = "Autodoc.ai"
    logo = "img/autodoc.png"

    # Create a grid to display title and image side by side
    col1, col2 = st.columns([2, 5])
    with col1:
        st.image(logo, width=100)

    with col2:
        st.header(title)

    st.markdown('___')

    # Add input field and button
    url = st.text_input("Input Github URL")
    
    if st.button("Clone"):

        with st.spinner('Generating Documentation.....'):
            output = buildDoc(url)
            st.title(url.split('/')[-1])
            st.markdown(output)
            
           
    # html_as_a_string = gh_md_to_html.core_converter.markdown(output)
    # st.subheader(output)

if __name__ == '__main__':
    main()

