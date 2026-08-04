from font_parser import parse_font_file
from text_overflow import calculate_text_width, check_text_overflow

# Font dosyasını okur
FONT_WIDTHS = parse_font_file("Fonts/LiberationSans16.c")

AREA_WIDTH = 70

TEST_TEXTS = [
    "motor",
    "Motor Durumu",
    "iiiiii",
    "WWWWWW",
    "123456",
    "",
    "      ",
    "ABCabc123"
]

for i, text in enumerate(TEST_TEXTS, start=1):

    print("=" * 50)
    print(f"TEST {i}")
    print("=" * 50)

    print(f"Metin : \"{text}\"")
    print()

    print("Karakter Genişlikleri")


    # Metindeki her karakterı tek tek dolaşır
    for character in text:
        
        # Karakter font dosyasında varsa gerçek genişliğini alıyoruz
        # Yoksa varsayılan olarak 8 piksel kullanıyoruz
        width = FONT_WIDTHS.get(character, 8)


        # Boşluk karakteri ekranda görünmediği için özel gösteriyoruz
        if character == " ":
            print(f"' ' -> {width} px")
        else:
            print(f"{character} -> {width} px")

    print()
    # metnin toplam pixel genişliğinin hesabı
    text_width = calculate_text_width(text)

    print(f"Toplam Metin Genişliği : {text_width} px")
    print(f"Alan Genişliği         : {AREA_WIDTH} px")

    # metnin taşma durumunun hesabı
    pixel_difference = check_text_overflow(text, AREA_WIDTH)

    print()

    if pixel_difference > 0:
        print(f"SONUÇ : Metin {pixel_difference} px taşıyor.")

    elif pixel_difference == 0:
        print("SONUÇ : Metin alana tam sığıyor.")

    else:
        print(f"SONUÇ : Metin alana sığıyor. {-pixel_difference} px boşluk kaldı.")

    print()