import json
from django.db import models



class ClassInfo():
    id: int
    mainDisciplineType: str
    name: str


class UserInfo():
    id: int
    username: str
    fullname: str
    email: str
    role: str
    
    studentGang: ClassInfo



class DisciplineInfo():
    id: int
    name: str
    description: str
    workload: int
    type: str
    
    def __init__(self, discipline: dict) -> None:
        self.id = discipline["id"]
        self.name = discipline["name"]
        self.description = discipline["description"]
        self.workload = discipline["workload"]
        self.type = discipline["type"]


class CompetenceInfo():
    id: int
    name: str
    description: str
    weight: float
    
    def __init__(self, info) -> None:
        self.id = info["id"]
        self.name = info["name"]
        self.description = info["description"]
        self.weight = info["weight"]
    
class StudentCompetence():
    id: int
    status: str
    competence: CompetenceInfo
    
    def __init__(self, competence: dict) -> None:
        self.id = competence["id"]
        self.status = competence["status"]
        
        self.competence = CompetenceInfo(competence["competence"])
    
class AvaliationInfo():
    id: int
    discipline: DisciplineInfo
    competences: list[StudentCompetence]
    
    def __init__(self, avaliation: dict) -> None:
        self.id = avaliation["id"]
        self.discipline = DisciplineInfo(avaliation["discipline"])
        
        self.competences = []
        for d in avaliation["competences"]:
            self.competences.append(StudentCompetence(d))
            
        

    

class UserAvaliation():
    user: UserInfo
    avaliations: list[AvaliationInfo]
    
    def load_from_json(self, json_text):
        obj = json.loads(json_text)
        self.load_from_dict(obj)
        pass
    
    def load_from_dict(self, obj):
        user_info = obj["user"]
        
        self.user = UserInfo()
        self.user.id = user_info["id"]
        self.user.username = user_info["username"]
        self.user.fullname = user_info["fullname"]
        self.user.role = user_info["role"]
        
        student_gang = ClassInfo()
        student_gang_info = user_info["studentGang"]
        
        student_gang.id = student_gang_info["id"]
        student_gang.mainDisciplineType = student_gang_info["mainDisciplineType"]
        student_gang.name = student_gang_info["name"]
        
        self.user.studentGang = student_gang
        
        self.avaliations = []
        for data in obj["avaliations"]:
            self.avaliations.append(AvaliationInfo(data))
            
        

    def __init__(self, json_text = "", obj = None) -> None:
        if json_text != "":
            self.load_from_json(json_text)
        else:
            self.load_from_dict(obj)
    
    
class ClassAvaliation():
    avaliations: list[UserAvaliation]
    
    def __init__(self, json_str) -> None:
        obj = json.loads(json_str)
        
        self.avaliations = []
        for data in obj:
            self.avaliations.append(UserAvaliation(obj=data))
            