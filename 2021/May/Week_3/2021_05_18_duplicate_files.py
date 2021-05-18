class Solution:
    def findDuplicate(self, paths: list) -> list:
        dict = {}
        duplicates = {}
        for p in paths:
            c_start = [i for i, c in enumerate(p) if c == '(']
            c_end = [i for i, c in enumerate(p) if c == ')']
            f_start = [i for i, c in enumerate(p) if c == ' ']
            prefix = p[:f_start[0]]
            files = []
            contents = []
            for i in range(len(c_start)):
                path = prefix + '/' + p[f_start[i]+1:c_start[i]]
                content = p[c_start[i]+1:c_end[i]]
                files.append(path)
                contents.append(content)
            for f, c in zip(files, contents):
                if c in dict: 
                    dict[c].append(f)
                    duplicates[c] = None
                else: dict[c] = [f]
        return [dict[c] for c in duplicates.keys()]




testcases = [
    (
        ["root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)"], 
        [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
        ["root/a/1.txt","root/c/3.txt"]]
    ),
    (
        ["root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)"],
        [["root/a/2.txt","root/c/d/4.txt"],
        ["root/a/1.txt","root/c/3.txt"]]
    ),
    (
        ["root/a 1.txt(abcd) 2.txt(efsfgh)",
        "root/c 3.txt(abdfcd)",
        "root/c/d 4.txt(efggdfh)"],
        []
    ),
    (
        ["root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)","root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)"],
        [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],
        ["root/a/1.txt","root/c/3.txt"]]
    )
]

for i, (paths, duplicates) in enumerate(testcases):
    result = Solution().findDuplicate(paths)
    print('Case #{}'.format(i+1))
    print('Should be:')
    print(duplicates)
    print('Is:')
    print(result)
    print('-'*30)
        