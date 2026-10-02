import pandas as pd

df = pd.read_csv("gunluk_ozet.csv")

# İstatistikleri hesaplıyoruz
ortalama = df["% Silica Concentrate"].mean()
std_sapma = df["% Silica Concentrate"].std()
limit = ortalama + 1.5 * std_sapma

print(f"Ortalama: {ortalama:.2f}")
print(f"Standart sapma: {std_sapma:.2f}")
print(f"Hesaplanan limit: {limit:.2f}")
print()

# Limiti aşan günleri işaretliyoruz
df["Limit_Asimi"] = df["% Silica Concentrate"] > limit

asan_gun_sayisi = df["Limit_Asimi"].sum()
print(f"Limiti aşan gün sayısı: {asan_gun_sayisi} / {len(df)}")
print()

print("Limiti aşan günler:")
print(df[df["Limit_Asimi"]][["gun", "% Silica Concentrate"]])

df.to_csv("analiz_sonucu.csv", index=False)
print()
print("Kaydedildi: analiz_sonucu.csv")