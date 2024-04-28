from rembg import remove


def remove_backgroud(input_image, output_image):
    if input_image.endswith(('.png', 'jpg', 'jpeg')):
        with open(input_image, 'rb') as inp, open(output_image, 'wb') as outp:
            backgroud_output = remove(inp.read())
            outp.write(backgroud_output)
    else:
        print("The file is not valid")


if __name__ == '__main__':
    image = "original_image.jpg"
    output = "pants.png"

    remove_backgroud(image, output)
