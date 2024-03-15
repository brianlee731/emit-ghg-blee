import glob
import os

cogs = glob.glob(f"/scratch/brodrick/methane/visions_delivery/20*/*/*tif")
cmr_files = glob.glob(f"/scratch/brodrick/methane/visions_delivery/20*/*/*cmr.json")
basenames = [os.path.basename(f) for f in cmr_files]

new_cogs = []
for cog in cogs:
    if os.path.basename(cog) not in basenames:
        print(cog)

