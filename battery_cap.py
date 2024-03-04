print("Battery Pack Specifications")

# Power Consumption in Watts of device (Rasberry Pi)
DeviceName = "Rasberry Pi4"
PowerConsumption = 6

# milliamp hours of battery pack
mAh = 42800
print(str(mAh) + " mAh")

# Voltage of Battery Pack
v = 5
print(str(v) + " Volts")


# Battery Capacity, usually given in miliamp-hours (mAh), we want Watt Hours (Wh)
def BatteryCapacity(mAh, v):
    x = (mAh * v)
    Capacity = x/1000
    return Capacity


def Runtime():
    RunTime_hrs = BatteryCapacity(mAh, v) / PowerConsumption
    return RunTime_hrs


print("\nBased on the Expected power consumption of:")
print(str(PowerConsumption) + " Watts")

print(DeviceName + " Will run for")
print(str(Runtime())+" Hours")
