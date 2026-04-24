# Microservice Projesi - Grup 10 Yol Haritası ve Görev Dağılımı

Bu doküman, proje kapsamında kullanılacak olan **DevOps ve Yönetim Araçlarını (Git, GitHub, Slack, Jira, Asana, Confluence)** test etmek ve hocanın **"en az 3 mikroservis ve Docker"** şartını sağlamak amacıyla hazırlanmış 2 kişilik görev dağılımını içerir.

---

## 👥 1. KİŞİ (Beyza): Ticket Yönetimi ve Dokümantasyon Sorumlusu
**Branch:** `feature/ticket-management-beyza`
**Odak Noktası:** Görev (Ticket) takibi, hata yönetimi ve proje dokümantasyonu.
**Sorumlu Olduğu Araçlar:** Jira, Confluence, Asana

### Görevleri:
1. **Jira:** Ücretsiz Jira hesabı açıp proje yönetim panosunu (Board) hazırlamak, sprint planlamak, microservislere ticket açmak.
2. **Confluence:** Jira'ya bağlı Confluence sayfasını oluşturup projenin mimarisini ve detaylarını buraya yazmak.
3. **Asana:** Jira'ya alternatif olarak Asana'yı kurup ikisini karşılaştırmalı göstermek.
4. **Mikroservis 1 (user-service):** Kullanıcı CRUD işlemleri yapan REST API servisi.
5. **Mikroservis 2 (order-service):** Sipariş yönetimi yapan REST API servisi.
6. **Döküman:** Projenin arka planını anlatan, Jira ve Asana karşılaştırmasını içeren **`project-paper.pdf`** belgesini hazırlamak.

---

## 👥 2. KİŞİ: Versiyon Kontrol ve İletişim Sorumlusu
**Branch:** `feature/version-control`
**Odak Noktası:** Kodların yönetimi, altyapı ve anlık bildirimler.
**Sorumlu Olduğu Araçlar:** Git, GitHub, Slack

### Görevleri:
1. **Git:** Branching stratejisi, workflow, komutları ve GitHub vs GitLab vs Gitea karşılaştırması yapmak.
2. **GitHub:** Repository yönetimi, Pull Request, Issues, webhook kurulumu.
3. **Slack:** GitHub/Jira entegrasyonu kurmak - commit/PR gelince Slack'e bildirim gitsin.
4. **Mikroservis 3 (notification-service):** Git commit tetiklenince Jira ticket'ı kapatan ve Slack'e bildirim gönderen servis.
5. **Docker Compose:** 3 servisi Docker'da ayağa kaldırmak.
6. **Döküman:** Projenin bilgisayara nasıl kurulacağını anlatan **`installization.pdf`** belgesini hazırlamak.

---

## 🤝 ORTAK YAPILACAKLAR (Projenin Kalbi)

### 1. Dockerizasyon (Zorunlu Kural)
* Her mikroservis için bir `Dockerfile` yazılacak.
* Tüm projenin tek komutla (`docker-compose up -d`) çalışabilmesi için `docker-compose.yml` yönetilecek.

### 2. GitHub Teslimi
* Projenin son hali gerçek GitHub'a yüklenecek.
* Hocanın e-posta adresi (`sinan.keskin@gidatarim.edu.tr`) bu repoya eklenecek.

### 3. Sunum ve Demo (project-presentation.pdf)
Sunum sırasında hocaya sistemin nasıl çalıştığı **canlı olarak** gösterilecek:
1. **Adım:** Beyza, Jira üzerinden "Koddaki hatayı çöz" şeklinde bir ticket açacak.
2. **Adım:** 2. kişi, kodu düzeltip GitHub'a commit atarken mesaja Jira ticket numarasını ekleyecek (Örn: `Fixes JIRA-12`).
3. **Adım:** notification-service devreye girecek - Jira ticket'ı otomatik "Done" olacak ve Slack'e bildirim düşecek.

---

## 📅 Deadlines
| No | Görev | Tarih |
|----|-------|-------|
| 1 | Proje ve grup seçimi | 31.03.2026 |
| 2 | Sınıfta sunum | 02.06.2026 |
| 3 | Dökümanlarla teslim | 14.06.2026 |
