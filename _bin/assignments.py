with open('../index.rst') as file:
    rst = [filename
           for line in file.readlines()
           if (filename := line.strip())
           and filename.endswith('.rst')]

print(rst)
