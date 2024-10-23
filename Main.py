from Trie import Trie
from Helper import save_trie, load_trie
import os

# Path to your dictionary file (a text file with one word per line)
dictionary_file = 'words.txt'
# Path to the saved trie file
pickle_file = 'trie.pkl'

def build_trie_from_file(filename):
    trie = Trie()
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            trie.insert(word)
    return trie

def main():
    if os.path.exists(pickle_file):
        # Load the trie from the pickle file if it exists
        print("Loading the trie from saved pickle file...")
        trie = load_trie(pickle_file)
    else:
        # Build the trie from the dictionary file and save it
        print(f"Building the trie from {dictionary_file}...")
        trie = build_trie_from_file(dictionary_file)
        save_trie(trie, pickle_file)
        print("Trie saved to pickle file.")

    while True:
        word = input("\nEnter a word to check (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            break

        if trie.search(word):
            print(f"'{word}' is spelled correctly.")
        else:
            suggestions = trie.suggest(word)
            if suggestions:
                print(f"Did you mean: {', '.join(suggestions)}?")
            else:
                print(f"No suggestions found for '{word}'.")

if __name__ == "__main__":
    main()