#!/usr/bin/env python3

import os
import subprocess

checkPath   = "/var/lib/docker/volumes/portainer_data/_data/compose"
identifier  = "IDENTIFIER_MEDIASERVER_1337"


def find_string_in_file(file_path, identifier):
    with open(file_path, 'r') as file:
        if identifier in file.read():
            return file_path
    return None

def find_string_in_directory(directory_path, identifier):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".yml"):
                file_path = os.path.join(root, file)
                found_path = find_string_in_file(file_path, identifier)
                if found_path is not None:
                    return found_path
    return None


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode != 0:
        print(f'Error occurred: {error.decode()}')


if __name__ == "__main__":
    found_path = find_string_in_directory(checkPath, identifier)
    if found_path is not None:
    #    run_command(f'docker compose -f {found_path} -p mediaserver down && docker compose -f {found_path} -p mediaserver up -d')
        print("Restart done :)")
    else:
        print(f'Could not find "{identifier}" in any text file in the directory: {checkPath}')
