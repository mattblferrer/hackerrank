if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for N_itr in range(N):
        cmd = input().split(" ")
        if cmd[0] == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(lst)
        elif cmd[0] == "remove":
            lst.remove(int(cmd[1]))
        elif cmd[0] == "append":
            lst.append(int(cmd[1]))
        elif cmd[0] == "sort":
            lst = sorted(lst)
        elif cmd[0] == "pop":
            lst.pop()
        elif cmd[0] == "reverse":
            lst = list(reversed(lst))
