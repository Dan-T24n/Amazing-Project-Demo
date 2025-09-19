'''
function: convert any text to ASCII art and print "Hello, World!" in that style.
'''

from pyfiglet import Figlet

def print_ascii_message(message: str):
	figlet = Figlet()
	ascii_art = figlet.renderText(message)
	print(ascii_art)

# Example usage:
# print_ascii_message("Hello, World!")
