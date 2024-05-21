from domain.category import categories_dict
from domain.image import Image
from domain.user import User
from domain.client import Client
from domain.consultant_schedule import schedule1




class Consultant(Client):
    # for showcasing purposes
    id_count = 0

    def __init__(self, name, photo, categories, education, experience, rate, schedule, bank_details):

        super().__init__(id=Consultant.id_count, name=name)
        Consultant.id_count += 1

        self.photo = photo
        self.categories = categories
        self.education = education
        self.experience = experience
        self.rate = rate
        self.schedule = schedule
        self.bank_details = bank_details


# Sample consultant data
consultant1 = Consultant(
    name="Alice",
    photo=Image(286,286,"Temp photos/Alice.png"),
    categories=[categories_dict["Computer Science"].name],
    education="PhD in Computer Science",
    experience="10 years",
    rate=150.00,
    schedule=schedule1, #To-do
    bank_details=("Alice Smith", "IBAN1111111111")
)

consultant2 = Consultant(
    name="Bob",
    photo=Image(286,286,"Temp photos/Bob.png"),
    categories=[categories_dict["Business"].name],
    education="Master of Business Administration",
    experience="8 years",
    rate=120.00,
    schedule=None,
    bank_details=("Bob Johnson", "IBAN2222222222")
)

consultant3 = Consultant(
    name="Charlie",
    photo=Image(286,286,"Temp photos/Charlie.png"),
    categories=[categories_dict["Mathematics"].name],
    education="Bachelor of Mathematics",
    experience="6 years",
    rate=100.00,
    schedule=None,
    bank_details=("Charlie Brown", "IBAN3333333333")
    )

consultant4 = Consultant(
    name="David",
    photo=Image(286,286,"Temp photos/David.png"),
    categories=[categories_dict["Engineering"].name,categories_dict["Materials Science"].name],
    education="Master of Engineering",
    experience="7 years",
    rate=135.00,
    schedule=None,
    bank_details=("David Lee", "IBAN4444444444")
)

consultant5 = Consultant(
    name="Eva",
    photo=Image(286,286,"Temp photos/Eva.png"),
    categories=[categories_dict["Economics"].name,categories_dict["Statistics"].name],
    education="Bachelor of Science in Economics",
    experience="9 years",
    rate=160.00,
    schedule=None,
    bank_details=("Eva Green", "IBAN5555555555")
)


# Creating a consultant dictionary
consultants_dict = {
    "Alice": consultant1,
    "Bob": consultant2,
    "Charlie": consultant3,
    "David": consultant4,
    "Eva": consultant5
}
        
        


CURRENT_USER = consultants_dict["Eva"]