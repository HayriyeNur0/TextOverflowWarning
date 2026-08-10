# TFT Overflow Warning

TFT ekranlarda kullanılan metinlerin belirlenen ekran alanına sığıp sığmadığını kontrol etmek amacıyla geliştirilmiş Python tabanlı bir analiz aracıdır.

## Projenin Amacı

Üretim aşamasında kullanılacak metinlerin TFT ekran üzerinde taşma oluşturup oluşturmadığını önceden tespit etmek ve metinlerin ekran alanına uygunluğunu kontrol etmektir.

## Nasıl Çalışır?

1. Kullanıcı TFT widget bilgilerini manuel olarak girer.
2. Kullanılacak font kullanıcı tarafından seçilir.
3. Seçilen emWin `.c` font dosyası analiz edilir.
4. Font içerisindeki karakter genişlikleri ve font yüksekliği okunur.
5. `texts.txt` dosyasındaki metinler okunur.
6. Metinlerin yatay ve dikey olarak ekrana sığıp sığmadığı kontrol edilir.
7. Her metin için PASS veya FAIL sonucu gösterilir.
8. Analiz sonunda toplam sonuçlar özetlenir.

## Özellikler

- Manuel Width, Height, Font, X ve Y bilgisi girişi
- emWin `.c` font dosyalarını parse etme
- Gerçek karakter genişliklerini kullanarak metin genişliği hesaplama
- Font yüksekliğini kullanarak dikey kontrol yapma
- `texts.txt` üzerinden birden fazla metni analiz etme
- Yatay taşma kontrolü
- Dikey taşma kontrolü
- PASS / FAIL sonuçları
- Analiz özeti

## Kullanılan Teknolojiler

- Python
- emWin Font Files
- Git
- GitHub
