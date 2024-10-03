magazin_save=[]
tovar_save=[]
place_save=[]
spisok={}

schet_magazin=0
schet_tovar=0
schet_place=0
schet2l_magazin=0

# for inter in input('Введите интересующие вас магазины:\n'):
#     magazin_save+=inter
#     if input('Еще есть магазины которые вы хотите сравнить?(y/n)\n')=='n':
#         break
# for inter in input('Введите интересующие вас товары:\n'):
#     place_save.append(int(input('Введите цену интересующего вас товара:\n')))
#     tovar_save+=inter
#     if input('Еще есть товары которые вы хотите сравнить?(y/n)\n')=='n':
#         break

while True:
    magazin_save.append(input('Введите интересующие вас магазины:\n'))
    print(magazin_save)
    if input('Еще есть магазины которые вы хотите сравнить?(y/n)\n')=='n':
        break
    
while True:
    tovar_save.append(input('Введите интересующие вас товары в магазинах:\n'))
    print(tovar_save)
    if input('Еще есть товары которые вы хотите сравнить в этом магазинах?(y/n)\n')=='n':
        break

while True:
    place_save.append(int(input('Введите цену товара:' + tovar_save[schet_tovar] + 'в магазине' + magazin_save[schet_magazin]+'\n' )))
    schet_tovar+=1
    print(place_save)
    if schet_tovar==len(tovar_save):
         print(len(tovar_save))
         print(schet_tovar)
         schet_magazin+=1
         schet_tovar=0
    if schet_magazin==len(magazin_save):
         break
         




while True:
    schet_tovar=0
    schet_magazin=0
    spisok2l={}
    spisok2l[schet_tovar]=place_save[schet_place]
    spisok[magazin_save[schet_magazin]]=spisok2l
    schet_place+=1
    schet_magazin+=1
    if schet

print(spisok)