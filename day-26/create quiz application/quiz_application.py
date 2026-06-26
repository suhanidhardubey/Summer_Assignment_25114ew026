score = 0

print("Welcome to the Quiz Application!")

# Question 1
answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is New Delhi.")

# Question 2
answer = input("2. Which language is used for Python programming? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Python.")

# Question 3
answer = input("3. How many continents are there in the world? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 7.")

# Display final score
print("\nYour final score is:", score, "/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good Job!")
else:
    print("Keep Practicing!")