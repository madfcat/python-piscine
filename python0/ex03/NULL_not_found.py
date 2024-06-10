def NULL_not_found(object: any) -> int:
    if (object is None):
        print("Nothing : ", object, type(object))
    elif (object != object):
        print("Cheese : ", object, type(object))
    elif (object == 0 and isinstance(object, int)):
        print("Zero : ", object, type(object))
    elif (object == ""):
        print("Empty : ", type(object))
    elif (object is False):
        print("Fake : ", object, type(object))
    else:
        print("Type not found")
        return 1
    return 0
