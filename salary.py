from people import Employee


# working_days - количество рабочих дней в месяце
def calculate_salary(working_days):
    # зарплата по количествы отработанных дней 
    salary_full = (
        Employee.get_salary_scale + Employee.get_salary_scale * Employee.get_bonus /100) / working_days * Employee.get_working_days_f

    # Сумма налоговых вычетов CV
    # налог на доходы физлиц составляет 13%
    n = Employee.get_num_of_children          # количество детей
    nd = Employee.get_disabled_children       # количество детей-инвалидов
    if n <=2:
        Cn = n * 1400
    else:
        Cn = 2*1400 + (n - 2)*3000
    
    CV = Cn + nd * 12000   # налоговый вычет на детей в том числе на детей-инвалидов (если есть)

    # налог на доходы физлиц составляет 13%
    NDFL = (salary_full - CV) * 0.13

    # сотруднику будет выплачена зарплата
    salary_n = salary_full - NDFL

    # Минимальный размер оплаты труда (МРОТ) 22400
    if salary_n <=22400:
        salary = 22400
    else:
        salary = salary_n

if __name__ == '__main__':
    # Пример использования
    emp = Employee(1, "Тест", "Должность")
    result = calculate_salary(emp, 22)
   
