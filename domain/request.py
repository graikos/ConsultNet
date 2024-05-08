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

request1 = Request("Request 1", "Description of request 1", client_dict["David"] , 100, consultants_dict["Alice"], "$100", categories_dict["Computer Science"].name, "2024-05-08")
request2 = Request("Request 2", "Description of request 2", client_dict["Sophia"], 200, consultants_dict["Bob"], "$150", categories_dict["Business"].name, "2024-05-09")
request3 = Request("Request 3", "Description of request 3", client_dict["James"], 300, consultants_dict["Charlie"], "$200", categories_dict["Mathematics"].name, "2024-05-10")     

request_dict = {
    "request1":request1,
    "request2": request2,
    "request3": request3
}
