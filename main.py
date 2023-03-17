def convert_weight_on_planet(weight, planet):
    # Gravity relative to Earth
    gravity = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Earth": 1.00,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19
    }

    # Calculate weight on planet
    weight_on_planet = weight * gravity[planet]
    return weight_on_planet

# Example usage
weight = float(input("Enter your weight on Earth in kg: "))
planet = input("Enter the planet you want to convert your weight to: ")
weight_on_planet = convert_weight_on_planet(weight, planet)
print(f"Your weight on {planet} is {weight_on_planet:.2f} kg.")