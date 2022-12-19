from multiple_quiz_functions import Question

question_prompts = [
    'What color are apples?\n(a) Red/Green\n(b) Purplre\n(c) Orange\n\n',
    'What color are strawberries?\n(a) Magenta\n(b) Red\n(c) Green\n\n',
    'What color are Bananas?\n(a) Yellow\n(b) Blue\n(c) Pink\n\n'
]

questions = [
    Question (question_prompts[0], 'a'),
    Question (question_prompts[1], 'b'),
    Question (question_prompts[2], 'a')
]

def run_test (questions):
    score = 0
    for question in questions:
        anser = input (question.prompt)
        if anser == question.answer:
            score += 1
    print ('You got ' + str(score) + '/' + str(len(questions)) + ' correct')

run_test (questions)
    

 