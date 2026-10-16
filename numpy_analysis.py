
import numpy as np


# 1. CREATE THE DATASET BY ENTERING STUDENT DETAILS

def create_dataset():
    students = []
    
    number_of_students = 20

    print("\n========== CREATE STUDENT DATASET ==========")


    for i in range(number_of_students):
        print(f"\nEnter details for Student {i + 1}")

        while True:
            try:
                student_id = int(input("Student ID: "))

                if any(row[0] == student_id for row in students):
                    print("This Student ID already exists. Enter a unique ID.")
                    continue

                age = int(input("Age: "))

                if age <= 0:
                 print("Age must be greater than zero. Enter this student again.")
                 continue
                
                math_marks = float(input("Math Marks: "))
                science_marks = float(input("Science Marks: "))
                english_marks = float(input("English Marks: "))
                ai_marks = float(input("AI Marks: "))

               

                marks = [math_marks, science_marks, english_marks, ai_marks]

                if any(mark < 0 or mark > 100 for mark in marks):
                    print("Marks must be between 0 and 100. Enter this student again.")
                    continue

                student = [
                    student_id,
                    age,
                    math_marks,
                    science_marks,
                    english_marks,
                    ai_marks
                ]

                students.append(student)
                break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                print("Please enter this student's details again.")

    # Convert the Python list into a NumPy array
    students_array = np.array(students, dtype=float)

    return students_array



# 2. DISPLAY THE DATASET

def display_dataset(students):
    print("\n========== STUDENT DATASET ==========")

    print(
        f"{'ID':<8} {'Age':<5} {'Math':<8} "
        f"{'Science':<9} {'English':<9} {'AI':<8}"
    )

    for student in students:
        print(
            f"{int(student[0]):<8} "
            f"{int(student[1]):<} "
            f"{student[2]:<8} "
            f"{student[3]:<9} "
            f"{student[4]:<9} "
            f"{student[5]:<8}"
        )

    print("\nComplete NumPy Array:")
    print(students)



# 3. DISPLAY ARRAY PROPERTIES

def display_array_properties(students):
    print("\n========== ARRAY PROPERTIES ==========")

    print("Shape:", students.shape)
    print("Dimensions:", students.ndim)
    print("Size:", students.size)
    print("Data Type:", students.dtype)


# 4. SEARCH FOR A STUDENT

def search_student(students):
    print("\n========== SEARCH STUDENT ==========")

    try:
        student_id = int(input("Enter Student ID: "))

        # Column 0 contains student IDs
        result = students[students[:, 0] == student_id]

        if result.size > 0:
            student = result[0]

            print("\nStudent Found!")
            print("Student ID:", int(student[0]))
            print("Age:", int(student[1]))
            print("Math Marks:", student[2])
            print("Science Marks:", student[3])
            print("English Marks:", student[4])
            print("AI Marks:", student[5])

        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid numeric Student ID.")


# 5. COMPARE PYTHON LISTS WITH NUMPY ARRAYS

def compare_lists_and_arrays():
    print("\n========== PYTHON LIST VS NUMPY ARRAY ==========")

    python_list = [10, 20, 30, 40]
    numpy_array = np.array([10, 20, 30, 40])

    print("Python List:", python_list)
    print("NumPy Array:", numpy_array)

    # Adding an element to a list
    python_list.append(50)

    print("\nAfter appending 50:")
    print("Python List:", python_list)

    # Adding a number to every array element
    print("\nArray + 5:", numpy_array + 5)

    # Multiplication comparison
    print("\nList * 2:", python_list * 2)
    print("Array * 2:", numpy_array * 2)

    # Element-wise addition of two arrays
    print("\nArray + Array:", numpy_array + numpy_array)

    print("\nExplanation:")
    print("- Lists can store mixed data types.")
    print("- NumPy arrays normally use one common data type.")
    print("- Multiplying a list by 2 repeats its contents.")
    print("- Multiplying an array by 2 doubles every element.")
    print("- NumPy supports convenient mathematical operations.")


# 6. CREATE A 3D ARRAY FOR TWO CLASSROOMS (BONUS)

def create_3d_classroom_array(students):
    print("\n========== 3D CLASSROOM ARRAY ==========")

    # 2 classrooms, 10 students per classroom,
    # and 6 values for every student
    classrooms = students.reshape(2, 10, 6)

    print("3D Array:")
    print(classrooms)

    print("\nShape:", classrooms.shape)
    print("Dimensions:", classrooms.ndim)
    print("Size:", classrooms.size)

    print("\nClassroom 1:")
    print(classrooms[0])

    print("\nClassroom 2:")
    print(classrooms[1])

    print("\nFirst student in Classroom 1:")
    print(classrooms[0, 0])

    print("\nMath mark of the first student in Classroom 1:")
    print(classrooms[0, 0, 2])

    print("\nColumn positions:")
    print("0 = Student ID")
    print("1 = Age")
    print("2 = Math")
    print("3 = Science")
    print("4 = English")
    print("5 = AI")


# 7. MAIN MENU

def main():
    print("STUDENT DATASET MANAGEMENT SYSTEM")
    print("First, enter the details of all 20 students.")

    students = create_dataset()

    while True:
        print("\n============================================")
        print("       STUDENT DATASET MANAGEMENT SYSTEM")
        print("============================================")
        print("1. Display Student Dataset")
        print("2. Display Array Properties")
        print("3. Search for a Student")
        print("4. Compare Python Lists vs NumPy Arrays")
        print("5. Display 3D Classroom Array (Bonus)")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            display_dataset(students)

        elif choice == "2":
            display_array_properties(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            compare_lists_and_arrays()

        elif choice == "5":
            create_3d_classroom_array(students)

        elif choice == "6":
            print("\nThank you for using the system!")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")




if __name__ == "__main__":
    main()
