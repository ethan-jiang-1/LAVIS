from train import main
import sys
# import argparse
#python -m torch.distributed.run --nproc_per_node=1 train.py --cfg-path lavis/projects/blip2/train/caption_coco_ft.yaml
if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Training")
    sys.argv.append("--cfg-path")
    sys.argv.append("lavis/projects/blip2/train/caption_coco_ft.yaml")
    # parser.add_argument("--cfg-path", default="lavis/projects/blip2/train/caption_coco_ft.yaml")
    
    # args = parser.parse_args()
    print(sys.argv)
    main()