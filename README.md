# WordPress'e Otomatik Blog Ekleme Programı

Bu Python programını dijital pazarlama ajansında staj yaparken SEO için blog yapan arkadaşlara yardımcı olsun diye yazdım.Böylece 200 300 bloğu tek seferde girebilecekler,tarih seçeneği vesaire ekleyip genişletilebilir. bir dizindeki `.docx` uzantılı Word dosyalarını okuyarak içeriklerini WordPress'te otomatik olarak blog yazısı olarak ekler. Blog yazıları, WordPress panelinde taslak olarak kaydedilir.

## Özellikler

- Klasördeki tüm `.docx` dosyalarını tarar.
- Her dosya için içerik okur ve WordPress'e taslak blog yazısı olarak ekler.
- Her dosya için kullanıcıdan başlık girişi ister.
- WordPress XML-RPC API kullanarak yazıları WordPress sitesine yükler.

## Gereksinimler

- Python 3.x
- `python-docx` kütüphanesi
- `wordpress-xmlrpc` kütüphanesi

## Kurulum

1. **Gereksinimleri Yükleyin**

   Aşağıdaki komutu kullanarak gerekli Python paketlerini yükleyin:
   

   pip install python-docx wordpress-xmlrpc

2. **WordPress Bilgilerinizi Ayarlayın**

## wp_url, wp_username ve wp_password değişkenlerini kendi WordPress site bilgilerinizle doldurun:
wp_url = "https://siteniz.com/xmlrpc.php"
wp_username = "kullaniciadi"
wp_password = "sifre"
Klasör Yolu Belirleyin

3.**İşlemek istediğiniz Word dosyalarının bulunduğu klasör yolunu directory değişkenine atayın:**
directory = ""

Programı çalıştırmak için terminal veya komut satırında aşağıdaki komutu kullanın:

python3 wordpress-otomatik-blog-ekleme.py
