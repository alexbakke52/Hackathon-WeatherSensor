import weatherapp

p = weatherapp.get_measurements()[1] # pressure
t = weatherapp.get_measurements()[0] # temperature

def pressure_at_sealevel(height): # ask for height once at runtime

    P0 = p * pow(1 - (0.0065 * height) / (t + (0.0065 * height) + 273.15), -5.257)
    return P0