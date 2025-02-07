"""
Quiz Game: Create a command-line quiz with multiple-choice questions
"""
import random as rD

class Quiz:
    def __init__(self):
        self.score = 0
        self.ques = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which programming language is known as 'snake'?",
        "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Dickens", "B. Shakespeare", "C. Tolstoy", "D. Orwell"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
        "answer": "B"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A. Albert Einstein", "B. Galileo Galilei", "C. Isaac Newton", "D. Nikola Tesla"],
        "answer": "C"
    },
    {
        "question": "Which year did World War II end?",
        "options": ["A. 1942", "B. 1945", "C. 1939", "D. 1950"],
        "answer": "B"
    },
    {
        "question": "Which data structure uses LIFO (Last In, First Out)?",
        "options": ["A. Queue", "B. Stack", "C. Array", "D. Linked List"],
        "answer": "B"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Random Access Memory", "B. Read And Modify", "C. Run After Memory", "D. Rapid Arithmetic Module"],
        "answer": "A"
    },
    {
        "question": "Which ocean is the largest in the world?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    }
]


    def ask_Ques(self):
        rD.shuffle(self.ques)
        print("\n🎯 Welcome to the Quiz Game! 🎯\n")
        
        for i, q in enumerate(self.ques, 1):
            print(f"Q{i}: {q['question']}")
            for option in q['options']:
                print(option)
            ans = input('Enter the answer(A/B/C/D): ').strip().upper()
            
            if ans == q['answer']:
                print("Correct answer! 👍")
                self.score +=1
            else:
                print(f"Incorrect answer! ❌ \nCorrect answer is {q['answer']} ")
        self.showResult()
    
    def calculate_Result(self):
        self.score += 1
    
    def showResult(self):
        if self.score == len(self.ques):
            print(f'{self.score}/{len(self.ques)}\nPerfect Score!!! 🐼')
        elif self.score > 0:
            print(f"{self.score}/{len(self.ques)} 😊")
        else:
            print("Better Luck Next time... 🙂")
            
quiz = Quiz()
quiz.ask_Ques()