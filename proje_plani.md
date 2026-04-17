# Microservice Projesi - Grup 10 Yol Haritası ve Görev Dağılımı

Bu doküman, proje kapsamında kullanılacak olan **DevOps ve Yönetim Araçlarını (Git, GitHub, Slack, Jira, Asana, Confluence)** test etmek ve hocanın **"en az 3 mikroservis ve Docker"** şartını sağlamak amacıyla hazırlanmış 2 kişilik görev dağılımını içerir.

## 👥 1. KİŞİ: Versiyon Kontrol ve İletişim Sorumlusu
**Odak Noktası:** Kodların yönetimi, altyapı ve anlık bildirimler.
**Sorumlu Olduğu Araçlar:** Git, GitHub (ve Lokal Gitea), Slack

### Görevleri:
1. **Lokal Git Sunucusu:** Bilgisayara Docker ile `Gitea` (Lokal GitHub) kurmak ve proje deposunu (Repository) oluşturmak.
2. **Slack Entegrasyonu:** Slack çalışma alanını kurmak, kanalları ayarlamak.
3. **Mikroservis 1 (Git Listener):** Git sunucusunda bir kod değişikliği (commit/push) olduğunda bunu algılayıp sistemi tetikleyen Python/Node.js servisini yazmak.
4. **Mikroservis 2 (Slack Notifier):** Diğer servislerden gelen bilgileri alıp Slack API'sini kullanarak kanala otomatik mesaj (Örn: "Yeni kod eklendi") gönderen servisi yazmak.
5. **Dokümantasyon:** Projenin bilgisayara nasıl kurulacağını ve Docker komutlarını anlatan **`installization.pdf`** belgesini hazırlamak.

---

## 👥 2. KİŞİ: Proje Yönetimi ve Dokümantasyon Sorumlusu
**Odak Noktası:** Görev (Ticket) takibi, hata yönetimi ve proje dokümantasyonu.
**Sorumlu Olduğu Araçlar:** Jira, Asana, Confluence

### Görevleri:
1. **Ticket Yönetimi:** Ücretsiz bir Jira hesabı (ve alternatif olarak Asana) açıp proje yönetim panosunu (Board) hazırlamak.
2. **Dokümantasyon (Confluence):** Jira'ya bağlı Confluence sayfasını oluşturup projenin detaylarını, mimarisini ve alınan kararları buraya yazmak.
3. **Mikroservis 3 (Ticket Operator):** Git Listener servisinden gelen komuta göre Jira/Asana API'sine bağlanıp otomatik "Ticket (Görev)" açan veya var olan görevi "Çözüldü (Done)" durumuna getiren servisi yazmak.
4. **Dokümantasyon:** Projenin arka planını anlatan, Asana ve Jira karşılaştırmasını da içeren teknik makaleyi yani **`project-paper.pdf`** belgesini (Confluence üzerinden) hazırlamak.

---

## 🤝 ORTAK YAPILACAKLAR (Projenin Kalbi)

### 1. Dockerizasyon (Zorunlu Kural)
* Her mikroservis için bir `Dockerfile` yazılacak.
* Tüm projenin (Gitea + 3 Mikroservis) tek komutla (`docker-compose up -d`) çalışabilmesi için ana dizinde bir `docker-compose.yml` dosyası hazırlanıp yönetilecek.

### 2. GitHub Teslimi
* Projenin son hali gerçek GitHub'a yüklenecek.
* Hocanın e-posta adresi (`sinan.keskin@gidatarim.edu.tr`) bu repoya eklenecek.

### 3. Sunum ve Demo (project-presentation.pdf)
Sunum sırasında hocaya sistemin nasıl çalıştığı **canlı olarak** gösterilecek:
1. **Adım:** 2. Kişi, Jira üzerinden "Koddaki hatayı çöz" şeklinde bir task (ticket) açacak.
2. **Adım:** 1. Kişi, kodu güya düzeltip lokal Git sunucusuna (Gitea'ya) Terminal üzerinden `git push` yapacak. (Commit mesajına Jira task numarasını ekleyerek: Örn: `Fixes JIRA-12`).
3. **Adım:** Yazılan mikroservisler devreye girecek! Jira'daki ticket otomatik olarak "Çözüldü" durumuna geçecek ve Slack'e "JIRA-12 taskı başarıyla kapatıldı ve kod güncellendi" diye mesaj düşecek.
