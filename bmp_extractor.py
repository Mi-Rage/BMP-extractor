CONTROL_SIZE = 20000000
source_dump = 'user.bmp'

with open(source_dump, "rb") as f:
    data = f.read()
print('Source file ', source_dump, ' with length', len(data))

for index in range(len(data)):
    if data[index] == 66 and data[index+1] == 77:
        print('[+] File found at ' + str(index) + ' offense')
        size_from_data = data[index + 2: index + 7]
        size = '0x'
        for i in reversed(size_from_data):
            size += str(hex(i))[2:]
            # print(str(hex(i))[2:])
        print('[+] File length ', size)
        int_size = int(size, 16)
        if int_size < CONTROL_SIZE:
            filename = 'result' + str(index) + '.bmp'
            with open(filename, 'wb') as f:
                f.write(data[index:index + int_size])
            print('[+] File saved!')
        else:
            print('[-] Wrong file size, dnt save.')


