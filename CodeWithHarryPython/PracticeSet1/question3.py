# Installing colorama package 
# Installing emogi package
from colorama import Fore, Style, init
import emoji

# Initialize colorama
init(autoreset=True)

print(Fore.GREEN + "Welcome to the Emoji Color Project!")
print(Fore.BLUE + emoji.emojize("Let's build something fun! 🚀"))

print(Fore.YELLOW + emoji.emojize("Python is awesome 😎"))
print(Fore.RED + emoji.emojize("Errors are just learning opportunities 💡"))

print(Style.RESET_ALL)
