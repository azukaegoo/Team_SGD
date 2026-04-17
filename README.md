# One Button App

A simple Flask-based web application .  
The app demonstrates a minimal full-stack setup where a single button click is stored in a PostgreSQL database.

The project is containerized using Docker and includes testing, CI integration, and a clean modular structure.

---

## 📌 Project Overview

This application follows a standard Flask architecture using an application factory pattern.

When a user clicks a button on the homepage:
- A POST request is sent to the backend
- A database record is created
- A success or error message is displayed

This project demonstrates:
- Backend development with Flask
- Database integration with PostgreSQL
- Containerized development using Docker
- Testing and CI workflows

---

##  Features

- Single-button interaction (core functionality)
- Database persistence of button clicks
- Flash messages for feedback
- Docker-based environment setup
- Automated testing using `pytest`
- Continuous Integration with GitHub Actions

---

## Tech Stack

- **Backend:** Flask
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (Flask-SQLAlchemy)
- **Migrations:** Flask-Migrate
- **Testing:** pytest
- **Environment Variables:** python-dotenv
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions

---

---

## How It Works

1. User opens the homepage
2. Clicks the **"Click Me"** button
3. A POST request is sent to the `/submit` route
4. Backend:
   - Creates a new database entry (`OneAppButton`)
   - Saves the timestamp
5. Result:
   - Success → confirmation message
   - Failure → rollback + error message

---

## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone repository
cd Team_SGD
```
### 2. Setting environment variable
```bash
cp .env_sample .env
```
### 3. Run with Docker
```bash
docker compose up --build
```
### 4. Open Application
```bash
http://localhost:5000
```


## Development Setup and AI Collaboration

### System Setup

Our application is built using **Flask** with **SQLAlchemy** and runs in a containerized environment using **Docker Compose**.

The system consists of:
- **web container** → Flask application
- **db container** → PostgreSQL database

Development is carried out in:
- Local Docker environments
- GitHub Codespaces (container-based)




### Team Roles

#### Human Members
- Design system architecture
- Implement and integrate features
- Review and test all code before merging
- Manage GitHub branches and pull requests

#### AI Assistance
- Assists with debugging errors (e.g., Docker, database issues)
- Explains concepts when needed
- Suggests improvements or alternative implementations
- Help generate tests when needed

AI is used as a development assistant, while all final decisions remain with the team.


### Ensuring Correct Direction

To ensure the project stays aligned:

- The team agrees on architecture and design decisions before implementation

- GitHub is used for:
  - version control
  - pull requests
  - tracking changes

- Code reviews ensure consistency and correctness
- Testing (`pytest`) is used to validate functionality

