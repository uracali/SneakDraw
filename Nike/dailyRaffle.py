from .NikeClass import Nike
import time

def dailyRaffle(data):
    id = data.get("id")
    password = data.get("password")
    nike = None
    try:
        nike = Nike(id,password)
        nike.login()
        raffleList = nike.findDraw()
        if len(raffleList):
            result = nike.raffle(raffleList)
        else:
            result = "NO_RAFFLE_ITEMS"
    except Exception as ex: 
        print(ex)
        result = "INTERNAL_ERROR"
    finally:
        nike.quitDriver()
        
    return {"result" : result}



