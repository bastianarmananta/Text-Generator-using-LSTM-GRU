# Text Generator using LSTM-GRU and Bidirectional Architecture

This project is a resulting text generator that utilizes LSTM/GRU models to create new text based on the user's input. The accompanying web application provides a user-friendly interface for generating new text, allowing users to input a starting text and obtain a unique output.

## Installation

To install and run the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using pip. You can do this by running the following command in your terminal:
`pip install -r requirements.txt`
3. Run the web app using the following command: `streamlit run app.py`
4. Access the web app by opening your web browser and navigating to `http://localhost:8501`.

## Usage

To utilize the web application, input the desired text into the designated text box and proceed to click the "Generate Text" button. The pre-trained model employed by the application will subsequently generate new sentences based on the length of the input and its contextual meaning.

## Example

Here's an example of how to use the web app:

1. Open your web browser and navigate to `http://localhost:8501`.
2. Enter the text to inisiate "arduino uno" into the text box.
3. Specify the amount of text you want to generate
4. Click the "Generate Text" button.
5. The web app should display generated text.

## Issues

The outcome of this project is an adaptable web application that can generate text based on the quantity of data entered by the user. This application exclusively utilizes Indonesian data. Therefore, to maximize output quality, it is essential to provide the application with Indonesian text input.

## Acknowledgements

This project was built using scikit-learn and Streamlit framework.
