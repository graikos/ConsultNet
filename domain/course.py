from domain.category import categories_dict
from domain.consultant import consultants_dict
from domain import Image,Media
from .add_on import AddOn

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
    description="An essential course designed to familiarize beginners with the fundamentals of Python, a versatile and widely-used programming language. Whether you're completely new to coding or transitioning from another language, this course provides a solid foundation in Python syntax, data types, and control structures. Through hands-on projects and practical exercises, you'll learn how to write Python code to solve real-world problems, manipulate data, and automate tasks. From variables and operators to loops and functions, each concept is explained in a clear and approachable manner, making it easy to understand for learners of all levels. By the end of the course, you'll have gained the confidence and skills to start writing your own Python programs and embark on a journey towards becoming a proficient Python developer. Whether you're interested in web development, data science, or software engineering, this course is the perfect starting point for your Python programming journey.",
    posted_on="2024-05-01",
    final_exam="Graded assignment",
    add_ons=[AddOn("Certificate of Completion", 5, None)]
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
    description="Mastering the Fundamentals of Business Models is an immersive course designed to equip learners with essential knowledge and skills vital for navigating the intricate world of business. Delve into the core principles of business models, exploring their significance, components, and the dynamic strategies behind them. Through comprehensive modules, uncover the intricacies of market analysis, revenue streams, cost structures, and value propositions. Gain insights into crafting robust business models tailored to diverse industries and market demands. With practical case studies and interactive learning tools, this course empowers individuals to conceptualize, develop, and refine innovative business models, setting a solid foundation for success in today's competitive global landscape.",
    posted_on="2024-04-25",
    final_exam="Graded assignment",
    add_ons=[AddOn("Quizzes and Assignments", 5, None)]
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
    description="A comprehensive course designed to develop critical thinking skills and deepen understanding of core mathematical concepts. Through engaging lectures and interactive exercises, this course explores fundamental principles such as logic, sets, functions, and proofs. You'll learn how to approach mathematical problems systematically, analyze patterns, and construct logical arguments. By honing your problem-solving abilities and mathematical reasoning, you'll gain confidence in tackling complex problems across various disciplines. Whether you're a student preparing for higher-level math courses or a professional seeking to enhance your analytical skills, this course provides a solid foundation for success in mathematics and beyond. Join us on a journey to unlock the power of mathematical thinking and discover its applications in everyday life and advanced fields of study",
    posted_on="2024-05-10",
    final_exam="Graded assignment",
    add_ons=[AddOn("Math Challenges and Solutions", 5, None)]
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
    description="Exploring the World of Materials Science: From Basics to Applications is a captivating journey through the intricate realm of materials science, from its fundamental principles to its diverse real-world applications. Delve into the building blocks of matter, uncovering the properties and behaviors of various materials, from metals and ceramics to polymers and composites. Navigate through cutting-edge research and technological advancements, understanding how materials shape our modern world. With engaging lectures, hands-on experiments, and practical projects, this course offers a comprehensive exploration of material science concepts, empowering learners to unlock innovation and tackle global challenges in fields such as engineering, nanotechnology, energy, and healthcare.",
    posted_on="2024-04-20",
    final_exam="Graded assignment",
    add_ons=[AddOn("Laboratory Assignments and Solutions", 5, None)]
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
    description="Understanding Statistics is an enlightening course designed to demystify the complexities of statistical analysis, empowering learners to harness the power of data-driven insights effectively. Delve into the foundational concepts of statistics, from probability theory to hypothesis testing, mastering essential techniques for data collection, analysis, and interpretation. Explore practical applications across diverse fields, from business and economics to science and healthcare, gaining the analytical skills needed to make informed decisions and solve complex problems. With interactive lessons, real-world examples, and hands-on exercises, this course equips individuals with the confidence and proficiency to navigate the intricacies of statistical reasoning and unlock new opportunities in their professional and academic pursuits.",
    posted_on="2024-04-28",
    final_exam="Graded assignment",
    add_ons=[AddOn("Real-world Projects and Solutions", 5, None)]
)

courses_dict = {
    "course1": course1,
    "course2": course2,
    "course3": course3,
    "course4": course4,
    "course5": course5
}

