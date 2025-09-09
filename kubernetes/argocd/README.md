# ArgoCD Lab - GitOps bilan Kubernetes Application Deploy

Bu modulda ArgoCD yordamida GitOps workflow ni o'rganamiz. FastAPI ilovasini ArgoCD orqali avtomatik deploy qilamiz.

## GitOps nima?

**GitOps** - bu Git repository ni "source of truth" sifatida ishlatib, Kubernetes cluster holatini boshqarish metodologiyasi.

### GitOps Printsiplari:
- 📝 **Declarative** - Barcha konfiguratsiya Git da saqlanadi
- 🔄 **Versioned** - Git versioning orqali o'zgarishlarni kuzatish
- 🚀 **Automated** - Avtomatik sync va deploy
- 🛡️ **Auditable** - Barcha o'zgarishlar audit qilinadi

## ArgoCD nima?

**ArgoCD** - Kubernetes uchun declarative, GitOps continuous delivery tool.

### ArgoCD Faydalar:
- 🎯 **Application Management** - Kubernetes applarni markazlashgan boshqarish
- 👁️ **Visual UI** - Real-time holatni ko'rish
- 🔄 **Auto Sync** - Git dan avtomatik yangilanish
- 📊 **Health Monitoring** - Application health monitoring
- 🎣 **Easy Rollback** - Tez va oson rollback

## Zaruriy Talablar

### Software
- **minikube** - Local Kubernetes cluster
- **kubectl** - Kubernetes CLI
- **Git** - Source code management

## ArgoCD O'rnatish

### 1. Minikube ishga tushirish
```bash
minikube start --driver=docker
```

### 2. ArgoCD o'rnatish (Script yordamida)
```bash
# ArgoCD o'rnatish
cd argocd
./scripts/install-argocd.sh
```

Yoki qo'lda o'rnatish:
```bash
# Namespace yaratish
kubectl apply -f manifests/namespace.yaml

# ArgoCD o'rnatish
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# ArgoCD server tayyor bo'lishini kutish
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=argocd-server -n argocd --timeout=300s
```

### 3. ArgoCD UI ga kirish

#### Port forwarding ishga tushirish:
```bash
# Script yordamida
./scripts/port-forward.sh

# Yoki qo'lda
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

#### Admin parolni olish:
```bash
# Script yordamida
./scripts/get-password.sh

# Yoki qo'lda
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

#### Browser da ochish:
- URL: **https://localhost:8080**
- Username: **admin**
- Password: yuqoridagi scriptdan olingan parol

## FastAPI Application Deploy

### 1. ArgoCD Application yaratish
```bash
# Git repository URL ni tekshiring (applications/fastapi-app.yaml da)
# Agar sizning repo URL boshqa bo'lsa, fayl ni tahrirlang

kubectl apply -f applications/fastapi-app.yaml
```

### 2. Application holatini tekshirish

#### CLI orqali:
```bash
# ArgoCD CLI o'rnatish (ixtiyoriy)
curl -sSL -o /tmp/argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 /tmp/argocd-linux-amd64 /usr/local/bin/argocd

# ArgoCD ga login
argocd login localhost:8080

# Application list
argocd app list

# Application details
argocd app get fastapi-app
```

#### UI orqali:
1. https://localhost:8080 ga kiring
2. "Applications" bo'limida **fastapi-app** ni ko'ring
3. Application card ni bosib details page ga kiring

## GitOps Workflow Demo

### 1. O'zgarish kiritish (Git da)

**Scenario 1: Replica count o'zgartirish**
```bash
# manifests/deployment.yaml da replicas: 3 dan 5 ga o'zgartiring
git add manifests/deployment.yaml
git commit -m "Scale replicas from 3 to 5"
git push origin main
```

ArgoCD 3 daqiqada avtomatik sync qiladi (yoki manual sync qilishingiz mumkin).

**Scenario 2: Image version yangilash**
```bash
# manifests/deployment.yaml da image: dor28/fastapi-demo:latest dan v2.0.0 ga o'zgartiring
git add manifests/deployment.yaml
git commit -m "Update image to v2.0.0"
git push origin main
```

### 2. Manual Sync

UI da:
1. Application page ga kiring
2. **"SYNC"** tugmasini bosing
3. **"SYNCHRONIZE"** ni tasdiqlang

CLI da:
```bash
argocd app sync fastapi-app
```

### 3. Configuration Drift Detection

**Test:** Kubernetes da manual o'zgarish
```bash
# Manual ravishda replica count ni o'zgartirish
kubectl scale deployment fastapi-deployment --replicas=10
```

ArgoCD bu o'zgarishni "OutOfSync" sifatida aniqlaydi va UI da ko'rsatadi.

**Self-heal:** ArgoCD avtomatik ravishda Git holatiga qaytaradi (selfHeal: true).

