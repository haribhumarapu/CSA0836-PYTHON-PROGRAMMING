taxi_number = [101, 102, 103]
passenger_name = ["Alice", "Bob", "Charlie"]
km_travelled = [15, 7, 12]
rate_per_km = 10
bill_amount = [km * rate_per_km for km in km_travelled]
print(f"{'Taxi Number':<12} {'Passenger Name':<15} {'Km Travelled':<15} {'Bill Amount':<12}")
for i in range(len(taxi_number)):
    print(f"{taxi_number[i]:<12} {passenger_name[i]:<15} {km_travelled[i]:<15} {bill_amount[i]:<12}")
