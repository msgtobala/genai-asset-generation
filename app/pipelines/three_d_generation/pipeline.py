from pathlib import Path
from PIL import Image
from .components.shapegen import Hunyuan3DDiTFlowMatchingPipeline
from .components.texgen import Hunyuan3DPaintPipeline

class Hunyuan3DGenerationPipeline:
    def __init__(self):
        self.shape_gen = Hunyuan3DDiTFlowMatchingPipeline()
        self.texture_gen = Hunyuan3DPaintPipeline()
    
    def generate(self):
        pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained('tencent/Hunyuan3D-2')
        mesh = pipeline(image='../../inputs/left.png')[0]

        pipeline = Hunyuan3DPaintPipeline.from_pretrained('tencent/Hunyuan3D-2')
        mesh = pipeline(mesh, image='../../inputs/left.png')
        print("Generated mesh")

