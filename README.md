# Student Dataset Management System using NumPy

## 📌 Project Overview

The **Student Dataset Management System** is a beginner-friendly Python project developed using NumPy. It allows users to enter and manage student information, explore NumPy array properties, and understand the differences between Python lists and NumPy arrays.

The project also demonstrates how to reshape a two-dimensional array into a three-dimensional array to represent two classrooms.

## 🎯 Project Objectives

- Create a dataset containing 20 students.
- Collect student information through user input.
- Store student IDs, ages, and subject marks in a NumPy array.
- Explore NumPy array properties such as `shape`, `ndim`, `size`, and `dtype`.
- Compare Python lists with NumPy arrays.
- Search for a student using their ID.
- Create a 3D NumPy array representing two classrooms.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Library:** NumPy
- **Development Environment:** VS Code / PyCharm / Google Colab

## 📊 Dataset Structure

The dataset contains 20 students, with six values recorded for each student.

| Column | Description |
|---|---|
| Student ID | Unique identifier for each student |
| Age | Student's age |
| Math | Mathematics marks |
| Science | Science marks |
| English | English marks |
| AI | Artificial Intelligence marks |

Marks must be between 0 and 100.

## ✨ Features

### 1. Interactive Dataset Creation
Users enter the details of 20 students manually through the terminal. The program collects each student's ID, age, and marks for four subjects.

### 2. Display Student Dataset
Displays all student records in a readable table format and prints the complete NumPy array.

### 3. Array Properties
Demonstrates four important NumPy properties:

- `shape` — Returns the number of rows and columns.
- `ndim` — Returns the number of dimensions.
- `size` — Returns the total number of elements.
- `dtype` — Returns the data type of the array.

For a dataset containing 20 students and six values per student:

```python
students.shape  # (20, 6)
students.ndim   # 2
students.size   # 120
```

The array uses a common numerical data type for all its elements.

### 4. Search for a Student
Allows users to search for a student using their ID and displays the student's details when a match is found.

### 5. Python Lists vs NumPy Arrays
Demonstrates the differences between lists and NumPy arrays, including appending elements, multiplication, and element-wise mathematical operations.

### 6. Bonus: Three-Dimensional Array
Reshapes the dataset into a 3D array representing two classrooms, with ten students in each classroom.

```python
classrooms = students.reshape(2, 10, 6)
```

The resulting shape is `(2, 10, 6)`:

- 2 classrooms
- 10 students per classroom
- 6 values per student

## ⚙️ Installation and Setup

### Prerequisites

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/student-dataset-management.git
```

### Step 2: Navigate to the Project Folder

```bash
cd student-dataset-management
```

### Step 3: Install NumPy

```bash
pip install numpy
```

### Step 4: Run the Program

```bash
python student_dataset.py
```

## ▶️ How to Use

1. Run the Python program.
2. Enter the required number of students: `20`.
3. Enter each student's ID, age, Math marks, Science marks, English marks, and AI marks.
4. Choose an option from the main menu.
5. View the dataset, inspect array properties, search for a student, compare lists and arrays, or explore the 3D classroom array.
6. Select the exit option to close the program.

## 📁 Project Structure

```text
student-dataset-management/
│
├── student_dataset.py
├── README.md
└── .gitignore
```

- `student_dataset.py` — Contains the complete Python program.
- `README.md` — Documents the project, its features, and instructions.
- `.gitignore` — Specifies files Git should ignore, if included.

## 🧠 Concepts Learned

Through this project, I practiced:

- Python functions and parameters
- Loops and conditional statements
- User input and input validation
- Python lists
- NumPy array creation
- Array indexing and reshaping
- Array properties and data types
- Formatted output using f-strings
- Basic data management

## 🚀 Future Improvements

- Save and load student records using CSV files.
- Allow users to update or delete student records.
- Calculate average marks and student rankings.
- Add data visualization using Matplotlib.
- Separate the project into modules for improved organization.

## 👨‍💻 Author

**Ackaash**

GitHub: [YOUR_GITHUB_PROFILE](https://github.com/YOUR_USERNAME)

## 📄 License

This project is available for educational and learning purposes. A formal open-source license can be added if the project is distributed for reuse.
