import pyodbc
import re
import uuid

def read_text_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def process_questions(text):
    # Adjusted the pattern to match questions with or without a colon at the end
    question_pattern = re.compile(r'(?P<question>.+?)(?:\:)?\s+(?P<options>(?:[A-D]\) .+\n?)+)ANSWER: (?P<answer>[A-D])', re.MULTILINE)
    questions = []
    for match in question_pattern.finditer(text):
        question_text = match.group('question').strip()
        options_text = match.group('options').strip().split('\n')
        answer = match.group('answer').strip()
        options = [opt[3:].strip() for opt in options_text]
        questions.append((question_text, options, answer))
    return questions

def connect_to_database():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=;DATABASE=;UID=;PWD=;')

def insert_question_and_options(conn, question, options, answer):
    cursor = conn.cursor()
    try:
        migration_code = str(uuid.uuid4())
        cursor.execute("""
        INSERT INTO question (question_text, course_id, created_at, question_type_id, migration_code) 
        VALUES (?, 116, '2024-03-24', 1, ?);
        """, (question, migration_code))
        conn.commit()

        cursor.execute("SELECT id FROM question WHERE migration_code = ?;", (migration_code,))
        question_id_result = cursor.fetchone()
        if question_id_result:
            question_id = question_id_result[0]
            for option_text in options:
                correct_score = 100 if options.index(option_text) == ord(answer) - ord('A') else 0
                is_correct = 1 if options.index(option_text) == ord(answer) - ord('A') else 0
                cursor.execute("""
                INSERT INTO alternative (question_id, description, fraction, created_at, correct) 
                VALUES (?, ?, ?, '2024-03-24', ?);
                """, (question_id, option_text, correct_score, is_correct))
            conn.commit()
        else:
            raise Exception("Failed to retrieve question_id with migration_code")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
        
    finally:
        cursor.close()

def main():
    path = 'questions_moodle_txt/module_i.txt'
    text = read_text_file(path)
    questions = process_questions(text)
    conn = connect_to_database()
    for question, options, answer in questions:
        insert_question_and_options(conn, question, options, answer)
    conn.close()

if __name__ == "__main__":
    main()

