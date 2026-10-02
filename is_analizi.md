# İş Analizi Dokümanı — Laboratuvar Kalite Kontrol Süreci

## 1. Mevcut Durum (As-Is)

Laboratuvar/kalite kontrol birimlerinde ölçüm verileri genellikle manuel olarak toplanır ve Excel'de elle incelenir. Limit aşımlarının tespiti kişisel gözleme dayanır, bu da şu sorunlara yol açar:
- Limit aşımlarının geç fark edilmesi
- Tutarsız/standart olmayan değerlendirme (kişiden kişiye değişen yorum)
- Zaman kaybı (manuel veri temizleme ve raporlama)

## 2. Sorun Tanımı

Ham ölçüm verisi büyük hacimli olduğunda (bu projede 737.453 satır), manuel inceleme pratik değildir. Limit aşımlarının otomatik, istatistiksel bir yöntemle tespit edilmesi ve raporlanması gerekmektedir.

## 3. Önerilen Çözüm (To-Be)

Geliştirilen araç şu akışı otomatikleştirir:
- Ham veri otomatik çekilir ve temizlenir
- Günlük/aylık özet otomatik hesaplanır
- İstatistiksel limit (ortalama + 1.5×standart sapma) otomatik belirlenir
- Limit aşan günler otomatik işaretlenir ve raporlanır
- Yapay zeka ile aşımlar hakkında yorum üretilir

## 4. Kullanıcı Hikayeleri (User Stories)

| # | Kullanıcı Hikayesi |
|---|---|
| 1 | Laboratuvar sorumlusu olarak, limit aşan günleri otomatik görmek istiyorum ki hızlı aksiyon alabileyim. |
| 2 | Kalite kontrol ekibi olarak, aylık ortalama değerleri görmek istiyorum ki trend değişimlerini takip edebileyim. |
| 3 | Yönetici olarak, belirli bir tarihteki ölçüm değerini hızlıca sorgulamak istiyorum ki geçmiş verileri karşılaştırabileyim. |
| 4 | Kalite kontrol ekibi olarak, anomaliler hakkında otomatik bir yorum almak istiyorum ki olası nedenleri hızlıca değerlendirebileyim. |

## 5. Basit Backlog / Geliştirme Planı

| Sprint | Kapsam |
|---|---|
| Sprint 1 | Veri çekme, temizleme, günlük özet |
| Sprint 2 | İstatistiksel limit hesaplama, anomali tespiti |
| Sprint 3 | Excel raporu (biçimlendirme, grafik, pivot table, arama formülü) |
| Sprint 4 | SQL analiz katmanı, yapay zeka entegrasyonu |

## 6. Beklenen Fayda

- Limit aşımlarının tespit süresinde azalma
- Standart, tekrarlanabilir bir değerlendirme yöntemi
- Manuel veri işleme yükünün azalması
