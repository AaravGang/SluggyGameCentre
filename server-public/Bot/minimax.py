
def minimax(position, depth, alpha, beta, is_maximising):
    if depth == 0 or position.game_over():
        return position.eval()

    if is_maximising:
        max_eval = -float("inf")
        for child in position.child():
            eval = minimax(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float("inf")
        for child in position.child():
            eval = minimax(child, depth-1, alpha, beta, True)
            min_eval = max(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval
