# LIBs
import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Summarization Function
def text_summerizer(text, summerizer="LSA", sentences_num=5):
    """
    Summarizes a given text using one of the available summarization algorithms.

    This function takes a text input, processes it into a format that can be understood by the 
    summarizer, and then returns a summary with the specified number of sentences. The 
    summarizer algorithm is chosen based on the user's selection.
    
    """
    parser = PlaintextParser(text, Tokenizer("english"))

    # Sumerizer Type
    if summerizer == "LSA":
        summerizer = LsaSummarizer()
    elif summerizer == "Luhn":
        summerizer = LuhnSummarizer()
    elif summerizer == "LexRank":
        summerizer = LexRankSummarizer()
    else :
        summerizer = TextRankSummarizer()

    summery = summerizer(parser.document, sentences_num)

    return " ".join(str(sentence) for sentence in summery)
    

# Streamlit UI
# About the App
st.sidebar.title("About This App")
st.sidebar.markdown("""
    ## Text Summarization Application

    This app allows you to input a text and summarize it using one of the following algorithms:
    - **LSA (Latent Semantic Analysis)**
    - **Luhn's Algorithm**
    - **LexRank**
    - **TextRank**

    Simply enter the text, select your preferred summarizer, and specify the number of sentences you want in the summary. The app will process the input and provide you with a concise summary.

    ### How it works:
    1. **LSA** analyzes the semantic structure of the text and selects sentences that capture the most important concepts.
    2. **Luhn** focuses on sentence relevance by selecting sentences with the most important terms.
    3. **LexRank** is a graph-based algorithm that ranks sentences based on their similarity to each other.
    4. **TextRank** uses a similar graph-based method, inspired by Google's PageRank, to rank sentences based on their importance.
                    
    #### How to Use:
    1. Enter your text in the main area.
    2. Choose your preferred summarization algorithm from the dropdown.
    3. Adjust the number of sentences for the summary.
    4. Press the **Summarize** button to get the summarized text.

    Enjoy summarizing your texts!
""")

# Title
st.title("📝Text Summarization Application")
st.markdown("""
    This app allows you to input a text and summarize it. 
    You can choose from various summarization algorithms and specify the number of sentences in the summary.
""")

# User Input
user_text = st.text_area("Please enter your text ...")

# Summerizer Type
summerizer_type = st.selectbox("Please choose the type of summarizer you would like to use :",("LSA", "Lunh", "LexRank", "TextRank"))

# Number of Summarized Sentences
sentences_count = st.slider("How many sentences would you like in the summary?", 1, 10, 5)

# Call to Action
if st.button("Summarize..."):
    if user_text.strip():
        summery = text_summerizer(user_text, summerizer_type, sentences_count)
        st.subheader("Summerized Text: ")
        st.write("- " + summery.replace('.', '.\n-'))

    else:
        st.error("Please enter some text before attempting to summarize.")




