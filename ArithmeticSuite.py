# this exercise is about CONDITIONALS CONDITIONALS CONDITIONALS CONDITIONALS CONDITIONALS CONDITIONALS

# Greet the users
print("Hallo! Willkommen in der Arithmetik-Suite!").strip().title()

# DEFine the main()-FUNCTION // Ask users which operation they want to do: adding / squaring / comparing?
def main():
    want = input("Was möchtest du machen? Addition (A) Quadrate (B) oder Vergleichen (C)")
            
    if want == "A":
        add()
    elif want == "B":
        square()
    elif want == "C":
        compare()
    else:
        sorry()



# DEFine the functions for each operation

def add():
    v = int(input("Hallo, wie groß ist dein erster Wert? "))
    w = int(input("Hallo, wie groß ist dein zweiter Wert? "))
    print(v + w)

def square():
    b = int(input("Hallo wie groß ist dein Wert? "))
    print(b ** 2)

def compare():
    n = int(input("Wie groß ist dein erster Wert? "))
    m = int(input("Wie groß ist dein zweiter Wert? "))

    if n > m:
        print(f"{n} ist größer als {m}!")
    elif n < m:
        print(f"{n} ist kleiner als {m}!")
    elif n == m or n >= m or n <= m:
        print(f"{n} und {m} sind gleich groß!")
    else:
        sorry()

def sorry():
    print("Pardon! Da ist was schief gegangen!")


main()