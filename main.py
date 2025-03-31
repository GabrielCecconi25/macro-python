import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0

# Variável global para controlar a execução
stop_execution = False

def stop_clicking():
    global stop_execution
    stop_execution = True
    

def main():
    # Atalho para desativar programa
    keyboard.add_hotkey('f8', stop_clicking)
    clicks = 200
    
    print(f"This program will click the mouse {clicks} times at the current position.")
    print("You 5 seconds to move the mouse to the desired position.")
    
    time.sleep(5)
    x = pyautogui.position()

    try:
        for _ in range(clicks):
            if stop_execution:
                print("Execution stopped by user.")
                break
            pyautogui.click(x=x[0], y=x[1], interval=0.05, button='left')
    except KeyboardInterrupt:
        print("Execution interrupted.")
    finally:
        keyboard.unhook_all_hotkeys()

if __name__ == "__main__":
    main()

