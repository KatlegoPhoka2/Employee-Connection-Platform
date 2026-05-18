# 🤝 Employee Connection Platform

An AI-powered employee networking and engagement automation platform built with Python, FastAPI, n8n, Google Sheets, LLM workflows, and automated email systems.

---

## 📖 Overview

The **Employee Connection Platform** helps employees build meaningful relationships outside of their immediate work responsibilities  automatically. Every month, the platform recommends internal connections, sends personalized emails, and tracks engagement, all powered by AI and workflow automation.

**The platform improves:**
- Employee engagement
- Cross-team collaboration
- Company culture
- Internal communication

---

## ✨ Features

### 📅 Monthly Connection Recommendations
Each employee receives **3 curated connection recommendations** every month.

### 📧 Personalized Emails
Recommendation emails include employee profiles, direct connect actions, and automated workflow links.

### 🔗 One-Click Connection Initiation
Employees can send a connection invitation directly from their email — no extra steps.

### ✅ Accept / Reject Invitations
Invited employees can accept, decline, or ignore invitations at their own pace.

### 🤖 AI-Powered HR Email Understanding
The system uses LLMs to intelligently parse HR confirmation emails, identify employees, and resolve ambiguity.

> **Example:** `"Me and Mike connected today"` → The AI determines who sent the email and who "Mike" refers to.

### 🔍 Duplicate Name Detection
If multiple employees share a first name, the system automatically requests clarification.

> **Example:** `"We found multiple employees named Mike. Please reply using the employee's full name."`

### 📊 Automated Google Sheets Logging
All confirmed connections are automatically saved and tracked in Google Sheets.

### 📈 Analytics Dashboard
Connect Microsoft Power BI to analyze engagement rates, participation trends, department interactions, and networking patterns.

---

## 🏗️ System Architecture

![image](https://github.com/KatlegoPhoka2/Employee-Connection-Platform/blob/764b96f68ab0fc108d0ac89845160d825946f290/connectArch.png)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, FastAPI |
| **Workflow Automation** | n8n |
| **Data Storage** | Google Sheets, SQLite *(future)*, PostgreSQL *(scaling)* |
| **Email** | Gmail SMTP, yagmail *(future: SendGrid, Resend)* |
| **AI / LLM** | OpenAI API |
| **Analytics** | Microsoft Power BI |

---

## 📁 Project Structure

```
Employee-Connection-Platform/
│
├── main.py
├── recommendations.py
├── loadEmployees.py
├── sendmail.py
├── emailbody.py
├── invitations.py
│
├── workflows/
│   ├── n8n/
│   └── ai/
│
├── data/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow Overview

### 1. Employee Data Loading
Reads employee records from Google Sheets, including fields like `first_name`, `last_name`, `email`, and `department`.

### 2. Recommendation Generation
Generates 3 random connection recommendations per employee, excluding themselves, with duplicate prevention logic.

### 3. Email Distribution
Sends personalized recommendation emails with employee names, profiles, and connect action links.

### 4. Connection Initiation
When an employee clicks **Connect**, the system triggers invitation workflows, email automation, and status tracking.

### 5. HR Confirmation Workflow
After employees connect, they notify HR via a simple email (e.g., `"Me and Mike connected today"`).

### 6. AI Extraction & Validation
The AI workflow extracts names, validates against the employee database, handles duplicates, and requests clarification when needed.

### 7. Connection Storage
Validated connections are appended to Google Sheets, with future database support planned.

### 8. Analytics & Reporting
Power BI dashboards surface engagement participation, networking trends, department collaboration, and monthly activity.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A Google Sheets account with API access
- An OpenAI API key
- n8n (self-hosted or cloud)
- Gmail account for SMTP

### Installation

```bash
git clone https://github.com/your-username/Employee-Connection-Platform.git
cd Employee-Connection-Platform
pip install -r requirements.txt
```

### Configuration

Set the following environment variables:

```bash
OPENAI_API_KEY=your_openai_key
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password
GOOGLE_SHEETS_ID=your_sheet_id
```

### Run

```bash
python main.py
```

---

## 🔮 Roadmap

- [ ] **Smart AI Matching** — Recommend employees based on department, interests, and previous interactions
- [ ] **Calendar Integration** — Auto-generate Google Meet / Teams links and calendar invites
- [ ] **Slack / Teams Integration** — Deliver notifications directly in Slack or Microsoft Teams
- [ ] **Sentiment Analysis** — Measure employee engagement sentiment from interactions
- [ ] **Web Admin Dashboard** — HR dashboard for analytics, workflow monitoring, and participation tracking
- [ ] **Database Upgrade** — Migrate from Google Sheets to SQLite / PostgreSQL

---

## 💡 Use Cases

- Employee engagement programs
- Cross-team collaboration initiatives
- Remote culture building
- Internal networking for large organizations
- Onboarding integration
- Team relationship analytics

---

## 🤔 Why This Project?

Modern organizations struggle with siloed teams, remote isolation, low engagement, and weak cross-department communication. This platform automates internal networking using workflow automation, AI understanding, intelligent engagement tracking, and analytics — turning connection into a habit, not an afterthought.
