from PIL import Image

import unittest, os


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_extract_frames(self):
        gif_path = "flag.gif"
        gif_image = Image.open(gif_path)

        # 获取GIF中的帧数
        num_frames = gif_image.n_frames

        output_directory = "output_png_frames/"
        os.makedirs(output_directory, exist_ok=True)

        for frame_number in range(num_frames):
            gif_image.seek(frame_number)
            frame_image = gif_image.copy()
            frame_image.save(f"{output_directory}{frame_number}.png")

    def test_extract_value_by_hash_md5(self):
        import os
        import hashlib

        current_directory = os.getcwd()

        for root, dirs, files in os.walk(current_directory):
            for i in range(1, 1100):
                file_name = str(i) + ".png"
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as file:
                        md5_hash = hashlib.md5()
                        while True:
                            data = file.read(4096)  # 每次读取4KB
                            if not data:
                                break
                            md5_hash.update(data)
                        if md5_hash.hexdigest() == "73b98b0ce63e17f9686d8f1c7c2c1ea4":
                            print("+", end='')
                        elif md5_hash.hexdigest() == "0603d47d8bbd5824d76d487a3f313b11":
                            print("[", end='')
                        elif md5_hash.hexdigest() == "abd01d8e57bd41d62a7444aadbb932a5":
                            print("-", end='')
                        elif md5_hash.hexdigest() == "59fe976c8572cdd59996b4e3c088809e":
                            print(">", end='')
                        elif md5_hash.hexdigest() == "af08104d55fae5787b073e974aa8f303":
                            print("<", end='')
                        elif md5_hash.hexdigest() == "e20180170280aeb074384bcbae840cf0":
                            print("]", end='')
                        elif md5_hash.hexdigest() == "fd439e1a7e9058ae4d635755dedf4191":
                            print(".", end='')
                        else:
                            print(f"File: {file_path} MD5: {md5_hash.hexdigest()}")

    def test_extract_durations(self):
        def extract_frame_durations(gif_path):
            gif = Image.open(gif_path)

            # Extract frame durations
            frame_durations = []
            while True:
                duration = gif.info.get('duration', 0)
                # duration = gif.info.get('duration', 0) // 60)
                frame_durations.append(duration)  # Some GIFs might not have a 'duration' field for each frame
                try:
                    gif.seek(gif.tell() + 1)
                except EOFError:
                    break  # No more frames

            return frame_durations

        gif_path = "flag.gif"  # Replace with the path to your GIF file
        durations = extract_frame_durations(gif_path)
        print("Frame Durations:", durations, len(durations))
