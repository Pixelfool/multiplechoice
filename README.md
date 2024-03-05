# Multiple Choice Quiz Application

This Python application enables users to take multiple choice quizzes based on questions loaded from CSV files. It supports quizzes with single or multiple correct answers, randomizes question order, and tracks the user's progress across sessions, focusing on areas of difficulty.

## Features

- **Quiz Selection:** Users can select from multiple quizzes based on the CSV files available in the `quizzes` directory.
- **Customizable Question Count:** Users can choose how many questions to answer in each quiz session.
- **Progress Tracking:** The application tracks the questions the user answers incorrectly, allowing for focused review sessions.
- **Review Mode:** Users can engage in special quiz sessions that only include questions they previously answered incorrectly, needing to answer each correctly 5 times for removal from the review list.
- **Support for Multiple Correct Answers:** Questions can have more than one correct answer, requiring the user to select all correct options for credit.
- **Result Reporting:** At the end of each quiz, users receive their score as both a percentage and a count of correctly answered questions.

## Getting Started

### Prerequisites

- Python 3.x
- CSV files for quizzes placed in the `quizzes` directory

### Installation

Clone this repository to your local machine:

git clone https://github.com/Pixelfool/multiplechoice.git
cd multiplechoice


### Usage

To start a quiz session, run the following command in the terminal:

python main.py


Follow the on-screen prompts to select a quiz, enter the number of questions you wish to attempt, and begin answering questions.

## How to Contribute

Contributions to improve the application are welcome. Here are some ways you can contribute:

- Reporting bugs
- Suggesting enhancements
- Adding new quiz CSV templates

For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
