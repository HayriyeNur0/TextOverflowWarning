from widget import Widget


def get_widget():

    #print("\nWidget bilgileri otomatik olarak alınamadı.")
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