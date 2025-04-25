# 配置文件，定义阈值和引脚配置
TEMP_HUMIDITY_SENSOR_PIN = 4  # DHT22传感器的引脚
SOIL_MOISTURE_PIN = 17       # 土壤湿度传感器引脚

# 环境参数的控制阈值
TEMP_THRESHOLD_LOW = 18  # 温度下限 (℃)
TEMP_THRESHOLD_HIGH = 30  # 温度上限 (℃)
HUMIDITY_THRESHOLD_LOW = 40  # 湿度下限 (%)
HUMIDITY_THRESHOLD_HIGH = 80  # 湿度上限 (%)
SOIL_MOISTURE_THRESHOLD_LOW = 50  # 土壤湿度下限 (%)
SOIL_MOISTURE_THRESHOLD_HIGH = 75  # 土壤湿度上限 (%)

# 执行器控制引脚
PUMP_PIN = 18
VALVE_PIN = 23
HEATER_PIN = 24
