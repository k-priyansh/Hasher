import os
import sys
import platform
import subprocess

def check_os():
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Darwin":
        return "Mac"
    elif os_name == "Linux":
        return "Linux"
    else:
        return "Unknown"

def check_and_setup_venv():
    folder_name = "pyenv"
    if not os.path.exists(folder_name):
        print(f"Folder '{folder_name}' not found. Creating virtual environment...")
        subprocess.run(["python3", "-m", "venv", "pyenv"], check=True)
    else:
        print(f"Folder '{folder_name}' exists. Activating virtual environment...")
        os_type = check_os()
        if os_type == "Windows":
            activate_script = "pyenv\\Scripts\\activate.bat"
        else:
            activate_script = "source ./pyenv/bin/activate"
        subprocess.run(activate_script, shell=True, check=True)

# def requirement_command():
#     install_depedencies = "pip3 install -r requirements.txt"
#     subprocess.run(install_depedencies, shell=True, check=True)

if __name__ == "__main__":
    print(f"Operating System: {check_os()}")
    check_and_setup_venv()
    # requirement_command()