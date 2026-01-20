from gpiozero import Button
from signal import pause
rain_sensor = Button(6)
BUCKET_SIZE = 0.2794
count = 0
def bucket_tipped():
    global count
    count += 1
    rainfall = count * BUCKET_SIZE
    print(f"Lluvia acumulada: {rainfall:.2f} mm")
def reset_rainfall():
    global count
    count = 0
    print("Contador de lluvia reiniciado")
rain_sensor.when_pressed = bucket_tipped
pause()
