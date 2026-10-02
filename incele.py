import pandas as pd

df = pd.read_csv("ham_veri.csv")

print("Satır, kolon:", df.shape)
print()
print("Kolon isimleri:")
for kolon in df.columns:
    print("-", kolon)
print()
print("Veri tipleri:")
print(df.dtypes)
print()
print("İlk 3 satır:")
print(df.head(3))