# Python standard lib
import json

# Third party
import click


def find_emoji(position):
    emojis = [
        (1, "🥶"),
        (900, "😎"),
        (990, "🥵"),
        (999, "🔥"),
        (1000, "😱"),
        (1001, "🥳"),
    ]

    if position is None:
        return emojis[0][1]

    for pos, emoji in emojis:
        if position < pos:
            return emoji


@click.command()
@click.option("-g", "--guesses-path", help="Path to guesses file")
def main(guesses_path):
    with open(guesses_path) as guesses_file:
        guesses = json.load(guesses_file)

    ordered_guesses = sorted(guesses, key=lambda g: g[3])

    padding = max([len(guess[1]) for guess in ordered_guesses])
    best_score = -101
    for score, word, pos, index in ordered_guesses:
        if score > best_score:
            print(
                f"{word:{padding}} {find_emoji(pos)} (score: {score:.2f}{f', pos: {pos}' if pos is not None else ''}), played as guess #{index}"
            )
            best_score = score


if __name__ == "__main__":
    main()
