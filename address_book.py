from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
 

class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def valid_phone(self, phone):
        if len(phone) != 10 or phone.isdigit() == False:
            print("\033[31m{}\033[0m".format("The number must consist of 10 digits. try again"))
        else:
            return phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if Phone(phone).valid_phone(phone):
            self.phones.append(Phone(phone))
   
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def edit_phone(self, old_phone, new_phone):
        if Phone(new_phone).valid_phone(new_phone):
            for p in self.phones:
                if p.value == old_phone:
                    p.value = new_phone


class AddressBook(UserDict):    
    def __init__(self):
        self.data = UserDict()
    
    def add_record (self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for cont in self.data:
            if str(cont) == name:
                return self.data.get(cont)
       
    def delete(self, name):
        cont_for_del=""
        for cont in self.data:
            if str(cont) == name:
                cont_for_del = cont             
        self.data.pop(cont_for_del)
                 
            
if __name__ == '__main__':

    book = AddressBook()
    rec = Record("Bill")
    print(rec)
    rec.add_phone("1234567890")
    rec.add_phone("1111111111")
    rec.add_phone("2222222222")
    print(rec)
    rec.remove_phone("1111111111")
    print(rec)
    found_phone = rec.find_phone("1234567890")
    print(f"{rec.name}: {found_phone}")
    rec.edit_phone("1234567890","0987654321")
    print(rec)
    book.add_record(rec)
    rec1=Record("Sofi")
    rec1.add_phone("3333333333")
    rec1.add_phone("4444444444")
    rec1.add_phone("5555555555")
    rec1.edit_phone("5555555555","5555555551")
    rec1.remove_phone("5555555551")
    book.add_record(rec1)
    john = book.find("Bill")
    print("johnjohnjohnjohnjohn",john)
    john.edit_phone("0987654321", "1234567890")
    print("johnjohnjohnjohnjohn",john)
    for name, record in book.data.items():
        print("AddressBook:   ",record)
    book.delete("Sofi")
    for name, record in book.data.items():
        print("AddressBook:   ",record)

   





