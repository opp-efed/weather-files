import os
from zipfile import ZipFile
from Code.utilities import nhd_regions
from Code.paths import project_path, output_path

# Create output directory
zipped_path = os.path.join(project_path, "Zipped")
if not os.path.exists(zipped_path):
    os.makedirs(zipped_path)

for region in nhd_regions:
    print(region)
    region_dir = output_path.format("region{}".format(region))
    out_file = os.path.join(zipped_path, "region{}.zip".format(region))
    with ZipFile(out_file, 'w') as z:
        for f in os.listdir(region_dir):
            try:
                z.write(os.path.join(region_dir, f))
            except PermissionError as e:
                print(e)