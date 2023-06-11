"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программане должна быть линейной
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.
"""

#functions
def db_read():
    with open (database_path, 'r') as database:
        database.seek(0, 0)
        return database.readlines()

def db_search():
    searchText = input("Введите фамилию, имя, отчество или телефон для поиска: ").lower()
    dbRead = db_read()
    for i, line in enumerate(dbRead):
        if searchText in line.lower():
            displayLine = line.replace('\n','')
            print(f"Найден искомый текст \"{searchText}\" в строке {i+1}: {displayLine}")

def db_create():        
    with open (database_path, 'a') as database:
        name = input("Введите ФИО новой записи: ")
        phone = input("Введите телефон новой записи: ")
        database.write(f"{name.ljust(16)}\t{phone}\n")
        print(f"Добавлена строка: {name}\t{phone}")

def db_update():
    dbRead = db_read()
    db_print(dbRead)
    delteItem = int(input("\nВведите номер изменяемой строки: "))
    newName = input("Введите новое ФИО: ")
    newPhone = input("Введите новый телефон: ")
    with open (database_path, 'w') as database:
        for i, line in enumerate(dbRead):
            if i + 1 == delteItem:
                database.write(f"{newName.ljust(16)}\t{newPhone}\n")
            else:
                database.write(line)
    print(f"Строка {delteItem} изменена")

def db_delete():
    dbRead = db_read()
    db_print(dbRead)
    delteItem = int(input("\nВведите номер удалямой строки: "))
    with open (database_path, 'w') as database:
        for i, line in enumerate(dbRead):
            if i + 1 != delteItem:
                database.write(line)
    print(f"Строка {delteItem} удалена")
    
def db_print(dbPrint):
    print("№ ФИО Телефон")
    for index, line in enumerate(dbPrint):
        print(f"{index+1} {line}", end="")

def menu_display():
    print("1 - вывести данные, 2 - поиск по имени и фамилии, 3 - добавить строку, 4 - изменить строку, 5 - удалить строку, 0 - выйти из программы")
    menu_select(int(input("Введите пункт меню: ")))
    print()

def menu_select(i):
    print()
    if i == 0:
        global isRunning
        isRunning = False            
    elif i == 1:
        db_print(db_read())
    elif i == 2:
        db_search()
    elif i == 3:
        db_create()        
    elif i == 4:
        db_update()
    elif i == 5:
        db_delete()
    else:
        print("Ошибка ввода")

#main
database_path = 'Homework08/database.txt'
isRunning = True
while isRunning:
    menu_display()
print("Завершение работы...")
