class Event:
    def __init__(self, event_name, location, start_time, end_time, special_event=False):
        self.event_name = event_name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.special_event = special_event
        self.tickets = []