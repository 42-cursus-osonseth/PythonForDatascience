def all_thing_is_obj(object: any) -> int:

    obj_type = type(object)

    match obj_type:
        case c if c is list:
            print(f"List : {obj_type}")
        case c if c is tuple:
            print(f"Tuple : {obj_type}")
        case c if c is set:
            print(f"Set : {obj_type}")
        case c if c is dict:
            print(f"Dict : {obj_type}")
        case c if c is str:
            print(f"{object} is in the kithen : {obj_type}")
        case _:
            print("Type not found")

    return 42
