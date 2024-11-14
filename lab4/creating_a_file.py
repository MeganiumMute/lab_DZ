from text import*
# import pickle
# import json
f=open('text.json', 'w')
q=0
# with f as file:
#     # file.writelines(arr[q])
#     # q+=1
#     print>>f, arr
# print(*f)
for element in arr:
    f.write(str(element)+'\n')
#    f.write('%s\n' % element)
    # print( element, file=file)
    # f.write(json.dumps(element))
    # fro key, value in element.items():
f.read()
f.close()