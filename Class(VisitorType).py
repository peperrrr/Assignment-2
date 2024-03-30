class VisitorType:
    def __init__(self, visitor_type):
        self.visitor_type = visitor_type

    def is_discount_eligible(self):
        return self.visitor_type in ['child', 'teacher', 'student', 'senior']

    def is_group_discount_eligible(self, group_size):
        return group_size >= 15