file = open('wider_face_train_bbx_gt.txt', 'rt')
content = file.read()

chunks = content.split('\n')
i = 0
classList = []

with open('new_annotations.txt', 'w') as fp:

    while i < len(chunks):
        if 'Street_Battle' not in chunks[i]:
            fp.write(chunks[i] + "\n")
        else:
            str = chunks[i]
            list1 = list(str)
            list1[0] = '6'
            list1[1] = '0'
            str = ''.join(list1)
            fp.write(str + "\n")
        i = i + 1
# >>> str1 = "mystring"
# >>> list1 = list(str1)
# >>> list1[5] = 'u'
# >>> str1 = ''.join(list1)
