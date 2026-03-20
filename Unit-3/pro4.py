class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        # Creating an instance of the inner class inside the outer class
        self.gadget = self.Laptop()

    def show_info(self):
        print(f"Doctor: {self.name} | Specialty: {self.specialty}")
        # Accessing the inner class method
        self.gadget.show_specs()

    # --- Inner Class ---
    class Laptop:
        def __init__(self):
            self.brand = "Apple"
            self.cpu = "M3"
            self.ram = "16GB"

        def show_specs(self):
            print(f"System: {self.brand}, {self.cpu}, {self.ram}")

# --- Execution ---

# 1. Create the outer class object
doc1 = Doctor("Dr. Smith", "Cardiology")
doc1.show_info()

# 2. You can also instantiate the inner class directly (if needed)
# though it's less common:
external_laptop = Doctor.Laptop()