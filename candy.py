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


def perform_clicks(points,longPoints):
    print("Starting to click on recorded points...")
    while True:
        if keyboard.is_pressed('s'):
                for i in range(2000):
                    longCLick(longPoints[0],longPoints[1])
                    for point in points:
                        pyautogui.click(point)
                        time.sleep(0.1)  # Small delay between clicks


def longCLick(x, y):
    x += random.randint(-2, 2)
    y += random.randint(-2, 2)
    pyautogui.moveTo(x, y) 
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()


def main():

    #points = [(1098, 595), (1097, 889)]#(1105, 836), (1097, 903)]
    points = [(1105, 836), (1097, 903)]
    longPoints = [1226, 739]
    print("Welcome to the Candy Recorder and Clicker!")

    if points and longPoints:
        perform_clicks(points,longPoints)
    else:
        points = record_points()
        
        if points:
            print(f"Recorded {len(points)} points: {points}")
            print(points)
        else:
            print("No points recorded. Exiting.")

if __name__ == "__main__":
    main()
