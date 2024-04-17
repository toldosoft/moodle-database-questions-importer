# py_moodle_questions_for_database

# Overview
This Python script processes educational questions stored in a text file and inserts them into a SQL Server database. The script is designed to parse questions, including their multiple-choice options and correct answers, and store them efficiently in the database. This is particularly useful for educational platforms or applications that need to manage large sets of exam or quiz questions.

# Features
    Text File Reading: Opens and reads contents of a text file containing quiz questions.
    Question Processing: Utilizes regular expressions to parse and extract individual questions, their multiple-choice options, and the correct answers.
    Database Interaction: Inserts parsed questions into a SQL Server database, managing both questions and their associated options.

# Requirements
    Python 3.x
    pyodbc library (for database connection)
    ODBC Driver 17 for SQL Server

# Setup
Install Python Dependencies:
Ensure Python 3.x is installed on your system. You can install the necessary Python libraries using pip:

bash:
pip install pyodbc

# Database Configuration:
You must have SQL Server installed and accessible. Update the connect_to_database function with the appropriate connection string parameters:

python_code:
'DRIVER={ODBC Driver 17 for SQL Server};SERVER=<your-server>;DATABASE=<your-database>;UID=<your-username>;PWD=<your-password>;'

# File Preparation:
Ensure your questions are formatted correctly in the text file. The expected format is:

example_moodle_questions_txt:
QuestionText: 
A) option1
B) option2
C) option3
D) option4
ANSWER: A

# Usage
To run the script, execute it from the command line:

bash:
python app.py

# Contributing
Contributions to the project are welcome. Please ensure that any pull requests or contributions adhere to the existing coding style and add relevant tests for new features.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

