import os


def inputInt(_prompt: str) -> int:
    while True:
        try:
            num = int(input(_prompt))
            if num < 0:
                print("Zero can't be bigger then entered value. Try again.")
            else:
                return num
        except ValueError:
            print("Value Error. Try again.")
        except TimeoutError:
            print("Timeout Error. Try again.")


def strInput(_prompt) -> str:
    while True:
        try:
            string = input(_prompt)
            return string
        except TimeoutError:
            print("Timeout Error. Try again.")


def getCurrentDir() -> str:
    return f"Current Directory is {os.getcwd()}"


def printOnlyDirs():
    rez = os.scandir('.')
    for i, item in enumerate(rez):
        if item.is_dir():
            print(f"{i} {item.name}  <-- Directory")


def printCurrentDirs():
    rez = os.scandir('.')  # . - current directory
    for i, item in enumerate(rez):
        if item.is_dir():
            print(f"{i} {item.name}  <-- Directory")
        elif item.is_file():
            print(f"{i} {item.name}  <-- File")


def getLowerOnTree() -> None:
    os.chdir(os.pardir)
    print(getCurrentDir())
    main()


def getUpperOnTree(dirName: str) -> None:
    os.chdir(dirName)  # moving to lower directory
    print(getCurrentDir())
    main()


def createDir(isNested: bool):
    """
    Function, which creating Directory, it can be nested or a common directory. (Depends on boolean argument)
    """
    if isNested == 1:
        nestedDir = strInput('Write down the nested directory:\n')
        os.makedirs(nestedDir)
    else:  # or == 0
        dir = strInput('Write down the directory:\n')
        os.mkdir(dir)
    main()


def renameItem(fullName: str) -> None:
    """
    Function, renaming file or directory.
    """
    name, extension = os.path.splitext(fullName)
    newFileName = strInput("Write down the new name of the file\n")
    newFile = f"{newFileName}{extension}"
    path = os.getcwd()
    os.rename(f"{path}/{fullName}", f"{path}/{newFile}")
    print(f"{path}/{newFile}")
    main()


def removeItem(itemDir: str, isDir: bool) -> None:
    """
    Function, which removing file or directory depending on boolean argument.
    """
    if isDir == 1:
        os.removedirs(itemDir)
    else:
        os.remove(itemDir)
    print(f"{itemDir} was deleted.")
    main()


def createFile() -> None:
    """
    Function, which creating new file (Not a directory).
    """
    extension = strInput("Write down the extension\n")
    name = strInput("Write down the file name\n")
    text = strInput("Write down the text for input\n")
    file = f"{name}.{extension}"
    os.system(f"echo {text} > {file}")
    print(f"{file} was created.")
    main()


# make logging

def main() -> None:
    rez = os.scandir('.')
    printCurrentDirs()
    choice = inputInt("\nChoose function:  1. Remove Item  2. Create Item  3. Rename Item  4. Get Upper on tree  "
                      "5. Get Lower on tree  6. Exit\n")
    match choice:
        case 1:
            choice = inputInt("Choose item from the list of files above\n")
            for i, item in enumerate(rez):
                if choice == i:
                    if item.name == "main.py":
                        print("You can't delete this file. It can break the project's ability to functionalize.\n")
                        break
                    else:
                        removeItem(os.path.abspath(item), item.is_dir())
        case 2:
            item = inputInt("You want to create: 1. Directory  2. Nested Directory  3. File\n")
            if item == 1:
                createDir(False)
            elif item == 2:
                createDir(True)
            elif item == 3:
                createFile()
        case 3:
            choice = inputInt("Choose item from the list of files above\n")
            for i, item in enumerate(rez):
                if choice == i:
                    if item.name == "main.py":
                        print("You can't rename this file. It can break the project's ability to functionalize.\n")
                        break
                    else:
                        print(item.name)
                        renameItem(item.name)
            main()
        case 4:
            printOnlyDirs()
            choice = inputInt("Choose item from the list of files above\n")
            for i, item in enumerate(rez):
                if choice == i:
                    if item.is_dir() == 1:
                        if item.name == "main.py":
                            print("You can't rename this file. It can break the project's ability to functionalize.\n")
                            break
                        else:
                            getUpperOnTree(item.name)
                    else:
                        print("This is not a directory. Try again.")
                        main()
        case 5:
            getLowerOnTree()
        case 6:
            exit()


if __name__ == "__main__":
    main()
