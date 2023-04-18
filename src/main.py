#!/usr/bin/env python3
import yaml
import sys


def main():
    filePath = sys.argv[1]

    with open(filePath, "r") as file:
        ymlData = yaml.safe_load(file)


    models = []
    version = ymlData["version"]
    # print(version)

    for i in ymlData["models"]:
       
        with open(i["name"] + '.yml', 'w') as ymlFile:
                # yaml.dump(i, ymlFile)
                print(ymlFile)
        
        
    # print(models)

if __name__ == "__main__":
    main()