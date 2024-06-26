# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AIKqK3o4UbVxk1dYl0DYpKb5dT8xPC-e
"""

from datetime import datetime
# Test case method to look at how adding an artwork works and it does since we added the mona lisa
def test_add_new_artwork():
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", datetime(1503, 1, 1), "A portrait of Lisa Gherardini", "permanent gallery")
    exhibition = Exhibition("Italian Renaissance", datetime(2024, 4, 1), datetime(2024, 10, 1), "Exhibition Hall 1")
    exhibition.add_artwork(artwork)
    print(f"Artwork '{artwork.title}' by {artwork.artist} added to the exhibition '{exhibition.name}'.")
    print(f"Artwork location: {artwork.location}")
    print()
#Test Case method to check when ever a new exhibition is added and where it is and the date
def test_open_new_exhibition():
    exhibition = Exhibition("Impressionist Masters", datetime(2024, 5, 15), datetime(2024, 12, 15), "Exhibition Hall 2")
    print(f"New exhibition '{exhibition.name}' will open at {exhibition.location} from {exhibition.start_date.strftime('%Y-%m-%d')} to {exhibition.end_date.strftime('%Y-%m-%d')}.")
    print()
#Test case method to check if the normal age discount works it works since user isn't elligible
def test_purchase_tickets():
    visitor = Visitor("John Doe", 30, "A12345678", "adult")
    event = Event("The Future of Art", "Main Gallery", datetime(2024, 5, 1, 10, 0), datetime(2024, 5, 1, 20, 0), special_event=False)
    ticket = Ticket(visitor, event)
    ticket.print_receipt()
    print()
#Test case method to check if the group discount works
def test_group_ticket_purchase():
    visitor = Visitor("Alice Smith", 28, "B87654321", "adult")
    group_size = 20  # A tour group of 20 visitors
    event = Event("Science in Art", "Exhibition Hall 3", datetime(2024, 6, 10, 9, 0), datetime(2024, 6, 10, 18, 0), special_event=False)
    group_ticket = Ticket(visitor, event, group_size)
    group_ticket.print_receipt()
    print()

#Just to run all the test case methods together
def testscases():
    test_add_new_artwork()
    test_open_new_exhibition()
    test_purchase_tickets()
    test_group_ticket_purchase()

# Execute the test cases
if __name__ == "__main__":
    testscases()