<div align="center">
  
# **Geolocalizador en Tiempo Real**


<img src="https://media.wired.com/photos/63ffb96f82f5460a73e0eb8b/master/w_1600%2Cc_limit/Radio-Hackers-Can-Eavesdrop-on-Any-DJI-Drone-to-Find-Its-Operator-Screenshot.jpg" width=40%>
  
</div>

Un **geolocalizador en tiempo real** es una herramienta poderosa que permite rastrear la ubicación exacta de un número de teléfono. Este script en Python utiliza múltiples librerías, APIs y herramientas para geolocalizar números telefónicos y mostrar la ubicación en un mapa interactivo.

### **Dependencias y APIs necesarias**
1. `phonenumbers` - Para analizar y obtener detalles del número de teléfono (como la ubicación y el operador).
2. `opencage` - Para convertir la descripción de la ubicación en coordenadas geográficas (latitud y longitud).
3. `folium` - Para mostrar la ubicación en un mapa interactivo.
4. **API Key** de OpenCage (requiere que generes tu clave de API para utilizar el servicio de geolocalización).

### **Explicación del Script**
1. **Entrada del número de teléfono**:
   El script pide al usuario que ingrese un número de teléfono. Si no tiene el prefijo `+`, lo agrega automáticamente con la lada nacional (+52 para México en este caso).

2. **Geolocalización del número**:
   Usando la librería `phonenumbers`, el número se analiza para obtener la descripción de la ubicación geográfica (como el estado o ciudad). También obtiene el nombre del operador.

3. **Geocodificación**:
   Con la descripción de la ubicación obtenida, se hace una solicitud a la API de OpenCage para obtener las coordenadas geográficas (latitud y longitud).

4. **Generación del mapa**:
   Con las coordenadas obtenidas, el script crea un mapa usando `folium`. La ubicación se marca en el mapa y se guarda como un archivo HTML para ser visualizado.

### **El Código**:

```python
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
```

### **Pasos Detallados**
1. **Ingreso de Número**: El script solicita al usuario que ingrese el número de teléfono.
2. **Análisis del Número**: Se verifica si el número tiene el prefijo internacional (`+`), y si no, se agrega la lada correspondiente.
3. **Obtención de Ubicación**: Usando `phonenumbers`, se obtiene la descripción de la ubicación y el nombre del operador.
4. **Consulta de Coordenadas**: La ubicación obtenida se consulta con la API de OpenCage para obtener las coordenadas geográficas exactas.
5. **Generación del Mapa**: `Folium` se encarga de crear el mapa interactivo con las coordenadas obtenidas, añadiendo un marcador y guardando el mapa como un archivo HTML.

### **Resultados**:
- Si el número tiene una ubicación válida, el script imprimirá las coordenadas y generará un mapa con un marcador en la ubicación.
- El archivo `location.html` contendrá el mapa y se podrá abrir en cualquier navegador para visualizar la ubicación.

### **Notas**:
- Asegúrate de reemplazar `"API-Key"` con tu propia clave de API de OpenCage.
- Este script está diseñado para ser usado de forma sencilla, pero se puede expandir para agregar más funcionalidades como rastrear múltiples números o agregar más precisión a la geolocalización.
- **¡Cuidado con la privacidad!** Asegúrate de usar este script de manera ética y legal.

<div align="center">
  
### **Hack the world.**

</div>
