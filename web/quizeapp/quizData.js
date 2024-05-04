class QuizDatabase {
    constructor() {
        this.questions = [
            {
                question: "What is the capital of France?",
                options: ["Paris", "London", "Berlin", "Madrid"],
                answer: "Paris"
            },
            {
                question: "What is 2+2?",
                options: ["3", "4", "5", "6"],
                answer: "4"
            },
            {
                question: "Which planet is known as the Red Planet?",
                options: ["Earth", "Mars", "Jupiter", "Venus"],
                answer: "Mars"
            },
            {
                question: "What year did the Titanic sink?",
                options: ["1912", "1905", "1898", "1923"],
                answer: "1912"
            }
        ];
    }

    getQuestions() {
        return this.questions;
    }
}
