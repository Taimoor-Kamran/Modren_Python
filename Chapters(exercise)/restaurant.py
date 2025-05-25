class Restaurant:
    def __init__(self, name: str, cuisine_type: str) -> None:
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}" )
        print(f"Restaurant Type: {self.cuisine_type}")

    
    def open_restaurent(self):
        print(f"{self.name} is now open.")

