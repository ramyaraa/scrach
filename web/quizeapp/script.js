const questions = [
    { question: "What is 2+2?", options: ["1", "2", "3", "4"], answer: "4" },
    { question: "What is the capital of France?", options: ["Paris", "London", "Berlin", "Madrid"], answer: "Paris" },
    // Add more questions as needed
];

let currentQuestionIndex = 0;

function showQuestion() {
    const question = questions[currentQuestionIndex];
    document.getElementById('question').textContent = question.question;
    const options = document.querySelectorAll('.option');
    const feedback = document.getElementById('feedback');
    feedback.textContent = ''; // Clear previous feedback
    options.forEach((option, index) => {
        option.textContent = question.options[index];
        option.onclick = function() {
            if (option.textContent === question.answer) {
                feedback.textContent = 'Correct!';
                feedback.style.color = 'green'; // Set the feedback color to green for correct
            } else {
                feedback.textContent = 'Wrong!';
                feedback.style.color = 'red'; // Set the feedback color to red for wrong
            }
        };
    });
}

document.getElementById('next-button').addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        alert('Quiz completed!');
        feedback.textContent = 'Congratulations! You have completed the quiz.';
        feedback.style.color = 'blue';
    }
});

window.onload = showQuestion;
