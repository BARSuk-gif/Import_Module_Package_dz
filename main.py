
import datetime
import requests
from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    get_employees("У Иван Иваныча")
    calculate_salary("большая")
    print(f"Дата: {datetime.date.today()}")
