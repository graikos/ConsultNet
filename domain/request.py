from domain.client import client_dict
from domain.consultant import consultants_dict
from domain.category import categories_dict

class Request:
    def __init__(self, name, description, user, esth, cons, compensation, category, posted_on):
        self.name = name
        self.description = description
        self.user = user
        self.esth = esth
        self.cons = cons
        self.compensation = compensation
        self.category = category
        self.posted_on = posted_on

request1 = Request("Digital Marketing Course", "I'm seeking a course on digital marketing because I'm eager to boost my skills in the ever-evolving online landscape. With the rapid growth of digital platforms, I see a prime opportunity to enhance my career prospects and contribute more effectively to my organization's marketing efforts. Additionally, I'm drawn to courses that offer hands-on projects and real-world case studies, as I believe these practical experiences will better equip me to navigate complex marketing challenges. Ultimately, I'm excited to acquire new knowledge and strategies that will not only benefit my professional growth but also drive tangible results for my team.", client_dict["David"] , 100, consultants_dict["Alice"], "$100", categories_dict["Computer Science"].name, "2024-05-08")
request2 = Request("Sustainable living Course", "I'm interested in enrolling in a course on sustainable living because I'm deeply passionate about environmental conservation. With the increasing urgency of climate change, I feel compelled to take proactive steps towards reducing my carbon footprint and promoting eco-friendly practices in my daily life. This course presents an opportunity to deepen my understanding of sustainability principles, learn practical strategies for energy efficiency, waste reduction, and ethical consumption, and connect with like-minded individuals who share my commitment to preserving our planet for future generations. I'm excited to gain the knowledge and skills needed to make meaningful contributions to a more sustainable world.", client_dict["Sophia"], 200, consultants_dict["Bob"], "$150", categories_dict["Business"].name, "2024-05-09")
request3 = Request("Meditation Course", "I'm eager to enroll in a course on mindfulness and meditation to cultivate inner peace and emotional resilience. In today's fast-paced world, I often find myself overwhelmed by stress and anxiety, and I believe that integrating mindfulness practices into my daily routine can help me achieve a greater sense of calm and balance. I'm drawn to courses that offer guidance on mindfulness techniques, such as mindful breathing and body scan exercises, as well as insights into the science behind meditation and its profound effects on mental well-being. By investing in my own self-care and personal growth, I aim to live a more mindful and fulfilling life.", client_dict["James"], 300, consultants_dict["Charlie"], "$200", categories_dict["Mathematics"].name, "2024-05-10")     

request_dict = {
    "request1":request1,
    "request2": request2,
    "request3": request3
}
