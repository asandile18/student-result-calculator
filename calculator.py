import csv

def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def main():
    print("📘 Student Results Calculator 📘")
    
    name = input("Enter student name: ")
    scores = []

    # Collect 3 subjects (you can increase if you want)
    for i in range(3):
        score = float(input(f"Enter score for subject {i+1}: "))
        scores.append(score)

    average = sum(scores) / len(scores)
    grade = calculate_grade(average)

    print(f"\nStudent: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    # Save to CSV file
    with open("results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, scores, average, grade])

    print("\n✅ Results saved to results.csv")

if __name__ == "__main__":
    main()
