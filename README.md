# README Generator

Description:
------------

The ReadMe Generator is a project that uses Streamlit and the LLaMA model to generate a README file for a given project. It allows users to input project details, upload files, and generate a README file with a preview option.

Features:
--------

* Generate a README file for a given project
* Input project details and upload files
* Toggle between Markdown and Code views
* Support for multiple file uploads


Installation Instructions:
-------------------------

1. Install the required dependencies:
	* Streamlit
	* Groq
	* dotenv
2. Clone the repository and navigate to the project directory
3. Run the application using `streamlit run app.py`


Usage Instructions:
-----------------

1. Open the application in your web browser
2. Input project details and upload files as desired
3. Click the "Generate" button to generate the README file
4. Toggle between Markdown and Code views using the preview button

Code Structure:
--------------

The project consists of the following files and directories:

* `app.py`: The main application file that sets up the Streamlit app and calls the `mainView` function
* `readme.py`: The file that contains the UI for the app
* `extractMarkdown.py`: The file that extracts code blocks from the generated Markdown content
* `readme_gen.py`: The file that contains the LLaMA model and generates the README file

Future Enhancements:
-------------------

* Improve the user interface and user experience
* Add more features to the README generator

Credits/References:
-------------------

* Streamlit: A popular Python library for building web applications
* LLaMA model: A large language model developed by Meta AI
* Groq: A Python library for interacting with the LLaMA model
* dotenv: A Python library for loading environment variables from a `.env` file
