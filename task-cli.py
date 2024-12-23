import sys

# Check if the user provides a command
if len(sys.argv) < 2:
    print("Usage: task-cli <command> [arguments]")
    sys.exit(1)  # Exit the program if no command is given

# Get the command from the user's input
command = sys.argv[1]
print(f"You entered the command: {command}")