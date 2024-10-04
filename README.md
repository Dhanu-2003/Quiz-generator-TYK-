# Quiz Generator

## Project Overview

**Quiz Generator** is a website built using the **Flask** framework that helps students prepare for competitive exams by generating unique multiple-choice questions (MCQs). The website is designed to streamline exam preparation by offering features like practice tests, performance analysis, and assistant guidance. It can generate **100 unique MCQs** in just **2 minutes** and provide both practice and test modes with comprehensive performance tracking.

## Key Features

1. **MCQ Generation**: Generate 100 unique MCQs in just 2 minutes.
2. **Practice Mode**:
   - Offers an assistant that guides students on how to solve problems.
   - No marks awarded for practice, but solved questions are saved for future reference.
   - Helps students learn problem-solving techniques.
3. **Test Mode**:
   - Full-screen mode for test-taking with restricted navigation.
   - Get a detailed analysis at the end of each test.
   - Solved questions and analysis are stored for future reference.
4. **Solved Section**: Access all previously solved questions for review.
5. **History Section**: View cumulative analysis of multiple tests taken on the same subject. 
   - Example: If you write three tests in Math with 10 questions each, you will get an analysis of all 30 questions in the history section.
6. **Rank Section**: Motivates students by displaying their rank among peers who took the same test.

## Technology Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQL integration for storing test results, solved questions, and user performance.
- **AI Integration**: Uses **Retrieval-Augmented Generation (RAG)** with **GPT-4** and **Gemini** for generating and augmenting MCQs.
- **Gen-AI Assistant**: Guides students through problem-solving and assists with test review.

## Installation & Setup

### Prerequisites

- **Python 3.x** installed
- **Flask** framework installed
- **Gen-AI API Key** (for AI assistance)
- Basic knowledge of how to run Flask applications

### Step-by-Step Setup

1. **Clone the Repository**:  
   Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/quiz-generator.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd quiz-generator
   ```

3. **Install Required Python Packages**:
   Install the dependencies listed in the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Your Gen-AI API Key**:
   - Open the `app.py` file.
   - Add your **Gen-AI API Key** to the relevant section.
   ```python
   # Example: Set your Gen-AI API Key
   api_key = "your-gen-ai-api-key"
   ```

5. **Run the Application**:
   Start the Flask development server.
   ```bash
   python app.py
   ```

6. **Access the Website**:
   Open a browser and go to `http://127.0.0.1:5000` to start using the Quiz Generator.

## Usage

1. **Generate MCQs**: 
   - Choose a subject and generate 100 MCQs in less than 2 minutes.
   
2. **Practice Mode**: 
   - Engage with the assistant for solving problems, and save questions for future review in the **Solved Section**.

3. **Test Mode**:
   - Take a test in a controlled environment, with a performance analysis at the end.
   - Get detailed feedback and guidance from the assistant post-test.

4. **Review & Analyze**:
   - Access solved questions and analyze your performance over multiple tests in the **History Section**.
   
5. **Rankings**:
   - View your rank among other test-takers to stay motivated.

## File Structure

```
quiz-generator/
│
├── templates/             # HTML templates for frontend
├── static/                # CSS and JavaScript files for frontend
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
├── Quiz Json Generaate.py
├── app.py
├── sql_table.py
├── example.py
├── README.md              # This README file
└── ...                    # Additional project files
```







## Contribution

Feel free to contribute to this project by submitting pull requests or reporting issues. All contributions are welcome to improve the functionality and user experience.

