#!/usr/bin/python3

class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    """ If some contacts are also suppliers, we can create a new
        Supplier class that acts like a Contact but has an additional 
        order method"""

    def order(self, order):
        print("If this was a real system we would send {} order to {}".format(order, self.name))


c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)

s.order("I need pliers")
