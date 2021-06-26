pip import phonenumbers
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
phone_number =phonenumbers.parse("9920596760")

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
print(timezone.time_zone_for_number(phone_number))