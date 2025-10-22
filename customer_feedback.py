def feedback_analysis():
    ratings = list(map(int, input("Enter ratings (1-5) separated by spaces: ").split()))
    if not ratings:
        print("No ratings available")
    else:
        positive = len([r for r in ratings if r >= 4])
        percent = (positive / len(ratings)) * 100
        print("Positive Feedback:", str(percent) + "%")

if __name__ == "__main__":
    feedback_analysis()
