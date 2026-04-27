# Git Araçları Karşılaştırması: GitHub vs GitLab vs Gitea

## Giriş

Versiyon kontrol sistemleri, yazılım geliştirme süreçlerinin temel taşlarından biridir. Git tabanlı platformlar arasında en yaygın kullanılanlar GitHub, GitLab ve Gitea'dır. Bu raporda söz konusu üç araç; kurulum, maliyet, güvenlik, özellikler ve kullanım kolaylığı açısından karşılaştırılmaktadır. Projemizde Gitea tercih edilmiş olup bu tercih gerekçesiyle birlikte açıklanmaktadır.

---

## 1. GitHub

GitHub, 2008 yılında kurulmuş ve 2018'den itibaren Microsoft bünyesinde faaliyet gösteren en popüler Git platformudur.

**Artıları:**
- Dünyanın en büyük açık kaynak topluluğuna ev sahipliği yapar
- GitHub Actions ile güçlü CI/CD desteği sunar
- Kullanıcı arayüzü son derece olgun ve kullanışlıdır
- Ücretsiz planda sınırsız public repo ve sınırlı private repo imkânı tanır

**Eksileri:**
- Tüm veriler Microsoft sunucularında barındırılır; veri gizliliği tam olarak sağlanamaz
- Self-hosted (kendi sunucusunda çalıştırma) seçeneği yalnızca GitHub Enterprise ile mümkündür ve ücretlidir
- Kurumsal kullanımda maliyetler hızla artabilir

---

## 2. GitLab

GitLab, 2011 yılında kurulan ve hem bulut hem de self-hosted seçeneği sunan kapsamlı bir DevOps platformudur.

**Artıları:**
- CI/CD pipeline'ları için piyasadaki en güçlü yerleşik araçlardan birini sunar
- Self-hosted kurulumu ücretsiz olarak yapılabilir
- Issue takibi, wiki, container registry gibi tüm DevOps araçları tek çatı altında sunulur
- Kaynak kodunun büyük bölümü açıktır

**Eksileri:**
- Kendi sunucusuna kurulumu kaynak açısından maliyetlidir (yüksek RAM gerektirir)
- Arayüz ve yapılandırma seçenekleri GitHub'a kıyasla daha karmaşıktır
- Küçük ekipler için fazla özellik içerebilir

---

## 3. Gitea

Gitea, 2016 yılında Gogs projesinden fork edilerek geliştirilen hafif ve açık kaynaklı bir self-hosted Git platformudur.

**Artıları:**
- Son derece hafif yapısı sayesinde düşük donanımlı sistemlerde rahatlıkla çalışır
- Docker ile tek komutla (`docker-compose up`) kurulabilir
- Tüm veriler yerel sunucuda tutulduğundan tam veri gizliliği sağlanır
- Tamamen ücretsiz ve açık kaynaklıdır
- Webhook, API ve temel CI/CD desteği mevcuttur

**Eksileri:**
- GitHub ve GitLab'a kıyasla daha küçük bir topluluğa sahiptir
- Gelişmiş CI/CD özellikleri sınırlıdır
- Kurulum ve bakım kullanıcının sorumluluğundadır

---

## Karşılaştırma Tablosu

| Kriter                | GitHub              | GitLab               | Gitea               |
|-----------------------|---------------------|----------------------|---------------------|
| Kurulum               | Bulut (hazır)       | Bulut / Self-hosted  | Self-hosted         |
| Fiyat                 | Freemium            | Freemium             | Tamamen ücretsiz    |
| Self-hosted           | Yalnızca Enterprise | Ücretsiz mevcut      | Varsayılan          |
| CI/CD                 | GitHub Actions      | GitLab CI (güçlü)    | Sınırlı             |
| Veri Gizliliği        | Microsoft sunucusu  | Self-hosted ile tam  | Tam kontrol         |
| Kaynak Kod            | Kapalı              | Kısmen açık          | Tamamen açık        |
| Sistem Gereksinimleri | Yok (bulut)         | Yüksek               | Çok düşük           |
| Topluluk Büyüklüğü    | Çok büyük           | Büyük                | Orta                |
| Kurulum Kolaylığı     | Yok (bulut)         | Orta                 | Kolay (Docker)      |

---

## Projemizdeki Tercih: Gitea

Bu projede **Gitea** tercih edilmesinin temel gerekçeleri şunlardır:

1. **Tam kontrol:** Tüm kod ve commit geçmişi kendi bilgisayarımızda barındırılmaktadır; veriler üçüncü taraf sunuculara gönderilmemektedir.
2. **Kolay kurulum:** Docker Compose ile tek komut (`docker-compose up -d gitea`) yeterlidir.
3. **Düşük kaynak tüketimi:** Gitea, GitLab'ın aksine sıradan bir dizüstü bilgisayarda sorunsuz çalışmaktadır.
4. **Webhook desteği:** Projemizin Jira ve Slack entegrasyonu, Gitea'nın webhook özelliği sayesinde hayata geçirilmiştir.

---

## Sonuç

GitHub geniş topluluk ve kullanım kolaylığıyla öne çıkarken, GitLab güçlü CI/CD altyapısıyla kurumsal ortamlar için idealdir. Gitea ise veri gizliliğine önem veren, kendi sunucusunda çalışmak isteyen ve hafif bir çözüm arayan ekipler için en uygun seçenektir. Projemizin ihtiyaçları doğrultusunda Gitea tercih edilmiş ve başarıyla yapılandırılmıştır.
