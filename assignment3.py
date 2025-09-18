import json

# Animal Question Tree Node
class Node:
    def __init__(self, question=None, animal=None, yes=None, no=None):
        self.question = question
        self.animal = animal # which is used when the node is a leaf
        self.yes = yes # left child
        self.no = no # right child

# print the tree(pre-order traversal)
def print_tree(node, depth=0): 
    if node is not None:
        print(" " * 4 * depth + "-> " + (node.question if node.question else node.animal))
        print_tree(node.yes, depth + 1)
        print_tree(node.no, depth + 1)

        
# Command-line interface for The Animal Guessing Game    
def repl() -> None:
    root = load()                     
    print("The Animal Guessing Game! Think of an animal.")
    while True:
        curr = root                   
        while True:
            if curr.question is not None:
                answer = input(curr.question + " (y/n) ").strip().lower()
                if answer == "y":
                    curr = curr.yes
                elif answer == "n":
                    curr = curr.no
                elif answer in ("exit", "quit"):
                    print("Exiting the game. Goodbye!")
                    return
                elif answer == "print":
                    print_tree(root)
                else:
                    print("Please answer with 'y' or 'n'.")
                continue

            # guess the animal
            final_answer = input(f"Is it a {curr.animal}? (y/n) ").strip().lower()
            if final_answer == "y":
                print("Yay! I guessed it right!")
            elif final_answer == "n":
                print("I give up! What animal were you thinking of?")
                animal = input().strip()

                print(f'Enter a yes/no question that distinguishes a {animal} from a {curr.animal}:')
                question = input().strip()

                # ask which answer corresponds to the new animal
                yn = input(f'For a {animal}, what is the answer to "{question}"? (y/n) ').strip().lower()
                if yn not in ("y", "n"):
                    print("Please answer with 'y' or 'n'. Let's try that round again.")
                    continue

                # replace current leaf with new question node
                old = curr.animal
                curr.question = question
                if yn == "y":
                    curr.yes = Node(animal=animal)
                    curr.no  = Node(animal=old)
                else:
                    curr.yes = Node(animal=old)
                    curr.no  = Node(animal=animal)
                curr.animal = None

                save(root)        
                print("Thanks! I've learned something new.")
            else:
                print("Please answer with 'y' or 'n'.")
                continue

            # End of round: ask to play again
            a = input("Press 'r' to play again, or any other key to quit: ").strip().lower()
            if a == 'r':
                print("Starting a new game! Think of an animal.")
                break                 
            else:
                print("Exiting the game. Goodbye!")
                return

"""
Helper functions to save/load the tree to/from a JSON file.
"""
def to_dict(node):
    if node is None:
        return None
    if node.animal:  # leaf node
        return {"animal": node.animal}
    return {
        "question": node.question,
        "yes": to_dict(node.yes),
        "no": to_dict(node.no)
    }

def from_dict(data):
    if "animal" in data:
        return Node(animal=data["animal"])
    return Node(
        question=data["question"],
        yes=from_dict(data["yes"]),
        no=from_dict(data["no"])
    )

def save(root):
    with open("animal_tree.json", "w") as f:
        json.dump(to_dict(root), f)

def load():
    with open("animal_tree.json", "r") as f:
        try:
            data = json.load(f)
            return from_dict(data)
        except:
            return None
            
if __name__ == "__main__":
    repl()

