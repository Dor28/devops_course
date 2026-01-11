# DevOps Kursi - O'quv Loyihasi

DevOps texnologiyalari va amaliyotlarini o'rganish uchun mo'ljallangan keng qamrovli o'quv kursi.

## Kurs Haqida

Ushbu kurs zamonaviy DevOps amaliyotlarini amaliy mashg'ulotlar orqali o'rgatadi. Kurs davomida talabalar versiya nazorati, konteynerlashtirish, CI/CD pipeline, infrastruktura kodi va monitoring kabi asosiy mavzularni o'rganadilar.

## Kurs Maqsadlari

- DevOps asoslarini tushunish
- Git va versiya nazorati bilan ishlash
- Docker konteynerlarini yaratish va boshqarish
- CI/CD pipeline qurish
- Infrastructure as Code (IaC) tamoyillarini qo'llash
- Monitoring va logging tizimlarini sozlash
- Production muhitida deployment amaliyotlari

## Darsliklar va Amaliy Mashg'ulotlar

### 📁 [Git - Versiya Nazorati](./git/)
- Git asoslari va buyruqlari
- Branch strategiyalari
- Merge va rebase amaliyotlari
- Conflict resolution
- GitHub workflow

### 📁 [Docker - Konteynerlashtirish](./docker/)
- Docker asoslari va kontseptsiyalari
- Dockerfile yaratish
- Multi-stage build
- Container xavfsizlik amaliyotlari
- Docker Compose

### 📁 [Kubernetes - Konteyner Orkestrasiya](./kubernetes/)
- Container orkestrasiya asoslari ✅
- Pod, Service, Deployment ✅
- Horizontal Pod Autoscaler (HPA) ✅
- **[Basic Kubernetes](./kubernetes/README.md)** - Manual deployment ✅
- **[ArgoCD GitOps](./kubernetes/argocd/README.md)** - GitOps workflow ✅

### 📁 CI/CD Pipeline
- GitHub Actions ✅
- Deployment strategiyalari ✅

### 📁 [Terraform - Infrastructure as Code](./terraform/)
- Terraform asoslari va tushunchalar ✅
- AWS/Cloud provider bilan ishlash ✅
- Infrastructure versioning ✅
- State management ✅
- Module yaratish va ishlatish ✅
- Best practices va xavfsizlik ✅

### 📁 [Monitoring va Logging](./monitoring/)
- Prometheus va Grafana ✅
- FastAPI metrics collection ✅
- Dashboard yaratish va sozlash ✅

### 📁 [Trivy - Container Security](./trivy/)
- Container vulnerability scanning ✅
- CI/CD integration ✅
- Security best practices ✅
- Local scanning va analiz ✅

## Texnik Talablar

- **Operating System**: Linux/macOS/Windows
- **Tools**: Git, Docker, Python 3.7+
- **Cloud Account**: AWS/GCP/Azure (ixtiyoriy)
- **IDE**: VS Code (tavsiya etiladi)

## CI/CD Pipeline

Ushbu loyiha GitHub Actions orqali avtomatik CI/CD pipeline bilan jihozlangan:

### Pipeline Xususiyatlari
- **Docker Build**: Har bir commit da avtomatik Docker image yaratish
- **Docker Hub Push**: Main branchga push qilinganda avtomatik deployment

### Pipeline Ishlash Tartibi
1. Code checkout
2. Docker image build
3. Docker Hub ga push (faqat main branch)

### Docker Hub Repository
- **Image**: [dor28/fastapi-demo](https://hub.docker.com/repository/docker/dor28/fastapi-demo/general)
- **Tags**: `latest`, commit SHA

### Lokal Test Qilish
```bash
cd docker
docker build -t fastapi-demo .
docker run -p 8000:8000 fastapi-demo
curl http://localhost:8000/health
```

## Qanday Boshlash

1. **Repository klonlash:**
```bash
git clone <repository-url>
cd devops_course
```

2. **Docker o'rnatish:** [Docker rasmiy sayti](https://docs.docker.com/get-docker/)

3. **Birinchi darsni boshlash:** `git` papkasiga o'ting

## Loyiha Tuzilishi

```
devops_course/
├── README.md              # Asosiy kurs hujjatlari
├── .github/workflows/     # GitHub Actions CI/CD pipeline
│   └── ci.yml            # Avtomatik build, test va deploy
├── git/                  # Git va versiya nazorati darsliklari
├── docker/               # Docker konteynerlashtirish darsliklari
│   ├── Dockerfile        # FastAPI ilovasi uchun
│   ├── main.py          # Demo FastAPI ilovasi
│   └── requirements.txt  # Python dependencies
├── kubernetes/           # Kubernetes orkestrasiya darsliklari ✅
│   ├── README.md         # Basic Kubernetes deployment
│   ├── manifests/        # K8s manifests (deployment, service)
│   └── argocd/          # GitOps bilan avtomatik deployment
│       ├── README.md     # ArgoCD setup va demo
│       ├── manifests/    # ArgoCD installation files
│       ├── applications/ # ArgoCD application configs
│       └── scripts/      # Setup automation scripts
├── terraform/            # Infrastructure as Code (Terraform) ✅
│   ├── README.md         # Terraform asoslari va amaliyot
│   ├── aws-resources/    # AWS infrastructure examples
│   └── modules/         # Reusable terraform modules
├── cicd/                # CI/CD pipeline darsliklari (kelgusida)
├── monitoring/          # Monitoring va logging ✅
│   ├── README.md         # Prometheus va Grafana setup
│   ├── DASHBOARD_GUIDE.md # Dashboard yaratish qo'llanmasi
│   ├── manifests/        # Kubernetes manifests for monitoring
│   ├── deploy.sh         # Avtomatik deployment script
│   └── port-forward.sh   # Port forwarding uchun script
└── trivy/               # Container Security Scanning ✅
    └── README.md         # Trivy vulnerability scanning guide
```

## Qo'llab-quvvatlash

Savollar yoki yordam kerak bo'lsa:
- Issue yarating repository da
- Telegram guruhiga yozing
- Email: psanti99.sp@gmail.com

## Litsenziya

Ushbu o'quv materiallari Mohirdev course talabalari  uchun  taqdim etilgan. Copy qilish faqat Mohirdev course talabalari uchun. 

---

*DevOps Engineer bo'lish sari birinchi qadam!* 🚀
