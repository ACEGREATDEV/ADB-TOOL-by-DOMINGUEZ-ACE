import subprocess

def connect_device():
    # Connect to the device using ADB
    subprocess.run(['adb', 'connect', 'localhost:5555'])

def disconnect_device():
    # Disconnect from the device using ADB
    subprocess.run(['adb', 'disconnect'])

def reboot_device():
    # Reboot the device using ADB
    subprocess.run(['adb', 'reboot'])

def install_apk():
    # Install an APK on the device using ADB
    apk_path = input("Enter the path to the APK file: ")
    subprocess.run(['adb', 'install', apk_path])

def uninstall_app():
    # Uninstall an app on the device using ADB
    package_name = input("Enter the package name of the app: ")
    subprocess.run(['adb', 'uninstall', package_name])

def run_shell_command():
    # Run a shell command on the device using ADB
    command = input("Enter the shell command: ")
    subprocess.run(['adb', 'shell', command])

def pull_file():
    # Pull a file from the device using ADB
    file_path = input("Enter the path to the file on the device: ")
    local_path = input("Enter the local path to save the file: ")
    subprocess.run(['adb', 'pull', file_path, local_path])

def push_file():
    # Push a file to the device using ADB
    local_path = input("Enter the local path to the file: ")
    file_path = input("Enter the path to save the file on the device: ")
    subprocess.run(['adb', 'push', local_path, file_path])

def list_packages():
    # List all packages on the device using ADB
    subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'])

def list_running_processes():
    # List all running processes on the device using ADB
    subprocess.run(['adb', 'shell', 'ps'])

def mahalin_si_Ace():
    # Print this message
    print("I love you cutie pie")

def main():
    print("\033[94m"""" 
      _   __     _   _   _      _     _   __      
 /\  /   |__     / _ |__) |__   /\   |     |  \ |__  \  / 
/~~\ \__, |___    \__> |  \ |___ /~~\  |     |__/ |___  \/ 
""")
    print("\033[94m" + "DEVELOPER:DOMINGUEZ ACE")
    print("\033[94m" + "ADB Controller")
    print("\033[94m" + "-------------")
    while True:
        print("\033[91m" + "1. Connect to device")
        print("\033[91m" + "2. Disconnect from device")
        print("\033[91m" + "3. Reboot device")
        print("\033[91m" + "4. Install APK")
        print("\033[91m" + "5. Uninstall app")
        print("\033[91m" + "6. Run shell command")
        print("\033[91m" + "7. Pull file from device")
        print("\033[91m" + "8. Push file to device")
        print("\033[91m" + "9. List packages")
        print("\033[91m" + "10. List running processes")
        print("\033[91m" + "11. Quit")
        print("\033[91m" + "12. Mahalin si Ace")
        choice = input("\033[93m" + "Enter your choice: " + "\033[0m")
        if choice == "1":
            connect_device()
        elif choice == "2":
            disconnect_device()
        elif choice == "3":
            reboot_device()
        elif choice == "4":
            install_apk()
        elif choice == "5":
            uninstall_app()
        elif choice == "6":
            run_shell_command()
        elif choice == "7":
            pull_file()
        elif choice == "8":
            push_file()
        elif choice == "9":
            list_packages()
        elif choice == "10":
            list_running_processes()
        elif choice == "11":
            break
        elif choice == "12":
            mahalin_si_Ace()
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
