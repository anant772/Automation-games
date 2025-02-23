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
    while True:
            for i in range(200):
                for i in range(10):
                    longCLick(longPoints[0],longPoints[1])
                for point in points:
                    pyautogui.click(point)
                    print(f"Clicked at: {point}")
                    time.sleep(0.5)  # Small delay between clicks


def longCLick(x, y):
    x += random.randint(-2, 2)
    y += random.randint(-2, 2)
    pyautogui.moveTo(x, y) 
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def main():

    points = [(1096, 884), (1000, 562), (416, 377), (419, 585), (1100, 891)]
    longPoints = [1422, 444]
    # [1422, 444]
    print("Welcome to the Gardening Recorder and Clicker!")

    if points or longPoints:
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
