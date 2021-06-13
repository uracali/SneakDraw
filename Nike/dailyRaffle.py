from .NikeClass import Nike


def dailyRaffle(data):
    id = data.get("id")
    password = data.get("password")
    print(id)
    try:
        nike = Nike(id, password)
        nike.login()
        raffleList = nike.findDraw()
        print("raffleList = ", raffleList)
        if len(raffleList):
            result = nike.raffle(raffleList)
        else:
            result = "NO_RAFFLE_ITEMS"
    except Exception as ex:
        print("error", ex)
        result = "INTERNAL_ERROR"
    finally:
        nike.quitDriver()

    return {"result": result}
