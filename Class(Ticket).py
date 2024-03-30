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
