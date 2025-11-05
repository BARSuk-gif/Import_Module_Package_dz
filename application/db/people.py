
# Получать данные о сотруднике предполагаю что нужно из базы данных организации
conn = sql.connect('tabel.db')
cursor = conn.cursor()

class Employee:
    def __init__(self, id, full_name, post):
        self.id = id
        self.full_name = full_name     # ФИО
        self.post = post               # должность

    # оклад
    def get_salary_scale(self):
        cursor.execute("SELECT * FROM tabel")
        salary_scale = cursor.fetchone()
        return salary_scale
    
    # премия, % от оклада
    def get_bonus(self):
        cursor.execute("SELECT * FROM tabel")
        bonus = cursor.fetchone()
        return bonus
    
    # количество детей до 18 лет для налогового вычета (если нет, то 0)
    def get_num_of_children(self):
        cursor.execute("SELECT * FROM tabel")
        num_of_children = cursor.fetchone()
        return num_of_children
    
    # количество детей-инвалидов до 18 лет для налогового вычета (если нет, то 0)
    def get_disabled_children(self):
        cursor.execute("SELECT * FROM tabel")
        disabled_children = cursor.fetchone()
        return disabled_children
    
        # количество отработанных дней в месяце
    def get_working_days_f(self):
        cursor.execute("SELECT * FROM tabel")
        working_days_f = cursor.fetchone()
        return working_days_f
        
if __name__ == '__main__':
    
    empl = Employee(5, "Иван Иванович Иванов", "экономист")
    
 

