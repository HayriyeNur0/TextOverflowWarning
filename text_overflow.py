from font_parser import parse_font_file

# Font dosyasını program başlarken bir kez oku
FONT_WIDTHS = parse_font_file("Fonts/LiberationSans16.c")


def calculate_text_width(text):
    """
    Verilen metnin ekranda kaplayacağı piksel genişliğini hesaplar.

    Karakter genişlikleri emWin Font Converter tarafından oluşturulan
    font dosyasından okunur.
    """

    text_width = 0

    for character in text:
        # Karakter font dosyasında varsa gerçek genişliğini kullan,
        # yoksa varsayılan olarak 8 piksel kabul et.
        text_width += FONT_WIDTHS.get(character, 8)
        

    return text_width


def check_text_overflow(text, area_width):
    """
    Yazının genişliğini hesaplar ve
    area_width ile arasındaki farkı döndürür.

    Dönüş değeri:
    > 0  : Yazı taşıyor.
    = 0 : Yazı tam sığıyor.
    < 0  : Yazı sığıyor.
    """

    text_width = calculate_text_width(text)

    pixel_difference = text_width - area_width

    return pixel_difference