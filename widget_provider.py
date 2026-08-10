from widget import Widget
from font_manager import select_font


def get_widget():

    print("\nWidget bilgileri otomatik olarak alınamadı.")
    print("Lütfen bilgileri manuel giriniz.\n")

    width = int(input("Width (px): "))
    height = int(input("Height (px): "))
    x = int(input("X: "))
    y = int(input("Y: "))

    font_path, font_name = select_font()

    return Widget(
        width,
        height,
        x,
        y,
        font_name,
        font_path
    )