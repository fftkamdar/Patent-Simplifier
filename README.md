# Patent-Simplifier

A web-based application that simplifies complex patent descriptions to make them easier to understand. It uses a simple text-processing approach to remove complex words and simplify sentences. This app is built using Flask, HTML, and CSS.

Features
Simplify Patent Descriptions: The app takes in a patent description and returns a simplified version.

User-friendly Interface: A clean and easy-to-use interface for inputting patent text.

Real-time Results: Displays simplified text instantly after the user submits the patent description.

Tech Stack
Frontend: HTML, Internal CSS

Backend: Flask (Python)

Libraries: None required (Flask is the main dependency)

Getting Started
Prerequisites
Make sure you have Python installed on your machine. You also need Flask to run the app. You can install Flask using the following command:

bash
Copy
Edit
pip install flask
Installation
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/patent-description-simplifier.git
cd patent-description-simplifier
Install the required dependencies (Flask):

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python app.py
Open the app in your browser:

cpp
Copy
Edit
http://127.0.0.1:5000
Usage
Enter a complex patent description into the text area.

Press the Simplify button to see the simplified version of the description.

The simplified patent description will appear below the input field.

Example Patent Description
"A system and method for optimizing the charging cycles of a lithium-ion battery pack by monitoring cell temperature and voltage, and dynamically adjusting the charge rate to extend battery life and improve efficiency. The system utilizes a microcontroller to interface with sensors, and software algorithms to predict optimal charging patterns based on usage data and environmental factors."

Simplified Version
"A system for optimizing battery charging by monitoring temperature and voltage. It adjusts the charge rate to improve battery life and efficiency using sensors and algorithms."

Contribution
Feel free to fork the repository, make improvements, or report issues. Pull requests are always welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
