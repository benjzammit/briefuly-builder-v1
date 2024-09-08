import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Briefly - Transform Your Briefs, Transform Your Results",
        page_icon=":bulb:",
        layout="wide",
    )

def add_footer():
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f8f9fa;
                color: #616161;
                text-align: center;
                padding: 10px 0;
                font-size: 14px;
            }
            .footer a {
                color: #2962FF;
                text-decoration: none;
            }
            .footer a:hover {
                text-decoration: underline;
            }
            .footer-icon {
                vertical-align: middle;
                margin-right: 5px;
            }
        </style>
        <div class="footer">
            Built by Benjamin Zammit - Strategy and Implementation Manager at InDomo, a WPP Company.
            <br>
            <a href="https://www.linkedin.com/in/benjamin-zammit/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" class="footer-icon" width="16" height="16">
                Connect with me on LinkedIn
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def apply_custom_styles():
    st.markdown(
        """
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f8f9fa;
            }

            .title {
                text-align: center;
                font-size: 48px;
                font-weight: bold;
                color: #ffffff;
                margin-bottom: 10px;
            }

            .subtitle {
                font-size: 28px;
                color: #ffffff;
                margin-bottom: 30px;
                background-color: rgba(218, 112, 214, 0.85);
                padding: 4px 8px;
                border-radius: 4px;
                display: inline;
                text-align: center;
            }

            .background-container {
                position: relative;
                width: 100%;
                height: auto;
                background-image: url('https://www.wpp.com/en/-/media/project/wpp/images/wpp-iq/2023/creativepowerhousemain.jpg');
                background-size: cover;
                background-position: center;
                padding: 60px 20px;
                box-sizing: border-box;
            }

            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.1);
                z-index: 1;
            }

            .content {
                position: relative;
                z-index: 2;
                text-align: center; 
            }

            .section-title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #800080;
                margin-top: 40px;
                margin-bottom: 20px;
            }

            .section-description {
                text-align: center;
                font-size: 18px;
                color: #616161;
                line-height: 1.6;
                margin-bottom: 40px;
            }

            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f8f9fa;
                color: #616161;
                text-align: center;
                padding: 10px 0;
                font-size: 14px;
            }
            .footer a {
                color: #2962FF;
                text-decoration: none;
            }
            .footer a:hover {
                text-decoration: underline;
            }
            .footer-icon {
                vertical-align: middle;
                margin-right: 5px;
            }

            .benefit-card-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
                gap: 20px; 
            }

            .benefit-card {
                background-color: #fff;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
                text-align: left; 
                display: flex; 
                flex-direction: column; 
            }

            .benefit-card .benefit-description {
                flex-grow: 1; 
            }

            .benefit-container { 
                display: flex;
                align-items: center; 
                margin-bottom: 15px; 
            }

            .benefit-icon {
                font-size: 28px; 
                margin-right: 10px; 
            }

            .benefit-title {
                color: #800080;
                font-size: 24px;
                margin-bottom: 0; 
            }

            .benefit-description {
                color: #616161;
                font-size: 16px;
                line-height: 1.5;
            }
            .error-text {
                color: red;
                font-weight: bold;
            }

            button[data-baseweb="tab"] {
                font-size: 18px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
