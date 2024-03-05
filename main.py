import os
import csv
import random
import json
from quiz_manager import QuizManager

def load_quizzes(directory):
    """Load quiz filenames from the specified directory."""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def select_quiz(quizzes):
    """Let the user select a quiz from the available options."""
    print("Available Quizzes:")
    for i, quiz in enumerate(quizzes, start=1):
        print(f"{i}. {quiz[:-4]}")  # Remove .csv extension for display
    choice = int(input("Select a quiz by number: ")) - 1
    return quizzes[choice]

def main():
    quizzes_directory = "./quizzes"
    quizzes = load_quizzes(quizzes_directory)
    
    if not quizzes:
        print("No quizzes found.")
        return
    elif len(quizzes) == 1:
        # Automatically select the quiz if there's only one
        quiz_file = quizzes[0]
        print(f"Automatically selected quiz: {quiz_file[:-4]}")  # Inform the user about the automatic selection
    else:
        quiz_file = select_quiz(quizzes)  # Prompt the user to select a quiz if there are multiple options
    
    quiz_manager = QuizManager(os.path.join(quizzes_directory, quiz_file))
    
    # Load progress
    try:
        with open("progress.json", "r") as file:
            progress = json.load(file)
            f = open("progress.json", "r")
            if f.read(2) != '{}':
                focus_on_wrong = not input("Focus on questions you've previously answered wrong? (yes/no): ").lower().startswith('n')
            else:
                focus_on_wrong = False
    except FileNotFoundError:
        progress = {}  # No progress found, proceed accordingly
        focus_on_wrong = False
    except json.JSONDecodeError:
        print("Error reading progress. Starting fresh.")
        focus_on_wrong = False
        progress = {}
    
    if not focus_on_wrong:
        try:
            num_questions_input = input("How many questions do you want to attempt? (Press enter for all): ").strip()
            num_questions = int(num_questions_input) if num_questions_input else None
        except ValueError:
            print("Please enter a valid number or press enter for all questions.")
            return
    else:
        num_questions = None

    quiz_manager.start_quiz(num_questions, progress, focus_on_wrong=focus_on_wrong)
    
    # Save progress
    with open("progress.json", "w") as file:
        json.dump(progress, file, indent=4)

if __name__ == "__main__":
    main()
