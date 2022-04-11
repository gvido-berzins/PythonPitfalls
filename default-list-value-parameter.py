"""
Summary:
    Using mutable variables as default parameters can lead to unexpected results
Description:
    The behavior is explained by how python works.
    Example: When creating a list, a reference is saved into the memory and
    the list can be modified from anywhere, in code bellow, the list is initialized
    before the class is initialized resulting in having a global list assigned to
    the class parameter and the same reference to the list is saved in the instances
    variable.
"""

# Pitfall :(
print("Bad code".center(50, "-"))


class Product:
    def __init__(self, labels=[]):
        self.labels = labels

    def add_labels(self, *args):
        self.labels.extend(args)


apple, banana = Product(), Product()
banana.add_labels("yellow", "monkey-food")
print("X: I don't remember adding labels to an apple")
print(f"apple: {apple.labels}")
print(f"banana: {banana.labels}")


# Fix :)
print("Good code".center(50, "-"))


class Product:
    def __init__(self, labels=None):
        self.labels = labels if isinstance(labels, list) else []

    def add_labels(self, *args):
        self.labels.extend(args)


apple, banana = Product(), Product()
banana.add_labels("yellow", "monkey-food")
apple.add_labels("green", "round")
print("X: Works better!")
print(f"apple: {apple.labels}")
print(f"banana: {banana.labels}")
