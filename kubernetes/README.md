# Kubernetes Lab - FastAPI Application Deployment

Bu modulda Docker modulidagi FastAPI ilovasini Kubernetes clusterga deploy qilamiz. Stateless application va NodePort service ishlatamiz.

## 📚 Lab Modules

Bu Kubernetes lab ikki qismdan iborat:

1. **[Basic Kubernetes](./README.md)** - Asosiy Kubernetes deployment (joriy fayl)
2. **[ArgoCD GitOps](./argocd/README.md)** - GitOps workflow bilan avtomatik deployment

## Zaruriy Talablar

### Software
- **minikube** - Local Kubernetes cluster
- **kubectl** - Kubernetes CLI
- **Docker** - Container runtime

### Installation

#### minikube o'rnatish:
```bash
# Linux uchun
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# macOS uchun
brew install minikube
```

#### kubectl o'rnatish:
```bash
# Linux uchun
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl

# macOS uchun
brew install kubectl
```

## Lab Boshlash

### 1. minikube Clusterini ishga tushirish

```bash
# Cluster ishga tushirish
minikube start --driver=docker

# Cluster holatini tekshirish
kubectl cluster-info
kubectl get nodes
```

### 2. Application deploy qilish

```bash
# Deployment yaratish
kubectl apply -f manifests/deployment.yaml

# Deployment holatini tekshirish
kubectl get deployments
kubectl get pods
kubectl describe deployment fastapi-deployment
```

### 3. Service yaratish (NodePort)

```bash
# Service yaratish
kubectl apply -f manifests/service.yaml

# Service holatini ko'rish
kubectl get services
kubectl describe service fastapi-service
```

### 4. Application ga kirish

#### WSL2/Headless environment uchun:
```bash
# Service URL olish (browser ochmasdan)
minikube service fastapi-service --url

# curl bilan test qilish
SERVICE_URL=$(minikube service fastapi-service --url)
curl $SERVICE_URL/health
curl $SERVICE_URL/api

# WSL2 da muammo: NodePort to'g'ridan-to'g'ri ishlamaydi
# minikube ip
# curl http://192.168.49.2:30080/health  # Bu ishlamaydi WSL2 da

# WSL2 da tunnel ishlatish kerak:
minikube service fastapi-service
# Tunnel ochiladi va localhost port beradi: http://127.0.0.1:40479
# Bu URL ni Windows browserida ochish mumkin
```

#### Desktop environment uchun:
```bash
# Browser da ochish
minikube service fastapi-service
```

## Monitoring va Debug

### Pod holatini tekshirish:
```bash
# Barcha podlarni ko'rish
kubectl get pods -o wide

# Pod loglarini ko'rish
kubectl logs -f deployment/fastapi-deployment

# Pod ichidagi container ma'lumotlari
kubectl describe pod <pod-name>
```

### Service connectivity test:
```bash
# Service endpoints
kubectl get endpoints fastapi-service

# Internal service test
kubectl exec -it <pod-name> -- curl http://fastapi-service:8000/health
```

### Resource utilization:
```bash
# Pod resource usage
kubectl top pods

# Node resource usage
kubectl top nodes
```

## Application Endpoints

Ilovaga minikube IP + NodePort (30080) orqali kirish mumkin:

- **/** - Asosiy sahifa (HTML)
- **/api** - JSON API endpoint
- **/health** - Health check
- **/info** - Application info
- **/docs** - FastAPI documentation

## Scaling va Management

### Horizontal scaling:
```bash
# Replica count o'zgartirish
kubectl scale deployment fastapi-deployment --replicas=5

```

### Rolling update:
```bash
# Image yangilash
kubectl set image deployment/fastapi-deployment fastapi-container=dor28/fastapi-demo:v2.0.0

# Rollout status
kubectl rollout status deployment/fastapi-deployment

# Rollback
kubectl rollout undo deployment/fastapi-deployment
```

## Cleanup

### Resourcelarni o'chirish:
```bash
# Application o'chirish
kubectl delete -f manifests/service.yaml
kubectl delete -f manifests/deployment.yaml

# minikube to'xtatish
minikube stop

# minikube o'chirish
minikube delete
```

## Troubleshooting

### Umumiy xatoliklar:

1. **ImagePullBackOff**
   ```bash
   kubectl describe pod <pod-name>
   # Docker image mavjudligini tekshiring
   ```

2. **CrashLoopBackOff**
   ```bash
   kubectl logs <pod-name>
   # Container loglarini tekshiring
   ```

3. **Service connection issues**
   ```bash
   # Service va endpoints tekshirish
   kubectl get svc,endpoints
   
   # DNS resolution test
   kubectl exec -it <pod-name> -- nslookup fastapi-service
   ```

4. **WSL2 da minikube NodePort muammosi**
   ```bash
   # NodePort (misal: 192.168.49.2:30080) ishlamasa:
   # 1. minikube tunnel ishlatish
   minikube service fastapi-service
   
   # 2. Port forwarding ishlatish
   kubectl port-forward service/fastapi-service 8080:8000
   # Keyin localhost:8080 ga kirish
   
   # 3. Service type LoadBalancer ishlatish (faqat tunnel bilan)
   minikube tunnel
   ```

## Lab Summary

Ushbu labda quyidagilarni o'rgandik:

✅ **Kubernetes Deployment** - Stateless application deploy qilish
✅ **NodePort Service** - External access uchun service yaratish  
✅ **Health Checks** - Liveness va Readiness probes
✅ **Resource Management** - CPU va Memory limits
✅ **Scaling** - Horizontal pod autoscaler
✅ **Monitoring** - Logs va metrics ko'rish

## 🚀 Keyingi Qadam: GitOps

Asosiy Kubernetes kontseptlarni o'rgangandan so'ng, **ArgoCD** bilan zamonaviy GitOps workflow ni o'rganishni tavsiya qilamiz:

👉 **[ArgoCD GitOps Lab](./argocd/README.md)**

GitOps quyidagi imkoniyatlarni beradi:
- 🔄 **Avtomatik deployment** - Git push = avtomatik deploy
- 👁️ **Visual monitoring** - Real-time application holati
- 🛡️ **Configuration drift detection** - Manual o'zgarishlarni aniqlash
- 🎣 **Easy rollback** - Bir click bilan rollback

---
