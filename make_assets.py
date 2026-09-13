from cards import Deck
from PIL import Image, ImageDraw, ImageFont
import os


SUIT_SYMBOLS = {"hearts": "♥", "diamonds": "♦", "clubs": "♣", "spades": "♠"}
SUIT_COLOURS = {"hearts": "red", "diamonds": "red", "clubs": "black", "spades": "black"}
RANK_DISPLAY = {11: "J", 12: "Q", 13: "K", 14: "A"}
RANK_FILECHAR = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}


if __name__ == "__main__":
        
    font_big = ImageFont.truetype("arial.ttf", 60)
    font_small = ImageFont.truetype("arial.ttf", 28)

    os.makedirs("assets", exist_ok=True)

    for card in Deck().cards:
        colour = SUIT_COLOURS[card.suit]

        img = Image.new("RGB", (100, 140), "white")
        draw = ImageDraw.Draw(img)

        display = RANK_DISPLAY.get(card.rank, str(card.rank))
        draw.text((8,5), display, fill=colour, font=font_small)

        symbol = SUIT_SYMBOLS[card.suit]
        draw.text((32, 45), symbol, fill=colour, font=font_big)

        filechar = RANK_FILECHAR.get(card.rank, str(card.rank))
        filename = filechar + card.suit[0] + ".png"
        img.save(os.path.join("assets", filename))

    print("Done - 52 cards in assets/")