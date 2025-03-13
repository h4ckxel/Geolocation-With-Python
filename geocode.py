import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


key = "API-Key" # Geocoder API Key need to paste here "your key" 
number = input("please giver your number: ")

if not number.startswith("+"):
    number = "+52" + number # LADA Number

new_number = phonenumbers.parse(number, "COUNTRY") # COUNTRY = MX, USA, etc.
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

# print(result)
if result:
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    print(f"Coordinates: {lat}, {lng}")

    # Folium Map
    my_map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(my_map)
    my_map.save("location.html")

    print("Location tracking completed. Map saved as 'location.html'.")
else:
    print("Error: Could not retrieve coordinates.")


# lat = result[0]['geometry']['lat']
# lng = result[0]['geometry']['lng']

# print(lat,lng)

# my_map = folium.Map(location=[lat,lng], zoom_start=9)
# folium.Marker([lat, lng], popup= location).add_to(my_map)

# my_map.save("location.html")

# print("location tracking completed")
# print("Thank you")
