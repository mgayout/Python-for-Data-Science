def NULL_not_found(object: any) -> int:
	class_param = type(object)
	type_param = class_param.__name__

	if type_param == "NoneType" and object is None:
		print(f"Nothing: {object} {class_param}")
	elif class_param is float and object != object:
		print(f"Cheese: {object} {class_param}")
	elif class_param == int and object == 0:
		print(f"Zero: {object} {class_param}")
	elif class_param is str and object == "":
		print(f"Empty: {object} {class_param}")
	elif class_param is bool and not object:
		print(f"Fake: {object} {class_param}")
	else:
		print("Type not found")
		return 1
	return 0