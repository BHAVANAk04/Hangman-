import random
 
def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if correct_guess == False:
        print(f"There is no {guess}, sorry.")
        update_display += 1
    x = 0
 
 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
word_list = ["apple", "ball", "cat", "dog", "egg", "fish", "grape", "hat", "ice", "juice", "kite", "lion", "milk", "nose", "orange", "pen", "queen", "rabbit", "sun", "tree", "umbrella", "van", "water",  "yarn", "zebra", "air", "boat", "car", "door", "eye", "fan", "game", "home", "idea", "jump", "key", "lamp", "moon", "net", "ocean", "plate", "quiet", "rose", "star", "table", "under", "voice", "wall", "yard", "zero", "above", "below", "child", "drive", "earth", "family", "garden", "happy", "inside", "join", "kind", "love", "music", "number", "open", "people", "quick", "river", "small", "talk", "use", "visit", "wait", "young", "zoo", "animal", "bright", "clean", "dance", "early", "funny", "green", "house", "insect", "jungle", "king", "light", "mountain", "new", "order", "party", "quietly", "round"]
 
chosen_word = list(random.choice(word_list))
 
blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)
 
update_display = 0
 
#----------------------------------------------------------------------------------------------
 
print(HANGMANPICS[update_display])
guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
making_a_guess()
print(HANGMANPICS[update_display])
print(''.join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print("YOU WIN!")
        break
    guess = input("Make another guess? ")
    making_a_guess()
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))
if update_display == 6:
    print("GAME OVER.")