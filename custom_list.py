class CustomList(list):
    """Custom list with throwing an exception, when index going beyond the list (without -1, -2 ... indexes )"""

    def __getitem__(self, index):
        if index < 0:
            raise IndexError(f"Expected a positive index, instead got {index}")

        return super(CustomList, self).__getitem__(index)

    def __setitem__(self, key, value):
        if key < 0:
            raise IndexError(f"Expected a positive index, instead got {key}")

        return super(CustomList, self).__setitem__(key, value)
