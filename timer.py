import pyautogui
import keyboard
import time
import random

points = [(1099, 893), (1422, 444)]
storageX = 500
storageY = 500
Longpointress = [(1099, 893), (1422, 444)]
# points = []


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
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.2))

    print("moving cordinate = ", x, y)
    
    # Perform the click
    pyautogui.click()

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




def main():
    print("Press 'r' to record a point, 's' to start dragging, and 'q' to quit.")

    x = "on"
    while True:


        z = 0
        c =1
        
        if keyboard.is_pressed('r'):
            record_point()
            
            print(points)
            time.sleep(0.2)  # Debounce the key press


        elif keyboard.is_pressed('s'):
            if len(points) >= 2:
                while True:
                    # click_at_coordinate(points[0][0], points[0][1])
                    longCLick(Longpointress[1][0], Longpointress[1][1])
                    # pyautogui.press('enter')


                    z = z + 1

                    if( z >= 52000 ):
                        c =0
                        break

            else:
                print("Need at least two points to start dragging.")
            time.sleep(0.2)  # Debounce the key press
        # if c == 0 or keyboard.is_pressed('n'):
        #     print("Quitting.")
        #     break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
