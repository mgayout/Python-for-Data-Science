
def modify_list(ft_list):
	ft_list[1] = "World!"
	return ft_list

def modify_tuple(ft_tuple):
	ft_tuple_temp = list(ft_tuple)
	ft_tuple_temp[1] = "France!"
	ft_tuple = tuple(ft_tuple_temp)
	return ft_tuple

def modify_set(ft_set):
	ft_set.remove("tutu!")
	ft_set.add("Nice!")
	return ft_set

def modify_dict(ft_dict):
	ft_dict["Hello"] = "42Nice!"
	return ft_dict

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list = modify_list(ft_list)
ft_tuple = modify_tuple(ft_tuple)
ft_set = modify_set(ft_set)
ft_dict = modify_dict(ft_dict)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)