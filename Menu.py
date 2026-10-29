from tabulate import tabulate

class Menu:
    def __init__(self):
        self.title = ""
        self.breadcrumb = ""
    def display():
        pass
class Pagination(Menu):
    def __init__(self, queryResult):
        super().__init__()
        self.queryResult = queryResult
        self.queryNum = 0
        self.pageSize = 3
    def display(self):
        print(tabulate(self.queryResult, headers="keys"))


queryResult = [
    {"studentName" : "A", "age" : 16, "className" : "Grade 10"},
    {"studentName" : "B", "age" : 16, "className" : "Grade 10"},
    {"studentName" : "C", "age" : 16, "className" : "Grade 10"},
    {"studentName" : "D", "age" : 16, "className" : "Grade 10"},
]
p = Pagination(queryResult)
p.display()
