class Visitor:
    def __init__(self, name, age, id_number, visitor_type):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.visitor_type = VisitorType(visitor_type)

