import streamlit as st
import streamlit.components.v1 as components 

def main():
    st.set_page_config(
        page_title="AUTODOC.AI"
    )


    col1, col2 = st.columns([0.6, 1], gap='small')

    with col1:
        st.image('img/autodoc.png', width = 220)
    with col2:
        st.title("AUTODOC.AI")
        st.header("Automatic Code Documentation")

    st.markdown("---")

    col3, col4 = st.columns([1.3, 1], gap='large')

    with col3:    
        st.subheader('“Never depend on a single income. Make an investment to create a second source.”  -Warren Buffett')
        st.title('Want to invest in stocks?')
        st.write("""We often think of value investing as more art than science but some of its greatest practitioners display quant-like discipline. AI has much to offer this field for those who are open to the possibilities.""")

        st.markdown('')

        st.info("""
        ⚡TO IMPROVE ACCURACY
        """)
        st.markdown('')
        st.info("""
        ⚡TO SAVE TIME
        """)
        st.markdown('')
        st.info("""
        ⚡TO INCREASE EFFICIENCY
        """)
        


if __name__ == '__main__':
    main()

