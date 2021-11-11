from CONSTANTS import *
import CONSTANTS


def get_amount():
    return CURSOR.execute("""SELECT amount FROM details WHERE detailId = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def get_detailId():
    return CURSOR.execute("""SELECT detailId FROM details WHERE detailId = ?""", (CONSTANTS.ID,)).fetchall()


def get_income():
    return CURSOR.execute("""SELECT income FROM details WHERE detailId = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def get_expenditure():
    return CURSOR.execute("""SELECT expenditure FROM details WHERE detailId = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def add_detailId():
    return CURSOR.execute("""INSERT INTO details (detailId) VALUES(?)""", (CONSTANTS.ID,))


def get_name():
    return CURSOR.execute("""SELECT name FROM details WHERE detailId = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def set_name(values):
    return CURSOR.execute("""UPDATE details SET name = ? WHERE detailId = ?""", values)


def set_amount(values):
    return CURSOR.execute("""UPDATE details SET amount = ? WHERE detailId = ?""", values)


def set_description(values):
    return CURSOR.execute("""UPDATE accounts SET description = ? WHERE id = ?""", values)


def get_description():
    return CURSOR.execute("""SELECT description FROM accounts WHERE id = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def del_regular_payment(values):
    return CURSOR.execute("""DELETE FROM payment_details
                                WHERE name = ?""", values)


def get_exp_data():
    return CURSOR.execute("""SELECT * FROM expenditures WHERE expenditureId = ?""",
                          (CONSTANTS.ID,)).fetchall()


def get_inc_data():
    return CURSOR.execute("""SELECT * FROM incomes WHERE incomeId = ?""",
                          (CONSTANTS.ID,)).fetchall()


def get_total_exp():
    return CURSOR.execute("""SELECT expenditure FROM details WHERE detailId = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def get_total_inc():
    return CURSOR.execute("""SELECT income FROM details WHERE detailId = ?""",
                          (CONSTANTS.ID,)).fetchone()[0]


def add_exp(values):
    return CURSOR.execute("""INSERT INTO expenditures(expenditureId, amount, category) VALUES(?, ?, ?)""",
                          values)


def add_inc(values):
    return CURSOR.execute("""INSERT INTO incomes(incomeId, amount, category) VALUES(?, ?, ?)""", values)


def update_exp(values):
    return CURSOR.execute("""UPDATE expenditures 
                                  SET amount = amount + ?
                                  WHERE category = ?""", values)


def update_inc(values):
    return CURSOR.execute("""UPDATE incomes 
                                  SET amount = amount + ?
                                  WHERE category = ?""", values)


def update_total_exp(values):
    return CURSOR.execute("""UPDATE details
                              SET expenditure = expenditure + ?
                              WHERE detailId = ?""", values)


def update_total_inc(values):
    return CURSOR.execute("""UPDATE details
                                SET income = income + ?
                                WHERE detailId = ?""", values)


def deduct_from_balance(values):
    return CURSOR.execute("""UPDATE details SET amount = amount - ?
                                WHERE detailId = ?""", values)


def add_to_balance(values):
    return CURSOR.execute("""UPDATE details SET amount = amount + ?
                                            WHERE detailId = ?""", values)


def get_payment_details():
    return CURSOR.execute(f"""SELECT name, category, amount, date
                                FROM payment_details 
                                WHERE paymentId = {CONSTANTS.ID}""").fetchall()


def save_payment(values):
    return CURSOR.execute("""INSERT INTO payment_details(paymentId, amount, category, 
                                type, name, date, frequency) 
                                VALUES(?, ?, ?, ?, ?, ?, ?)""", values)


def get_all_payments():
    return CURSOR.execute("""SELECT date, amount, type, frequency, name, category FROM payment_details 
                                WHERE paymentId = ?""", (CONSTANTS.ID,)).fetchall()


def update_payment_date(values):
    CURSOR.execute("""UPDATE payment_details SET date = ?
                        WHERE name = ?""", values)
