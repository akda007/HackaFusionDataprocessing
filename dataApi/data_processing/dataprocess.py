from dataApi.models import ClassAvaliation, UserAvaliation

competence_evaluations = {
    "LEARNING": 0.5,
    "UNQUALIFIED": 0.0,
    "QUALIFIED": 1.0
}

# instructor
[
    {
        "subject": str,
        "class_score": int,
        "student_score": int
        
    }
]

# student
[
    {
        "subject": str,
        "student_score": int        
    }
]

def get_user_score(user_avaliation: UserAvaliation):
    scores = {}
    
    for obj in user_avaliation.avaliations:
        subject = obj.discipline.name
        
        if subject not in scores.keys():
            scores[subject] = {
                "weights": [],
                "values": []
            }
        
        for compentece in obj.competences:
            status_value = competence_evaluations[compentece.status]
            weight = compentece.competence.weight
            
            scores[subject]["weights"].append(weight)
            scores[subject]["values"].append(status_value * weight)
    
    return scores
            
            
def get_class_score(class_avaliation: ClassAvaliation):
    class_scores = {}
    
    values = {}
    
    for avaliation in class_avaliation.avaliations:
        scores = get_user_score(avaliation)
        
        class_scores[avaliation.user.username] = {}
        for k, i in build_user_array(scores).items():
            if k not in values.keys():
                values[k] = []
            
            values[k].append(i["score"])
            class_scores[avaliation.user.username][k] = i
    a = []
    
    for k, i in class_scores.items():
        for discipline in i.keys():
            class_scores[k][discipline]["class_score"] = sum(values[discipline]) // len(values[discipline])
        
    
    return class_scores



def build_user_array(scores: dict):
    result = {}
    
    for k, v in scores.items():
        result[k] = {"score": int(sum(v["values"]) / sum(v["weights"]) * 100)}    
    
    return result


    

def dataprocess_instructor(json, student_name = ""):
    avaliation = ClassAvaliation(json)
    scores = get_class_score(avaliation)
    
    return scores
    

def dataprocess_student(json):
    avaliation = UserAvaliation(json)
    
    score = get_user_score(avaliation)
    result = build_user_array(score)
    
    return result