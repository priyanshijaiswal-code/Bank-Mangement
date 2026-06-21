import streamlit as st
import json
import random
import string
from pathlib import Path

DATABASE = "data1.json"


# -----------------------------
# Data Handling
# -----------------------------
def load_data():
    if Path(DATABASE).exists():
        try:
            with open(DATABASE, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_data(data):
    with open(DATABASE, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# Account Number Generator
# -----------------------------
def generate_account_number():
    while True:
        acc = "".join(
            random.choices(string.ascii_uppercase, k=3)
            + random.choices(string.digits, k=5)
        )

        data = load_data()

        if not any(user["account_no"] == acc for user in data):
            return acc


# -----------------------------
# Create Account
# -----------------------------
def create_account(name, age, email, pin):
    data = load_data()

    account = {
        "name": name,
        "age": age,
        "email": email,
        "pin": pin,
        "account_no": generate_account_number(),
        "balance": 0,
        "transactions": []
    }

    data.append(account)
    save_data(data)

    return account


# -----------------------------
# Find User
# -----------------------------
def find_user(account_no, pin):
    data = load_data()

    for user in data:
        if user["account_no"] == account_no and user["pin"] == pin:
            return user

    return None


# -----------------------------
# Deposit
# -----------------------------
def deposit(account_no, pin, amount):
    data = load_data()

    for user in data:
        if user["account_no"] == account_no and user["pin"] == pin:
            user["balance"] += amount

            user["transactions"].append(
                f"Deposited ₹{amount}"
            )

            save_data(data)
            return True

    return False


# -----------------------------
# Withdraw
# -----------------------------
def withdraw(account_no, pin, amount):
    data = load_data()

    for user in data:
        if user["account_no"] == account_no and user["pin"] == pin:

            if user["balance"] < amount:
                return "Insufficient Balance"

            user["balance"] -= amount

            user["transactions"].append(
                f"Withdrawn ₹{amount}"
            )

            save_data(data)
            return "Success"

    return "User Not Found"


# -----------------------------
# Update User
# -----------------------------
def update_user(account_no, pin, name, email, new_pin):
    data = load_data()

    for user in data:
        if user["account_no"] == account_no and user["pin"] == pin:

            if name:
                user["name"] = name

            if email:
                user["email"] = email

            if new_pin:
                user["pin"] = new_pin

            save_data(data)
            return True

    return False


# -----------------------------
# Delete Account
# -----------------------------
def delete_account(account_no, pin):
    data = load_data()

    for user in data:
        if user["account_no"] == account_no and user["pin"] == pin:
            data.remove(user)
            save_data(data)
            return True

    return False


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏦 Banking Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)

# Create Account
if menu == "Create Account":

    st.header("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create"):

        if len(pin) != 4:
            st.error("PIN must be 4 digits")

        else:
            account = create_account(
                name,
                age,
                email,
                pin
            )

            st.success("Account Created Successfully")

            st.write("Account Number:")
            st.code(account["account_no"])


# Deposit
elif menu == "Deposit":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if deposit(acc, pin, amount):
            st.success("Money Deposited")
        else:
            st.error("Invalid Credentials")


# Withdraw
elif menu == "Withdraw":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):

        result = withdraw(acc, pin, amount)

        if result == "Success":
            st.success("Money Withdrawn")

        elif result == "Insufficient Balance":
            st.error("Insufficient Balance")

        else:
            st.error("Invalid Credentials")


# Show Details
elif menu == "Show Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):

        user = find_user(acc, pin)

        if user:

            st.subheader("Account Details")

            st.write(f"Name: {user['name']}")
            st.write(f"Age: {user['age']}")
            st.write(f"Email: {user['email']}")
            st.write(f"Balance: ₹{user['balance']}")

            st.subheader("Transaction History")

            for transaction in user["transactions"]:
                st.write(transaction)

        else:
            st.error("User Not Found")


# Update
elif menu == "Update Details":

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN", type="password")

    if st.button("Update"):

        if update_user(
            acc,
            pin,
            new_name,
            new_email,
            new_pin
        ):
            st.success("Details Updated")
        else:
            st.error("Invalid Credentials")


# Delete
elif menu == "Delete Account":

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        if delete_account(acc, pin):
            st.success("Account Deleted")
        else:
            st.error("Invalid Credentials")