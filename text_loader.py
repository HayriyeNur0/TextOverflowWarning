# bu dosyanın görevi txt okumaktır

def load_texts(file_path):
    texts = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:

            line = line.strip()

            if line != "":
                texts.append(line)

    return texts