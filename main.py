import time
from sensors import read_temperature_humidity, read_soil_moisture
from actuators import setup, control_pump, control_valve, control_heater, cleanup
from ai_controller import predict_action
from ui import display_data

def main():
    setup()
    try:
        while True:
            temperature, humidity = read_temperature_humidity()
            soil_moisture = read_soil_moisture()

            if temperature is not None and humidity is not None:
                action = predict_action(temperature, humidity, soil_moisture)
                display_data(temperature, humidity, soil_moisture, action)

                if action == 0:
                    control_pump(False)
                    control_valve(False)
                    control_heater(False)
                elif action == 1:
                    control_pump(True)
                    control_valve(True)
                    control_heater(False)
                elif action == 2:
                    control_pump(False)
                    control_valve(False)
                    control_heater(True)

            time.sleep(60)  # 每分钟读取一次数据
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()

if __name__ == '__main__':
    main()
