def taxi_fare():
    trips = list(map(int, input("Enter distances for trips (in km) separated by spaces: ").split()))
    total_fare = 0
    for i in range(len(trips)):
        fare = 50 + 10 * trips[i]
        total_fare += fare
        print("Trip", i + 1, ":", "$", fare)
    print("Total Fare: $", total_fare)

if __name__ == "__main__":
    taxi_fare()
