# Docker Implementation - DevOps Kursi O'quv Loyihasi

Ushbu papka DevOps kursi o'quv loyihasining bir qismi bo'lgan FastAPI Hello World ilovasining Docker implementatsiyasini o'z ichiga oladi.

## Umumiy Ma'lumot

Bu papka konteynerlashtirish kontseptsiyalarini va Docker eng yaxshi amaliyotlarini ko'rsatadi, FastAPI ilovamizni portativ va engil konteynerga o'rash orqali.

## Tarkib

- `Dockerfile` - Ko'p bosqichli build bilan konteyner ta'rifi
- `main.py` - FastAPI ilova manba kodi
- `requirements.txt` - Python bog'liqliklari

## Tezkor Boshlash

### Docker image yaratish:
```bash
docker build -t devops-fastapi .
```

### Konteynerni ishga tushirish:
```bash
docker run -d -p 8000:8000 devops-fastapi
```

Ilova quyidagi manzilda mavjud bo'ladi: http://localhost:8000

## Ko'rsatilgan Docker Xususiyatlari

- **Ko'p bosqichli build** - Optimallashtirilgan image hajmi
- **Root bo'lmagan foydalanuvchi** - Xavfsizlik eng yaxshi amaliyotlari
- **Health check** - Konteyner monitoring
- **Samarali keshlash** - To'g'ri qatlam tartibi bilan tezroq buildlar

## O'rganish Maqsadlari

Ushbu Docker implementatsiyasi quyidagilarni o'z ichiga oladi:
- Konteyner asoslari va Dockerfile sintaksisi
- Image optimallash usullari
- Konteynerlashtirish xavfsizlik masalalari
- CI/CD pipeline bilan integratsiya
- Production deployment strategiyalari

## Tegishli Hujjatlar

To'liq loyiha ma'lumotlari uchun [asosiy loyiha README](../README.md) faylini ko'ring.

## Kurs Konteksti

Bu quyidagilarni o'z ichiga olgan keng qamrovli DevOps o'rganish loyihasining bir qismi:
- Git bilan versiya nazorati
- Docker bilan konteynerlashtirish
- CI/CD pipeline implementatsiyasi
- Infrastructure as Code
- Monitoring va logging

---

*DevOps kursi uchun o'quv loyihasi - amaliy konteynerlashtirish ko'nikmalarini namoyish etish*