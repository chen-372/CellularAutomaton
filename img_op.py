from PIL import Image, ImageDraw
import imageio
import os

# local
from model import Grid


def save_jpg(grid: Grid, path: str, size: int) -> None:
    img = Image.new("L", (size * len(grid.cells), size * len(grid.cells)), (255))
    draw_img = ImageDraw.Draw(img)

    for row in grid.cells:
        for cell in row:
            start = (cell.coord[0] * size, cell.coord[1] * size)
            end = ((cell.coord[0] + 1) * size - 1, (cell.coord[1] + 1) * size - 1)
            color = 0 if cell.alive else (200 if cell.activated else 255)
            draw_img.rectangle((start, end), color)
    img.save(path)
    print(f"{path} saved...")


def save_gif(img_paths: list[str], path: str) -> None:
    """duration - duration for each jpg"""
    imgs = [imageio.imread(img_path) for img_path in img_paths]
    imageio.mimsave(path, imgs)
    print(f"{path} saved...")


def del_jpg(path: str, file_name: str) -> None:
    os.popen(f"cd {path} & del {file_name}")
    print(f"file {path} {file_name} is deleted")
