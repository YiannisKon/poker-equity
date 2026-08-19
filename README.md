# Poker-Equity Calculator

A command-line tool that computes win probabilities for Texas Hold'em hands (2 cards each) via a Monte Carlo simulation. The program is capable of accurately predicting the equity between 2 players whose hands are known and also the equity of a "hero" player whose cards are known against N random opponents. Outcomes can be calculated for any poker scenario: Pre-flop, Flop, Turn, and River.
Built in pure Python as a personal project - argparse for CLI, pytest for testing.

## Install

```bash
git clone https://github.com/YiannisKon/poker-equity.git
cd poker-equity
python -m venv venv
./venv/Scripts/activate     #Windows
pip install -r requirements.txt
```

## Usage

```bash
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
Optional: '--trials N'      (default: 100,000)
          '--opponents N'   (default: 1)
          '--hand_2 (hand)' (default: None)

## How it works

A Monte Carlo engine estimates equity by simulating 100,000 random outcomes (by default), converging on the true probabilities via the Law of Large Numbers. Each player's best hand is found by exhaustively evaluating all 21 five-card combinations of their 7 cards with a custom hand evaluator. Results are printed to 1 decimal place and validated against published equities.
- AA vs KK  ~= 81/19
- AKs vs QQ ~= 46/54
- AA vs 4 random opponents ~= 55

## Tests

```bash
pytest
```
Tests cover the card model, hand evaluator, equity simulation, and hand/board parsing. Statistical tests run 20,000 trials to keep the suite fast, with +/- 2-3% tolerance bands because Monte Carlo output varies between runs. Deterministic edge cases  (a locked river board must score exactly 100; a board that plays for both players must score exactly 50/50) need no tolerance at all because the randomness is collapsed by construction.