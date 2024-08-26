from chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)