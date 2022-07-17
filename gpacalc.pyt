class GpaCalculator():

    count = 0
    hrs = 0
    numberofclasses = 0
    totalhours = 0
    totalPoints = 0.0
    gpa = 0.0

    numberofclasses = int(input("Enter number of  classes "))

    for count in range(count, numberofclasses):

        print("For class # ", count+1)

        hrs = int(input("Enter the credit hrs "))

        grade = input("Enter the letter grade ")

        if grade == 'A' or grade == 'a':
            totalPoints = totalPoints + (hrs * 4)
            totalhours = totalhours + hrs
        elif grade == 'B' or grade == 'b':
            totalPoints += (hrs * 3.0)
            totalhours += hrs
        elif grade == 'C' or grade == 'c':
            totalPoints += (hrs * 2.0)
            totalhours += hrs
        elif grade == 'D' or grade == 'd':
            totalPoints += (hrs * 1.0)
            totalhours += hrs

        else:
            totalPoints += (hrs * 0.0)
            totalhours += hrs

    gpa = totalPoints / totalhours
    print("Your GPA is :", gpa)


def main():
    gpa = GpaCalculator()


if __name__ == '__main__':
    main()
