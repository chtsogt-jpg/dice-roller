import random

def roll_d6():
    """Roll a single D6 dice (1-6)"""
    return random.randint(1, 6)

def main():
    print("=" * 30)
    print("      D6 DICE ROLLER")
    print("=" * 30)

    while True:
        input("\nPress Enter to roll the dice (or Ctrl+C to quit)...")

        result = roll_d6()

        # Display the dice face
        dice_faces = {
            1: "[ . ]",
            2: "[. .]",
            3: "[...]",
            4: "[: :]",
            5: "[:·:]",
            6: "[::]"
        }

        print(f"\nYou rolled: {dice_faces[result]}")
        print(f"Result: {result}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThanks for playing!")
