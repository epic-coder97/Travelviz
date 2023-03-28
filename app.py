import streamlit as st
import openai
import datetime

# Set up OpenAI API credentials
#openai.api_key = "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"
openai.api_key = st.secrets["api_key"]
# Define a function to generate an itinerary for a given day
def generate_itinerary(start_loc, end_loc, days):
    # Use GPT-3 API to generate itinerary
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt = f"Generate an itinerary for a trip starting at {start_loc} and exploring {end_loc}. The itinerary should include {days} days and cover the following details: recommended activities, places to eat, accommodation options, transportation options, and any other relevant information to ensure a memorable trip.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract generated text from API response
    itinerary = response.choices[0].text.strip().split("\n")

    return itinerary

def clean_itinerary(itinerary):
    new_itinerary = []
    day_num = 1
    for i, item in enumerate(itinerary):
        if item.startswith("Day"):
            new_itinerary.append(item)
            day_num += 1
        elif item.startswith("• "):
            new_itinerary.append(f"{day_num - 1}. {item}")
        else:
            new_itinerary.append(item)
    return new_itinerary

# Define Streamlit app
def app():
    st.set_page_config(page_title="Itinerary Generator", page_icon=":airplane:", layout="wide")
    st.title("TripWiz - Itinerary Generator")
    st.markdown("---")
    st.sidebar.title("Options")
    start_loc = st.sidebar.text_input("Start Location")
    end_loc = st.sidebar.text_input("End Location")
    days = st.sidebar.number_input("Number of days", min_value=1, max_value=30, value=1)
    if st.sidebar.button("Generate Itinerary"):
        with st.spinner("Generating itinerary..."):
            itinerary = generate_itinerary(start_loc, end_loc, days)
            clean_itinerary1 = clean_itinerary(itinerary)
            today = datetime.date.today()
            for item in clean_itinerary1:
                if item.startswith("Day"):
                    st.markdown(f"## {item} ({today})")

                else:
                    st.markdown(f"{item}")
                
            st.markdown("---")

if __name__ == "__main__":
    app()
