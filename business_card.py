from faker import Faker

class BaseContact:
    def __init__(self, imie, nazwisko, email, private_phone):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.private_phone = private_phone

    def contact(self):
        print(f"Wybieram numer prywatny {self.private_phone} i dzwonię do {self.imie} {self.nazwisko}.")
    
    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, email, private_phone, firma, stanowisko, business_phone):
        
        super().__init__(imie, nazwisko, email, private_phone)
        self.firma = firma
        self.stanowisko = stanowisko
        self.business_phone = business_phone

    
    def contact(self):
        print(f"Wybieram numer służbowy {self.business_phone} i dzwonię do {self.imie} {self.nazwisko}.")


fake = Faker()

def create_contacts(contact_type, count):
    contacts = []
    for _ in range(count):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        email = fake.email()
        private_phone = fake.phone_number()

        if contact_type == 'business':
            firma = fake.company()
            stanowisko = fake.job()
            business_phone = fake.phone_number()
            contact = BusinessContact(imie, nazwisko, email, private_phone, firma, stanowisko, business_phone)
        else:
            contact = BaseContact(imie, nazwisko, email, private_phone)
        
        contacts.append(contact)
    
    return contacts

if __name__ == "__main__":

    print("Wizytówki firmowe:")
    business_contacts = create_contacts('business', 3)
    for contact in business_contacts:
        contact.contact()
        print(f"Długość etykiety: {contact.label_length}\n")

    print("Wizytówki bazowe:")
    base_contacts = create_contacts('base', 2)
    for contact in base_contacts:
        contact.contact()
        print(f"Długość etykiety: {contact.label_length}\n")


