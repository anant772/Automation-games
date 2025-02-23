import pyautogui
import keyboard
import time
import random

points = []
storageX = 500
storageY = 500

def record_point():
    """Record the current mouse position."""
    x, y = pyautogui.position()
    print(f"Recorded point: ({x}, {y})")
    points.append((x, y))

def move_to_random_location():
    """Move the mouse to a random location on the screen."""
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width-100)
    random_y = random.randint(0, screen_height-100)
    # Randomize the duration of the drag
    duration = random.uniform(1, 1.5)  # Random duration between 0.3 to 1.5 seconds
    pyautogui.moveTo(random_x, random_y, duration=duration)

def click_and_drag(start, end, duration=random.uniform(2, 2.5)):
    """
    Click and drag the mouse from start to end.

    :param start: Tuple of (x, y) coordinates to start the drag.
    :param end: Tuple of (x, y) coordinates to end the drag.
    :param duration: Duration of the drag operation.
    """
    pyautogui.moveTo(start[0], start[1])
    pyautogui.mouseDown()
    pyautogui.moveTo(end[0], end[1], duration=duration)
    pyautogui.mouseUp()

def click_at_coordinate(x, y):
    """
    Move the mouse to a specific (x, y) coordinate and perform a click.

    :param x: The x-coordinate on the screen.
    
    :param y: The y-coordinate on the screen.
    """
    # Add a slight random offset to make the click less predictable
    x += random.randint(-2, 2)
    y += random.randint(-2, 2)
    
    # Move to the coordinate
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))
    time.sleep(3)

    print("moving cordinate = ", x, y)
    
    # Perform the click
    pyautogui.click()


def main():
    print("Press 'r' to record a point, 's' to start dragging, and 'q' to quit.")

    x = "on"
    while True:


        z = 0
        
        if keyboard.is_pressed('l'):
            time.sleep(0.2)  # Debounce the key press
            print("getting storage cordinates")
            storageX, storageY = pyautogui.position()
            print("storage cordinates = ", storageX, storageY)

        if keyboard.is_pressed('r'):
            record_point()
            time.sleep(0.2)  # Debounce the key press

        
        if keyboard.is_pressed('r'):
            record_point()
            time.sleep(0.2)  # Debounce the key press
        elif keyboard.is_pressed('s'):
            if len(points) >= 2:
                while True:
                    for i in range(0, len(points) ):
                        if i + 1 < len(points):
                            click_and_drag(points[i], points[i + 1])
                            time.sleep(random.uniform(7, 9))  # Pause between drags
                            move_to_random_location()
                            if keyboard.is_pressed('n'):
                                x = "off"
                                print("Quitting.")
                                break
                    if keyboard.is_pressed('n') or x=="off":
                        x = "off"
                        print("Quitting.")
                        break
                    z = z + 1
                    if( z >= 1 ):
                        keyboard.press_and_release('q')
                        time.sleep(0.2)  # Debounce the key press
                        click_at_coordinate(storageX, storageY)

                        keyboard.press_and_release('q')
                        time.sleep(0.2)  # Debounce the key press

            else:
                print("Need at least two points to start dragging.")
            time.sleep(0.2)  # Debounce the key press
        if x == "off" or keyboard.is_pressed('n'):
            print("Quitting.")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
