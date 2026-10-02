# Laboratuvar Veri Analizi ve Raporlama Aracı

Gerçek bir maden/flotasyon tesisi verisini (Kaggle: [Quality Prediction in a Mining Process](https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process)) temizleyip analiz eden, limit aşımlarını tespit eden, Excel raporu üreten ve yapay zeka (Google Gemini) ile otomatik yorum ekleyen uçtan uca bir veri analizi projesi.

## Projenin Amacı

Bir laboratuvarın/kalite kontrol biriminin günlük işini simüle eder:
1. Ham ölçüm verisini temizler ve günlük özete indirger
2. İstatistiksel bir limit hesaplayıp bu limiti aşan günleri tespit eder
3. Sonucu, renkli işaretlemeli, grafikli, özetli bir Excel raporuna dönüştürür
4. Yapay zeka ile limit aşımları hakkında profesyonel bir yorum ürettirir

## Kullanılan Teknolojiler

- **Python**: pandas (veri işleme), openpyxl (Excel oluşturma)
- **Kaggle API / kagglehub**: gerçek veri setini otomatik indirme
- **Google Gemini API**: otomatik anomali yorumu üretimi
- **Excel**: Pivot Table, INDEX+MATCH formülü (manuel eklenen ileri Excel analizleri)

## Veri Akışı

```
Kaggle (737.453 satır, 24 kolon)
  → veri_cek.py       : veriyi indirir, kaydeder
  → temizle.py        : 5 kolona indirger, günlük ortalamaya çevirir (172 gün)
  → analiz.py          : istatistiksel limit hesaplar (ort + 1.5×std sapma), aşan günleri işaretler
  → gemini_yorum.py    : limit aşan günler için AI yorumu üretir
  → excel_rapor.py     : her şeyi lab_raporu_final.xlsx içine yazar
```

## Excel Raporunun İçeriği

- **Veri sayfası**: 172 günlük temiz veri, limit aşan satırlar kırmızı işaretli
- **Özet sayfası**: istatistikler, trend grafiği, AI değerlendirmesi
- **Pivot_Analiz sayfası**: aylık ortalama silika oranı (Pivot Table)
- **Özet sayfasında arama formülü**: belirli bir tarihin değerini anında getiren INDEX+MATCH

## Kurulum

```bash
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
pip install pandas openpyxl kagglehub[pandas-datasets] google-genai python-dotenv
```

`.env` dosyası oluştur:
```
GEMINI_API_KEY=kendi_api_keyin
```

## Çalıştırma Sırası

```bash
python veri_cek.py
python temizle.py
python analiz.py
python gemini_yorum.py
python excel_rapor.py
```

---

## İleri Excel Analizleri — Adım Adım Nasıl Yapıldı

Bu iki analiz, kod ile değil **doğrudan Excel arayüzünden** eklenmiştir.

### 1. Pivot Table (Aylık Ortalama Analizi)

1. `Veri` sayfasında herhangi bir hücreye tıkla
2. **Insert (Ekle) → PivotTable**
3. Veri aralığının doğru algılandığından emin ol (`Veri!$A$1:$E$173`), **New Worksheet** seçili bırak, **OK**
4. Sağdaki alan listesinden:
   - `gun` alanını **Rows** kutusuna sürükle
   - `% Silica Concentrate` alanını **Values** kutusuna sürükle
5. Values kutusundaki alana tıkla → **Value Field Settings** → **Average** seç (varsayılan "Sum" yerine)
6. Aylık gruplama için: tarih hücrelerinden birine sağ tıkla → **Group** → **Months** işaretle → **OK**
7. Sayfa adını **Pivot_Analiz** olarak değiştir

**Sonuç:** Her ay için ortalama silika oranını gösteren özet bir tablo.

### 2. INDEX+MATCH ile Tarih Bazlı Arama

`Özet` sayfasında, boş bir alana:

1. Bir hücreye **"Tarih Sorgula:"** yaz, yanındaki hücreye sorgulanacak tarihi yaz (örn. `2017-04-20`)
2. Bir alt satıra **"Silica Değeri:"** yaz, yanındaki hücreye şu formülü ekle:

```
=INDEX(Veri!E:E,MATCH(TEXT(B46,"yyyy-mm-dd"),Veri!A:A,0))
```

**Formülün mantığı:**
- `MATCH(...)`: aranan tarihi `Veri` sayfasının A sütununda (tarih sütunu) bulur, kaçıncı satırda olduğunu döndürür
- `TEXT(B46,"yyyy-mm-dd")`: Excel'in tarihi kendi formatına çevirmesinden kaynaklanan uyuşmazlığı önlemek için, aranan tarihi Veri sayfasıyla aynı metin formatına çevirir
- `INDEX(Veri!E:E,...)`: bulunan satır numarasını kullanıp E sütunundaki (% Silica Concentrate) değeri getirir

**Not:** Daha yeni Excel/Microsoft 365 sürümlerinde `XLOOKUP` fonksiyonu da aynı işi tek fonksiyonla yapar:
```
=XLOOKUP(B46,Veri!A:A,Veri!E:E,"Bulunamadı")
```
Bu projede her Excel sürümünde çalışması için INDEX+MATCH tercih edilmiştir.

**Test etmek için:** Tarih hücresindeki değeri değiştirince sonucun otomatik güncellendiğini görebilirsiniz.

## Notlar

- Veri Kaggle'dan alınan gerçek ölçüm verisidir, laboratuvar bağlamı (limit, kalite kontrol dili) bu projeye özel olarak kurgulanmıştır.
- `ham_veri.csv` boyutu nedeniyle (143 MB) bu repoda yer almaz; `veri_cek.py` çalıştırıldığında Kaggle'dan otomatik indirilir.
