import random
import pyautogui
import keyboard
import time

points = []

def record_points():
    print("Press 'r' to record a point. Press 'q' to quit recording.")
    while True:
        if keyboard.is_pressed('r'):  # Record a point
            x, y = pyautogui.position()
            points.append((x, y))
            time.sleep(0.5)  # Prevent duplicate recordings

        if keyboard.is_pressed('q'):  # Quit recording
            print("Stopped recording.")
            break

    return points


def perform_clicks(points, longPoints):
    print("Starting to click on recorded points...")
    for i in range(20000):
        j = 0
        for i in range(6):
                    longCLick(longPoints[0],longPoints[1])
        for point in points:
            if(j==2):
                time.sleep(2)
            if j == 3:
                for x in range(13):
                    pyautogui.click(point)
                    print(f"Clicked at: {point}")
                    time.sleep(0.2)  # Small delay between clicks 
                j = j+ 1
            else:
                pyautogui.click(point)
                print(f"Clicked at: {point}")
                time.sleep(0.5)  # Small delay between clicks
                j = j+ 1


def longCLick(x, y):
    x += random.randint(-2, 2)
    y += random.randint(-2, 2)
    pyautogui.moveTo(x, y) 
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def main():

    # longPoints = []
    # points = []
    points = [(1094, 889), (749, 520), (994, 430), (862, 406), (1106, 887)]
    longPoints = [1422, 444]
    # [(1422, 444)]
    print("Welcome to the Summoning Recorder and Clicker!")

    if points and longPoints:
        while True:
            if keyboard.is_pressed('s'):
                perform_clicks(points, longPoints)
    else:
        points = record_points()
        
        if points:
            print(f"Recorded {len(points)} points: {points}")
            print(points)
        else:
            print("No points recorded. Exiting.")

if __name__ == "__main__":
    main()
