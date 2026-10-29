#!/usr/bin/env python3

contacts = [
    { "name" : "Alice", "mail" : "alice@example.org" },
    { "name" : "Steve", "mail" : "steve@minecraft.com" },
    { "name" : "Bob", "mail" : "bob@fau.de" },
]

for contact in contacts:
    print("Name: {}, E-Mail: {}".format(contact["name"], contact["mail"]))
