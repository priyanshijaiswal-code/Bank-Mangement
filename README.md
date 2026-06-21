# 🏦 Banking Management System

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bg2t5pbzn7vkbgmmytfuh5.streamlit.app/)

A Python-based Banking Management System containing both a graphical web interface (built with Streamlit) and a command-line interface (CLI).

## Live Demo
You can try out the live web application here:
🔗 **[https://bg2t5pbzn7vkbgmmytfuh5.streamlit.app/](https://bg2t5pbzn7vkbgmmytfuh5.streamlit.app/)**

## Features
- **Create Account**: Generates a unique account number after validating user details (age, pin).
- **Deposit Money**: Deposit funds into a specific account.
- **Withdraw Money**: Withdraw funds with balance validation.
- **Show Details**: Display account information along with transaction history.
- **Update Details**: Modify account information (Name, Email, PIN).
- **Delete Account**: Close and remove an account from the system.

## Project Structure
- `app.py`: Streamlit-based web interface.
- `main.py`: Command Line Interface (CLI) application.
- `data.json`: CLI application local database (ignored in git).
- `data1.json`: Streamlit application local database (ignored in git).

## Setup & Running

### Prerequisites
Make sure you have Python installed on your system.

### Install Dependencies
To run the Streamlit app, you will need to install Streamlit:
```bash
pip install streamlit
```

### Running the Applications

#### 1. Web Application (Streamlit)
To run the Streamlit interface, run:
```bash
streamlit run app.py
```

#### 2. CLI Application
To run the CLI application, run:
```bash
python main.py
```
