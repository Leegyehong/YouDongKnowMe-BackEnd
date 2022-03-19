import yaml
import os

def read_config(config_path):
    print(config_path)
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config