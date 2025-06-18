# 🧠 Employee Promotion Analysis

This project is a Machine Learning-based web application that predicts whether an employee is eligible for promotion based on multiple organizational factors. Built using Django and integrated with a Gaussian Naive Bayes classifier, the system helps HR professionals make data-driven, unbiased promotion decisions.

## 📌 Project Objective

To automate and improve the accuracy of promotion decision-making in organizations using data analytics and machine learning, reducing bias and increasing employee satisfaction and retention.

---

## 🚀 Features

- 🔍 Predicts employee promotion eligibility in real-time
- 📊 Data analysis of key factors like ratings, experience, training
- 👩‍💼 Admin module to track prediction history and manage users
- 👥 User login and registration system
- 📈 Visual analytics and charts based on dataset
- ⚙️ Interactive UI using Bootstrap, HTML, CSS

---

## 🛠 Tech Stack

| Area           | Technology                  |
|----------------|-----------------------------|
| Frontend       | HTML, CSS, JavaScript, Bootstrap |
| Backend        | Django (Python)             |
| Database       | SQLite                      |
| ML Algorithm   | Gaussian Naive Bayes        |
| Data Handling  | Pandas, NumPy               |
| Model Training | Scikit-learn                |

---

## 📂 Dataset Features

The dataset includes:
- Department
- Education
- Gender
- Recruitment Channel
- Training Count
- Age
- Previous Ratings
- Length of Service
- Awards Won
- Average Training Scores

**Target Variable:** `is_promoted` (0 or 1)

Dataset Source: [Kaggle - Employee Evaluation for Promotion](https://www.kaggle.com/datasets/muhammadimran112233/employees-evaluation-for-promotion)

---

## 📷 Screenshots

![Home Page](screenshots/home.png)
![User Prediction](screenshots/predict.png)
![Admin Dashboard](screenshots/admin_history.png)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/employee-promotion-analysis.git

# Change directory
cd employee-promotion-analysis

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Django server
python manage.py runserver
