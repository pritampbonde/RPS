import random

def player(prev_play, opponent_history=[]):
    # Define a list of possible moves
    moves = ["R", "P", "S"]

    # If it's the first game or opponent history is not provided, start with a random move
    if not prev_play or not opponent_history:
        return random.choice(moves)

    # Define a dictionary to keep track of opponent's moves frequency
    opp_moves_freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        opp_moves_freq[move] += 1

    # Determine the opponent's most frequent move
    opp_most_freq_move = max(opp_moves_freq, key=opp_moves_freq.get)

    # Choose the move that beats the opponent's most frequent move
    if opp_most_freq_move == "R":
        return "P"
    elif opp_most_freq_move == "P":
        return "S"
    else:
        return "R"
