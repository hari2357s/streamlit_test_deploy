# 💬 Web-Based Chat Application using Streamlit

## 📌 Introduction  
This project is a web-based chat application developed using **Python** and the **Streamlit** framework.  
It provides a simple, interactive, and lightweight platform for real-time messaging between users.

The application focuses on clean architecture, modular design, and ease of deployment.

---

## ❓ Problem Statement  
Most chat applications require complex frontend-backend setups and heavy frameworks.  
This project aims to build a **simple yet functional chat system** using Streamlit, reducing development complexity while maintaining usability.

---

## 🎯 Objectives  
- Build a real-time chat interface  
- Use Python for backend logic  
- Implement clean architecture and design patterns  
- Ensure easy deployment and maintenance  
- Provide a responsive and user-friendly UI  

---

## 🚀 Features  
- User authentication  
- One-to-one chat  
- Message history  
- Simple and clean UI  
- Modular code structure  
- Easy deployment  

---

## 🛠️ Tech Stack  
- **Language:** Python  
- **Framework:** Streamlit  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure  
project/
│
├── requirements.txt
├── README.md
├── pyproject.toml
├── src
| ├── myapp
|   ├── app.py
|   ├── common/
│     └── database/
|   ├── modules/
│     ├── chat/
│     ├── group/
│     ├── user/
│     └── message/

---

## ⚙️ Installation  

1. Clone the repository  

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Create a virtual environment

python -m venv chatvenv
source chatvenv/bin/activate   # Linux / Mac
chatvenv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

▶️ Run the Application

streamlit run app.py

Then open the browser at:

http://localhost:8501
