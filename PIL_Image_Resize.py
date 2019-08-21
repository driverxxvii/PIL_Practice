from PIL import Image
import pathlib


# Resizes down all files to new_size
# png files are converted to jpg to reduce file size

def main():
    new_size = (3840, 2160)     # 4K resolution
    dir_path = pathlib.Path(r"C:\RedditBot\Images")
    save_path = pathlib.Path(r"C:\Wallpapers - Reddit")

    if not save_path.exists():
        pathlib.Path(save_path).mkdir()

    for filename in dir_path.iterdir():

        if filename.suffix in (".jpg", ".png") and filename.is_file():
            im = Image.open(filename)
            print(filename.name, im.mode)

            # png files with transparency (RGBA) can't be saved to jpeg
            # convert file to RGB first
            if im.mode == "RGBA":
                im = im.convert("RGB")

            im.thumbnail(new_size, Image.ANTIALIAS)

            try:
                im.save(save_path.joinpath(f"{filename.stem}.jpg"))

            except IOError:
                print(f"error occurred on file {filename.name}")

    input("Press enter to close this window")


if __name__ == "__main__":
    main()
