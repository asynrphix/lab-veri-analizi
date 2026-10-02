import sqlite3
import pandas as pd

# CSV'yi oku
df = pd.read_csv("analiz_sonucu.csv")

# SQLite veritabanı oluştur (bellekte değil, dosya olarak - repo'da gösterebilmek için)
conn = sqlite3.connect("laboratuvar.db")

# DataFrame'i SQL tablosuna aktar
df.to_sql("olcumler", conn, if_exists="replace", index=False)

print("Veritabanı oluşturuldu: laboratuvar.db")
print("=" * 50)

# --- SORGU 1: Limiti aşan günler ---
print("\n1) Limiti aşan günler:\n")
sorgu1 = """
SELECT gun, "% Silica Concentrate"
FROM olcumler
WHERE Limit_Asimi = 1
ORDER BY gun;
"""
sonuc1 = pd.read_sql_query(sorgu1, conn)
print(sonuc1)

# --- SORGU 2: Aylık ortalama ---
print("\n2) Aylık ortalama silika oranı:\n")
sorgu2 = """
SELECT 
    substr(gun, 1, 7) AS ay,
    ROUND(AVG("% Silica Concentrate"), 2) AS ortalama_silica,
    COUNT(*) AS gun_sayisi
FROM olcumler
GROUP BY ay
ORDER BY ay;
"""
sonuc2 = pd.read_sql_query(sorgu2, conn)
print(sonuc2)

# --- SORGU 3: En yüksek 5 silika değeri ---
print("\n3) En yüksek 5 silika değeri:\n")
sorgu3 = """
SELECT gun, "% Silica Concentrate"
FROM olcumler
ORDER BY "% Silica Concentrate" DESC
LIMIT 5;
"""
sonuc3 = pd.read_sql_query(sorgu3, conn)
print(sonuc3)

# --- SORGU 4: Limit aşımı oranı (genel istatistik) ---
print("\n4) Genel özet:\n")
sorgu4 = """
SELECT 
    COUNT(*) AS toplam_gun,
    SUM(Limit_Asimi) AS asan_gun_sayisi,
    ROUND(100.0 * SUM(Limit_Asimi) / COUNT(*), 1) AS asan_yuzde
FROM olcumler;
"""
sonuc4 = pd.read_sql_query(sorgu4, conn)
print(sonuc4)

conn.close()
print("\nTamamlandı.")