import pandas as pd

frame = pd.read_csv("data_set.tsv", header=0, sep="\t")  # Считываем данные с файла .tsv

frame = frame.append({"Name": "Александров А. Л.", "Birth": "12.05.1986", "City": "Ростов",
                      "Position": "инженер"}, ignore_index=True)  # Добавляем новую запись


frame.to_csv("changed_data.tsv", sep='\t', header=True, index=False)  # Сохраняем в tsv файл
