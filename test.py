queryResult = [
    {"studentName" : "A", "age" : 16, "className" : "Grade 10"},
    {"studentName" : "B", "age" : 16, "className" : "Grade 10"},
    {"studentName" : "C", "age" : 16, "className" : "Grade 10"},
    {"studentName" : "D", "age" : 16, "className" : "Grade 10"},
]
headers =  [k for k, v in queryResult[0].items()]
print(headers)