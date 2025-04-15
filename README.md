# 📘 StudyMate AI Assistant

**StudyMate AI** is an intelligent productivity assistant for students and instructors. It automates the parsing of course syllabi, extracts important deliverables (assignments, quizzes, exams), syncs them with Google Calendar, and generates AI-powered interactive quizzes for effective revision — all within a beautiful Streamlit UI.

---

## 🚀 Features

### 1. 📄 Syllabus Parser
- Upload any PDF syllabus.
- Extracts course title and tasks like assignments, quizzes, exams.
- Tasks are structured with `task_name`, `deadline`, and `priority`.

### 2. 📅 Calendar Integration
- Add tasks directly to Google Calendar.
- Supports manual date selection if no deadline is found.
- Reminders are automatically configured.

### 3. 🧪 AI Quiz Generator
- Paste course material (notes/slides/text).
- Generate 5 multiple-choice questions (MCQs) with difficulty levels.
- Interactive quiz interface with answer validation.

---

## 🛠️ Tech Stack

- `Python 3.10+`
- `Streamlit`
- `OpenAI GPT-4 Turbo`
- `Google Calendar API`
- `PyPDF2`
- `dotenv` for secure config management

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/jatphat/StudyMate.git
cd StudyMate

# Install dependencies
pip install -r requirements.txt
