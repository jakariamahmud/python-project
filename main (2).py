import phonenumbers as ph
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number: ")
phone = ph.parse(number)
time = timezone.time_zones_for_number(phone)
sim_de = carrier.name_for_number(phone, "en")
register = geocoder.description_for_number(phone, "en")
print(number)
print(phone)
print(time)
print(sim_de)
print(register)