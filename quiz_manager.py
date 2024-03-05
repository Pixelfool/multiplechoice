import csv
import random

class QuizManager:
    def __init__(self, quiz_file):
        self.quiz_file = quiz_file
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """Load questions from the CSV file according to the new format."""
        with open(self.quiz_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming CSV format: Question, "Option1;Option2;...", CorrectIndex(es)
                question_text = row[0]
                options = row[1].split(';')  # Split options by semicolon
                correct_indexes = [int(i) for i in row[2].split(';')]  # Split correct indexes and convert to int

                self.questions.append({
                    'text': question_text,
                    'options': options,
                    'correct': correct_indexes
                })

    def start_quiz(self, num_questions=None, progress={}, focus_on_wrong=False):
        """Start the quiz session with a specified number of questions, focusing on wrong answers if requested."""
        if focus_on_wrong:
            # Filter questions to those that are in progress with incorrect answers
            # questions_to_ask = [q for q in self.questions if q['text'] in progress and progress[q['text']] <= 2]
            questions_to_ask = [q for q in self.questions if q['text'] in progress]
        else:
            questions_to_ask = self.questions

        if num_questions is None or num_questions <= 0 or num_questions > len(questions_to_ask):
            num_questions = len(questions_to_ask)

        questions = random.sample(questions_to_ask, k=num_questions)
        correct_answers = 0

        for question in questions:
            print(question['text'])
            for i, option in enumerate(question['options'], start=1):
                print(f"{i}. {option}")
            user_answer = input("Your answers (for multiple, separate by comma): ").strip()
            if user_answer:  # Proceed if the user provided an answer
                user_indexes = [int(i) for i in user_answer.split(',')]
                if set(user_indexes) == set(question['correct']):
                    print("Correct!")
                    correct_answers += 1
                    progress[question['text']] = progress.get(question['text'], 0) + 1
                    # Remove question from wrong list if answered correctly 5 times
                    if progress[question['text']] >= 5:
                        del progress[question['text']]
                else:
                    print("Wrong. Correct answer(s):", ', '.join(str(i) for i in question['correct']))
                    progress[question['text']] = 0
            else:
                print("No answer provided.")

        self.show_results(correct_answers, len(questions))


    def show_results(self, correct_answers, total_questions):
        """Display the quiz results to the user."""
        percentage = (correct_answers / total_questions) * 100
        print(f"\nYou answered {correct_answers} out of {total_questions} questions correctly ({percentage:.2f}%).")
