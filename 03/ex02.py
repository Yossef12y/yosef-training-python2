import os
FILE_NAME = r"/home/yosef/clones/yosef-training-python2/03/check.txt"

def find_the_right_method(name_of_method: str) -> str:
    for name in dir(os.path):
        if name_of_method in name.lower():
            return(name)


def split_file(file_name: str, n: int):
    if not os.path.exists(file_name):
        return f"path{file_name} dose not exists"
    
    size_of_te_file = os.path.getsize(FILE_NAME)
    size_for_file = size_of_te_file // (n - 1)
    last_file_size = size_of_te_file % (n - 1)
    print("last file size  ", last_file_size)

    with open(file_name, 'rb') as data:
        data = data.read()
    
    start = 0
    for i in range(1, n + 1):
        new_file = f"filename{i}"
        if i < n: 
            with open(new_file, 'wb') as f:
                part = data[start: (start + size_for_file)]
                f.write(part)
                start += size_for_file
                print(start)
        if i == n:
            print(i, "print when i is == n")
            print(n)
            with open(new_file, 'wb') as f:
                 part = data[start: (start + last_file_size)]
                 f.write(part)
    return

def main():
    #print(find_the_right_method("size"))
    print(os.path.getsize(FILE_NAME))
    print(split_file(FILE_NAME, 5))


if __name__ == "__main__":
    main()