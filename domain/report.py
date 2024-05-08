from domain.client import client_dict
from domain.consultant import consultants_dict

class Report:
    def __init__(self, subject, posted_by, posted_for, description, user, media, posted_on):
        self.subject = subject
        self.posted_by = posted_by
        self.posted_for = posted_for
        self.description = description
        self.media = media
        self.posted_on = posted_on

report1 = Report("Term Violation", client_dict["David"], consultants_dict["Alice"], "Description of report 1", "User1", "media1.jpg", "2024-05-08")
report2 = Report("Term Violation", client_dict["Sophia"], consultants_dict["Bob"], "Description of report 2", "User2", "media2.jpg", "2024-05-09")
report3 = Report("Term Violation", client_dict["James"], consultants_dict["Charlie"], "Description of report 3", "User3", "media3.jpg", "2024-05-10")

report_dict = {
    "report1":report1,
    "report2": report2,
    "report3": report3
}

