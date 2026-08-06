from widget import Widget
from simulator_provider import get_widget_from_simulator


def get_widget():

    widget = get_widget_from_simulator()

    if widget is not None:

        print("Widget bilgileri simulator'den alındı.")

        return widget

    print("\nWidget bilgileri otomatik olarak alınamadı.")
    print("Lütfen bilgileri manuel giriniz.\n")

    width = int(input("Width (px): "))
    height = int(input("Height (px): "))
    x = int(input("X: "))
    y = int(input("Y: "))
    font = input("Font: ")

    return Widget(
        width,
        height,
        x,
        y,
        font
    )