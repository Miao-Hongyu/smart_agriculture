import matplotlib.pyplot as plt

def display_data(temperature, humidity, soil_moisture, action):
    plt.figure(figsize=(10, 6))
    labels = ['Temperature', 'Humidity', 'Soil Moisture']
    values = [temperature, humidity, soil_moisture]
    plt.bar(labels, values, color=['blue', 'green', 'red'])
    plt.title(f'Environment Data - Action: {action}')
    plt.show()
