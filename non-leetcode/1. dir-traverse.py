import os
def dirTraverse(paths:list[str]) -> list[str]:
    # check is dir is empty: y -> return dir, n -> move forward
    # list all contents of directory
    # for each content -> if file -> append fpath to paths -> if dir call dirTraverse

    dir = paths[-1]
    if os.path.isdir(dir):
        contents = os.listdir(dir)
        for c in contents:
            sub = os.path.join(dir, c)
            if os.path.isdir(sub):
                paths.append(sub)
                dirTraverse(paths)
            elif os.path.isfile(sub):
                paths.append(sub)
    
    print("Number of contents = {}\n".format(len(paths)),"\n".join(paths))

paths = ['path_location']
dirTraverse(paths)
