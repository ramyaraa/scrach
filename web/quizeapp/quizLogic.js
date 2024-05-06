document.addEventListener('DOMContentLoaded', function() {
    const quizData = new QuizDatabase();
    const questions = quizData.getQuestions();
    let currentQuestionIndex = 0;
    let totalScore = 0;
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const feedbackElement = document.getElementById('feedback');
    const timerElement = document.getElementById('timer');
    const resetButton = document.getElementById('reset-button');
    let answerTimeout, countdownInterval;

    function displayQuestion() {
        clearTimeout(answerTimeout);
        clearInterval(countdownInterval);
        if (currentQuestionIndex < questions.length) {
            const currentQuestion = questions[currentQuestionIndex];
            questionElement.textContent = currentQuestion.question;
            optionsElement.innerHTML = '';
            let timeLeft = 15;
            timerElement.textContent = `Time left: ${timeLeft}s`;

            countdownInterval = setInterval(() => {
                timeLeft -= 1;
                timerElement.textContent = `Time left: ${timeLeft}s`;
                if (timeLeft <= 0) {
                    clearInterval(countdownInterval);
                    showCorrectAnswer(currentQuestion.answer);
                }
            }, 1000);

            currentQuestion.options.forEach(option => {
                const button = document.createElement('button');
                button.textContent = option;
                button.classList.add('option-button');
                button.addEventListener('click', () => checkAnswer(option, false));
                optionsElement.appendChild(button);
            });
        } else {
            showResults();
        }
    }

    function checkAnswer(selectedOption, timeout = false) {
        clearTimeout(answerTimeout);
        clearInterval(countdownInterval);
        const correctAnswer = questions[currentQuestionIndex].answer;
        if (selectedOption === correctAnswer) {
            feedbackElement.textContent = 'Correct! +10 points';
            totalScore += 10;
        } else {
            feedbackElement.textContent = 'Wrong!';
        }
        currentQuestionIndex++;
        setTimeout(displayQuestion, 1000); // Move to next question after 1 second
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
