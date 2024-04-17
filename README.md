# Database Questions Importer

## Overview
This Python script processes quiz questions from a text file and inserts them into a SQL Server database. It's designed for educational platforms that require efficient data management of quiz contents.

## Features
- **Text File Reading**: Reads questions and options from a text file.
- **Question Processing**: Uses regular expressions to parse questions, options, and answers.
- **Database Interaction**: Inserts processed data into a SQL Server database, handling both questions and their options.

## Requirements
- Python 3.x
- `pyodbc` library
- SQL Server with ODBC Driver 17

## Setup
1. **Install Python Dependencies**:
   Ensure Python 3.x is installed on your system. Install the necessary Python library using pip:
   ```bash
   pip install pyodbc
   ```

2. **Database Configuration**:
   - Configure your database connection in the `connect_to_database` function:
     ```python
     'DRIVER={ODBC Driver 17 for SQL Server};SERVER=<your-server>;DATABASE=<your-database>;UID=<your-username>;PWD=<your-password>;'
     ```

3. **Prepare Your Data File**:
   - Place your text file containing the questions in the format specified in the `process_questions` function within the `questions_moodle_txt` directory.

## Usage
Run the script from the command line to process and insert the questions into the database:
```bash
python app.py
```

## Example of Data Format
Your text file should include questions formatted as follows:
```
QuestionText: 
A) option1
B) option2
C) option3
D) option4
ANSWER: A
```

## Contributing
Contributions to this project are welcome. Please ensure that any pull requests or contributions adhere to the existing coding style and add relevant tests for new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
