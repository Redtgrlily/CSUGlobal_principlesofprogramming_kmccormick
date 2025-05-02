#Part 1 - The check, please.
food_charge = float(input("What is the price for the food?: $"))

tip = food_charge * 0.18
tax = food_charge * 0.07

total = food_charge + tip + tax

print(f"\nFood Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total Amount: ${total:.2f}")

#Part 2 - Army Dad Alarm Clock
current_time = int(input("What time is it? (0-23)"))
wait_hours = int(input("Please tell army dad to be quiet until: "))

alarm_time = (current_time + wait_hours) % 24

print(f"\nArmy Dad, go back to bed. We wake up at {alarm_time}:00 hours.")