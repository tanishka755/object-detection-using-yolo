def get_health_data():
    heart_rate = random.randint(60, 120)  # Simulate heart rate between 60-120 bpm
    pulse = random.randint(70, 110)       # Simulate pulse rate
    return heart_rate, pulse

def is_emergency(heart_rate, pulse):
    if heart_rate > 100 or pulse > 100:  # Threshold for emergency
        return True
    return False

def drive_to_hospital():
    print("Emergency detected! Driving to the nearest hospital...")
    time.sleep(5)  # Simulate the time it takes to drive to a hospital
    print("Arrived at the hospital.")

def send_health_data_to_hospital(heart_rate, pulse):
    url = "http://hospital-server.com/api/health_data"  # Replace with actual hospital API
    data = {
        "heart_rate": heart_rate,
        "pulse": pulse,
        "timestamp": time.time()
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Health data sent successfully to the hospital.")
    else:
        print(f"Failed to send data: {response.status_code}")

if is_emergency(heart_rate, pulse):
    drive_to_hospital()
    send_health_data_to_hospital(heart_rate, pulse)
    break  # Exit after sending the data and driving to the hospital
