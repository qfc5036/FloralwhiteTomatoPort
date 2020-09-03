temperature = input ("Enter temperature: ")
temperature = float(temperature)
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  print("Converting Fahrenehit to Celsius.")
elif unit == "C" or unit == "c":
  print("Converting Celsius to Fahrenheit.")
else:
  print (f"Invalid unit(bad).")
print (str(temperature) + chr(176) + " in Celsius is equivalent to " + str(temperature *1.8 +32) + chr(176) + " Fahrenheit. ")