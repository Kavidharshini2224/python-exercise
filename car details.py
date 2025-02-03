

class Car:
    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
        self.engine_started = False 

    def start_engine(self):
        """Start the engine of the car."""
        if not self.engine_started:
            self.engine_started = True
            print(f"The engine of the {self.year} {self.make} {self.model} has started.")
        else:
            print("The engine is already running.")

    def stop_engine(self):
        """Stop the engine of the car."""
        if self.engine_started:
            self.engine_started = False
            print(f"The engine of the {self.year} {self.make} {self.model} has stopped.")
        else:
            print("The engine is already off.")

    def car_info(self):
        """Display information about the car."""
        status = "running" if self.engine_started else "off"
        print(f"{self.year} {self.make} {self.model} (Engine: {status})")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)


car1.start_engine()  
car1.car_info()  
car1.stop_engine() 
car1.car_info()   
car2.start_engine()  
car2.car_info() 
