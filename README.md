# Text Summarization Application
![summarization-featured](https://github.com/user-attachments/assets/3e2a7c8a-8083-443f-ac06-eab63fd92bad)

This application allows you to input a text and summarize it using one of the following algorithms:
- **LSA (Latent Semantic Analysis)**
- **Luhn's Algorithm**
- **LexRank**
- **TextRank**

## Features

- **Multiple Summarization Algorithms**: Choose from LSA, Luhn, LexRank, and TextRank.
- **Customizable Summary Length**: Specify the number of sentences you want in the summary.
- **User-Friendly Interface**: Built with Streamlit for an easy-to-use web interface.

## How to Use

1. **Enter your text** in the main area.
2. **Choose your preferred summarization algorithm** from the dropdown.
3. **Adjust the number of sentences** for the summary using the slider.
4. **Press the "Summarize" button** to get the summarized text.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd text_summarization
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

To run the application locally, use the following command:
```sh
streamlit run Text_Summarizetion_APP.py
```

Alternatively, you can access the deployed application on Streamlit Cloud using the following link:
[Deployed Text Summarization Application](https://textsummarizationapp1.streamlit.app/)
