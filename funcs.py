from git import Repo
import os
from multiprocessing import Process
import hashlib
from pathlib import Path




def clone_repo(i):
    name_folder = f'folder_{i}'
    os.mkdir(name_folder)
    clone = Repo.clone_from(r'https://gitea.radium.group/radium/project-configuration.git', rf'C:\Users\vladi\Desktop\job_test\{name_folder}')
    return clone.working_dir


def sha256_update_from_dir(directory, hash):
    assert Path(directory).is_dir()
    for path in sorted(Path(directory).iterdir(), key=lambda p: str(p).lower()):
        hash.update(path.name.encode())
        if path.is_file():
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash.update(chunk)
        else:
            hash = sha256_update_from_dir(path, hash) 
    return hash


def sha256_dir(directory):
    return sha256_update_from_dir(directory, hashlib.sha256()).hexdigest()

def main(num):
    process = [Process(target=clone_repo, args=(f'{i}',)) for i in range(3)]
    for p in process:
        p.start()
    for p in process:
        p.join()
    return sha256_dir(rf"C:\Users\vladi\Desktop\job_test\folder_{num}")