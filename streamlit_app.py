# Importing libraries
import streamlit as st
import streamlit.components.v1 as components
from model import *

st.set_page_config(layout="wide")
st.header("Sentiment Based Product Recommendation System")


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: lightsalmon;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>With ❤ by <a href="https://github.com/saurabhdugdhe">Saurabh Dugdhe</a></p>
</div>
"""

def color_survived(val):
    color = 'red' if val<=30 else 'orange' if (val>30 and val<60) else 'skyblue' if (val>60 and val<85) else 'lightgreen'
    return f'background-color: {color}'


menu = ["Home", "About"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    with st.form(key="form1"):
        userName = st.text_input("Enter a Username: (E.g. sandy, rebecca, mike, nicole, chris, tony, kimberly, alexis etc. )")
        submitButton = st.form_submit_button()
        
    if submitButton:
        items = GetSentimentRecommendations(userName.lower())
        if str(type(items))=="<class 'NoneType'>":
            st.text(f"User '{userName}' not found")
        else:
            st.subheader("Top 20 recommendations")
            #st.dataframe(items)
            st.table(items[['name', 'brand', 'positive_sentiment_percent']].style.applymap(color_survived, subset=['positive_sentiment_percent']))

if choice == "About":
    st.header("About")
    st.text("Saurabh Dugdhe - Senior Software Engineer")
    st.markdown("Github: [@saurabhdugdhe](https://github.com/saurabhdugdhe)")    


st.markdown(footer,unsafe_allow_html=True)
