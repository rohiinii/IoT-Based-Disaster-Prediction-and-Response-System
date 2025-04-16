import network
import time
import dht
from machine import Pin, ADC
from umqtt.simple import MQTTClient

# ======= WiFi Credentials =======
wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# ======= ThingSpeak MQTT Credentials =======
mqtt_server = "mqtt3.thingspeak.com"
mqtt_client_id = "FxIzHSAOFDUlDQ43MwI7ISU"
mqtt_user = "FxIzHSAOFDUlDQ43MwI7ISU"
mqtt_password = "4bIQ1jSi+hjqNwep9sUoevRe"
mqtt_topic = "channels/2842458/publish"

# ======= Sensor Setup =======
dht_sensor = dht.DHT22(Pin(15))      # Temp & Humidity
mq135 = ADC(Pin(35))                 # Air quality sensor
pot = ADC(Pin(34))                   # Wind speed via potentiometer
ldr = ADC(Pin(32))                   # Light sensor

# Adjust ADC range for 0–4095
for sensor in [mq135, pot, ldr]:
    sensor.atten(ADC.ATTN_11DB)

# ======= Utility: Map ADC readings =======
def map_value(val, in_min, in_max, out_min, out_max):
    return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# ======= WiFi Connection =======
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    while not wlan.isconnected():
        print("🔌 Connecting to WiFi...")
        time.sleep(1)
    print("✅ Connected to WiFi:", wlan.ifconfig())

# ======= MQTT Connection =======
def mqtt_connect():
    client = MQTTClient(client_id=mqtt_client_id,
                        server=mqtt_server,
                        user=mqtt_user,
                        password=mqtt_password,
                        keepalive=60,
                        ssl=False)
    client.connect()
    print("✅ Connected to ThingSpeak MQTT")
    return client

# ======= Main Program =======
wifi_connect()
client = mqtt_connect()

while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        air_quality = mq135.read()
        wind_speed = map_value(pot.read(), 0, 4095, 0, 100)
        light = map_value(ldr.read(), 0, 4095, 0, 1023)

        # Compose ThingSpeak payload for fields 1–5
        payload = f"field1={temperature}&field2={humidity}&field3={wind_speed}&field4={air_quality}&field5={light}"


        client.publish(mqtt_topic, payload)
        print("📤 Published to ThingSpeak:", payload)

    except Exception as e:
        print("❌ Error:", e)

    time.sleep(10)  # ThingSpeak allows updates every 15+ seconds
