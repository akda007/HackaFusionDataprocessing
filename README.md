# Python backend data processing for competence evaluation.




## Api routes

| Route| Desc |
| -----| ----- |
| data/instructor | Return class info |
| data/student | Return single student info |




## data/instructor
output exemple:

```
{
    "murylaoSala1part2": {
        "Python": {
            "score": 50,
            "class_score": 72
        }
    },
    "murylaoSala1part23": {
        "Python": {
            "score": 66,
            "class_score": 72
        },
        "Java": {
            "score": 100,
            "class_score": 100
        }
    },
    "murylaoSala1part2555324543453": {
        "Python": {
            "score": 100,
            "class_score": 72
        }
    }
}

```



## data/instructor
Output example:
```
{
    "Python": {
        "score": 50
    },
    "Java": {
        "score": 37
    }
}
```