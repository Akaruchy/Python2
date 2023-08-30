# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

lst = [91, 2, 15, 18, 12, 11, 53, 668, 71, 254, 667, 216, 1, 171]
rep_elem = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in rep_elem:
            rep_elem.append(lst[i])
print(rep_elem)