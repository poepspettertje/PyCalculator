from pyfiglet import Figlet

def print_gigantic_text(text, font="standard"):
    f = Figlet(font=font)
    gigantic_text = f.renderText(text)
    print(gigantic_text)
    

# Voorbeeld van het gebruik:
your_text = "PyCalculator"
selected_font = "big"  # Pas dit aan naar wens, kijk naar beschikbare fonts met f.getFonts()

print_gigantic_text(your_text, selected_font)
print("with the Pycalculator you can multiply 2 numbers with each others. Butt you can't multiple numbers with decimals.")

a =int(input("type your first number: "))
b =int(input("type your second number: "))

print(a*b)
