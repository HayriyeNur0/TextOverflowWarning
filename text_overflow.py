def calculate_text_width(text, font_widths):
    """
    Metnin toplam piksel genişliğini hesaplar.
    """

    text_width = 0

    for character in text:

        width = font_widths.get(character, 8)

        text_width += width

    return text_width


def calculate_text_height(font_height):
    """
    Tek satırlık text'in yüksekliğini döndürür.
    """

    return font_height


def check_text_overflow(
    text,
    area_width,
    font_widths
):
    """
    Metnin yatay taşma miktarını hesaplar.

    > 0 : Taşma
    = 0 : Tam sığıyor
    < 0 : Boşluk var
    """

    text_width = calculate_text_width(
        text,
        font_widths
    )

    return text_width - area_width


def check_text_height_overflow(
    area_height,
    font_height
):
    """
    Tek satırlık text'in dikey taşma miktarını hesaplar.

    > 0 : Taşma
    = 0 : Tam sığıyor
    < 0 : Boşluk var
    """

    text_height = calculate_text_height(
        font_height
    )

    return text_height - area_height