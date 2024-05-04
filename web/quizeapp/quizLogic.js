document.addEventListener('DOMContentLoaded', function() {
    const quizData = new QuizDatabase();
    const questions = quizData.getQuestions();
    let currentQuestionIndex = 0;
    let totalScore = 0; // Track the total score
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const feedbackElement = document.getElementById('feedback');
    const resetButton = document.getElementById('reset-button');

    function displayQuestion() {
        if (currentQuestionIndex < questions.length) {
            const currentQuestion = questions[currentQuestionIndex];
            questionElement.textContent = currentQuestion.question;
            optionsElement.innerHTML = '';

            currentQuestion.options.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option;
                button.classList.add('option-button');
                button.addEventListener('click', () => checkAnswer(option));
                optionsElement.appendChild(button);
            });
        } else {
            showResults();
        }
    }

    function checkAnswer(selectedOption) {
        const correctAnswer = questions[currentQuestionIndex].answer;
        if (selectedOption === correctAnswer) {
            feedbackElement.textContent = 'Correct! +10 points';
            totalScore += 10; // Add points for correct answer
        } else {
            feedbackElement.textContent = 'Wrong!';
        }
        currentQuestionIndex++; // Move to the next question
        setTimeout(displayQuestion, 1000); // Wait for 1 second before next question
    }

    function showResults() {
        feedbackElement.textContent = `Quiz completed! Total Score: ${totalScore}`;
        questionElement.textContent = '';
        optionsElement.innerHTML = '';
    }

    resetButton.addEventListener('click', () => {
        currentQuestionIndex = 0;
        totalScore = 0; // Reset the score
        displayQuestion();
        feedbackElement.textContent = '';
    });

    // Function to start the quiz
    window.startQuiz = function() {
        displayQuestion();
    };
});
