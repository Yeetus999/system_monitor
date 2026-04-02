import psutil
import time
import os



while True :
    os.system("cls" if os.name == "nt" else "clear")

    cpu = psutil.cpu_percent(interval=1) ##misst die CPU-Auslastung, interval=1 heißt 1 Sekunde messen
    ram = psutil.virtual_memory() ## liefert Informationen über den Arbeitsspeicher


    print("\n---Systemdaten---")
    print("CPU-Auslastung:", cpu, "%")
    print("RAM gesamt:", round(ram.total / (1024**3), 2), "GB") ## 1024**3 rechnet Byte in Gigabyte um
    print("RAM verwendet:", round(ram.used / (1024**3), 2), "GB")
    print("RAM Auslastung:", ram.percent, "%")

    print("\n--- Prozesse ---")

    count = 0                           ##zählt wie viele Prozesse angezeigt werden
    for process in psutil.process_iter():
        if count >= 10:
            break



        try:
            name = process.name()


            if name and name != "System Idle Process":
                print(name, "(PID:", process.pid, ")")
                count += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    time.sleep(3)