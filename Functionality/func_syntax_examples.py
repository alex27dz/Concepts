'''  python Syntax  '''


def variables():
    name = "John"
    age = 25
    height = 1.75
    is_student = True
def strings():
    string = 'example'
    substring = 'example2'
    old = 'e'
    new = 'a'
    separator = ','
    print(string[0])  # String indexing
    print(string[1:4])  # String Slicing
    len(string)  # Returns the length of the string.
    string.lower()  # Returns the lowercase version of the string.string.upper(): Returns the uppercase version of the string.
    string.strip()  # Removes leading and trailing whitespace from the string.
    string.replace(old, new)  # Replaces all occurrences of old in the string with new.
    string.split(separator)  # Splits the string into a list of substrings based on the separator.
    string.startswith(substring)  # Returns True if the string starts with the specified substring.
    string.endswith(substring)  # Returns True if the string ends with the specified substring.
    string.count(substring)  # Returns the number of times substring appears in the string.
    string.find(substring)  # Returns the index of the first occurrence of substring in the string.
    string.isnumeric()  # Returns True if the string consists of only numeric characters.
    string.isalpha()  # Returns True if the string consists of only alphabetic characters.
    string.isalnum()  # Returns True if the string consists of only alphanumeric characters.
def lists():
    lista = [5, 2, 3]
    print(lista)
    len(lista)  # Returns the number of elements in the list.
    listb = ['alex', 'bob', 'john']
    new_list = listb[0:3]  # slicing
    print(new_list)
    listc = ['a', 'b', 'c', 'd']
    print(listc)
    item = 1
    index = 1
    listb.append(item)  # Adds an element to the end of the list.
    listb.insert(index, item)  # Inserts an element at a specific index in the list.
    listb.remove(item)  # Removes the first occurrence of an element from the list.
    listb.pop(index)  # Removes and returns the element at a specific index in the list.
    list.sort(lista)  # Sorts the elements of the list in ascending order.
    print(lista)
    listb.reverse()  # Reverses the order of the elements in the list.
    listb.index(item)  # Returns the index of the first occurrence of an element in the list.
    listb.count(item)  # Returns the number of times an element appears in the list.
    listb.copy()  # Returns a shallow copy of the list.
    listb.clear()  # Removes all elements from the list
    iterable = 'a'
    listb.extend(iterable)  # Appends the elements of an iterable to the end of the list.
def dictionary():
    fruits = {
        "apple": 1,
        "banana": 2,
        "cherry": 3
    }
    print(fruits)
    print(fruits["apple"])  # printing value of apple key
    print(len(fruits))  # Output: 3
    print(fruits.keys())  # Output: dict_keys(['apple', 'banana', 'cherry'])
    print(fruits.values())  # Output: dict_values([1, 2, 3])
    print(fruits.items())  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])
    print(fruits.get("apple", 0))  # Output: 1
    print(fruits.get("orange", 0))  # Output: 0
    removed_value = fruits.pop("banana", 0)
    print(removed_value)  # Output: 2
    print(fruits)  # Output: {'apple': 1, 'cherry': 3}
    key, value = fruits.popitem()
    print(key, value)  # Output: ('cherry', 3)
    print(fruits)  # Output: {'apple': 1}
    fruits.update({"orange": 4, "grape": 5})
    print(fruits)  # Output: {'apple': 1, 'orange': 4, 'grape': 5}
    fruits.clear()
    print(fruits)  # Output: {}
    person = {"name": "Alice", "age": 25, "city": "New York"}
    print(person["name"])
def email_send():
    import yagmail

    # Email
    email = 'alex27dz@gmail.com'
    subject = 'test1'
    body = 'hello world'
    pass_auth = 'yeqnnbfgkfetetcr'

    def send_email(email, subject, body):
        ya_email = yagmail.SMTP('alex27dz@gmail.com', pass_auth)
        ya_email.send(email, subject, body)
        print('email sent')

    send_email(email, subject, body)
# email_send()


def linux_bash_commands():
    '''
    Bash and terminal commands in Linux:

    ls: List files and directories in the current directory.
    cd: Change the current directory.
    pwd: Print the working directory (current directory).
    mkdir: Create a new directory.
    rm: Remove/delete files or directories.
    cp: Copy files or directories.
    mv: Move or rename files or directories.
    touch: Create an empty file or update the access/modification time of a file.
    cat: Concatenate and display the content of files.
    more: Display file content one screen at a time.
    less: View file content with backward navigation support.
    head: Display the beginning of a file (default: first 10 lines).
    tail: Display the end of a file (default: last 10 lines).
    grep: Search for a specific pattern in files.
    find: Search for files and directories in a directory hierarchy.
    ps: Show information about running processes.
    kill: Terminate processes using their process ID (PID).
    top: Display system monitoring information and current processes.
    df: Show disk space usage for file systems.
    du: Estimate file and directory space usage.
    chmod: Change file permissions.
    chown: Change file ownership.
    tar: Create or extract tar archives.
    ssh: Connect to a remote server using SSH.
    scp: Securely copy files between local and remote systems over SSH.
    ping: Send ICMP echo requests to a host.
    wget: Download files from the internet.
    curl: Transfer data with URLs.
    history: Display the command history.
    man: Display the manual page of a command.
    '''










