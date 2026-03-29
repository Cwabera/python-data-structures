# 🎓 Student Data Management System

A Python-based application for managing and analyzing student records using core data structures and modern Python techniques.

---

## 📌 Overview

This project demonstrates how to efficiently store, filter, and process student data using:

* Lists
* Dictionaries
* Tuples
* Sets
* List Comprehensions
* Generator Expressions

It is designed as a hands-on lab to apply real-world data handling techniques in Python.

---

## 🗂️ Project Structure

```
PYTHON-DATA-STRUCTURES/
│
├── lib/
│   ├── __init__.py
│   ├── student_data.py        # Student dataset
│   ├── data_generator.py      # Generator functions
│   ├── data_processing.py     # Data analysis & aggregation
│   ├── filters.py             # Filtering logic
│   ├── set_operations.py      # Set-based operations
│
├── testing/
│   ├── __init__.py
│   ├── test_data_generator.py
│   ├── test_data_processing.py
│   ├── test_filters.py
│   ├── test_set_operations.py
│
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
```

---

## 🚀 Features

* 📦 Store student records using lists and dictionaries
* 🔍 Filter students dynamically using list comprehensions
* ⚡ Process large datasets efficiently using generators
* 🧠 Track unique attributes (majors, courses) using sets
* 📊 Perform data analysis (e.g., average age, counts by major)

---

## ▶️ Getting Started

### 1. Clone the Repository

```
git clone <your-repo-url>
cd PYTHON-DATA-STRUCTURES
```

---

### 2. Install Dependencies

Using Pipenv:

```
pipenv install
pipenv shell
```

---

### 3. Run the Application

```
python3 -m lib.main
```

---

### 4. Run Tests

```
pytest
```

or for verbose output:

```
pytest -v
```

---

## 🧪 Example Functionalities

* Filter students by major
* Get average student age
* Retrieve all unique majors
* Find all courses offered
* Iterate through students using generators

---

## 🛠️ Technologies Used

* Python 3
* Pipenv (dependency management)
* Pytest (testing framework)

---

## 📚 Learning Objectives

This project helps reinforce:

* Python data structures (lists, sets, dictionaries, tuples)
* Functional programming concepts
* Efficient data handling with generators
* Writing clean, testable Python code

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.
