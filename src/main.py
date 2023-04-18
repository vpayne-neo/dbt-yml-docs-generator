#!/usr/bin/env python3
import yaml
import os
import sys


def main():
    filePath = sys.argv[1]

    with open(filePath, "r") as file:
        ymlData = yaml.safe_load(file)
    
    version = ymlData["version"]
    
    directoryToJoin = "/Users/vincepayne/neo-analytics/packages/dbt/models/marts/cx"

    for i in ymlData["models"]:
        with open(os.path.join(directoryToJoin, i["name"] + '.yml'), 'w') as ymlFile:
                yaml.dump({"version": version, "models": i }, stream=ymlFile, sort_keys=False)

if __name__ == "__main__":
    main()