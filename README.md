# ⌨️ KeyLogger

**KeyLogger**, Python `pynput` kütüphanesi kullanılarak geliştirilmiş, düşük seviyeli (low-level) bir klavye dinleme ve veri kayıt aracıdır. Bu proje, siber güvenlikte **Post-Exploitation (Sızma Sonrası)** aşamasında kullanıcı davranışlarını ve veri sızıntılarını analiz etmek amacıyla eğitim odaklı geliştirilmiştir.

---

## ✨ Öne Çıkan Özellikler

- ⚡ **Event-Driven Mimari**  
  Sadece tuşa basıldığında tetiklenir, sistemi gereksiz yere yormaz.

- 🕶️ **Gizli Kayıt**  
  Arka planda sessizce çalışarak tüm girdileri `key_log.txt` dosyasına kaydeder.

- 🧹 **Karakter Optimizasyonu**  
  Gereksiz tırnak işaretlerini (`'`) temizleyerek daha okunabilir çıktı üretir.

---

## 🚀 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin.

### 1️⃣ Gereksinimleri Yükleyin

Proje, klavye hareketlerini yakalamak için `pynput` kütüphanesine ihtiyaç duyar:

```bash
pip install pynput
```

### 2️⃣ Projeyi Çalıştırın

Terminal veya CMD üzerinden proje klasörüne gidin ve aşağıdaki komutu çalıştırın:

```bash
python key_log.py
```

### 3️⃣ Durdurma ve Çıktıları Görüntüleme

Programı durdurmak için terminalde `CTRL + C` kombinasyonunu kullanın.

Kaydedilen tüm tuş vuruşları, aynı klasörde otomatik olarak oluşturulan `key_log.txt` dosyasında saklanır.

---

## 🛠️ Teknik Detaylar

Bu araç, Python’un thread yapısını kullanarak bir `Listener` objesi oluşturur.

- `on_press` fonksiyonu her tuş vuruşunu yakalar.
- Dosya, `append ("a")` modunda açılarak yeni veriler mevcut kayıtların üzerine yazılmadan eklenir.
- `with` blok yapısı sayesinde dosya yönetimi güvenli şekilde gerçekleştirilir ve veri kaybı riski azaltılır.

---

## ⚠️ Yasal Uyarı

Bu araç tamamen eğitim ve etik hacking süreçlerini anlamak amacıyla geliştirilmiştir.

Yazılımın hedef sistemlerde izinsiz kullanımı yasal sorumluluk doğurabilir. Geliştirici, kötü amaçlı kullanımlardan sorumlu tutulamaz.

---

## 👨‍💻 Geliştirici

**Beste Berfin TOPALOĞLU**