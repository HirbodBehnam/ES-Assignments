from enum import IntEnum
import random
import time

def generate_next_temp(previous_temp: int) -> int:
    time.sleep(1)
    # Act like Math.Clamp is C#
    return min(max(previous_temp + random.randint(-5, 5), -10), 50)

print("We are going to simulate the cooling system until you press Ctrl + C!")
print("Starting with initial temp of 30")

# State definitions
class MainStates(IntEnum):
    NORMAL = 1
    WARM = 2
    COLD = 3

class CoolerRPS(IntEnum):
    RPS4 = 4
    RPS6 = 6
    RPS8 = 8
    OUT = 0

class HeaterIntensity(IntEnum):
    HEATER1 = 1
    HEATER2 = 2
    HEATER3 = 3
    OUT = 0

# Initial variables
current_temp = 30
previous_main_state = MainStates.NORMAL
next_main_state = MainStates.NORMAL
previous_cooler_state = CoolerRPS.OUT
next_cooler_state = CoolerRPS.OUT
previous_heater_state = HeaterIntensity.OUT
next_heater_state = HeaterIntensity.OUT

# Simulate!
while True:
    match previous_main_state:
        case MainStates.NORMAL:
            print("Heater and cooler are off")
            current_temp = generate_next_temp(current_temp)
            print("Generated", current_temp, "as next temp")
            if current_temp < 15:
                next_main_state = MainStates.COLD
            elif current_temp > 35:
                next_main_state = MainStates.WARM
        case MainStates.COLD:
            print("Heater is on")
            previous_heater_state = HeaterIntensity.HEATER1
            while previous_heater_state != HeaterIntensity.OUT:
                print("Heater intensity is", int(previous_heater_state))
                current_temp = generate_next_temp(current_temp)
                print("Generated", current_temp, "as next temp")
                match previous_heater_state:
                    case HeaterIntensity.HEATER1:
                        if current_temp > 30:
                            next_heater_state = HeaterIntensity.OUT
                        elif current_temp < 10:
                            next_heater_state = HeaterIntensity.HEATER2
                    case HeaterIntensity.HEATER2:
                        if current_temp > 20:
                            next_heater_state = HeaterIntensity.HEATER1
                        elif current_temp < 0:
                            next_heater_state = HeaterIntensity.HEATER3
                    case HeaterIntensity.HEATER3:
                        if current_temp > 10:
                            next_heater_state = HeaterIntensity.HEATER2
                previous_heater_state = next_heater_state
            next_main_state = MainStates.NORMAL
        case MainStates.WARM:
            print("Cooler is on")
            previous_cooler_state = CoolerRPS.RPS4
            while previous_cooler_state != CoolerRPS.OUT:
                print("Cooler RPS is", int(previous_cooler_state))
                current_temp = generate_next_temp(current_temp)
                print("Generated", current_temp, "as next temp")
                match previous_cooler_state:
                    case CoolerRPS.RPS4:
                        if current_temp < 25:
                            next_cooler_state = CoolerRPS.OUT
                        elif current_temp > 40:
                            next_cooler_state = CoolerRPS.RPS6
                    case CoolerRPS.RPS6:
                        if current_temp < 35:
                            next_cooler_state = CoolerRPS.RPS4
                        elif current_temp > 45:
                            next_cooler_state = CoolerRPS.RPS8
                    case CoolerRPS.RPS8:
                        if current_temp < 40:
                            next_cooler_state = CoolerRPS.RPS6
                previous_cooler_state = next_cooler_state
            next_main_state = MainStates.NORMAL
    previous_main_state = next_main_state