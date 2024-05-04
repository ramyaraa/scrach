document.addEventListener('DOMContentLoaded', function() {
    const quizData = new QuizDatabase();
    const questions = quizData.getQuestions();
    let currentQuestionIndex = 0;
    let totalScore = 0;
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const feedbackElement = document.getElementById('feedback');
    const resetButton = document.getElementById('reset-button');
    let answerTimeout;

    function displayQuestion() {
        clearTimeout(answerTimeout); // Clear any existing timers
        if (currentQuestionIndex < questions.length) {
            const currentQuestion = questions[currentQuestionIndex];
            questionElement.textContent = currentQuestion.question;
            optionsElement.innerHTML = '';
            currentQuestion.options.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option;
                button.classList.add('option-button');
                button.addEventListener('click', () => checkAnswer(option, false));
                optionsElement.appendChild(button);
            });
            // Set a timer for the question
            answerTimeout = setTimeout(() => showCorrectAnswer(currentQuestion.answer), 15000);
        } else {
            showResults();
        }
    }

    function checkAnswer(selectedOption, timeout = false) {
        clearTimeout(answerTimeout); // Stop the timer as the user has answered
        const correctAnswer = questions[currentQuestionIndex].answer;
        if (selectedOption === correctAnswer) {
            feedbackElement.textContent = 'Correct! +10 points';
            totalScore += 10;
        } else {
            feedbackElement.textContent = 'Wrong!';
        }
        if (!timeout) {
            currentQuestionIndex++;
            setTimeout(displayQuestion, 1000); // Move to next question after 1 second
        }
    }

    function showCorrectAnswer(correctAnswer) {
        optionsElement.querySelectorAll('.option-button').forEach(button => {
            if (button.textContent === correctAnswer) {
                button.style.backgroundColor = 'green'; // Highlight correct answer
            }
        });
        feedbackElement.textContent = 'Time up! Moving to next question...';
        currentQuestionIndex++;
        setTimeout(displayQuestion, 3000); // Move to next question after 3 seconds
    }

    function showResults() {
        feedbackElement.textContent = `Quiz completed! Total Score: ${totalScore}`;
        questionElement.textContent = '';
        optionsElement.innerHTML = '';
    }

    resetButton.addEventListener('click', () => {
        currentQuestionIndex = 0;
        totalScore = 0;
        displayQuestion();
        feedbackElement.textContent = '';
    });

    window.startQuiz = function() {
        displayQuestion();
    };
});
