def washhands():
    print("washing hands")
def servefood():
    print("serving food")
def eatfood():
    washhands()
    servefood()
    print("eating food")
    washhands()
eatfood()