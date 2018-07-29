import pandas as pd

frame = pd.read_csv("data_set.tsv", header=0, sep="\t")

# Получаем выборку с помощью функции loc
print(frame.loc[[1, 2, 3], ["Name", "Position"]])

# Получаем выборку с помощью функции iloc
print(frame.iloc[[1, 2, 3], [0, 3]])

# Получаем выборку с помощью функции ix
print(frame.ix[[1, 2, 3], [0, 3]])

print()
# Условие выборки
print(frame[(frame.City != "Волгоград") & (frame.Position == "инженер")])
