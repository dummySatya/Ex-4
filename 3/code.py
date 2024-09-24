"""Program to show difference between __init__() and __call__()"""

# We use __call__() to make instances of class like a function
# We use __init__() to initialize an instance

# Example - Calculate the Average of a batsman in a test series

class AverageCalculator:
    """Calculates the average of batsman in test series"""

    def __init__(self, player_name):
        self.scores = []
        self.total_runs = 0
        self.innings = 0
        self.player_name = player_name

    def __call__(self, score):
        self.scores.append(score)
        self.total_runs += score
        self.innings += 1
        average = round(self.total_runs / self.innings, 2)
        print(f"Average of {self.player_name} is {average}")
        return average

def main():
    """List out players to calculated averages on the go"""

    sachin = AverageCalculator("Sachin")
    dhoni = AverageCalculator("Dhoni")
    dhoni(80)
    dhoni(30)
    sachin(100)
    sachin(39)
    sachin(64)
    dhoni(77)
    sachin(99)

if __name__ == "__main__":
    main()
