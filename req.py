import random


def generate_seed(word_list, word_count):
  seed = []
  while len(seed) < word_count:
    word_choice = random.choice(word_list)
    seed.append(word_choice)
  return seed


def read_wordlist(filename):
  """Reads words from a file.

  Args:
      filename: The path to the wordlist file.

  Returns:
      A list of words from the file.
  """
  try:
    with open(filename) as wordlist:
      return [line.strip() for line in wordlist]
  except FileNotFoundError:
    print(f"Error: Could not find wordlist file: {filename}")
    return None  # Indicate error


# Read word list from file
word_list = read_wordlist("wordlist.txt")  # Replace with your wordlist path
if not word_list:
  exit()  # Exit if error reading wordlist

# Ask for desired number of phrases
while True:
  try:
    num_phrases = int(input("How many phrases do you want to create? "))
    if num_phrases > 0:
      break
    else:
      print("Please enter a positive number of phrases.")
  except ValueError:
    print("Please enter a valid number.")

# Ask for desired number of words ONCE (outside the loop)
while True:
  try:
    num_words = int(input("How many words in EACH phrase? "))
    if num_words > 0:
      break
    else:
      print("Please enter a positive number of words.")
  except ValueError:
    print("Please enter a valid number.")

# Generate and save phrases
with open("phrase.txt", "w") as outfile:  # Open for writing
  for _ in range(num_phrases):
    seed = generate_seed(word_list, num_words)
    phrase = ' '.join(seed)
    outfile.write(phrase + "\n")  # Write each phrase with a newline
  print(f"Phrases saved successfully to phrase.txt")
