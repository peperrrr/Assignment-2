# -*- coding: utf-8 -*-
"""ICS220 - Assignment 2: Software Implementation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eVW80m2mv8l_VSOTqNSaZXVrooucxvmO
"""

from datetime import datetime #importing date since it is easier than using integers to label date times

#Variables given to the pricing which wont change through out
BASE_PRICE = 63  # Base price for adults between 18 and 60
VAT_RATE = 0.05  # 5% VAT

# VisitorType Class to be able to apply the discount after getting Visitor information
class VisitorType:
    def __init__(self, visitor_type):
        self.visitor_type = visitor_type

    def is_discount_eligible(self):
        return self.visitor_type in ['child', 'teacher', 'student', 'senior']

    def is_group_discount_eligible(self, group_size):
        return group_size >= 15

# Visitor class to get their information
class Visitor:
    def __init__(self, name, age, id_number, visitor_type):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.visitor_type = VisitorType(visitor_type)

# Artwork class so we can be able to add artwork to any exhibition when ever we recieve a new piece
class Artwork:
    def __init__(self, title, artist, created_date, historical_significance, location):
        self.title = title
        self.artist = artist
        self.created_date = created_date
        self.historical_significance = historical_significance
        self.location = location

# Exhibition Class so then we can identify where an artwork is
class Exhibition:
    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.artworks = []
#Creating a method to add the artworks to a certain exhibition easier
    def add_artwork(self, artwork):
        self.artworks.append(artwork)

# Event Class to be able to label if an event is going on and show dates and stuff regarding it
class Event:
    def __init__(self, event_name, location, start_time, end_time, special_event=False):
        self.event_name = event_name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.special_event = special_event
        self.tickets = []

# Ticket Class to be able to create a ticket
class Ticket:
    def __init__(self, visitor, event, group_size=1):
        self.visitor = visitor
        self.event = event
        self.group_size = group_size
        self.price = self.calculate_price()
#Method to calculate the price incase there is a discount
    def calculate_price(self):
        if self.visitor.visitor_type.is_discount_eligible(): #Discount for children or the elderly
            base_price = 0
        elif self.visitor.visitor_type.is_group_discount_eligible(self.group_size): #Group discount which cuts the price in half if group above 15 members
            base_price = BASE_PRICE * 0.5
        else:
            base_price = BASE_PRICE

        if self.event.special_event:
            base_price = 100  #  price for special event since it would be different than normal price

        final_price = base_price * (1 + VAT_RATE)
        return final_price * self.group_size

#After doing all the other methods last method is just to print the recipet with the vistior
    def print_receipt(self):
        print(f"Receipt for: {self.visitor.name}")
        print(f"Event: {self.event.event_name}")
        print(f"Total Price (VAT included): AED {self.price:.2f}")