### 4. Rollback

**UI orqali:**
1. Application History ni ko'ring
2. Oldingi version ni tanlang
3. **"ROLLBACK"** tugmasini bosing

**CLI orqali:**
```bash
# History ko'rish
argocd app history fastapi-app

# Rollback
argocd app rollback fastapi-app
```

## ArgoCD Configuration Tushunish

### Application Manifest (applications/fastapi-app.yaml)
```yaml
spec:
  source:
    repoURL: https://github.com/Dor28/devops_course.git  # Git repo
    targetRevision: main                                   # Branch
    path: kubernetes/manifests                             # Manifest path
  destination:
    server: https://kubernetes.default.svc               # Target cluster
    namespace: default                                    # Target namespace
  syncPolicy:
    automated:
      prune: true      # O'chirilgan resourcelarni avtomatik o'chirish
      selfHeal: true   # Manual o'zgarishlardan avtomatik qaytarish
```

### Sync Policy Options:
- **manual:** Faqat qo'lda sync
- **automated:** Avtomatik sync (har 3 daqiqada)
- **prune:** Git dan o'chirilgan resourcelarni cluster dan ham o'chirish
- **selfHeal:** Manual o'zgarishlarni avtomatik tuzatish

## Monitoring va Troubleshooting

### ArgoCD Logs
```bash
# ArgoCD server logs
kubectl logs -n argocd -l app.kubernetes.io/name=argocd-server

# ArgoCD application controller logs  
kubectl logs -n argocd -l app.kubernetes.io/name=argocd-application-controller
```

### Application Status
```bash
# CLI orqali
argocd app get fastapi-app

# kubectl orqali
kubectl get applications -n argocd
kubectl describe application fastapi-app -n argocd
```

### Common Issues:

#### 1. **Repository access error**
```bash
# SSH key yoki token kerak bo'lishi mumkin
# Public repo uchun HTTPS ishlatish yaxshiroq
```

#### 2. **OutOfSync status**
```bash
# Manual sync
argocd app sync fastapi-app

# Yoki UI da SYNC tugmasini bosing
```

#### 3. **Application health degraded**
```bash
# Pod statuslarini tekshirish
kubectl get pods
kubectl logs -f deployment/fastapi-deployment
```

## Demo Script

### Complete Demo Flow:
1. **ArgoCD o'rnatish** - `./scripts/install-argocd.sh`
2. **UI ochish** - `./scripts/port-forward.sh` 
3. **Application deploy** - `kubectl apply -f applications/fastapi-app.yaml`
4. **Git o'zgarish** - replica count o'zgartirish
5. **Sync kuzatish** - UI da real-time sync
6. **Manual drift** - `kubectl scale` bilan test
7. **Self-heal** - avtomatik tuzatilishini ko'rish
8. **Rollback** - oldingi versiyaga qaytish

## Cleanup

### ArgoCD Application o'chirish:
```bash
kubectl delete -f applications/fastapi-app.yaml
```

### ArgoCD o'chirish:
```bash
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl delete -f manifests/namespace.yaml
```

### FastAPI application o'chirish:
```bash
kubectl delete -f ../manifests/
```

## GitOps Best Practices

### 1. **Repository Structure**
```
├── applications/          # ArgoCD app definitions
├── manifests/            # Kubernetes manifests
└── argocd/              # ArgoCD configurations
```

### 2. **Branch Strategy**
- **main** - Production (yagona branch)

### 3. **Security**
- Private repositories ishlatish
- RBAC konfiguratsiya qilish
- Image signing va verification

## Lab Summary

Ushbu labda quyidagilarni o'rgandik:

✅ **GitOps Workflow** - Git orqali infrastructure boshqarish  
✅ **ArgoCD Installation** - Kubernetes clusterda ArgoCD o'rnatish  
✅ **Application Management** - GitOps orqali application deploy  
✅ **Auto Sync** - Git o'zgarishlarni avtomatik sync qilish  
✅ **Configuration Drift** - Manual o'zgarishlarni aniqlash  
✅ **Self-Healing** - Avtomatik tuzatish mexanizmi  
✅ **Rollback** - Oldingi versiyaga tez qaytish  
✅ **Monitoring** - Real-time application monitoring  

**GitOps** - bu zamonaviy DevOps workflow bo'lib, infrastructure va applicationlarni Git orqali boshqarish imkonini beradi. ArgoCD esa bu workflow ni Kubernetes da amalga oshirish uchun eng yaxshi tool hisoblanadi.

---

## Qo'shimcha Resurslar

- [ArgoCD Official Docs](https://argo-cd.readthedocs.io/)
- [GitOps Principles](https://www.gitops.tech/)
- [ArgoCD Best Practices](https://argoproj.github.io/argo-cd/operator-manual/)