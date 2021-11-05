import sqlite3

COUNT_OF_CURRENCIES = 31

CONNECTION = sqlite3.connect("accounts_db.db")

CURSOR = CONNECTION.cursor()
#
# FREQUENCY_IN_TIME = {"Каждый день": datetime.timedelta(days=1),
#                      "Каждый месяц": relativedelta(months=1)}
