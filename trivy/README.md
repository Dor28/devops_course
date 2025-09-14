# Trivy Container Security Scanning

Docker konteynerlaridagi xavfsizlik zaifliklarini aniqlash va tahlil qilish uchun Trivy dan foydalanish.

## Trivy nima?

Trivy - bu konteyner imagelari, fayl tizimlari va Git repositoriyalarida xavfsizlik zaifliklarini topish uchun ishlatiluvchi oddiy va keng qamrovli skaner.

### Asosiy xususiyatlar:
- **Tezkor**: Bir necha soniyada skanerlash
- **Oddiy**: Bitta buyruq bilan ishga tushadi
- **Bepul**: Open source va tekin
- **Keng qamrov**: OS va dasturiy ta'minot paketlarini skanerlaydi

## CI/CD ga integratsiya

GitHub Actions workflow da Trivy scanning qo'shildi:

```yaml
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'fastapi-demo:latest'
    format: 'table'
```

## Lokal da Trivy dan foydalanish

### 1. Trivy o'rnatish

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```

**macOS:**
```bash
brew install trivy
```

**Docker orqali:**
```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest
```

### 2. Docker image skanerlash

**Asosiy skanerlash:**
```bash
trivy image fastapi-demo:latest
```

**Faqat CRITICAL va HIGH zaifliklarni ko'rsatish:**
```bash
trivy image --severity CRITICAL,HIGH fastapi-demo:latest
```

**JSON formatda natija:**
```bash
trivy image --format json --output result.json fastapi-demo:latest
```

### 3. Amaliy mashg'ulot

**Bizning FastAPI ilovasini skanerlash:**

1. **Docker image yaratish:**
```bash
cd docker
docker build -t fastapi-demo:latest .
```

2. **Trivy bilan skanerlash:**
```bash
trivy image fastapi-demo:latest
```

3. **Natijalarni tahlil qilish:**
- CVE raqamlarini ko'ring
- Severity darajasini tushining (LOW, MEDIUM, HIGH, CRITICAL)
- Fixed version mavjudligini tekshiring

## Natijalarni tushunish

### Zaiflik darajalari:
- **CRITICAL**: Darhol tuzatilishi kerak
- **HIGH**: Muhim, tezda tuzatilishi lozim
- **MEDIUM**: O'rtacha muhimlik
- **LOW**: Past darajadagi xavf

### Misollar:

```
fastapi-demo:latest (debian 11.7)
═══════════════════════════════════════════════

Total: 150 (UNKNOWN: 3, LOW: 100, MEDIUM: 35, HIGH: 10, CRITICAL: 2)

┌─────────────────────────────────┬────────────────┬──────────┬────────────────┬───────────────────┬──────────────────────────────────┐
│            Library              │  Vulnerability │ Severity │ Installed Ver. │  Fixed Version    │             Title                │
├─────────────────────────────────┼────────────────┼──────────┼────────────────┼───────────────────┼──────────────────────────────────┤
│ openssl                         │ CVE-2023-0464  │ HIGH     │ 1.1.1w-0       │ 1.1.1w-1+deb11u1 │ OpenSSL: Denial of service by... │
└─────────────────────────────────┴────────────────┴──────────┴────────────────┴───────────────────┴──────────────────────────────────┘
```

## Best Practices

### 1. CI/CD da ishlatish
- Har bir build da avtomatik skanerlash
- CRITICAL/HIGH zaifliklar uchun build ni to'xtatish
- Natijalarni Security tab ga yuklash

### 2. Base image tanlash
- Minimal base imagelardan foydalaning (`alpine`, `distroless`)
- Eng yangi versiyalarni ishlating
- Multi-stage build qo'llang

### 3. Xavfsizlik monitoringi
- Doimiy skanerlash
- Zaifliklar bazasini yangilab turing
- Security advisory larni kuzatib boring

## Qo'shimcha buyruqlar

**Filesystem skanerlash:**
```bash
trivy fs .
```

**Git repository skanerlash:**
```bash
trivy repo https://github.com/username/repo.git
```

**Config fayllarni tekshirish:**
```bash
trivy config .
```

## Muammolarni hal qilish

**Agar Trivy sekin ishlasa:**
- Cache ni tozalang: `trivy clean --all`
- Internetga ulanishni tekshiring
- Proxy sozlamalarini ko'ring

**Database yangilanmasa:**
- Manual yangilash: `trivy image --download-db-only`
- Firewall sozlamalarini tekshiring

## Keyingi qadamlar

1. **Dockerfile ni optimallashtiring** - kam zaiflikli base imagelarga o'ting
2. **Trivy operator** - Kubernetes da doimiy skanerlash uchun
3. **Policy yarating** - qaysi zaifliklar qabul qilinadigan darajada
4. **Monitoring** - zaifliklar sonini vaqt bo'yicha kuzating

## Foydali havolalar

- [Trivy rasmiy hujjatlari](https://trivy.dev/)
- [GitHub Actions Integration](https://github.com/aquasecurity/trivy-action)
- [CVE ma'lumotlari](https://cve.mitre.org/)
- [NIST zaiflik bazasi](https://nvd.nist.gov/)

---

**Eslatma:** Container security DevOps jarayonining ajralmas qismidir. Har doim eng so'nggi xavfsizlik amaliyotlarini qo'llang! 🔒