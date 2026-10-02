import pandas as pd

df = pd.read_csv("ham_veri.csv")

# Sadece ihtiyacımız olan kolonları seçiyoruz
kolonlar = ["date", "% Iron Feed", "% Silica Feed", "% Iron Concentrate", "% Silica Concentrate"]
df = df[kolonlar]

# Tarihi gerçek tarih/saat tipine çeviriyoruz
df["date"] = pd.to_datetime(df["date"])

# Boş hücre var mı kontrol edelim
print("Boş hücre sayısı:")
print(df.isna().sum())

# Günlük ortalamaya indiriyoruz (737 bin satırı ~180 güne indirir)
df["gun"] = df["date"].dt.date
gunluk = df.groupby("gun")[["% Iron Feed", "% Silica Feed", "% Iron Concentrate", "% Silica Concentrate"]].mean()
gunluk = gunluk.round(2)
gunluk = gunluk.reset_index()

print()
print("Günlük özet, satır sayısı:", len(gunluk))
print(gunluk.head())

gunluk.to_csv("gunluk_ozet.csv", index=False)
print()
print("Kaydedildi: gunluk_ozet.csv")