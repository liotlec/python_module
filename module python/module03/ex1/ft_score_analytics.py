
import sys

def main():
    print("=== Player Score Analytics ===")
    a = 0
    if len(sys.argv) <= 2:
        raise ValueError(f"No scores provided. Usage: ft_score_analytics.py <score1> <score2> ...")
    scores = []
    for i in range(1, len(sys.argv)):
        try:
            score = float(sys.argv[i])
            scores.append(score)
        except ValueError:
            raise ValueError(f"No scores provided!")
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Range of scores:", max(scores) - min(scores))

main()
