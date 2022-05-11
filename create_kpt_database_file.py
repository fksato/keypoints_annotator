import glob

from pathlib import Path

import orjson

import click

from kpt_configs import categories


@click.command()
@click.argument("data-path", type=Path)
@click.option("-p", "--port", type=int, default=6008, help="Port for where the image server will run from. defaults to 6008")
def main(data_path: Path, port: int):
    image_dir_regx = f'{data_path}/**/*.jpg'
    img_data = glob.glob(image_dir_regx, recursive=True)
    images = []

    for image_path in img_data:
        image_file_name = Path(image_path).relative_to(data_path)
        image_id = f"{image_file_name.parents[1].stem}{image_file_name.parents[2].stem}{image_file_name.stem}"
        image_url = f"http://localhost:{port}/{image_file_name}"
        images.append({
            "id": image_id,
            "file_name": str(image_file_name),
            "url": image_url
        })

    dataset = {
        "categories": categories,
        "images": images,
        "annotations": [],
        "licenses": []
    }

    dataset_file_path = f"{data_path}/keypoints_database.json"

    with open(dataset_file_path, 'wb') as f:
        f.write(orjson.dumps(dataset, f))        


if __name__=="__main__":
    main()