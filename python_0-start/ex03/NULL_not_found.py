def NULL_not_found(object: any) -> int:

    dic = {"Nothing": None, "Zero": 0, "Empty": "", "Fake": False}
    obj_type = type(object)
    if object != object:
        print(f"Chesse : {object} {obj_type}")
        return 0
    elif not object:
        for key, value in dic.items():
            if object == value and obj_type == type(value):
                print(f"{key}: {value} {obj_type}")
        return 0
    else:
        print("Type not Found")
        return 1
