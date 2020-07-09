"""Get the version number from pyproject.toml and update meta.yaml with it"""
from pathlib import Path
import re

repo_base = Path(__file__).resolve().parents[1]
toml = repo_base / "pyproject.toml"
meta = repo_base / "meta.yaml"

def _find_toml_version_line(toml_file):
    """Find and return the line that gives the version number in pyproject.toml"""
    with open(toml_file, "r") as f:
        for line in f.readlines():
            if line.startswith("version = "):
                return line
    return None

def _get_toml_version_from_line(version_line):
    rgx = 'version = "(.+)"'
    matcher = re.match(rgx, version_line)
    return matcher.groups()[0]


def get_toml_version():
    line = _find_toml_version_line(toml)
    ver = _get_toml_version_from_line(line)
    return ver

def _find_conda_version_line(meta_file):
    """Find the line with version used in meta.yaml"""
    with open(meta_file, "r") as f:
        for line in f.readlines():
            if line.startswith(r"{% set version"):
                return line
    return None

def _get_conda_version_from_line(version_line):
    rgx = '{% set version = "(.+)" %}'
    matcher = re.match(rgx, version_line)
    return matcher.groups()[0]

def get_conda_version():
    line = _find_conda_version_line(meta)
    ver = _get_conda_version_from_line(line)
    return ver

def update_meta():
    """Get the version from pyproject.toml and apply it to meta.yaml"""
    toml_ver = get_toml_version()
    conda_ver = get_conda_version()
    # Read in the file
    with open(meta, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(conda_ver, toml_ver)

    # Write the file out again
    with open(meta, 'w') as file:
        file.write(filedata)
    print(f"meta.yaml version was {conda_ver}, now {toml_ver}")
    return True


update_meta()

