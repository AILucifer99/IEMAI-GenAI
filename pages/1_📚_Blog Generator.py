import streamlit as st
import google.generativeai as genai  
import requests
import os
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from authorization import authorization
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_loading = "https://lottie.host/cc2b3b2d-5589-4c22-a42b-9c3d50fb8315/b8kIpS7sC0.json"
lottie_loading = load_lottieurl(lottie_url_loading)


st.set_page_config(
    page_title="AI Blog Generator",
    layout="wide", 
    page_icon="📚"
)

st.markdown(
    r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
            <style>
                .stButton button {
                    background-color: #000001;
                    color: white;
                }
            </style>
        """, 
unsafe_allow_html=True
)


gemini_safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=gemini_safety_settings,
)


st.title("Automatic SEO Optimized *Blog Generator* Engine ✨", )
st.subheader(
    "Just provide a *blog title*, along with important *keywords* and \
    let our AI Model generate a blog for the same.", 
    divider="rainbow"
)

st.sidebar.header("Configuration for the System", divider="rainbow")

blog_title = st.sidebar.text_area("Enter the Title of the Blog", "Creation of the universe and the galaxies.")
keywords = st.sidebar.text_area("Keywords (Comma-Seperated)", "Universe, Galaxies of the skies, Formation of the universe")
num_words = st.sidebar.slider("Number of tokens", min_value=200, max_value=1600, step=2)
tone_of_blog = st.sidebar.radio(
    "Style of Blog Generation", 
    options=["Professional", "Creative", "Friendly", "Informative", "Default"], 
    horizontal=True, 
)


if st.sidebar.button("✨ Generate ✨") :
    if not api_key:
        st.sidebar.error("Google API Key is not set. Please set it in the environment variables.")
    else:
        try :
            if tone_of_blog == "Professional" :
                generation_configuration = {
                    "temperature" : 0.65,
                    "top_p" : 1,
                    "max_output_tokens" : num_words, 
                    "top_k" : 40,
                }

                st.subheader("Generating The Blog With Tone :- *{}*, Please Wait.....".format(tone_of_blog))
                with st_lottie_spinner(lottie_loading, height=175, width=175, speed=0.75, quality="high") :
                    try:
                        prompt_instruction = [
                            f"Generate a comprehensive, engaging and {tone_of_blog} blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words." 
                        ]
                        response = model.generate_content(
                            prompt_instruction, 
                            generation_config=generation_configuration
                        )
                        st.success("Blog Generated Successfully.")
                        st.subheader("AI Response :-", divider="rainbow")
                        container = st.container(border=True, height=None)
                        container.write(response.text)
                        
                    except Exception as exp :
                        st.warning("Error Occured While Generation, please try later.")
                        st.write(exp)

            elif tone_of_blog == "Creative" :
                generation_configuration = {
                    "temperature" : 0.95,
                    "top_p" : 0,
                    "max_output_tokens" : num_words, 
                    "top_k" : 140,
                }
                st.subheader("Generating the blog with Tone :- *{}*, please wait.....".format(tone_of_blog))
                with st_lottie_spinner(lottie_loading, height=175, width=175, speed=0.75, quality="high") :
                    try:
                        prompt_instruction = [
                            f"Generate a comprehensive, engaging and {tone_of_blog} blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words." 
                        ]
                        response = model.generate_content(
                            prompt_instruction, 
                            generation_config=generation_configuration
                        )
                        st.success("Blog Generated Successfully.")
                        st.subheader("AI Response :-", divider="rainbow")
                        container = st.container(border=True, height=None)
                        container.write(response.text)

                    except Exception as exp :
                        st.warning("Error Occured While Generation, please try later.")
                        st.write(exp)

            elif tone_of_blog == "Friendly" :
                generation_configuration = {
                    "temperature" : 0,
                    "top_p" : 0.9,
                    "max_output_tokens" : num_words, 
                    "top_k" : 20,
                }
                st.subheader("Generating the blog with Tone :- *{}*, please wait.....".format(tone_of_blog))
                with st_lottie_spinner(lottie_loading, height=175, width=175, speed=0.75, quality="high") :
                    try:
                        prompt_instruction = [
                            f"Generate a comprehensive, engaging and {tone_of_blog} blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words." 
                        ]
                        response = model.generate_content(
                            prompt_instruction, 
                            generation_config=generation_configuration
                        )
                        st.success("Blog Generated Successfully.")
                        st.subheader("AI Response :-", divider="rainbow")
                        container = st.container(border=True, height=None)
                        container.write(response.text)

                    except Exception as exp :
                        st.warning("Error Occured While Generation, please try later.")
                        st.write(exp)

            elif tone_of_blog == "Informative" :
                generation_configuration = {
                    "temperature" : 0.75,
                    "top_p" : 0,
                    "max_output_tokens" : num_words, 
                    "top_k" : 10,
                }
                st.subheader("Generating the blog with Tone :- *{}*, please wait.....".format(tone_of_blog))
                with st_lottie_spinner(lottie_loading, height=175, width=175, speed=0.75, quality="high") :
                    try:
                        prompt_instruction = [
                            f"Generate a comprehensive, engaging and {tone_of_blog} blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words." 
                        ]
                        response = model.generate_content(
                            prompt_instruction, 
                            generation_config=generation_configuration
                        )
                        st.success("Blog Generated Successfully.")
                        st.subheader("AI Response :-", divider="rainbow")
                        container = st.container(border=True, height=None)
                        container.write(response.text)

                    except Exception as exp :
                        st.warning("Error Occured While Generation, please try later.")
                        st.write(exp)
            else :
                generation_configuration = {
                    "temperature" : 0.95,
                    "top_p" : 0,
                    "max_output_tokens" : num_words, 
                    "top_k" : 140,
                }
                st.subheader("Generating the blog with Tone :- *{}*, please wait.....".format(tone_of_blog))
                with st_lottie_spinner(lottie_loading, height=175, width=175, speed=0.75, quality="high") :
                    try:
                        prompt_instruction = [
                            f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words." 
                        ]
                        response = model.generate_content(
                            prompt_instruction, 
                            generation_config=generation_configuration
                        )
                        st.success("Blog Generated Successfully.")
                        st.subheader("AI Response :-", divider="rainbow")
                        container = st.container(border=True, height=None)
                        container.write(response.text)

                    except Exception as exp :
                        st.warning("Error Occured While Generation, please try later.")
                        st.write(exp)
        
        except Exception as exp :
            st.warning("Harmful Content Generation Detected, please try again...")

            
