from .NikeClass import Nike
import time

def dailyRaffle(data):
    id = data.get("id")
    password = data.get("password")
    print(id, password)
    nike = None
    try:
        nike = Nike(id,password)
        nike.login()
        # time.sleep(2000)
    finally:
        nike.quitDriver()
        
    return {"result" : "SUCCESS"}



