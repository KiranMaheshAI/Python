
sumlambda = lambda a: a+a

def ApplyOnaList(l1, func):
    resultList = []
    for i in l1:
        resultList.append(func(i))
    return resultList

isEven = lambda x: x%2==0

f1_filter = list(filter(isEven, [1,2,3,4,5]))
f1_map = list(map(lambda a: a*a, [1, 2, 3, 4]))

if __name__ == "__main__":
    a = sumlambda(1)
    print(a)
    print(ApplyOnaList([1,2,3,4], sumlambda))
    print(ApplyOnaList([1,2,3,4], lambda x: x*x))
    print(ApplyOnaList([1,2,3,4], lambda x: x*x*x))
    print(f1_filter)
    print(f1_map)