from PIL import Image
import argparse

LIMIT = "#####"

def text_to_binary(text: str) -> str:
    result = ''.join(format(ord(char), '08b') for char in text)
    return result

def binary_to_text(text: str) -> str:
    result = ''.join(chr(int(text[i:i+8], 2))for i in range(0, len(text), 8))
    return result


def hide_message(origin_path, message, final_path):
    img = Image.open(origin_path).convert("RGB")
    message = message + LIMIT
    message_binary = text_to_binary(message)

    pixels = list(img.getdata())
    capacity = len(pixels) * 3

    if len(message_binary) > capacity:
        raise ValueError("The message is bigger than the image")

    new_pixels = []
    indice_bit = 0

    for r, g, b in pixels:
        if indice_bit < len(message_binary):
            bit = int(message_binary[indice_bit])
            r = (r & ~1) | bit
            indice_bit += 1

        if indice_bit < len(message_binary):
            bit = int(message_binary[indice_bit])
            g = (g & ~1) | bit
            indice_bit += 1

        if indice_bit < len(message_binary):
            bit = int(message_binary[indice_bit])
            b = (b & ~1) | bit
            indice_bit += 1

        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(final_path)


def extract_message(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())

    bits = []
    message = []

    for r, g, b in pixels:
        bits.append(str(r & 1))
        bits.append(str(g & 1))
        bits.append(str(b & 1))

        while len(bits) >= 8:
            byte = ''.join(bits[:8])
            del bits[:8]

            letter = binary_to_text(byte)
            message.append(letter)

            if ''.join(message[-len(LIMIT):]) == LIMIT:
                return ''.join(message[:-len(LIMIT)])

    raise ValueError("No LIMIT in the image.")

def main():
    parser = argparse.ArgumentParser(
        description="Steganography Tool: encode and decode messages in images"
    )
    parser.add_argument(
        "action",
        choices=["encode", "decode"],
        help="Action: encode to hide, decode to extract",
    )
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="image path",
    )
    parser.add_argument(
        "-m",
        "--message",
        help="Message to hide (required in encode mode)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Final image path (required in encode mode)",
    )

    args = parser.parse_args()

    try:
        if args.action == "encode":
            if not args.message:
                parser.error("In encode mode, the argument -m/--message is required.")
            if not args.output:
                parser.error("In encode mode, the argument -o/--output is required.")

            hide_message(args.image, args.message, args.output)
            print(f"Message was hidden successfully in: {args.output}")
        else:
            mensagem = extract_message(args.image)
            print(f"Message extracted: {mensagem}")
    except Exception as error:
        parser.exit(status=1, message=f"Error: {error}\n")


if __name__ == "__main__":
    main()