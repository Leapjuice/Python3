# Sal's Shipping
# Written by Andrew Talbot
# Website: andrewtalbot.org

weight = 4.8
price = 0.0
ground_flat = 20.00
ground_premium = 125.00
drone_flat = 0.0
shipping_method = 1

if shipping_method == 1:

# Ground Shipping

  if weight <= 2.0:
    price = (weight * 1.5) + ground_flat
  elif (weight > 2.0) and (weight <= 6.0):
    price = (weight * 3) + ground_flat
  elif (weight > 7) and (weight <= 10):
    price = (weight * 4) + ground_flat
  elif weight > 10:
    price = (weight * 4.75) + ground_flat

elif shipping_method == 3:
# Drone Shipping

  if weight <= 2.0:
    price = (weight * 4.5) + drone_flat
  elif (weight > 2.0) and (weight <= 6.0):
    price = (weight * 9.0) + drone_flat
  elif (weight > 7) and (weight <= 10):
    price = (weight * 12.0) + drone_flat
  elif weight > 10:
    price = (weight * 14.25) + drone_flat


print(price)
print("Ground Premium Shipping costs: " + str(ground_premium))
