from gpiozero import Button
from signal import pause
from datetime import datetime

# Sensor en GPIO 6 con resistencia pull-up interna
rain_sensor = Button(6, pull_up=True, bounce_time=0.1)

BUCKET_SIZE = 0.2794  # mm por vuelco
count = 0

print("Pluviómetro iniciado. Esperando pulsos...\n")

def bucket_tipped():
    global count
    count += 1
    rainfall = count * BUCKET_SIZE
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] Vuelco detectado → Lluvia acumulada: {rainfall:.2f} mm")

rain_sensor.when_pressed = bucket_tipped

pause()
