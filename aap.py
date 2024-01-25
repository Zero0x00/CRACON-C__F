def fancy_hello_world():
    # Fancy colors for printing
    class colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    # Fancy message
    message = f"{colors.HEADER}{colors.BOLD}Hello, {colors.OKGREEN}World{colors.ENDC}!{colors.ENDC}"

    # Print the fancy message
    print(message)

# Call the fancy_hello_world function
fancy_hello_world()
