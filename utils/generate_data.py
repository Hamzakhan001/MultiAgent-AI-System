import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

# --- Create Tables ---
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerId INTEGER PRIMARY KEY,
    FirstName TEXT, LastName TEXT,
    Email TEXT, Phone TEXT, City TEXT
);
CREATE TABLE IF NOT EXISTS Accounts (
    AccountId INTEGER PRIMARY KEY,
    CustomerId INTEGER,
    AccountType TEXT,  -- e.g. Savings, Current, ISA
    Balance REAL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionId INTEGER PRIMARY KEY,
    AccountId INTEGER,
    Date TEXT,
    Amount REAL,
    Type TEXT,         -- Credit / Debit
    Description TEXT,
    FOREIGN KEY (AccountId) REFERENCES Accounts(AccountId)
);
CREATE TABLE IF NOT EXISTS Loans (
    LoanId INTEGER PRIMARY KEY,
    CustomerId INTEGER,
    LoanType TEXT,     -- Personal, Mortgage, Car
    Amount REAL,
    Status TEXT,       -- Active, Closed, Pending
    InterestRate REAL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);
CREATE TABLE IF NOT EXISTS Products (
    ProductId INTEGER PRIMARY KEY,
    Name TEXT,
    Category TEXT,     -- Savings, Loan, Card
    InterestRate REAL,
    Description TEXT
);
""")

# --- Seed Data ---
for i in range(1, 51):  # 50 customers
    cursor.execute("INSERT INTO Customers VALUES (?,?,?,?,?,?)",
        (i, fake.first_name(), fake.last_name(),
         fake.email(), fake.phone_number(), fake.city()))

account_types = ["Savings", "Current", "ISA"]
for i in range(1, 51):
    cursor.execute("INSERT INTO Accounts VALUES (?,?,?,?)",
        (i, i, random.choice(account_types), round(random.uniform(100, 50000), 2)))

tx_types = ["Credit", "Debit"]
descs = ["Direct Debit", "Salary", "ATM Withdrawal", "Online Transfer", "Card Payment"]
for i in range(1, 201):  # 200 transactions
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO Transactions VALUES (?,?,?,?,?,?)",
        (i, random.randint(1, 50), date,
         round(random.uniform(5, 3000), 2),
         random.choice(tx_types), random.choice(descs)))

loan_types = ["Personal", "Mortgage", "Car Loan"]
statuses = ["Active", "Closed", "Pending"]
for i in range(1, 31):  # 30 loans
    cursor.execute("INSERT INTO Loans VALUES (?,?,?,?,?,?)",
        (i, random.randint(1, 50),
         random.choice(loan_types),
         round(random.uniform(1000, 250000), 2),
         random.choice(statuses),
         round(random.uniform(2.5, 15.0), 2)))

products = [
    (1, "FlexSaver Account", "Savings", 4.5, "Easy access savings with competitive rate"),
    (2, "Personal Loan", "Loan", 6.9, "Unsecured personal loan up to £25,000"),
    (3, "Platinum Credit Card", "Card", 19.9, "Rewards card with 0% intro APR for 12 months"),
    (4, "Help to Buy ISA", "Savings", 3.5, "Government-backed ISA for first-time buyers"),
    (5, "Car Finance", "Loan", 5.4, "Flexible car loan with fixed monthly payments"),
]
cursor.executemany("INSERT INTO Products VALUES (?,?,?,?,?)", products)

conn.commit()
conn.close()
print("banking.db created successfully!")