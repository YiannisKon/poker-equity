import os
import pygame
import argparse

from cards import Deck
from equity import parse_hand, parse_board
from make_assets import RANK_FILECHAR


WINDOW_W, WINDOW_H = 800, 600
CARD_W, CARD_H = 100, 140
GREEN = (0, 100, 0)

BOARD_Y = 230       # board row: vertical position
BOARD_X_START = 125 # left edge of the first board card
CARD_GAP = 110      # left-edge to left-edge spacing

HERO_Y = 430        # hero row
HERO_X_START = 295  # left edge of hero's first card


def card_filename(card):
    rank = RANK_FILECHAR.get(card.rank, str(card.rank))
    suit = card.suit[0]
    return rank + suit + ".png"

def load_card_image(card):
    path = os.path.join("assets", card_filename(card))
    return pygame.image.load(path)

def draw_table(screen, hero_cards, board_cards):
    screen.fill(GREEN)

    for i, card in enumerate(board_cards):
        img = load_card_image(card)
        x = BOARD_X_START + i*CARD_GAP
        screen.blit(img, (x, BOARD_Y))

    for i, card in enumerate(hero_cards):
        img = load_card_image(card)
        x = HERO_X_START + i*CARD_GAP
        screen.blit(img, (x, HERO_Y))

def random_deal(n_board):
    deck = Deck()
    deck.shuffle()
    hero = deck.deal(2)
    board = deck.deal(n_board)
    return hero, board


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render a mock poker table.")
    parser.add_argument("--hand", help="Hero's 2 cards, e.g. AhKh")
    parser.add_argument("--board", help="Board cards, e.g. Qh7h2c")
    parser.add_argument("--random", type=int, choices=[0, 3, 4, 5],
                        help="Deal a random hand with this many board cards")
    args = parser.parse_args()

    if args.random is not None:
        hero_cards, board_cards = random_deal(args.random)
    else:
        if not args.hand:
            raise SystemExit("Provide --hand (e.g. --hand AhKh) or --radom N")
        hero_cards = parse_hand(args.hand)
        board_cards = parse_board(args.board)

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))    
    pygame.display.set_caption("Mock Poker Table")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_table(screen, hero_cards, board_cards)
        pygame.display.flip()

    pygame.quit()