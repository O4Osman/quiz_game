print("Welcome to my computer quiz!")

# Ask the user if they want to play
playing = input("Do you want to play? ").lower()

# If the user doesn't want to play, exit the game
if playing != "yes":
    quit()

print("Okay! Let's play :)")

# Initialize score
score = 0

# Ask the questions
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Show the final score
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")