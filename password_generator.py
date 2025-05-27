#!/usr/bin/env python3
"""
Number Guessing Game
===================
A fun guessing game with different difficulty levels
"""

import random

def display_welcome():
    """Display welcome message and rules"""
    print("🎯 Welcome to the Number Guessing Game!")
    print("=" * 40)
    print("🎮 How to play:")
    print("• I'll think of a number in your chosen range")
    print("• You guess the number")
    print("• I'll give you hints (higher/lower)")
    print("• Try to guess in as few attempts as possible!")
    print("=" * 40)

def choose_difficulty():
    """Let player choose difficulty level"""
    print("\n🎚️ Choose difficulty:")
    print("1. Easy (1-50, unlimited guesses)")
    print("2. Medium (1-100, 10 guesses)")
    print("3. Hard (1-500, 12 guesses)")
    print("4. Expert (1-1000, 15 guesses)")
    
    while True:
        try:
            choice = int(input("Select difficulty (1-4): "))
            if choice == 1:
                return 1, 50, float('inf')
            elif choice == 2:
                return 1, 100, 10
            elif choice == 3:
                return 1, 500, 12
            elif choice == 4:
                return 1, 1000, 15
            else:
                print("❌ Please choose 1-4!")
        except ValueError:
            print("❌ Please enter a valid number!")

def get_guess(min_num, max_num):
    """Get a valid guess from the player"""
    while True:
        try:
            guess = int(input(f"🤔 Enter your guess ({min_num}-{max_num}): "))
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"❌ Please guess between {min_num} and {max_num}!")
        except ValueError:
            print("❌ Please enter a valid number!")

def give_hint(guess, target, attempts):
    """Provide hints based on the guess"""
    difference = abs(guess - target)
    
    if difference == 0:
        return "🎉 Correct!"
    elif difference <= 5:
        return "🔥 Very close!"
    elif difference <= 10:
        return "🌡️ Getting warm!"
    elif difference <= 25:
        return "❄️ Getting cold!"
    else:
        return "🧊 Very cold!"

def calculate_score(attempts, max_attempts, difficulty_multiplier):
    """Calculate player score based on performance"""
    if attempts == 1:
        return 1000 * difficulty_multiplier
    elif attempts <= max_attempts // 3:
        return 750 * difficulty_multiplier
    elif attempts <= max_attempts // 2:
        return 500 * difficulty_multiplier
    elif attempts <= max_attempts:
        return 250 * difficulty_multiplier
    else:
        return 0

def play_game():
    """Main game logic"""
    min_num, max_num, max_attempts = choose_difficulty()
    target_number = random.randint(min_num, max_num)
    attempts = 0
    guessed_numbers = []
    
    # Difficulty multiplier for scoring
    difficulty_multipliers = {50: 1, 100: 2, 500: 3, 1000: 4}
    difficulty_multiplier = difficulty_multipliers[max_num]
    
    print(f"\n🎲 I'm thinking of a number between {min_num} and {max_num}")
    if max_attempts != float('inf'):
        print(f"⏰ You have {max_attempts} guesses!")
    print("🚀 Let's start!\n")
    
    while attempts < max_attempts:
        attempts += 1
        
        # Show remaining attempts
        if max_attempts != float('inf'):
            remaining = max_attempts - attempts + 1
            print(f"📊 Attempt {attempts}/{max_attempts} (Remaining: {remaining})")
        else:
            print(f"📊 Attempt {attempts}")
        
        # Show previous guesses
        if guessed_numbers:
            print(f"🔍 Previous guesses: {', '.join(map(str, guessed_numbers))}")
        
        guess = get_guess(min_num, max_num)
        guessed_numbers.append(guess)
        
        if guess == target_number:
            print("\n" + "🎉" * 20)
            print(f"🏆 CONGRATULATIONS! You found the number!")
            print(f"🎯 The number was: {target_number}")
            print(f"📈 You guessed it in {attempts} attempts!")
            
            # Calculate and show score
            score = calculate_score(attempts, max_attempts, difficulty_multiplier)
            print(f"⭐ Your score: {score} points")
            
            if attempts == 1:
                print("🎭 INCREDIBLE! First try - you're a mind reader!")
            elif attempts <= 3:
                print("🌟 AMAZING! You're really good at this!")
            elif attempts <= 5:
                print("👏 GREAT JOB! Nice guessing skills!")
            else:
                print("🎯 WELL DONE! You got there in the end!")
            
            return True
        else:
            # Provide hints
            if guess < target_number:
                direction = "📈 Too low! Go higher."
            else:
                direction = "📉 Too high! Go lower."
            
            hint = give_hint(guess, target_number, attempts)
            print(f"{direction} {hint}\n")
    
    # Game over - out of attempts
    print("\n💥 Game Over!")
    print(f"😅 You've used all {max_attempts} attempts!")
    print(f"🎯 The number was: {target_number}")
    print("💪 Better luck next time!")
    return False

def main():
    """Main function to run the game"""
    display_welcome()
    
    while True:
        won = play_game()
        
        print("\n" + "=" * 40)
        play_again = input("🔄 Play again? (y/n): ").lower().strip()
        
        if not play_again.startswith('y'):
            print("\n👋 Thanks for playing!")
            print("🎮 Come back anytime for more guessing fun!")
            break
        
        print("\n" + "🎮" * 20)

if __name__ == "__main__":
    main()
