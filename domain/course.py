from domain.category import categories_dict
from domain.consultant import consultants_dict
from domain import Image,Media

class Course:
    def __init__(self, name, categories, image, media, cons, rating, num_of_sales, price, description, posted_on, final_exam, add_ons):
        self.name = name
        self.categories = categories
        self.image = image
        self.media = media
        self.cons = cons
        self.rating = rating
        self.num_of_sales = num_of_sales
        self.price = price
        self.description = description
        self.posted_on = posted_on
        self.final_exam = final_exam
        self.add_ons = add_ons

# Sample instances
course1 = Course(
    name="Introduction to Python Programming",
    categories=[categories_dict["Computer Science"].name],
    image=Image(200,200,"Temp Courses/python.png"),
    media=Media(2),
    cons=consultants_dict["Alice"],
    rating=4.5,
    num_of_sales=1000,
    price=49.99,
    description="An introduction to programming and python",
    posted_on="2024-05-01",
    final_exam="Graded assignment",
    add_ons="Certificate of Completion"
)

course2 = Course(
    name="Mastering the Fundamentals of Business Models",
    categories=[categories_dict["Business"].name],
    image=Image(200,200,"Temp Courses/business.png"),
    media=Media(2),
    cons=consultants_dict["Bob"],
    rating=4.0,
    num_of_sales=500,
    price=29.99,
    description="Learning the basics in business",
    posted_on="2024-04-25",
    final_exam="Graded assignment",
    add_ons="Quizzes and Assignments"
)

course3 = Course(
    name="Foundations of Mathematical Thinking",
    categories=[categories_dict["Mathematics"].name],
    image=Image(200,200,"Temp Courses/math.png"),
    media=Media(2),
    cons=consultants_dict["Charlie"],
    rating=3.7,
    num_of_sales=800,
    price=69.99,
    description="Master the foundations of mathematical reasoning",
    posted_on="2024-05-10",
    final_exam="Graded assignment",
    add_ons="Math Challenges and Solutions"
)

course4 = Course(
    name="Exploring the World of Materials Science: From Basics to Applications",
    categories=[categories_dict["Materials Science"].name],
    image=Image(200,200,"Temp Courses/material.png"),
    media=Media(2),
    cons=consultants_dict["David"],
    rating=4.2,
    num_of_sales=300,
    price=59.99,
    description="An introduction to the science of materials.",
    posted_on="2024-04-20",
    final_exam="Graded assignment",
    add_ons="Laboratory Assignments and Solutions"
)

course5 = Course(
    name="Understanding Statistics",
    categories=[categories_dict["Statistics"].name],
    image=Image(200,200,"Temp Courses/statistics.png"),
    media=Media(1),
    cons=consultants_dict["Eva"],
    rating=4.6,
    num_of_sales=1200,
    price=79.99,
    description="Become an expert at statistics with just a few lessons",
    posted_on="2024-04-28",
    final_exam="Graded assignment",
    add_ons="Real-world Projects and Solutions"
)

courses_dict = {
    "course1": course1,
    "course2": course2,
    "course3": course3,
    "course4": course4,
    "course5": course5
}

