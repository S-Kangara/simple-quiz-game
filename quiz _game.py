# simple Quiz game

questions = {
    "1. What is the largest planet in our solar system?" : "jupiter",
    "2. How many districs in Sri Lanka?" : "25",
    "3. What is the fastest land animal in the world? ": "cheetah",
    "4. How many continents are there on Earth?" : "7",
    "5. Which ocean is the largest in the world?" : "pacific ocean"
}

score = 0

print("Welcome to the General Knowledge Quiz! \n")

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is '{answer}'.\n")

percentage = (score/len(questions)) * 100
print(f"Your final score is {score}/5")
print(f"That's {percentage}% correct!!!")

if percentage >= 75:
    print("Congratulations! You passed the quiz...")
else:
    print("Oops! You are Lost...")
