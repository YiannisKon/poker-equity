# Poker Equity Calculator

A command-line tool that computes win probabilities for Texas Hold'em hands. For heads-up matchups where both hands are known, the engine **exhaustively enumerates every possible board runout** to produce exact equities. For a "hero" hand against N random opponents, it switches to **Monte Carlo simulation**, converging on the true probabilities via the Law of Large Numbers. Both modes work at any street: pre-flop, flop, turn, and river.

Built in pure Python as a personal project — argparse for the CLI, pytest for testing. A computer-vision extension (pygame table renderer + OpenCV card recognition) is in active development.

## Install

```
git clone https://github.com/YiannisKon/poker-equity.git
cd poker-equity
python -m venv venv
./venv/Scripts/activate     # Windows
pip install -r requirements.txt
```

## Usage

```
python equity.py --hand_1 AsAh --hand_2 KdKc
python equity.py --hand_1 AhKh --hand_2 QdQc --board Qh7h2c
python equity.py --hand_1 AhKh --opponents 3 --board Qh7h2c
```

Sample output:

```
81.9/18.1
25.7/74.3
52.2
```

Options:
- `--hand_2 <hand>` — second known hand (default: None; omit to play against random opponents)
- `--opponents N` — number of random opponents (default: 1)
- `--board <cards>` — partial or full board (flop, turn, or river)
- `--trials N` — Monte Carlo trial count (default: 100,000; ignored when exact enumeration applies)

## How it works

When both hands are known heads-up, the remaining board cards are fully enumerated, so the result is exact — no sampling error. Against random opponents the space is too large to enumerate, so the engine deals random hands and runouts across 100,000 trials by default. In both modes, each player's best hand is found by evaluating all 21 five-card combinations of their 7 cards with a custom hand evaluator.

Results are printed to 1 decimal place and validated against published equities:

* AA vs KK ≈ 81/19
* AKs vs QQ ≈ 46/54
* AA vs 4 random opponents ≈ 55

## Computer vision extension (in progress)

The next phase reads hands directly off a table instead of taking CLI input:

- **Card assets** — `make_assets.py` generates all 52 card images with Pillow *(done)*
- **Mock table** — a pygame window renders a hero hand and board at fixed layout coordinates *(in progress)*
- **Recognition** — screen capture, region cropping, and OpenCV template matching identify the cards and feed them into the equity engine *(planned)*

The pipeline demos against the self-built table window rather than a real poker client, which keeps the recognition problem well-defined and the project self-contained.

## Tests

```
pytest
```

Tests cover the card model, hand evaluator, equity simulation, and hand/board parsing. Statistical tests run 20,000 trials to keep the suite fast, with ±2–3% tolerance bands because Monte Carlo output varies between runs. Deterministic edge cases (a locked river board must score exactly 100; a board that plays for both players must score exactly 50/50) need no tolerance at all because the randomness is collapsed by construction.