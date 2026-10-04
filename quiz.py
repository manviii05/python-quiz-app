questions = [
    {"q": "Python ka creator kaun hai?",
     "options": ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates"],
     "answer": "A"},
    {"q": "2 + 3 * 2 = ?",
     "options": ["A. 10", "B. 8", "C. 12"],
     "answer": "B"},
]

score = 0

for item in questions:
    print("\n" + item["q"])
    for opt in item["options"]:
        print(opt)
    ans = input("Your answer (A/B/C): ").upper()
    if ans == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Sahi answer:", item["answer"])

print(f"\nFinal Score: {score}/{len(questions)}")