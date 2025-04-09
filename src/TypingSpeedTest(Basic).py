import time
import random

# Sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help improve your accuracy.",
    "Python is a fun programming language to learn.",
    "Practice makes perfect when it comes to typing.",
    "Fast typing requires good hand-eye coordination."
]

def typing_test():
    print("📘 Typing Speed Test")
    print("-" * 40)
    
    # Force Enter key only
    while True:
      ready = input("\nPress Enter when you're ready...")
      if ready == "":
          break
      else:
        print("❗ Please do not type anything. Just press Enter to start.")
   
    sentence = random.choice(sentences)
    print(f"\nType this sentence:\n\n➡️  {sentence}")

    print("\nStart typing below:\n")
    start_time = time.time()
    user_input = input("Your input: ")
    end_time = time.time()

    time_taken = end_time - start_time
    time_in_minutes = time_taken / 60

    word_count = len(user_input.split())
    wpm = word_count / time_in_minutes

    # Calculate correct characters and total characters typed
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(chosen_sentence) and c == chosen_sentence[i])
    total_chars = max(len(user_input), len(chosen_sentence))
    accuracy = (correct_chars / total_chars) * 100

    print("\n⏱️ Results")
    print("-" * 40)
    print(f"Time Taken     : {round(time_taken, 2)} seconds")
    print(f"Words Per Min  : {round(wpm, 2)} WPM")
    print(f"Accuracy       : {round(accuracy, 2)}%")

# Run the test
typing_test()