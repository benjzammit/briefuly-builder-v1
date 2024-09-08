import streamlit as st
import pandas as pd
import docx
import io
import asyncio
import ui_config

from text_extraction import extract_text_from_docx, extract_text_from_pdf
from sentiment_analysis import analyze_sentiment, interpret_sentiment
from ai_analysis import analyze_text_async, improve_section
from utils import parse_and_improve
from ui_config import add_footer

# --- UI Configuration ---
ui_config.set_page_config()
ui_config.apply_custom_styles()

# --- Main App ---
st.markdown(
    """
    <div class="background-container">
        <div class="overlay"></div>
        <div class="content">
            <h1 class="title">💡 Briefly.</h1>
            <p class="subtitle">&nbsp&nbspTransform Your Briefs, Transform Your Results.&nbsp&nbsp</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- File Upload ---
uploaded_file = st.file_uploader(
    "Upload Your Marketing Brief (DOCX or PDF)", type=["docx", "pdf"], accept_multiple_files=False
)

# --- Process Uploaded File ---
if uploaded_file is not None:
    try:
        file_bytes = uploaded_file.read()

        if uploaded_file.name.endswith(".docx"):
            document_text = extract_text_from_docx(file_bytes)
        elif uploaded_file.name.endswith(".pdf"):
            document_text = extract_text_from_pdf(file_bytes)
        else:
            st.error("Unsupported file type. Please upload a DOCX or PDF file.")
            st.stop()

        if document_text is None:
            st.error("Failed to extract text from the uploaded file. Please try again with a different file.")
            st.stop()

        # --- Analyze the Text ---
        with st.spinner("Analyzing your brief..."):
            df_results, overall_score, gap_analysis_results, competitors_mentioned = asyncio.run(analyze_text_async(document_text))

        # Store analysis results in session state
        st.session_state['df_results'] = df_results
        st.session_state['document_text'] = document_text

        # --- Interactive Improvement Sections ---
        st.header("Improve Your Marketing Brief")

        for section in df_results.index:
            original_text = document_text  # Extract relevant section text here
            st.subheader(section)
            st.text_area(f"Current {section}", value=original_text, key=f"current_{section}")

            user_input = st.text_area(f"Your Improved {section}", key=f"user_{section}")
            if st.button(f"Submit {section}"):
                improved_text = improve_section(original_text, user_input, section)
                st.write(improved_text)
                st.session_state[f"improved_{section}"] = improved_text

        # --- Compile Final Brief ---
        if st.button("Generate Final Brief"):
            final_brief = "\n\n".join([st.session_state.get(f"improved_{section}", "") for section in df_results.index])
            doc = docx.Document()
            doc.add_paragraph(final_brief)
            doc_bytes = io.BytesIO()
            doc.save(doc_bytes)
            doc_bytes.seek(0)

            st.download_button(
                label="Download Improved Brief (DOCX)",
                data=doc_bytes,
                file_name="improved_brief.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

    except Exception as e:
        st.error(f"An error occurred: {e}")

add_footer()