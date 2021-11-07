from .NikeClass import Nike


def dailyRaffle(data):
    id = data.get("id")
    password = data.get("password")
    size = data.get("shoes_size")
    print(id)
    try:
        nike = Nike(id, password, size)
        login_status = nike.login()
        if login_status == False:
            raise NameError('login failed')
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
