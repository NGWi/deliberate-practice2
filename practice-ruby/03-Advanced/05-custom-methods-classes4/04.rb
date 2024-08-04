# Write a Contact class that stores the name, age, and contact_info, where contact_info is a hash that stores any additional information about the contact.
class Contact
  attr_writer :name, :age, :contact_info
end

contact = Contact.new

contact.name = "Joe"
contact.age = 11
contact.contact_info = {address: "123 ABC Place", phone_number: "18001112222"}
pp contact