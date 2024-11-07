import pandas as pd
import os


# Belirli uzantıya sahip dosyaları bulur
def find_excel_files(directory, extension=".xlsx"):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(extension)]


# Kullanıcıdan sütun seçimi yapmasını ister
def select_columns(dataframe):
    print("Mevcut sütunlar:", list(dataframe.columns))
    selected_columns = input("Lütfen istediğiniz sütunları virgülle ayırarak girin: ").split(",")
    selected_columns = [col.strip() for col in selected_columns]
    return selected_columns


# Seçime göre birleştirme ya da listeleme yapar
def process_data(files, merge=False):
    result = pd.DataFrame()
    for file in files:
        df = pd.read_excel(file)
        selected_columns = select_columns(df)
        df_selected = df[selected_columns]

        if merge:
            result = pd.concat([result, df_selected], ignore_index=True)
        else:
            print(f"{file} dosyasından seçilen sütunlar:\n", df_selected)

    if merge:
        result.to_excel("birlesik_sonuc.xlsx", index=False)
        print("Birleştirilmiş dosya 'birlesik_sonuc.xlsx' olarak kaydedildi.")


# Kullanım
directory = input("Excel dosyalarının bulunduğu klasör yolunu girin: ")
files = find_excel_files(directory)
process_choice = input("Birleştirme yapmak istiyor musunuz? (evet/hayir): ").strip().lower()
merge = True if process_choice == "evet" else False

process_data(files, merge)
