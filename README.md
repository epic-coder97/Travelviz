# Travelviz


This is a simple Streamlit web application that generates a travel itinerary based on user inputs. The application takes in the start destination, end destination, and the number of days the user plans to travel. It then generates a detailed itinerary with recommended activities, dining options, and accommodation for each day.

Installation
To use this application, you must first clone this repository to your local machine. You can do this by running the following command in your terminal:



Once the repository is cloned, navigate to the project directory and create a virtual environment by running the following command:

```
{
python -m venv venv
}
```
Activate the virtual environment by running the following command:

bash
```
source venv/bin/activate
```
Install the required packages by running the following command:

```
pip install -r requirements.txt

```
Usage
To run the application, navigate to the project directory in your terminal and activate the virtual environment by running the following command:

bash
```

source venv/bin/activate

```
Then, run the following command to start the Streamlit server:

```streamlit run app.py ```
This should open a new tab in your web browser with the application running. Enter the required inputs and click on the "Generate Itinerary" button to generate your travel itinerary.

## Credits
This application was developed using the Streamlit framework and the OpenAI GPT-3 API for text generation.
