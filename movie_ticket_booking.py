def movie_tickets():
    total_seats = int(input("Enter total seats: "))
    booked = list(map(int, input("Enter booked seats separated by spaces: ").split()))
    book = int(input("Enter seat number to book: "))
    cancel = int(input("Enter seat number to cancel: "))
    if book not in booked and 1 <= book <= total_seats:
        booked.append(book)
    if cancel in booked:
        booked.remove(cancel)
    available = [x for x in range(1, total_seats + 1) if x not in booked]
    print("Available seats:", available)

if __name__ == "__main__":
    movie_tickets()
