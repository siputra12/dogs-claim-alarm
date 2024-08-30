import requests, time, subprocess
from datetime import datetime

def check_busy():
    res = requests.post("https://ton-claim.sign.tg/api/airdrop-open/query-pid", json={"slug":"dogs","recipient":"UQACVaM1jvUE2FGG3xnfNUWcdNJFwCl1UhI4mZowl8hCsXPI"}).json()
    ret = True if len(res['data']['projectIds']) >= 1 else False
    return ret

def mpp(file):
    args = ["termux-media-player", "play", file]
    proc = subprocess.run(
            args, capture_output=True, check=True, text=True
        )
    return proc

def mps():
    args = ["termux-volume", "stop"]
    proc = subprocess.run(
            args, capture_output=True, check=True, text=True
        )
    return proc

def fv():
    args = ["termux-volume", "music", "100"]
    proc = subprocess.run(
            args, capture_output=True, check=True, text=True
        )
    return proc

while True:
    cb = check_busy()
    dt_object = datetime.fromtimestamp(datetime.now().timestamp())
    formatted_date = dt_object.strftime('%d-%m-%Y %H:%M:%S')
    if cb:
        print(f"[{formatted_date}] Status : Online")
        fv()
        mpp("Alarm.mp3")
        input("Enter to stop...")
        mps()
        break
    else:
        print(f"[{formatted_date}] Status : Busy", end="\r")
        time.sleep(60)