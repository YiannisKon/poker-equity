# Poker-Equity Calculator

A command-line tool that computes the pre-flop win/tie probability for Texas Hold'em hands (2 card each). Built in pure Python as a personal project - argparse for CLI, pytest for testing.

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
```

Sample output:

```
81.9/18.1
```
Optional: '--trials N' (default 100,000).


## How it works

A Monte Carlo engine estimates equity by simulating 100,000 random boards (by default), converging on the true probabilities via the Law of Large Numbers. Each player's best hand is found by exhaustively evaluating all 21 five-card combinations of their 7 cards with a custom hand evaluator. Results are printed to 1 decimal place and validated against published pre-flop equities 
- e.g. AA vs KK ~= 81/19.

## Tests

```bash
pytest
```

Statistical tests run 20,000 trials with +/- 2-3% tolerance bands to keep the suite fast; deterministic tests cover the card model, evaluator, and hand parsing.