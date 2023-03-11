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
#     output = """ # Feedback As with all of my projects,
#     feedback (even if it is just something small like telling me your use case for my project, or telling me that you didn't like the README's structure, or telling me that you specifically liked one specific feature) is much appreciated, and helps me make this project better, even if it's something very tiny! You can just drop an issue with your feedback, short and non-formal, or even email me if you don't want to raise an issue for some reason. I do not plan on adding features in the future at the moment, but I am always open to fixing and tweaking existing features, documentation et cetera, and I would obviously love to hear your feature suggestions even if I do not plan on adding them in the near future.

# Me supporting you & You supporting me
# I am generally very responsive when it comes to GitHub issues, and I take them very serious and try to solve them ASAP. If you run into bugs, weird behaviors, installation errors and the like whilst using my tool, don't hesitate to tell me in an issue, so I can fix the problem!

# If you found this tool useful, please consider starring it on GitHub to show me your appreciation! I would also appreciate if you told me about issues you encountered even if you managed to fix them in your own copy of the code, so I can fix them in this repo, too."""
    
    if st.button("Clone"):

        with st.spinner('Generating Documentation.....'):
            output = buildDoc(url)
            st.title(url.split('/')[-1])
            st.markdown(output)
            
           
    # html_as_a_string = gh_md_to_html.core_converter.markdown(output)
    # st.subheader(output)

if __name__ == '__main__':
    main()

