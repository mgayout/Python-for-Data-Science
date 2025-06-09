from ft_filter import ft_filter

def is_even(n):
    return n % 2 == 0

def is_true(b):
    return b is True

def is_integer(i):
    return type(i) == int

def main():
    numbers = [1, -2, 3, 4, -5, 6]
    bools = [True, True, False, True, True, False]
    mixed = ["Hello World!", -42, True, 0.0001, None, 0]

    events = filter(is_even, numbers)
    print(f"\nfilter(is_even, numbers) = {list(events)}")
    events = ft_filter(is_even, numbers)
    print(f"ft_filter(is_even, numbers) = {list(events)}")
    
    events = filter(is_true, bools)
    print(f"\nfilter(is_true, bools) = {list(events)}")
    events = ft_filter(is_true, bools)
    print(f"ft_filter(is_true, bools) = {list(events)}")
    
    events = filter(is_integer, mixed)
    print(f"\nfilter(is_integer, mixed) = {list(events)}")
    events = ft_filter(is_integer, mixed)
    print(f"ft_filter(is_integer, mixed) = {list(events)}")
    
    events = filter(None, mixed)
    print(f"\nfilter(None, mixed) = {list(events)}")
    events = ft_filter(None, mixed)
    print(f"ft_filter(None, mixed) = {list(events)}")
    
    print(f"\nfilter.__doc__ = \n{filter.__doc__}\n")
    print(f"ft_filter.__doc__ = \n{ft_filter.__doc__}")

if __name__ == "__main__":
    main()