class QuizDatabase {
    constructor() {
        this.questions = [
            {
                question: "What is 2+2?",
                options: ["3", "4", "5", "6"],
                answer: "4"
            },
            {
                question: "Whose statement is this ' kura bro lera mauasta hay qashmary qomchy '",
                options: ["dana chawrash", "3umar dababa", "mamosta pola", "all"],
                answer: "all"
            },
            {
                question: "Which planet is known as the Red Planet?",
                options: ["Earth", "Mars", "Jupiter", "Venus"],
                answer: "Mars"
            },
            {
                question: "what do you have for the person who created this website",
                options: ["thanks", "keep going", "long live", "ay dasxush"],
                answer: "ay dasxush"
            }
        ];
    }

    getQuestions() {
        return this.questions;
    }
}
