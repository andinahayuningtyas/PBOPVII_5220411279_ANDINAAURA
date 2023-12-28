# Base class
class Clothing:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size

    def display_info(self):
        print(f"Brand: {self._brand}, Size: {self._size}")

    def calculate_price(self):
        # Default implementation
        return 0

# Child class
class Shirt(Clothing):
    def __init__(self, brand, size, sleeve_length):
        super().__init__(brand, size)
        self._sleeve_length = sleeve_length

    # Overriding display_info
    def display_info(self):
        super().display_info()
        print(f"Sleeve Length: {self._sleeve_length}")

    # Overloading calculate_price
    def calculate_price(self, discount=0):
        base_price = 50
        discounted_price = base_price - (base_price * discount / 100)
        return discounted_price

# Grandchild class
class FormalShirt(Shirt):
    def __init__(self, brand, size, sleeve_length, collar_type):
        super().__init__(brand, size, sleeve_length)
        self._collar_type = collar_type

    # Overriding display_info
    def display_info(self):
        super().display_info()
        print(f"Collar Type: {self._collar_type}")

    # Overloading calculate_price
    def calculate_price(self, discount=0, tax=0):
        base_price = super().calculate_price(discount)
        total_price = base_price + (base_price * tax / 100)
        return total_price

# Example usage
if __name__ == "__main__":
    shirt = Shirt("Nike", "L", 20)
    shirt.display_info()
    price = shirt.calculate_price(discount=10)
    print(f"Total Price: ${price}")

    formal_shirt = FormalShirt("Adidas", "M", 22, "Button-down")
    formal_shirt.display_info()
    total_price = formal_shirt.calculate_price(discount=15, tax=5)
    print(f"Total Price: ${total_price}")
