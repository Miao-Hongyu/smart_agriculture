import RPi.GPIO as GPIO

# 初始化执行器
PUMP_PIN = 18
VALVE_PIN = 23
HEATER_PIN = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PUMP_PIN, GPIO.OUT)
    GPIO.setup(VALVE_PIN, GPIO.OUT)
    GPIO.setup(HEATER_PIN, GPIO.OUT)

def control_pump(state):
    GPIO.output(PUMP_PIN, state)

def control_valve(state):
    GPIO.output(VALVE_PIN, state)

def control_heater(state):
    GPIO.output(HEATER_PIN, state)

def cleanup():
    GPIO.cleanup()
