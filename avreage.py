def avreage(mylist):
    total = sum(mylist)
    avreage = total / len(mylist)
    return avreage

scores = [1, 2, 8, 16, 32, 64, 128, 256]
avreagescore = avreage(scores)
print('The avreage score is ', avreagescore)
