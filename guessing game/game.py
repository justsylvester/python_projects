from Question import Question

question_prompts = [
    "What color is the sky?\n(a) Pink\n(b) Red\n(c) Blue\n\n",
    "Whats 5 times 9?\n(a) 54\n(b) 45\n(c) 93\n\n",
    "Whats 2 to the power of 17?\n(a) 131072\n(b) 113424\n(c) 556422\n\n"
]
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answers:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)