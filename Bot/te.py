import subprocess


def run_adb_command(command):
    full_command = ["adb"] + command.split()
    try:
        result = subprocess.run(full_command, capture_output=True, text=True)
        if result.returncode == 0:
            print("Output:\n", result.stdout)
        else:
            print("Error:\n", result.stderr)
    except FileNotFoundError:
        print("ADB not found. Ensure it's installed and added to PATH.")


# Example usage:
run_adb_command("devices")                  # List connected devices
