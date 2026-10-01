from abc import ABC, abstractmethod


class Question(ABC):
    def __init__(self, text, marks):
        self.text = text
        self.marks = marks

    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, text, marks, correct_option):
        super().__init__(text, marks)
        self.correct_option = correct_option

    def evaluate_answer(self, answer):
        return self.marks if answer.strip().lower() == self.correct_option.lower() else 0


class TrueFalseQuestion(Question):
    def __init__(self, text, marks, correct_answer):
        super().__init__(text, marks)
        self.correct_answer = correct_answer       # True or False

    def evaluate_answer(self, answer):
        return self.marks if answer == self.correct_answer else 0


class DescriptiveQuestion(Question):
    def __init__(self, text, marks, keywords):
        super().__init__(text, marks)
        self.keywords = keywords

    def evaluate_answer(self, answer):
        found = sum(1 for k in self.keywords if k.lower() in answer.lower())
        return round(self.marks * found / len(self.keywords), 2)


exam = [
    (MCQQuestion("Which keyword defines a function in Python?", 2, "def"), "def"),
    (TrueFalseQuestion("Python is a compiled-only language.", 1, False), True),
    (DescriptiveQuestion("What is abstraction?", 5, ["hide", "implementation", "interface"]),
     "Abstraction means to hide the implementation and show only the interface."),
]

total = 0
for q, answer in exam:
    score = q.evaluate_answer(answer)
    total += score
    print(f"{q.text} -> Score: {score}/{q.marks}")
print("Total score:", total)
