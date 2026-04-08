class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def convertFahrenheit(self):
        # Formula: (Celsius * 9/5) + 32
        result = (self.temp * 9/5) + 32
        return f"{self.temp}°C is {result}°F"

    def convertCelsius(self):
        # Formula: (Fahrenheit - 32) * 5/9
        result = (self.temp - 32) * 5/9
        return f"{self.temp}°F is {result}°C"

# Usage
t1 = Temperature(37)
print(t1.convertFahrenheit())