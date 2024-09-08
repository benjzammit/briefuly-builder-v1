import google.generativeai as genai
import json
from json_repair import repair_json
import pandas as pd
import asyncio
import streamlit as st
from utils import clean_response

# --- Load API Key from Secrets ---
api_key = st.secrets["api_keys"]["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

def generate_prompt(text):
    return f"""
    ## Marketing Brief Analysis Request

    Please analyze the following marketing brief and provide a structured response suitable for Python processing, with scores as numbers out of 100. 
    Extract specific details and insights where possible.

    **Marketing Brief Text:**

    ```
    {text}
    ```

    **Response Format:**

    ```json
    {{
      "overall_score": {{score}},
      "breakdown": {{
        "clarity_of_objectives": {{
          "score": {{score}},
          "feedback": "{{feedback}}",
          "extracted_objectives": ["list of extracted objectives from the text"], 
          "keywords": ["list of relevant keywords"]
        }},
        "strategic_alignment": {{
          "score": {{score}},
          "feedback": "{{feedback}}",
          "alignment_issues": ["list of potential misalignments with business goals (if any)"]
        }},
        "target_audience_definition": {{
          "score": {{score}},
          "feedback": "{{feedback}}",
          "extracted_demographics": ["age", "location", "interests", "other relevant demographics"],
          "target_audience_examples": ["specific examples of the target audience mentioned in the text"]
        }},
        "competitive_analysis": {{
          "score": {{score}},
          "feedback": "{{feedback}}",
          "competitors_mentioned": ["list of competitor brands mentioned"],
          "competitive_advantages": ["list of mentioned or implied competitive advantages"]
        }},
        "channel_strategy": {{
          "score": {{score}},
          "feedback": "{{feedback}}",
          "recommended_channels": ["list of potentially effective channels based on the brief"],
          "channel_justifications": ["reasons for recommending each channel"]
        }},
        "key_performance_indicators": {{
          "score": {{score}},
          "feedback": "{{feedback}}",
          "extracted_kpis": ["list of KPIs mentioned in the brief"],
          "kpi_suggestions": ["suggestions for additional relevant KPIs"]
        }}
      }},
      "gap_analysis": [
            "List of missing elements (if any)",
            "Another missing element"
        ]
    }}
    """

async def analyze_text_async(text):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, analyze_text, text)
    return result

def analyze_text(text):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = generate_prompt(text)

    try:
        response = model.generate_content(prompt)
        response_text = response.text

        # --- Clean up the response ---
        response_text = clean_response(response_text)

        # --- Repair potentially malformed JSON ---
        try:
            response_text = repair_json(response_text)
        except Exception as e:
            print(f"Warning: json_repair could not fix the JSON: {e}")

        # Directly try to parse as JSON
        response_data = json.loads(response_text)

        # Extract data for DataFrame (corrected structure)
        data = {}

        for category, details in response_data['breakdown'].items():
            category_title = category.replace('_', ' ').title()
            
            # Store all details for the category in a dictionary
            data[category_title] = {
                'Score': int(details['score']),
                'Feedback': details['feedback'],
                'Extracted Objectives': details.get('extracted_objectives', []),
                'Keywords': details.get('keywords', []),
                'Alignment Issues': details.get('alignment_issues', []),
                'Extracted Demographics': details.get('extracted_demographics', []),
                'Target Audience Examples': details.get('target_audience_examples', []),
                'Competitors Mentioned': details.get('competitors_mentioned', []),
                'Competitive Advantages': details.get('competitive_advantages', []),
                'Recommended Channels': details.get('recommended_channels', []),
                'Channel Justifications': details.get('channel_justifications', []),
                'Extracted KPIs': details.get('extracted_kpis', []),
                'KPI Suggestions': details.get('kpi_suggestions', []),
                'Target Locations': details.get('target_locations', [])
            } 

        df_results = pd.DataFrame.from_dict(data, orient='index')
        overall_score = int(response_data['overall_score'])

        # Extract gap analysis results
        gap_analysis_results = response_data.get('gap_analysis', [])

        # Extract competitors mentioned
        competitors_mentioned = data['Competitive Analysis']['Competitors Mentioned']

        return df_results, overall_score, gap_analysis_results, competitors_mentioned 
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Raw response: {response.text}")
        return None, None, None, []

def improve_section(original_text, user_input, section):
    """Generates an improved section using Google Gemini."""
    prompt = f"""
    ## Improve {section.title()}

    Original Text:
    ```
    {original_text}
    ```

    User Suggestions:
    ```
    {user_input}
    ```

    Please provide an enhanced version incorporating both the original and user suggestions.
    """
    
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text
