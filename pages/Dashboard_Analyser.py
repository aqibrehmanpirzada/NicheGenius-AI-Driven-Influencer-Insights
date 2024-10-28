import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd
import tempfile
import os
from dotenv import load_dotenv
load_dotenv()

# Function to read and combine text from all pages in a PDF
def read_pdf(uploaded_file):
    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Initialize PyPDFLoader with the temporary file path
    loader = PyPDFLoader(temp_file_path)

    # Load PDF and combine text from all pages
    docs = loader.load()
    combined_text = ""
    for doc in docs:
        combined_text += doc.page_content + "\n"

    # Delete the temporary file
    temp_file.close()
    return combined_text

# Streamlit app title and instructions
st.markdown(
        """
        <style>
        /* Sidebar styles */
        div[data-testid="stSidebar"] {
            background-color: #007BFF;  /* Blue background color */
            color: #ffffff;  /* White text color */
        }
        div[data-testid="stSidebar"] a {
            color: #ffffff;  /* White links */
        }
        div[data-testid="stSidebar"] .stButton > button {
            color: #ffffff;
            background-color: #0056b3;  /* Darker blue for buttons */
        }

        /* Main title styling */
        .title {
            font-size: 3em;
            text-align: center;
            padding-bottom: 20px;
            animation: glow 2s linear infinite alternate;
            text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
        }

        /* Animation for glowing effect */
        @keyframes glow {
            from {
                text-shadow: 0 0 10px #007BFF, 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3;
            }
            to {
                text-shadow: 0 0 20px #007BFF, 0 0 30px #007BFF, 0 0 40px #0056b3, 0 0 70px #0056b3, 0 0 80px #0056b3, 0 0 100px #0056b3, 0 0 150px #0056b3, 0 0 200px #0056b3, 0 0 300px #0056b3;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown("<h1 class='title'> PDF Business Document Analyzer</h1>", unsafe_allow_html=True)
st.write("Upload a Business Document to get recommended Influencers")

# File upload widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Process the uploaded PDF file
    pdf_text = read_pdf(uploaded_file)

    # Initialize OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    openai_api_key = api_key
    llm = ChatOpenAI(model="gpt-4o", openai_api_key=openai_api_key)

    # Define template for OpenAI prompt
    template = """
    Analyse the document and provide 10 recommended ecommerce influencers related to the business in the document, and also provide information on which platforms we can approach them.
    {doc_text}
    """
    prompt = PromptTemplate(template=template, input_variables=["doc_text"])
    llmchain = LLMChain(llm=llm, prompt=prompt)

    # Invoke OpenAI model with PDF text
    response = llmchain.invoke({"doc_text": pdf_text})
    data = response["text"]

    # Option 1: Display the output as plain text
    st.subheader("The Recommended Influencers Related to Your Business Are:")
    st.write(data)

    # Option 2: Try to format the data into a table (if the data follows a structured format)
    try:
        influencers = data.split("\n")  # Split the text by line breaks

        # Create a list to store influencer data
        influencer_list = []

        # Iterate over each influencer detail and extract information
        for influencer in influencers:
            # Example of expected format: "Influencer 1: Name - Platform - Contact Info"
            details = influencer.split(" - ")
            if len(details) == 3:
                influencer_dict = {
                    "name": details[0],
                    "platform": details[1],
                    "contact_info": details[2]
                }
                influencer_list.append(influencer_dict)

        # Convert to a DataFrame for tabular display
        # df = pd.DataFrame(influencer_list)

        # # Display DataFrame
        # st.subheader("Formatted Influencer Information:")
        # st.write(df)

    except Exception as e:
        st.error(f"Failed to format data into a table: {e}")
        st.write("Displaying the raw response instead:")
        st.code(data)
