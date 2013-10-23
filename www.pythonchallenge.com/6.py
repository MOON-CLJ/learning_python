import zipfile

zip_file = zipfile.ZipFile('channel.zip')
file_name = "channel/%s.txt"

ll = []
no = 90052
while 1:
    with open(file_name % no) as f:
        l = f.readline()
        no = l.split()[-1]
        print no
        if not no.isdigit():
            break
        else:
            ll.append(zip_file.getinfo("%s.txt" % no).comment)

print ''.join(ll)
