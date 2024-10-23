# utils.py (helper.py)
import pickle

def save_trie(trie, filename="trie.pkl"):
    """Saves the Trie object to a pickle file."""
    with open(filename, 'wb') as file:  # 'wb' means write in binary mode
        pickle.dump(trie, file)

def load_trie(filename="trie.pkl"):
    """Loads the Trie object from a pickle file."""
    with open(filename, 'rb') as file:  # 'rb' means read in binary mode
        return pickle.load(file)
