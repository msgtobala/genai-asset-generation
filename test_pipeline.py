from app.pipelines.three_d_generation import Hunyuan3DGenerationPipeline

pipeline = Hunyuan3DGenerationPipeline()
glb_path = pipeline.generate()
print("3D model generated:", glb_path)
