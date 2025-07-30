import os
from pathlib import Path
from PIL import Image
import colorsys
import argparse

# Define 12 base colors including black and white
base_colors = {
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "brown": (139, 69, 19),
    "gray": (128, 128, 128),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}


def rgb_to_hls(rgb):
    return colorsys.rgb_to_hls(*(x / 255.0 for x in rgb))


def hls_to_rgb(hls):
    return tuple(int(x * 255) for x in colorsys.hls_to_rgb(*hls))


def generate_variants(rgb, count=100):
    h, l, s = rgb_to_hls(rgb)

    shades = []

    if rgb == (0, 0, 0):  # black → dark grays
        for i in range(count):
            lightness = (i / (count - 1)) * 0.3  # from 0.0 to 0.3
            shades.append(hls_to_rgb((0, lightness, 0)))  # hue and saturation = 0
    elif rgb == (255, 255, 255):  # white → light grays
        for i in range(count):
            lightness = 0.7 + (i / (count - 1)) * 0.3  # from 0.7 to 1.0
            shades.append(hls_to_rgb((0, lightness, 0)))  # hue and saturation = 0
    else:
        for i in range(count):
            # lightness between 0.2 and 0.8
            lightness = 0.2 + (i / (count - 1)) * 0.6
            saturation = min(1.0, max(0.0, s * (0.7 + 0.006 * i)))
            new_rgb = hls_to_rgb((h, lightness, saturation))
            shades.append(new_rgb)

    return shades


def save_color_image(color, path, size=(100, 100)):
    img = Image.new("RGB", size, color)
    img.save(path)


def main():

    parser = argparse.ArgumentParser(description="Generate color concept images.")
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="concept_colors_100",
        help="Directory to save generated color images.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    for name, rgb in base_colors.items():
        folder = Path(output_dir) / name
        folder.mkdir(parents=True, exist_ok=True)

        shades = generate_variants(rgb, count=100)

        for i, color in enumerate(shades):
            filename = f"{name}_{i+1:03d}.png"
            save_color_image(color, folder / filename)

    print(
        f"Dataset created in '{output_dir}' with 12 base colors × 100 shades each (1200 total images)."
    )


if __name__ == "__main__":
    main()
