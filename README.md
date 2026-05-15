# ⌨️ PyKey-Logger v1.0

**PyKey-Logger**, Python `pynput` kütüphanesi kullanılarak geliştirilmiş, düşük seviyeli (low-level) bir klavye dinleme ve veri kayıt aracıdır. Bu proje, siber güvenlikte **"Post-Exploitation"** (Sızma Sonrası) aşamasında kullanıcı davranışlarını ve veri sızıntılarını analiz etmek amacıyla eğitim odaklı geliştirilmiştir.

## ✨ Öne Çıkan Özellikler
- **Event-Driven Mimari:** Sadece tuşa basıldığında tetiklenir, sistemi gereksiz yormaz.
- **Gizli Kayıt:** Arka planda sessizce çalışarak tüm girdileri `key_log.txt` dosyasına raporlar.
- **Karakter Optimizasyonu:** Gereksiz tırnak işaretlerini (`'`) temizleyerek okunabilirliği artırılmış çıktı sağlar.

---

## 🚀 Kurulum ve Çalıştırma

Bu projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla takip edin:

### 1. Gereksinimleri Yükleyin
Proje, klavye hareketlerini yakalamak için `pynput` kütüphanesine ihtiyaç duyar:
```bash
pip install pynput

### 2. Projeyi Çalıştırın
Terminal veya CMD üzerinden proje klasörüne giderek şu komutu verin:
python key_log.py

### 3. Durdurma ve Çıktıları Görüntüleme
Programı durdurmak için terminalde CTRL + C kombinasyonunu kullanın.

Kaydedilen tüm tuş vuruşları, aynı klasör içerisinde otomatik olarak oluşturulan key_log.txt dosyasında saklanır.

🛠️ Teknik Detaylar
Bu araç, Python'un thread yapısını kullanarak bir Listener objesi oluşturur. on_press fonksiyonu, her tuş vuruşunu yakalar ve dosyayı append (a) modunda açarak veriyi kaydeder. with blok yapısı sayesinde dosya yönetimi güvenli bir şekilde yapılır ve veri kaybı önlenir.

⚠️ Yasal Uyarı
Bu araç tamamen eğitim ve etik hacking süreçlerini anlamak için tasarlanmıştır. Bu yazılımın hedef sistemlerde izinsiz kullanımı yasal sorumluluk doğurabilir. Geliştirici, kötü amaçlı kullanımlardan sorumlu tutulamaz.

Geliştiren: Beste Berfin TOPALOĞLU