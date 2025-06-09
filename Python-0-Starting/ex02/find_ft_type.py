def all_thing_is_obj(object: any) -> int:
	types = { "list", "tuple", "set", "dict" }
	class_param = type(object)
	type_param = class_param.__name__
	if type_param == "str":
		print(f"{object} is in the kitchen : {class_param}")
	elif type_param not in types:
		print(f"Type not found")
	else:
		print(f"{type_param.capitalize()} : {class_param}")
	return 42