import sys

def get_poem_text(color):
    """Geeft de bijbehorende tekst voor een opgegeven kleur."""
    poems = {
        "blauw": "Blauw zoals de lucht.",
        "rood": "Rood met passie.",
        "geel": "Geel als de stralen van de zon.",
        "groen": "Groen van de natuur.",
        "paars": "paars de maanlicht",
        "wit": "als een eeuwige blijheid",
        "zwart": "zwart de nacht die doorgaat"
    }
    return poems.get(color.lower(), None)

def main():
    color = input("Voer je lievelingskleur in: ")
    poem_text = get_poem_text(color)
    
    if poem_text is None:
        print("Onbekende kleur. De applicatie wordt afgesloten.")
        sys.exit(1)
    
    with open("gedicht.txt", "a", encoding="utf-8") as file:
        file.write(poem_text)
    
    print(f"Gedicht opgeslagen in 'gedicht.txt':\n{poem_text}")

if __name__ == "__main__":
    main()
