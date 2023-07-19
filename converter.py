print("How many kilometers did you cycle today?")
distance = input()
miles = float(distance) / 1.60934
miles = round(miles, 3)
print(f"That is equal to {miles} miles")