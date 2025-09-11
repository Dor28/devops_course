#!/bin/bash

echo "🚀 Starting port forwarding for monitoring services..."

echo "📊 Grafana will be available at: http://localhost:3000"
kubectl port-forward -n monitoring svc/grafana-service 3000:3000 &

echo "🔍 Prometheus will be available at: http://localhost:9090" 
kubectl port-forward -n monitoring svc/prometheus-service 9090:9090 &


echo ""
echo "✅ Port forwarding started!"
echo "Access your services at:"
echo "  - Grafana: http://localhost:3000 (admin/admin)"
echo "  - Prometheus: http://localhost:9090"  
echo ""
echo "Press Ctrl+C to stop all port forwards"
wait