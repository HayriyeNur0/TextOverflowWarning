import re


def parse_font_file(font_file):
    """
    emWin .c font dosyasından:
    - karakter genişliklerini
    - font yüksekliğini
    okur.
    """

    font_widths = {}
    font_height = None

    # Karakter genişliklerini bulmak için regex
    width_pattern = re.compile(
        r"\{\s*(\d+)\s*,\s*\d+\s*,\s*\d+\s*,\s*acGUI_.*?_(\w+)\s*\}"
    )

    # Font yüksekliğini bulmak için regex
    height_pattern = re.compile(
        r",\s*(\d+)\s*/\*\s*height of font\s*\*/"
    )

    with open(font_file, "r", encoding="utf-8", errors="ignore") as file:

        for line in file:

            # Font yüksekliğini bul
            if font_height is None:

                height_match = height_pattern.search(line)

                if height_match:
                    font_height = int(height_match.group(1))

            # Karakter genişliğini bul
            width_match = width_pattern.search(line)

            if width_match:

                width = int(width_match.group(1))
                unicode_hex = width_match.group(2)

                try:

                    character = chr(int(unicode_hex, 16))
                    font_widths[character] = width

                except ValueError:
                    pass

    return font_widths, font_height