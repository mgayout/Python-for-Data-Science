import time

local_time = time.localtime()

s1 = time.time()
s2 = format(s1, ".2e")

print(f"Seconds since January 1, 1970: {s1} or {s2} in scientific notation")
print(time.strftime("%b %d %Y", local_time))