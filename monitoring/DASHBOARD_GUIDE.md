# Oddiy Grafana Dashboard Yaratish

## 1-qadam: Grafana ga kirish
1. `./port-forward.sh` ni ishga tushiring
2. http://localhost:3000 ni oching
3. Login: `admin` / `admin`

## 2-qadam: Ma'lumot Manbalarini Qo'shish

### Prometheus Ma'lumot Manbasini Qo'shish
1. **Configuration** (⚙️) → **Data Sources** ga bosing
2. **Add data source** ga bosing
3. **Prometheus** ni tanlang
4. URL ni o'rnating: `http://prometheus-service.monitoring.svc.cluster.local:9090`
5. **Save & Test** ga bosing


## 3-qadam: Dashboard Yaratish

### Yangi Dashboard Yaratish
1. **+** → **Dashboard** ga bosing
2. **Add new panel** ga bosing

### Panel 1: Jami HTTP So'rovlar
1. **Query**: `http_requests_total`
2. **Visualization**: Stat
3. **Panel title**: "Jami HTTP So'rovlar"
4. **Apply** ga bosing

### Panel 2: So'rov Tezligi
1. **Add panel** ga bosing
2. **Query**: `rate(http_requests_total[5m])`
3. **Visualization**: Graph
4. **Panel title**: "So'rov Tezligi (so'rov/soniya)"
5. **Apply** ga bosing

### Panel 3: Javob Vaqti
1. **Add panel** ga bosing
2. **Query**: `histogram_quantile(0.95, http_request_duration_seconds_bucket)`
3. **Visualization**: Stat
4. **Panel title**: "95% Javob Vaqti"
5. **Unit**: seconds (s)
6. **Apply** ga bosing

### Panel 4: Faol So'rovlar
1. **Add panel** ga bosing
2. **Query**: `http_requests_active`
3. **Visualization**: Gauge
4. **Panel title**: "Faol So'rovlar"
5. **Apply** ga bosing


## 4-qadam: Dashboard ni Saqlash
1. **💾 Save** ga bosing (yuqori o'ng burchakda)
2. **Name**: "FastAPI Monitoring"
3. **Save** ga bosing

## 5-qadam: Traffic Yaratish
Metrikalarni ko'rish uchun traffic yarating:
```bash
# Ilovangizga port forward qiling
kubectl port-forward svc/fastapi-service 8000:8000

# So'rovlar yarating
for i in {1..100}; do curl http://localhost:8000/health; done
```

Endi Grafana dashboardingizni yangilang va metrikalarni ko'ring!

## Sinov Uchun Tezkor So'rovlar

Grafana ning Explore bo'limida sinab ko'ring:

**Prometheus so'rovlar:**
- `http_requests_total` - Jami so'rovlar
- `rate(http_requests_total[5m])` - So'rov tezligi
- `http_requests_active` - Faol so'rovlar
- `up` - Xizmat ishlayapti

**Loglarni ko'rish uchun:**
```bash
kubectl logs -f -l app=fastapi-demo
```