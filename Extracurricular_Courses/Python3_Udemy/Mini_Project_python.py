### Mathematics Grade Calculating

## Total Score is 100% ##
# Exercise total score is 50 (10%).
# Project total score is 100 (20%).
# Quiz 1 total score is 10 (10%).
# Quiz 2 total score is 10 (10%).
# Midterm exam total score is 100 (20%).
# Final exam total score is 150 (30%).

## Grading
# Grade A+: total score is over 96.67%.
# Grade A: total score is over 93.33% but less than 96.67%.
# Grade A-: total score is over 90.0% but less than 93.33%.
# Grade B+: total score is over 86.67% but less than 90.0%.
# Grade B: total score is over 83.33% but less than 86.67%.
# Grade B-: total score is over 80.0% but less than 83.33%.
# Grade C+: total score is over 76.67% but less than 76.67%.
# Grade C: total score is over 70.0% but less than 76.67%.
# Grade D: total score is over 60.0% but less than 70.0.
# Grade F: total score is below 60%.
# Note -- If input the variable which is not a number, the result will print ERROR.


# Set the function for Math grade calculator
def cal_grade(exercise, project, quiz1, quiz2, midterm, final):
    exercise_weight = 0.1
    project_weight = 0.2
    quiz1_weight = 0.1
    quiz2_weight = 0.1
    midterm_weight = 0.5
    final_weight = 0.3

    total_score = (exercise * exercise_weight) + (project * project_weight) + (quiz1 * quiz1_weight) + (quiz2 * quiz2_weight) + (midterm_weight * midterm_weight) + (final * final_weight)

    return total_score

def get_grade(total_score):
    if total_score > 96.67 and total_score <= 100:
        return "A+"
    elif total_score > 93.33:
        return "A"
    elif total_score > 90.0:
        return "A-"
    elif total_score > 86.67:
        return "B+"
    elif total_score > 83.33:
        return "B"
    elif total_score > 80.0:
        return "B-"
    elif total_score > 76.67:
        return "C+"
    elif total_score > 70.0:
        return "C"
    elif total_score > 60.0:
        return "D"
    else:
        return "F"

def main():
    id = input("Enter student ID: ")
    name = input("Enter student Name: ")
    exercise = float(input("Enter exercise score (50): "))
    quiz1 = float(input("Enter quiz 1 score (10): "))
    project = float(input("Enter project score (50): "))
    midterm = float(input("Enter midterm exam score (100): "))
    quiz2 = float(input("Enter quiz 2 score (10): "))
    final = float(input("Enter final exam score (150): "))

    total_score = cal_grade(exercise, project, quiz1, quiz2, midterm, final)
    grade = get_grade(total_score)

    print("Mathematics Grade Calculate")
    print(f'Student ID: {id}')
    print(f'Student Name: {name}')
    print(f'Exercise Score: {exercise} / 50')
    print(f'Quiz 2 Score: {quiz1} / 10')
    print(f'Quiz 2 Score: {quiz2} / 10')
    print(f'Project Score: {project} / 50')
    print(f'Midterm Exam score: {midterm} / 100')
    print(f'Final Exam Score: {final} / 150')
    print(f'Total Score Percent (100%): {total_score:.2f}%')
    print(f'Grade: {grade}')
    print(f'Feedback: {feedback}')

if __name__ == "__main__":
    main()