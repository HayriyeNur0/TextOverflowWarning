from font_parser import parse_font_file


FONT_WIDTHS, FONT_HEIGHT = parse_font_file(
    "Fonts/LiberationSans16.c"
)


def calculate_text_width(text):
    """
    Metnin toplam piksel genişliğini hesaplar.
    """

    text_width = 0

    for character in text:
        width = FONT_WIDTHS.get(character, 8)
        text_width += width

    return text_width


def calculate_text_height():
    """
    Tek satırlık text'in yüksekliğini döndürür.
    """

    return FONT_HEIGHT


def check_text_overflow(text, area_width):
    """
    Metnin yatay taşma miktarını hesaplar.

    > 0 : Taşma
    = 0 : Tam sığıyor
    < 0 : Boşluk var
    """

    text_width = calculate_text_width(text)

    return text_width - area_width


def check_text_height_overflow(area_height):
    """
    Tek satırlık text'in dikey taşma miktarını hesaplar.

    > 0 : Taşma
    = 0 : Tam sığıyor
    < 0 : Boşluk var
    """

    text_height = calculate_text_height()

    return text_height - area_height