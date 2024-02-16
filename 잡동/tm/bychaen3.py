from collections import defaultdict

dic = defaultdict(list)


def mkdir(directory):
    arr = directory.lstrip('/').split('/')
    name = ''
    for i in range(len(arr)):
        if arr[i] not in dic[name]:
            dic[name].append(arr[i])
        name += '/' + arr[i]


def rm(directory):
    end = len(directory)
    for i in range(end - 1, -1, -1):
        if directory[i] == '/':
            end = i
            break
    prev_directory = directory[:end]
    rm_directory = directory[end + 1:]
    if rm_directory in dic[prev_directory]:  # 상위 디렉터리에서 삭제할 디렉터리 삭제
        dic[prev_directory].remove(rm_directory)
    rm_dfs(directory)  # 하위 디렉터리 삭제


def rm_dfs(name):
    global dic
    if name not in dic.keys():
        return
    del dic[name]
    for v in dic[name]:
        dir_name = name + '/' + v
        rm_dfs(dir_name)


def cp(source, dest):
    arr = source.lstrip('/').split('/')
    dest = dest.lstrip('/')
    dic[dest].append(arr[-1])
    cp_dfs(source, dest)


def cp_dfs(name, dest):
    global dic
    if name not in dic.keys():
        return
    for value in dic[name]:
        dir_name = name + '/' + value
        cp_dfs(dir_name, dest + name)
    arr = name.lstrip('/').split('/')
    dic[dest + '/' + arr[-1]] = dic[name][:]


def solution(directories, commands):
    global dic
    dic = defaultdict(list)
    for directory in directories:
        mkdir(directory)
    for i in range(len(commands)):
        arr = commands[i].split(' ')
        if arr[0][0] == 'm':  # mkdir
            directory = arr[1]
            mkdir(directory)
        elif arr[0][0] == 'r':  # rm
            directory = arr[1]
            rm(directory)
        elif arr[0][0] == 'c':  # cp
            source = arr[1]
            dest = arr[2]
            cp(source, dest)
    result = []
    for key, values in dic.items():
        for value in values:
            result.append(key + '/' + value)
    result.sort()
    return result


print(solution([
    "/",
    "/hello",
    "/hello/tmp",
    "/root",
    "/root/abcd",
    "/root/abcd/etc",
    "/root/abcd/hello"
], [
    "mkdir /root/tmp",
    "cp /hello /root/tmp",
    "rm /hello"
]))

print(solution([
    "/"
],
    [
        "mkdir /a",
        "mkdir /a/b",
        "mkdir /a/b/c",
        "cp /a/b /",
        "rm /a/b/c"
    ]
))
