document.addEventListener('DOMContentLoaded', function() {
    const quizData = new QuizDatabase();
    const questions = quizData.getQuestions();
    let currentQuestionIndex = 0;
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const feedbackElement = document.getElementById('feedback');
    const nextButton = document.getElementById('next-button');
    const resetButton = document.getElementById('reset-button');

    function displayQuestion() {
        const currentQuestion = questions[currentQuestionIndex];
        questionElement.textContent = currentQuestion.question;
        optionsElement.innerHTML = '';
        nextButton.style.display = 'none'; // Hide Next button initially

        currentQuestion.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option;
            button.classList.add('option-button');
            button.addEventListener('click', () => checkAnswer(option));
            optionsElement.appendChild(button);
        });
    }

    function checkAnswer(selectedOption) {
        const correctAnswer = questions[currentQuestionIndex].answer;
        if (selectedOption === correctAnswer) {
            feedbackElement.textContent = 'Correct!';
        } else {
            feedbackElement.textContent = 'Wrong!';
        }

        nextButton.style.display = 'block'; // Show Next button
    }

    nextButton.addEventListener('click', () => {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            displayQuestion();
        } else {
            feedbackElement.textContent = "Quiz completed!";
            nextButton.style.display = 'none';
        }
    });

    resetButton.addEventListener('click', () => {
        currentQuestionIndex = 0;
        displayQuestion();
        feedbackElement.textContent = '';
    });

    // Function to start the quiz
    window.startQuiz = function() {
        displayQuestion();
    };

    // Set a timer to move to the next question automatically after 30 seconds
    setInterval(() => {
        if (nextButton.style.display !== 'none') { // Only move forward if Next is visible
            nextButton.click();
        }
    }, 10000); // 10 seconds
});
