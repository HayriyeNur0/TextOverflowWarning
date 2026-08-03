import re
from pathlib import Path


def parse_font_file(font_file):
    """
    emWin Font Converter tarafından oluşturulan .c dosyasını okuyarak
    karakter genişliklerini sözlük olarak döndürür.
    """

    # Karakterlerin genişliklerini saklayacağımız boş bir sözlük (dictionary) oluşturuyoruz.
    font_widths = {}

    # GUI_CHARINFO satırını (örn: { 12, 16, 10, acGUI_..._0021 }) yakalamak için regex deseni derliyoruz.
    # 1. Grup (\d+): Karakterin genişliği (width)
    # 2. Grup (\w+): Karakterin hex kodunu belirten son kısımdaki ifade
    pattern = re.compile(
        r"\{\s*(\d+)\s*,\s*\d+\s*,\s*\d+\s*,\s*acGUI_.*?_(\w+)\s*\}"
    )

    # Belirtilen C font dosyasını UTF-8 formatında, hataları yok sayarak güvenli bir şekilde açıyoruz.
    with open(font_file, "r", encoding="utf-8", errors="ignore") as file:

        # Dosyadaki her bir satırı sırasıyla okuyoruz.
        for line in file:

            # O anki satırda regex desenimizi arıyoruz.
            match = pattern.search(line)

            # Eğer satır aradığımız formata uyuyorsa eşleşme (match) yakalanır.
            if match:
                # 1. gruptaki veriyi (genişlik) tam sayıya (integer) çeviriyoruz.
                width = int(match.group(1))

                # 2. gruptaki hex kodunu (karakter belirtecini) alıyoruz.
                unicode_hex = match.group(2)

                try:
                    # Hex kodunu 16'lık tabandan sayıya, ardından gerçek karakter karşılığına (örn: 'A') çeviriyoruz.
                    character = chr(int(unicode_hex, 16))
                    
                    # Karakteri anahtar (key), genişliğini ise değer (value) olarak sözlüğe ekliyoruz.
                    font_widths[character] = width
                except ValueError:
                    # Dönüşüm sırasında bir hata oluşursa programın çökmesini engellemek için es geçiyoruz.
                    pass

    # Tüm dosya tarandıktan sonra doldurduğumuz karakter-genişlik sözlüğünü döndürüyoruz.
    return font_widths


if __name__ == "__main__":
    # Okunacak C font dosyasının dosya yolu (path)
    font_path = "Fonts/LiberationSans16.c"

    # Fonksiyonu çağırarak font verilerini sözlük olarak alıyoruz.
    font = parse_font_file(font_path)

    # Elde edilen sözlüğü ekrana yazdırıyoruz.
    print(font)

    # Toplam kaç adet karakterin başarıyla parse edildiğini gösteriyoruz.
    print("Toplam karakter:", len(font))