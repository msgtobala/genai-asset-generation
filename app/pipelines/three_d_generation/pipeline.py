from pathlib import Path
from PIL import Image
from .components.shapegen import Hunyuan3DDiTFlowMatchingPipeline
from .components.texgen import Hunyuan3DPaintPipeline
from .components.rembg import BackgroundRemover

class Hunyuan3DGenerationPipeline:
    def __init__(self):
        self.shape_gen = Hunyuan3DDiTFlowMatchingPipeline()
        self.texture_gen = Hunyuan3DPaintPipeline()
    
    def generate(self):
        images = {
            "front": "app/inputs/front.png",
            "left": "app/inputs/left.png",
            "back": "app/inputs/back.png",
            "right": "app/inputs/right.png",
        }

        for key in images:
            image = Image.open(images[key]).convert("RGBA")
            if image.mode == 'RGB':
                rembg = BackgroundRemover()
                image = rembg(image)
                images[key] = image
        # Shape generation
        pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(
            'tencent/Hunyuan3D-2mv',
            subfolder='hunyuan3d-dit-v2-mv',
            variant='fp16'
        )
        mesh = pipeline(
            image=images,
            num_inference_steps=50,
            octree_resolution=380,
            num_chunks=20000,
            generator=torch.manual_seed(12345),
            output_type='trimesh'
        )[0]
        mesh.export(f'mesh.glb')

        # Texture generation
        # pipeline = Hunyuan3DPaintPipeline.from_pretrained('tencent/Hunyuan3D-2')
        # mesh = pipeline(mesh, image='../../inputs/left.png')
        # print("Generated mesh")

