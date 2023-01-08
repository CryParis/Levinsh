
import argparse
import pickle
import ast
import glob
import tokenize

parser = argparse.ArgumentParser()
parser.add_argument('-b', dest="scores", required=True)
args = parser.parse_args()

# Левинштейн
def dist(a ,b):
    def rec(i, j):
        if i == 0 or j == 0:
            # если строка пустая, то расстояние равняется её длине 
            return max(i,j)
        elif a[i-1] == b[j-1]:
            # если последние символы одинаковы, просто сЬедаем их
            return rec(i-1, j-1)
        else:
            # иначе считаем min вариант
            return 1+min(
                rec(i, j-1),# удаление символа
                rec(i-1, j),# вставка символа
                rec(i-1, j-1)# замена символа
            )

    return rec(len(a), len(b))



str1 = "привет"
str2 = "Привет"

# преобразуем всё к нижнему регистру
def tolowercase(a, b): 
    a = a.casefold()
    b = b.casefold()
    return a,b

str1,str2=tolowercase(str1,str2)
print(str1,str2)

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) * 100

print(
    "Строка #1 : {str1}\nСтрока #2 : {str2} \n===\nСхожесть : {pct}%".format(str1=str1,str2=str2,pct=pct)
)
 
# args.scores = pct  
# сериализация 
with open('model.pkl', 'wb') as f:
    pickle.dump(pct, f)

with open('model.pkl', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)