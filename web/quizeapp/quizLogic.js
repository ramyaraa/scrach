document.addEventListener('DOMContentLoaded', function() {
    const quizData = new QuizDatabase();
    const questions = quizData.getQuestions();
    let currentQuestionIndex = 0;
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');
    const feedbackElement = document.getElementById('feedback');
    if (!questionElement || !optionsElement || !feedbackElement) {
        console.error('One or more quiz elements are missing!');
        return; // Stop execution if elements are missing
    }


    function displayQuestion() {
        const currentQuestion = questions[currentQuestionIndex];
        questionElement.textContent = currentQuestion.question;
        optionsElement.innerHTML = ''; // Clear previous options

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

        // Move to the next question or end quiz
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            setTimeout(displayQuestion, 1000); // Wait for 1 second before showing the next question
        } else {
            feedbackElement.textContent += " Quiz completed!";
        }
    }

    // Function to start the quiz
    window.startQuiz = function() {
        displayQuestion();
    };
});
