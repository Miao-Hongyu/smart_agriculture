import Adafruit_DHT
import RPi.GPIO as GPIO

# 初始化传感器
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
SOIL_MOISTURE_PIN = 17

def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

def read_soil_moisture():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)
    return GPIO.input(SOIL_MOISTURE_PIN)
