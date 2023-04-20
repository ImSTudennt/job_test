import os
from funcs import clone_repo, sha256_dir, sha256_update_from_dir, main
import hashlib
import shutil


def test_clone():
    assert os.path.exists(clone_repo(1)) == True


def test_update_from_dir():
    dir_name = 'dir_test/files'
    file_name = 'file_test_2.txt'
    os.makedirs(dir_name)
    with open(rf'dir_test/file_test_1.txt', 'w') as f:
        f.write('Test1!')
    with open(rf'{dir_name}/{file_name}', 'w') as f:
        f.write('Test2!')
    hash_dir_test = sha256_update_from_dir(r'C:\Users\vladi\Desktop\job_test\dir_test', hashlib.sha256()).hexdigest()
    hash_folder_1 = sha256_update_from_dir(r"C:\Users\vladi\Desktop\job_test\folder_1", hashlib.sha256()).hexdigest()
    assert hash_dir_test != hash_folder_1
    shutil.rmtree(r'C:\Users\vladi\Desktop\job_test\dir_test')


def test_sha256_dir():
    assert type(sha256_dir(r"C:\Users\vladi\Desktop\job_test\folder_1")) == str


def test_main():
    num = 2
    assert main(num) == sha256_dir(rf"C:\Users\vladi\Desktop\job_test\folder_{num}")