import subprocess
import time
import pyautogui

def execute_program(program_path):
    try:
        subprocess.Popen(program_path)
        time.sleep(10)

        pyautogui.write("test")
        pyautogui.press('tab')
        pyautogui.write("test1234")
        pyautogui.press('enter')
        
        print("Username and password entered successfully.")
    except Exception as e:
        print(f"Program failure: {e}")

if __name__ == "__main__":

    app_path = r'C:\my\app.exe'

    execute_program(app_path)
