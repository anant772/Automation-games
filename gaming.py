import pyautogui
import keyboard
import time
import random

# List to store recorded positions
click_positions = [1116, 951]
click_positions2 = [(1335, 957), (1618, 576), (1271, 175), (863, 758), (1280, 178), (862, 772), (1294, 174), (861, 766), (1282, 183), (1002, 774), (1503, 402), (1249, 346)]
Longpointress = [(1099, 893), (1381, 424)]
xxx = 0

def record_clicks():
    print("Press 'r' to start recording clicks, and press 's' to stop.")
    while True:
        if keyboard.is_pressed('r'):
            x, y = pyautogui.position()  # Get current mouse position
            click_positions.append((x, y))
            print(f"Recorded click at: ({x}, {y})")
            time.sleep(0.3)  # Small delay to prevent multiple captures

        if keyboard.is_pressed('s'):
            print("Stopped recording.")
            break

def record_clicks2():
    print("Press 'r' to start recording clicks, and press 's' to stop.")
    while True:
        if keyboard.is_pressed('r'):
            x, y = pyautogui.position()  # Get current mouse position
            click_positions2.append((x, y))
            print(f"Recorded click at: ({x}, {y})")
            time.sleep(0.3)  # Small delay to prevent multiple captures

        if keyboard.is_pressed('s'):
            print("Stopped recording.")
            print(click_positions2)
            break

def replay_clicks():
    pyautogui.click(1116, 951)
    time.sleep(random.uniform(0.5, 1.5))  # Random delay between clicks
    

def replay_clicks2():
    c = 0
    for pos in click_positions2:
        if not( xxx % 6 == 0 and c == 11 ):
            pyautogui.click(pos[0], pos[1])
            time.sleep(2)
            time.sleep(random.uniform(0.5, 1.5))  # Random delay between clicks
        c = c + 1


def longCLick(x, y):
    """
    Move the mouse to a specific (x, y) coordinate and perform a click.

    :param x: The x-coordinate on the screen.
    :param y: The y-coordinate on the screen.
    """
    # Add a slight random offset to make the click less predictable
    x += random.randint(-2, 2)
    y += random.randint(-2, 2)
    
    # Move to the coordinate
    pyautogui.moveTo(x, y)


    pyautogui.mouseDown()  # Start holding down the mouse button
    time.sleep(0.1)          # Hold for 2 seconds
    pyautogui.mouseUp()

if __name__ == "__main__":
        while True:
            print("Welcome to gaming")
            if keyboard.is_pressed('s'):
                while True:
                    replay_clicks()  # Replay the recorded clicks in a loop
                    time.sleep(1)
                    for i in range(3):
                        longCLick(Longpointress[1][0], Longpointress[1][1])
                    time.sleep(1)
                    replay_clicks2()  # Replay the recorded clicks in a loop
                    time.sleep(1)
                    xxx = xxx + 1
