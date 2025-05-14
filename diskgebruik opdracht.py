import os
import sys
import collections

def get_size(start_path='.'):
    """Berekent de totale grootte van bestanden in een opgegeven map."""
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def categorize_files(drive):    
    """Categoriseert bestanden op basis van hun extensie en berekent de totale grootte per categorie."""
    categories = {
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Muziek": [".mp3", ".wav", ".flac"],
        "Documenten": [".pdf", ".docx", ".txt", ".xlsx"],
        "Afbeeldingen": [".jpg", ".png", ".gif", ".bmp"]
    }
    usage = collections.defaultdict(int)
    overige_grootte = 0
    
    for dirpath, _, filenames in os.walk(drive):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            if os.path.exists(filepath):
                filesize = os.path.getsize(filepath)
                ext = os.path.splitext(file)[1].lower()
                found = False
                
                for category, extensions in categories.items():
                    if ext in extensions:
                        usage[category] += filesize
                        found = True
                        break
                
                if not found:
                    overige_grootte += filesize
    
    usage["Overig"] = overige_grootte
    return usage

def format_size(size):
    """Converteert bytes naar een leesbaar formaat (MB, GB, etc.)."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def main():
    drive = input("Voer de schijfletter of map in om te scannen (bijv. C:/ of /home): ")
    if not os.path.exists(drive):
        print("De opgegeven schijf/mappad bestaat niet.")
        sys.exit(1)
    
    print("Schijfgebruik wordt geanalyseerd...")
    usage = categorize_files(drive)
    
    print("\nOpslaggebruik per categorie:")
    for category, size in usage.items():
        print(f"{category}: {format_size(size)}")

if __name__ == "__main__":
    main()
