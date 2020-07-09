# Oneshell means I can run multiple lines in a recipe in the same shell, so I don't have to
# chain commands together with semicolon
.ONESHELL:
# Need to specify bash in order for conda activate to work.
SHELL=/bin/bash
# Note that the extra activate is needed to ensure that the activate floats env to the front of PATH
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
ENV_NAME = ianlibdemo_conda_env
CONDA_LIB_DIR = //r4001/finpublic/FP\&A/channel_test/noarch
.PHONY: versionsync clean pip conda

clean:
	# remove pip packages
	rm -rf ./dist/*
	# remove conda packages and build artifacts
	$(CONDA_ACTIVATE) $(ENV_NAME)
	bash scripts/conda_clean.sh

pip: clean
	$(CONDA_ACTIVATE) $(ENV_NAME)
	poetry build

pip_ext_pub: pip
	$(CONDA_ACTIVATE) $(ENV_NAME)
	poetry publish --repository testpypi

pip_int_pub: pip
	$(CONDA_ACTIVATE) $(ENV_NAME)
	poetry publish --repository localpypi


versionsync:
	$(CONDA_ACTIVATE) $(ENV_NAME)
	python scripts/version_sync.py

conda: versionsync pip
	$(CONDA_ACTIVATE) $(ENV_NAME)
	bash scripts/conda_build.sh

conda_ext_pub: conda
	$(CONDA_ACTIVATE) $(ENV_NAME)
	anaconda upload $$(conda-build . --output)

conda_int_pub: conda
	$(CONDA_ACTIVATE) $(ENV_NAME)
	cp $$(conda-build . --output) $(CONDA_LIB_DIR)

all_int_pub: pip_int_pub conda_int_pub
	echo "publishing to internal conda and pip repository"

all_ext_pub: pip_ext_pub conda_ext_pub
	echo "publishing to external conda and pip repository"