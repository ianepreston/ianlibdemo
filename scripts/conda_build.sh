#!/bin/bash
# output folder dumps a bunch of files I don't think I need, might use it later though
conda-build . # --output-folder dist
CONDA_PACK=$(conda-build . --output)
cp $CONDA_PACK dist/