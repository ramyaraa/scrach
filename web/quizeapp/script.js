let currentQuestionIndex = 0;

function showQuestion() {
    const question = quizQuestions[currentQuestionIndex];
    document.getElementById('question').textContent = question.question;
    const options = document.querySelectorAll('.option');
    const feedback = document.getElementById('feedback');
    feedback.textContent = ''; // Clear previous feedback
    options.forEach((option, index) => {
        option.textContent = question.options[index];
        option.onclick = function() {
            if (option.textContent === question.answer) {
                feedback.textContent = 'Correct!';
                feedback.style.color = 'green';
            } else {
                feedback.textContent = 'Wrong!';
                feedback.style.color = 'red';
            }
        };
    });
}

document.getElementById('next-button').addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < quizQuestions.length) {
        showQuestion();
    } else {
        alert('Quiz completed!');
        feedback.textContent = 'Congratulations! You have completed the quiz.';
        feedback.style.color = 'blue';
    }
});

window.onload = showQuestion;
