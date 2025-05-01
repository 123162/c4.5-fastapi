
# 🌳 C4.5 Decision Tree Classifier API

This project implements a classification API using a custom implementation of the C4.5 decision tree algorithm, served via FastAPI and fully containerized using Docker.

## 🚀 Features

- Custom implementation of the C4.5 decision tree algorithm
- RESTful API powered by FastAPI
- Containerized environment with Docker for consistency and portability
- JSON-based input/output for easy integration
- Ready for local or cloud deployment

---

## 📁 Project Structure

```
c4.5/
│
├── data/
│   └── theWorldBank.xlsx
│
├── main.py
├── model/
│   ├── __init__.py
│   ├── __pycache__/
│   └── tree_model.py
├── __pycache__/
│   └── main.cpython-312.pyc
├── requirements.txt
└── venv/
    ├── bin/
    ├── include/
    ├── lib/
    ├── lib64 -> lib/
    ├── pyvenv.cfg
    └── share/
```

---

## ⚙️ Setup & Running the App

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/c4.5-fastapi.git
cd c4.5-fastapi
```

### 2. Install Requirements

Make sure Python 3.7+ is installed. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 3. Run the Application Locally

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 💡 Development Plans

- Add a visual interface to upload datasets
- Save and load trained decision trees
- Evaluate and visualize tree performance (accuracy, confusion matrix)
- Add Docker deployment guide

---

## 👤 Developer

- **Name:** Rabia Şenlik
- **GitHub:** [@rabia-senlik](https://github.com/rabia-senlik)

