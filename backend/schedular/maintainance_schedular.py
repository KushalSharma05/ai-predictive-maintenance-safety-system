import schedule
import time
from ml.predict import predict_failure

def check_machine_status():
    pred = predict_failure(70, 5, 30)  # sample values
    if pred < 10:
        print("⚠ ALERT: Machine may fail soon! Schedule maintenance.")
    else:
        print("✔ Machine operating normally.")

schedule.every(1).minute.do(check_machine_status)

while True:
    schedule.run_pending()
    time.sleep(1)
