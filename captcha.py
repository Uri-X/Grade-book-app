import random

def generate_captcha():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    operation = random.choice(['+', '-'])
    if operation == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2
    return f"What is {num1} {operation} {num2}?", answer

def verify_captcha():
    question, answer = generate_captcha()
    print(question)
    user_answer = input("Answer: ")
    try:
        user_answer = int(user_answer)
        return user_answer == answer
    except ValueError:
        return False
