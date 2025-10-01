class MatingGame:
    def __init__(self, name1, name2):

        self.name1 = name1.lower().replace(" ", "")
        self.name2 = name2.lower().replace(" ", "")

    def calculate(self):

        name1_list = list(self.name1)
        name2_list = list(self.name2)

        i = 0
        while i < len(name1_list):
            ch = name1_list[i]
            if ch in name2_list:
                name1_list.pop(i)
                name2_list.remove(ch)
            else:
                i += 1

        # Count remaining letters
        count = len(name1_list) + len(name2_list)

        # Special Case
        if count == 0:
            return "Not compatible! Single forever </3"

        # FLAMES elimination
        flames = ["F", "L", "A", "M", "E", "S"]
        index = 0
        while len(flames) > 1:
            index = (index + count - 1) % len(flames)
            flames.pop(index)

        #  Map result
        mapping = {
            "F": "Friendship",
            "L": "Love",
            "A": "Affection",
            "M": "Marriage",
            "E": "Enemy",
            "S": "Sibling"
        }
        return mapping[flames[0]]


# Example usage
if __name__ == "__main__":
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    game = MatingGame(name1, name2)   # create an object
    result = game.calculate()         # call method
    print("\nResult:", result)
