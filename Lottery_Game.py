class LotteryGame:
    def __init__(self):
        self.winning_numbers = set()
        self.player_numbers = set()

    def set_winning_numbers(self):
        """Input 6 winning numbers manually (1–60)."""
        print("Enter the 6 WINNING numbers (1–60):")
        while len(self.winning_numbers) < 6:
            try:
                num = int(input(f"Winning number {len(self.winning_numbers)+1}: "))
                if num < 1 or num > 60:
                    print("Number must be between 1 and 60.")
                elif num in self.winning_numbers:
                    print("Duplicate! Enter a different number.")
                else:
                    self.winning_numbers.add(num)
            except ValueError:
                print("Invalid input. Enter an integer.")

    def set_player_numbers(self):
        """Input 6 player numbers manually (1–60)."""
        print("\nEnter YOUR 6 numbers (1–60):")
        while len(self.player_numbers) < 6:
            try:
                num = int(input(f"Your number {len(self.player_numbers)+1}: "))
                if num < 1 or num > 60:
                    print("Number must be between 1 and 60.")
                elif num in self.player_numbers:
                    print("Duplicate! Enter a different number.")
                else:
                    self.player_numbers.add(num)
            except ValueError:
                print("Invalid input. Enter an integer.")

    def check_matches(self):
        """Return matched numbers as a set."""
        return self.player_numbers & self.winning_numbers

    def calculate_prize(self, match_count):
        """Compute prize based on number of matches."""
        if match_count == 6:
            return 1_000_000
        return match_count * 1000

    def display_results(self):
        """Show lottery results."""
        matches = self.check_matches()
        match_count = len(matches)
        prize = self.calculate_prize(match_count)

        print("\n=== Lottery Results ===")
        print(f"Winning Numbers: {sorted(self.winning_numbers)}")
        print(f"Your Numbers:   {sorted(self.player_numbers)}")
        print(f"Matched Numbers: {sorted(matches) if matches else 'None'}")
        print(f"Total Matches: {match_count}")
        print(f"Prize: ₱{prize:,}")

game = LotteryGame()
game.set_winning_numbers()
game.set_player_numbers()
game.display_results()
