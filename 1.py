from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search_records(self, **criteria):
        results = []
        for record in self.values():
            match = all(getattr(record, key).value == value for key, value in criteria.items())
            if match:
                results.append(record)
        return results
# Створюємо записи та адресну книгу
record1 = Record("John Doe")
record1.add_phone("123-456-7890")

record2 = Record("Jane Doe")
record2.add_phone("987-654-3210")

address_book = AddressBook()

# Додаємо записи в адресну книгу
address_book.add_record(record1)
address_book.add_record(record2)

# Пошук записів за критеріями
search_results = address_book.search_records(name="John Doe")
for result in search_results:
    print(f"Name: {result.name.value}, Phones: {[phone.value for phone in result.phones]}")





