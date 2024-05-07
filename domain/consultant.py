from domain.category import categories_dict
from domain.image import Image

class Consultant:
    def __init__(self, name, photo, categories, education, experience, rate, schedule, bank_details):
        self.name = name
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
    categories=categories_dict["Computer Science"],
    education="PhD in Computer Science",
    experience="10 years",
    rate=150.00,
    schedule=None, #To-do
    bank_details=("Alice Smith", "IBAN1111111111")
)

consultant2 = Consultant(
    name="Bob",
    photo=Image(286,286,"Temp photos/Bob.png"),
    categories=categories_dict["Business"],
    education="Master of Business Administration",
    experience="8 years",
    rate=120.00,
    schedule=None,
    bank_details=("Bob Johnson", "IBAN2222222222")
)

consultant3 = Consultant(
    name="Charlie",
    photo=Image(286,286,"Temp photos/Charlie.png"),
    categories=categories_dict["Mathematics"],
    education="Bachelor of Mathematics",
    experience="6 years",
    rate=100.00,
    schedule=None,
    bank_details=("Charlie Brown", "IBAN3333333333")
    )

consultant4 = Consultant(
    name="David",
    photo=Image(286,286,"Temp photos/David.png"),
    categories=[categories_dict["Engineering"],categories_dict["Materials Science"]],
    education="Master of Engineering",
    experience="7 years",
    rate=135.00,
    schedule=None,
    bank_details=("David Lee", "IBAN4444444444")
)

consultant5 = Consultant(
    name="Eva",
    photo=Image(286,286,"Temp photos/Eva.png"),
    categories=[categories_dict["Economics"],categories_dict["Statistics"]],
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
        
        

