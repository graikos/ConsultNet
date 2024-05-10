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

report1 = Report("Innapropriate Language", client_dict["David"], consultants_dict["Alice"], "User posted explicit content containing graphic imagery and offensive language, violating community guidelines on decency and respectful conduct. Content was reported by multiple users for its inappropriate nature and potential harm to other users. Immediate action is recommended to remove the offending material and enforce consequences to uphold community standards and ensure a safe online environment for all users. Further review may be necessary to determine if additional violations or patterns of misconduct exist within the user's posting history.", "User1", "media1.jpg", "2024-05-08")
report2 = Report("Spamming", client_dict["Sophia"], consultants_dict["Bob"], "Reported instance of spamming behavior by user, involving repetitive posting of promotional content unrelated to community interests. Violates platform guidelines on spam and self-promotion, diminishing user experience and cluttering discussion threads. Urgent action advised to mitigate further disruption and maintain the integrity of the platform's content ecosystem. Review user's posting history for any recurrent spamming patterns and consider appropriate disciplinary measures to deter future infractions.", "User2", "media2.jpg", "2024-05-09")
report3 = Report("Harassment", client_dict["James"], consultants_dict["Charlie"], "Flagged user for engaging in targeted harassment, persistently directing derogatory comments and personal attacks towards another user. Violation breaches platform's policies on harassment and respectful communication, creating a hostile environment for affected users. Immediate intervention necessary to address the situation, including removal of offending content and imposition of sanctions against the responsible party. Conduct thorough investigation to identify any related instances of harassment and ensure comprehensive resolution, prioritizing user safety and well-being within the community.", "User3", "media3.jpg", "2024-05-10")

report_dict = {
    "report1":report1,
    "report2": report2,
    "report3": report3
}

