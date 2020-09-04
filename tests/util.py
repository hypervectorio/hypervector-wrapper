from pathlib import Path


def get_resource_path(filename):
    resources_dir = str(Path(__file__).parent) + "/resources/"
    return resources_dir + filename