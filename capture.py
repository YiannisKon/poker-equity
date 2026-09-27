import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import mss
import time

import numpy as np
import pygetwindow as gw

from table import CARD_W, CARD_H, BOARD_X_START, BOARD_Y, CARD_GAP, HERO_X_START, HERO_Y, WINDOW_H, WINDOW_W
from PIL import Image

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

WINDOW_TITLE = "Mock Poker Table"
CROP_DIR = "crops"

def find_table_window():
    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    if not windows:
        raise SystemError("Mock Poker Table not found. Is table.py running?")

    win = windows[0]
    try:
        win.activate()      # bring table window to the front
    except Exception:
        pass
    time.sleep(0.2)         # gives windows time to repaint it
    return win


def grab_window(win):
    region = {"left": win.left, "top": win.top, "width": win.width, "height": win.height}
    with mss.MSS() as sct:
        shot = sct.grab(region)
        return np.array(shot)

def client_offset(win):
    #pixel offset from window's outer top-left to the drawing are
    frame_h, frame_w = frame.shape[:2]
    border = (frame_w - WINDOW_W)//2
    title_bar = frame_h - WINDOW_H - border
    return (border, title_bar)

def crop_card(frame, x, y, offset):
    offset_x, offset_y = offset
    left = x + offset_x
    top = y + offset_y
    return (frame[top : top + CARD_H, left: left + CARD_W])

def crop_all(frame, offset):
    crops = {}

    for i in range(2):
        x = HERO_X_START + i * CARD_GAP
        crops[f"hero_{i}"] = crop_card(frame, x, HERO_Y, offset)

    for i in range(5):
        x = BOARD_X_START + i * CARD_GAP
        crops[f"board_{i}"] = crop_card(frame, x, BOARD_Y, offset)

    return crops

def save_crops(crops):
    os.makedirs(CROP_DIR, exist_ok=True)

    for name, arr in crops.items():
        rgb = arr[:, :, :3][:, :, ::-1]
        path = os.path.join(CROP_DIR, name + ".png")
        Image.fromarray(rgb).save(path)

if __name__ == "__main__":
    win = find_table_window()
    frame = grab_window(win)
    print("captured frame shape:", frame.shape)

    offset = client_offset(frame)
    crops = crop_all(frame, offset)
    save_crops(crops)
    print(f"Saved {len(crops)} crops to {CROP_DIR}/")
