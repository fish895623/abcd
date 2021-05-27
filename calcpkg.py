from os import path
import yaml


class dir:
    def __init__(self, yaml_loc) -> None:
        # Get setting Yaml
        # Parse Yaml
        with open(yaml_loc) as f:
            db = yaml.load(f, Loader=yaml.FullLoader)

        self.location = db["GitLocation"]
