# Dealerships Review Portal - IBM Full Stack Developer Capstone Project

Welcome to the **Dealerships Review Portal**, the capstone project for the **IBM Full Stack Software Developer Professional Certificate**. This full-stack, cloud-native application connects car buyers across all 50 states with verified dealerships, allowing users to browse dealership locations, read and filter customer reviews, analyze review sentiment using natural language processing (NLP), post new reviews, and manage vehicle inventories.

---

## 🚀 Project Overview

The Dealerships Review Portal is architected as a distributed multi-tier application composed of:
1. **Frontend (React.js):** A modern, responsive single-page application (SPA) providing an interactive user interface for browsing dealerships, filtering by state, viewing reviews, and submitting new reviews with car make/model selection.
2. **Backend Web Application (Django & Python):** Handles user session management (authentication, registration, login/logout), serves static pages (`About Us`, `Contact Us`, and the landing page), manages SQLite databases via Django ORM for vehicle makes and models, and provides Django Admin tools.
3. **Database & Microservice API (Node.js & Express / MongoDB):** Serves dealership data and customer reviews stored in MongoDB documents via RESTful endpoints (`/fetchDealers`, `/fetchDealer/:id`, `/fetchReviews/dealer/:id`, `/insert_review`).
4. **Sentiment Analyzer Microservice (Python & Flask / NLTK):** Evaluates user review sentiments (positive, neutral, negative) using NLTK's `SentimentIntensityAnalyzer` (VADER) to augment customer feedback.
5. **CI/CD & Cloud Deployment:** Automated linting with `flake8` and test suites executed via **GitHub Actions**, containerized with Docker, and deployed on **IBM Cloud Code Engine**.

---

## 🛠️ Architecture & Tech Stack

```
   +------------------------------------------------------------------+
   |                     Browser / Client Device                      |
   +------------------------------------------------------------------+
                             |              ^
       HTTP / REST (Port 8000)|              | JSON Data
                             v              |
   +------------------------------------------------------------------+
   |                Django Web Application (Port 8000)                |
   |   - Django ORM (SQLite: CarMake, CarModel, Users)               |
   |   - Session Auth: /login, /logout, /register                     |
   |   - Django Admin: /admin                                         |
   |   - React Static Host & Proxy Views                              |
   +------------------------------------------------------------------+
            |                                           |
            | HTTP GET/POST                             | HTTP GET (/analyze/<text>)
            v                                           v
+-------------------------------+           +-------------------------------+
| Express / Node.js (Port 3030) |           | Flask Sentiment Analyzer (5050)|
|   - Dealerships REST API      |           |   - NLTK Vader Lexicon        |
|   - Reviews REST API          |           |   - Polarity Score Analysis   |
|   - MongoDB / Mongoose        |           |   - Positive/Neutral/Negative |
+-------------------------------+           +-------------------------------+
```

### Technologies Used:
- **Languages:** Python 3.10+, JavaScript (ES6+), HTML5, CSS3
- **Frameworks & Libraries:** Django 3.2+, React 18, Express 4.x, Flask, Mongoose, NLTK
- **Databases:** SQLite (Django relational data), MongoDB (dealerships and reviews)
- **DevOps & Cloud:** Docker, GitHub Actions CI/CD, IBM Cloud Code Engine
- **Testing & Quality:** flake8, Django test client, pytest

---

## 📋 Features

1. **Nationwide Dealership Directory:**
   - Real-time display of 50 dealerships with address, city, state, zip code, and geographic coordinates.
   - Dynamic state-based filtering (e.g., Kansas, Texas, California) without full page reloads.

2. **Verified Reviews with NLP Sentiment Analysis:**
   - View reviews with automated emotional sentiment indicators (Positive 😊, Neutral 😐, Negative 🙁).
   - Sentiment analysis powered by NLTK VADER polarity scoring.

3. **User Authentication & Management:**
   - User sign-up (Username, First Name, Last Name, Email, Password).
   - Secure login and logout with session state reflected dynamically across headers and navigation.

4. **Review Submission:**
   - Authenticated users can write and post reviews with purchase dates, car makes, car models, and model years.
   - Immediate feedback and review list refresh.

5. **Car Inventory Administration:**
   - Django Admin integration for managing `CarMake` and `CarModel` records.
   - Inline tabular editing of car models per manufacturer.

6. **Static Information Pages:**
   - Responsive `About Us` page showcasing executive leadership with realistic avatars, bios, and direct contact emails.
   - Comprehensive `Contact Us` page featuring toll-free hotlines, operating hours, headquarters address, and partnership inquiry desks.

---

## 🔌 API Endpoints Reference

### Django Backend (`http://localhost:8000`)
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/djangoapp/login` | Authenticate user credentials and start session |
| `GET` | `/djangoapp/logout` | Terminate user session |
| `POST` | `/djangoapp/register` | Register new user account |
| `GET` | `/djangoapp/get_cars` | Retrieve all car makes and models |
| `GET` | `/djangoapp/get_dealers` | Fetch all dealerships |
| `GET` | `/djangoapp/get_dealers/<state>` | Filter dealerships by state |
| `GET` | `/djangoapp/dealer/<dealer_id>` | Fetch dealership details by ID |
| `GET` | `/djangoapp/reviews/dealer/<dealer_id>` | Fetch dealer reviews with sentiment tags |
| `POST` | `/djangoapp/add_review` | Submit a new customer review |

### Express / MongoDB Backend (`http://localhost:3030`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/fetchDealers` | Fetch all dealership documents |
| `GET` | `/fetchDealers/:state` | Fetch dealerships located in specified state |
| `GET` | `/fetchDealer/:id` | Fetch single dealership by numerical ID |
| `GET` | `/fetchReviews` | Fetch all customer reviews |
| `GET` | `/fetchReviews/dealer/:id` | Fetch customer reviews for a dealer ID |
| `POST` | `/insert_review` | Insert a new review document |

### Sentiment Analyzer Microservice (`http://localhost:5050`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/analyze/<input_txt>` | Analyze text string and return JSON sentiment classification |

---

## 💻 Local Setup & Execution Guide

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm
- Git

### 1. Clone Repository
```bash
git clone https://github.com/daliyakaran1-alt/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone
```

### 2. Set Up Python Environment & Django Backend
```bash
cd server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python -c "from djangoapp.populate import initiate; initiate()"
```

### 3. Build Frontend Assets
```bash
cd frontend
npm install --legacy-peer-deps
npm run build
cd ..
```

### 4. Start Microservices & Development Servers
In separate terminal windows:
```bash
# Terminal 1: Database & Express Backend
cd server/database
npm install
node app.js

# Terminal 2: Sentiment Analyzer Microservice
python server/djangoapp/microservices/app.py

# Terminal 3: Django Development Server
cd server
python manage.py runserver 8000
```

---

## 🧪 CI/CD Pipeline

The project incorporates continuous integration via **GitHub Actions** (`.github/workflows/main.yml`):
- Automated checkout and Python environment setup
- Dependency installation
- Code quality and PEP 8 enforcement with `flake8`
- Django migration and system validation (`python manage.py check`)

---

## 🌐 Live Deployment

- **Application URL:** [https://dealerships-capstone.1a8b3c9d7e.us-south.codeengine.appdomain.cloud](https://dealerships-capstone.1a8b3c9d7e.us-south.codeengine.appdomain.cloud)
- **Deployment Platform:** IBM Cloud Code Engine (Kubernetes-based container runtime)

---

## 👤 Author

- **GitHub:** [@daliyakaran1-alt](https://github.com/daliyakaran1-alt)
- **Course:** IBM Full Stack Software Developer Capstone Project
