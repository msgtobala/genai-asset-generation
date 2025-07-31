from PIL import Image
from typing import Tuple, Dict
from pathlib import Path


class ViewPreprocessor3D:
    def __init__(self, target_size: int = 518):
        self.target_size = target_size
        # TODO: Load background removal model (e.g. Rembg, U^2Net, etc.)
        print(f"Initialized ViewPreprocessor3D with target size: {target_size}px")

    def load_and_process_all(self, input_dir: Path) -> Dict[str, Tuple[Image.Image, Image.Image]]:
        """
        Loads and processes front, left, right, and back images from input_dir.
        Returns a dict with keys 'front', 'left', 'right', 'back' and values as (image, mask) tuples.
        """
        views = ['front', 'left', 'right', 'back']
        results = {}

        for view in views:
            img_path = input_dir / f"{view}.png"
            image, mask = self.load_and_process_image(img_path)
            results[view] = (image, mask)

        return results

    def load_and_process_image(self, path: Path) -> Tuple[Image.Image, Image.Image]:
        """
        Loads image from path, resizes it, removes background, and returns (image_with_alpha, mask).
        """
        print(f"Processing: {path}")
        image = Image.open(path).convert("RGB")
        image = self.resize_image(image)
        image_with_alpha, mask = self.remove_background(image)
        return image_with_alpha, mask

    def resize_image(self, image: Image.Image) -> Image.Image:
        """Resize image to self.target_size x self.target_size"""
        return image.resize((self.target_size, self.target_size), Image.LANCZOS)

    def remove_background(self, image: Image.Image) -> Tuple[Image.Image, Image.Image]:
        """
        Remove background and return image with alpha and binary mask.
        Placeholder: implement with Rembg, segment-anything, or another method.
        """
        print("Removing background... (placeholder)")
        # TODO: Replace this with real logic
        alpha = Image.new("L", image.size, color=255)  # Dummy mask (all visible)
        image_with_alpha = image.copy()
        image_with_alpha.putalpha(alpha)
        return image_with_alpha, alpha
