import sqlite3

COUNT_OF_CURRENCIES = 31

CONNECTION = sqlite3.connect("accounts_db.db")

CURSOR = CONNECTION.cursor()

ID = None

EXPENDITURE = None

INCOME = None