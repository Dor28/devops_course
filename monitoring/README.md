# Monitoring Lab - Grafana, Prometheus

FastAPI ilovangiz uchun Kubernetes da oddiy monitoring tizimi.

## Tezkor Boshlash

1. **minikube ishga tushirish:**
```bash
minikube start
```

2. **FastAPI ilovasini deploy qilish:**
```bash
kubectl apply -f ../kubernetes/manifests/
```

3. **Monitoring tizimini deploy qilish:**
```bash
cd monitoring
./deploy.sh
```

4. **Xizmatlarga kirish (WSL2/port-forward):**
```bash
./port-forward.sh
```
- Grafana: http://localhost:3000 (admin/admin)
- Prometheus: http://localhost:9090


- **Prometheus**: Ilovangizdan metrikalar yig'ish
- **Grafana**: Dashboard va vizualizatsiya
- **Oddiy metrikalar**: `/metrics` endpoint orqali mavjud

## Dashboard Yaratish

**Qo'lda dashboard yaratish:**
[DASHBOARD_GUIDE.md](./DASHBOARD_GUIDE.md) faylida batafsil qo'llanma


## Muammolarni Hal Qilish

**Agar Prometheus metrikalarni yig'a olmasa:**

1. **FastAPI ilovasini yangi `/metrics` endpoint bilan rebuild qiling:**
```bash
cd ../docker
# Docker Hub ga login qiling
docker login
docker build -t dor28/fastapi-demo:latest .
docker push dor28/fastapi-demo:latest
kubectl rollout restart deployment/fastapi-deployment
```

2. **Docker build muammolari bo'lsa, minikube ichida build qiling:**
```bash
eval $(minikube docker-env)
docker build -t dor28/fastapi-demo:latest .
```

3. **Metrikalar endpoint ni tekshiring:**
```bash
kubectl port-forward svc/fastapi-service 8000:8000 &
curl http://localhost:8000/metrics
```

## Tozalash

```bash
kubectl delete namespace monitoring
```