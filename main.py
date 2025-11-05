
import datetime
import requests
import netologi.Import_Module_Package.application.db.people as people
import netologi.Import_Module_Package.application.salary as salary


if __name__ == '__main__':
    # Создаем объект сотрудника
    employee = people.Employee(1, "Иван Иванов", "экономист")

    # Расчет зарплаты (22 - рабочих дней в месяце)
    salary_result = salary.calculate_salary(employee, 22)

    print(
        f"Для {employee} начислена зарплата: {salary_result['final_salary']:.2f} руб.")
    print(f"Дата: {datetime.date.today()}")
