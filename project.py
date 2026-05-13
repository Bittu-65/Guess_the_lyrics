import lyricsgenius
import random

import os
genius = lyricsgenius.Genius(os.environ.get("GENIUS_API_KEY"))

def get_lyrics(song, artist):
    result = genius.search_song(song, artist)
    if result:
        return result.lyrics
    return None

def make_blank(line):
    words = line.split()
    if len(words) < 3:
        return None, None
    index = random.randint(1, len(words)-1)
    answer = words[index]
    words[index] = "_____"
    return " ".join(words), answer

def give_hint(answer, hints_used):
    if hints_used == 0:
        # hint 1 - first letter
        return f"First letter: {answer[0]}"
    elif hints_used == 1:
        # hint 2 - word length
        return f"Number of letters: {len(answer)}"
    elif hints_used == 2:
        # hint 3 - first and last letter
        return f"First and last letter: {answer[0]}{'_' * (len(answer)-2)}{answer[-1]}"
    else:
        return "No more hints available!"

def play_round(lyrics, round_num):
    lines = [l for l in lyrics.split("\n") if len(l.split()) >= 3]
    line = random.choice(lines)
    blanked, answer = make_blank(line)

    if not blanked:
        return 0

    print(f"\n--- Round {round_num} ---")
    print(f"Fill in the blank:\n{blanked}")

    hints_used = 0
    max_hints = 3
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        print(f"\nAttempts left: {max_attempts - attempts}")
        print(f"Hints left: {max_hints - hints_used}")
        print("(type 'hint' for a hint or 'skip' to skip)")

        guess = input("Your guess: ").strip()

        if guess.lower() == "skip":
            print(f"Skipped! Answer was: {answer}")
            return 0

        elif guess.lower() == "hint":
            if hints_used < max_hints:
                print(f"Hint: {give_hint(answer, hints_used)}")
                hints_used += 1
            else:
                print("No more hints!")

        elif answer and guess.lower() == answer.lower():
            if hints_used == 0:
                print("Perfect! No hints used! +3 points!")
                return 3
            elif hints_used == 1:
                print("Correct! +2 points!")
                return 2
            elif hints_used == 2:
                print("Correct! +1 point!")
                return 1
            else:
                print("Correct! But no points for using all hints!")
                return 0

        else:
            print("Wrong guess, try again!")
            attempts += 1

    print(f"Out of attempts! Answer was: {answer}")
    return 0

def main():
    print("=== Lyrics Guessing Game ===")
    song = input("Song name: ")
    artist = input("Artist name: ")

    print(f"\nSearching for {song} by {artist}...")
    lyrics = get_lyrics(song, artist)

    if not lyrics:
        print("Song not found! Try again.")
        return

    print(f"Found it! Let's play!\n")

    score = 0
    rounds = 5

    for i in range(rounds):
        score += play_round(lyrics, i+1)
        print(f"Current score: {score}")

    print(f"\n=== Game Over ===")
    print(f"Final score: {score}/{rounds * 3}")

    if score == rounds * 3:
        print("Perfect score! You're a lyrics genius!")
    elif score >= rounds * 2:
        print("Great job! You know your lyrics!")
    elif score >= rounds:
        print("Not bad! Keep listening!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
