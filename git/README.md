# Git - Versiya Nazorati Darsliklari

Git versiya nazorati tizimi bilan ishlashning asosiy buyruqlari va amaliy misollar.

## Git Nima?

Git - bu kodni versiyalash va o'zgarishlarni kuzatish uchun taqsimlangan versiya nazorati tizimi. U bir nechta dasturchilar birgalikda ishlashi va kod tarixini saqlashi imkonini beradi.

## Asosiy Tushunchalar

- **Repository (Repo)** - Loyihaning barcha fayllari va ularning tarixi
- **Commit** - Kod o'zgarishlarining saqlanishi
- **Branch** - Kodni parallel rivojlantirish uchun alohida yo'l
- **Merge** - Branchlarni birlashtirish
- **Clone** - Repositoriyani nusxalash

## Asosiy Git Buyruqlari

### 1. Repository Yaratish va Sozlash

```bash
# Yangi repository yaratish
git init

# Mavjud repositoriyani klonlash
git clone https://github.com/username/repository.git

# Git foydalanuvchi ma'lumotlarini sozlash
git config --global user.name "Ismingiz"
git config --global user.email "email@example.com"

# Sozlamalarni ko'rish
git config --list
```

### 2. Fayllar bilan Ishlash

```bash
# Barcha o'zgarishlarni ko'rish
git status

# Fayl qo'shish (staging area ga)
git add hello.py
git add requirements.txt

# Barcha fayllarni qo'shish
git add .

# O'zgarishlarni commit qilish
git commit -m "FastAPI hello world ilovasi qo'shildi"

# Qisqa yo'l: add va commit birga
git commit -am "requirements.txt yangilandi"
```

### 3. Tarix va Log

```bash
# Commit tarixini ko'rish
git log

# Qisqa formatda ko'rish
git log --oneline

# Oxirgi 5 ta commitni ko'rish
git log -5

# Muayyan faylning tarixini ko'rish
git log hello.py

# O'zgarishlar bilan birga ko'rish
git log -p
```

### 4. O'zgarishlarni Ko'rish

```bash
# Hozirgi o'zgarishlarni ko'rish
git diff

# Staging area dagi o'zgarishlarni ko'rish
git diff --staged

# Muayyan faylning o'zgarishini ko'rish
git diff hello.py

# Ikki commit orasidagi farqni ko'rish
git diff HEAD~1 HEAD
```

### 5. Branch bilan Ishlash

```bash
# Branchlarni ko'rish
git branch

# Yangi branch yaratish
git branch feature-api

# Branchni o'zgartirish
git checkout feature-api

# Yangi branch yaratib, o'tish
git checkout -b bugfix-health-endpoint

# Branchni o'chirish
git branch -d feature-api

# Remote branchlarni ko'rish
git branch -r
```

### 6. Merge va Rebase

```bash
# main branchga o'tish
git checkout main

# feature branchni merge qilish
git merge feature-api

# Rebase qilish
git rebase main

# Merge conflict hal qilish
# 1. Conflictli fayllarni tahrirlash
# 2. Hal qilingan fayllarni add qilish
git add hello.py
# 3. Merge ni yakunlash
git commit
```

### 7. Remote Repository bilan Ishlash

```bash
# Remote repositoriyalarni ko'rish
git remote -v

# Remote qo'shish
git remote add origin https://github.com/username/devops_course.git

# O'zgarishlarni yuborish
git push origin main

# O'zgarishlarni olish
git pull origin main

# Faqat fetch qilish (merge qilmasdan)
git fetch origin
```

### 8. Undo va Reset

```bash
# Oxirgi commitni bekor qilish (fayllar saqlanadi)
git reset --soft HEAD~1

# Staging area ni tozalash
git reset HEAD hello.py

# Faylni oldingi holatiga qaytarish
git checkout -- hello.py

# Commitni to'liq bekor qilish (XAVFLI!)
git reset --hard HEAD~1

# Muayyan commitga qaytish
git revert <commit-hash>
```

## Amaliy Misollar - Git Papkasi Fayllari bilan

### Misol 1: FastAPI Ilovasini Qo'shish

```bash
# Yangi fayllarni qo'shish
git add hello.py requirements.txt

# Commit yaratish
git commit -m "FastAPI hello world ilovasi va dependencies qo'shildi

- hello.py: Asosiy FastAPI ilova fayli
- requirements.txt: Python bog'liqliklari (fastapi, uvicorn)"

# Tarixni ko'rish
git log --oneline
```

### Misol 2: Feature Branch Yaratish

```bash
# Yangi endpoint uchun branch yaratish
git checkout -b feature-user-endpoint

# hello.py ga yangi endpoint qo'shish (tahrirlash kerak)
# Keyin:
git add hello.py
git commit -m "Foydalanuvchi ma'lumotlari uchun yangi endpoint qo'shildi"

# Main branchga qaytish va merge qilish
git checkout main
git merge feature-user-endpoint
```

### Misol 3: Dependencies Yangilash

```bash
# requirements.txt ni yangilash
git add requirements.txt
git commit -m "FastAPI versiyasi 0.104.1 ga yangilandi

- Xavfsizlik yamoqlari
- Performance yaxshilanishlari"

# O'zgarishlarni remote ga yuborish
git push origin main
```

### Misol 4: Bug Fix

```bash
# Bug fix uchun branch
git checkout -b bugfix-health-response

# hello.py dagi health endpoint ni tuzatish
git add hello.py
git commit -m "Health endpoint javobini standartlashtirish

- status 'healthy' o'rniga 'ok' qaytaradi
- timestamp qo'shildi"

# Main branchga merge
git checkout main
git merge bugfix-health-response
git branch -d bugfix-health-response
```

## Git Best Practices

### Commit Messages

**Yaxshi commit messages:**
```bash
git commit -m "FastAPI logging qo'shildi"
git commit -m "Foydalanuvchi autentifikatsiya moduli yaratildi"
git commit -m "Docker konfiguratsiyasi optimallashtirildi"
```

**Yomon commit messages:**
```bash
git commit -m "fix"
git commit -m "changes"
git commit -m "updated file"
```

### Branch Naming

```bash
# Feature branchlari
feature/user-authentication
feature/api-documentation

# Bug fix branchlari
bugfix/login-error
hotfix/security-patch

# Release branchlari
release/v1.0.0
```

### .gitignore Fayli

```bash
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
venv/
.env

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

## Foydali Git Aliaslar

```bash
# Qisqa aliaslar sozlash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# Ishlatish
git st    # git status o'rniga
git co main  # git checkout main o'rniga
```

## Keyingi Qadamlar

1. **GitHub/GitLab bilan ishlash** - Remote repositoriyalar
2. **Pull Requests** - Kod review jarayoni
3. **Git Flow** - Branch strategiyalari
4. **Git Hooks** - Avtomatik tekshiruvlar
5. **Git Advanced** - Cherry-pick, bisect, submodules

---

*Git - zamonaviy dasturlashning asosi!* 🔧