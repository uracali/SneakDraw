from .WokrsoutClass import Worksout


def dailyRaffle(data):
    id = data.get("id")
    password = data.get("password")
    print(id)
    try:
        worksout = Worksout(id, password)
        worksout.login()
        worksout.findDraw()
        if len(worksout.href_list):
            result = worksout.raffle()
        else:
            result = "NO_RAFFLE_ITEMS"
    except Exception as ex:
        print("error", ex)
        result = "INTERNAL_ERROR"
    finally:
        worksout.quitDriver()

    return {"result": result}
