import builtins


class ft_filter:
    def __init__(self, func, iterable):
        self.lst = []
        for i in iterable:
            if (func and func(i)) or (func is None and i):
                self.lst.append(i)
        self.iterable = iter(self.lst)

    def __iter__(self):
        return self.iterable

    def __next__(self):
        return next(self.iterable)


def keep_odds(nbr: int) -> bool:
    """return true if the int arg is an odd, otherwise return false"""
    if nbr % 2 == 0:
        return True
    return False


def keep_lower(c: str) -> bool:
    """return true is the char is lower, otherwise return false"""
    if c.islower():
        return True
    return False


def main():
    """filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for
    which function(item) is true.
    If function is None, return the items that are true."""


print("----------TEST LIST OF INT ----------------")
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"list = {list}")
print("__ft_filter__")
new_list = ft_filter(keep_odds, list)
print(f"type = {type(new_list)}")
print(f"new_list = {new_list}")
for i in new_list:
    print(i)
print("__filter-original__")
new_list = builtins.filter(keep_odds, list)
print(f"new_list = {new_list}")
for i in new_list:
    print(i)
print("----------TEST STRING ----------------")
str = "CouCou On Est LA !!"
print(f"str = {str}")
new_str = ft_filter(keep_lower, str)
print(f"new str = {new_str}")
for c in new_str:
    print(c)
print("__filter-original__")
new_str = builtins.filter(keep_lower, str)
print(f"new str = {new_str}")
for c in new_str:
    print(c)
print("----------TEST FUNC IS NONE ----------------")
list = [1, 0, 2, 3, False, 4, 5, {}, 6, 7, 8, "", 9]
print(f"list = {list}")
new_list = ft_filter(None, list)
print(f"type = {type(new_list)}")
print(f"new_list = {new_list}")
for i in new_list:
    print(i)
print("__filter-original__")
new_list = builtins.filter(None, list)
print(f"new_list = {new_list}")
for i in new_list:
    print(i)
if __name__ == "__main__":
    main()
