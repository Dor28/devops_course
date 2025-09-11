#!/bin/bash

echo "🚀 Starting monitoring lab deployment..."

echo "📝 Creating monitoring namespace..."
kubectl apply -f manifests/namespace.yaml

echo "🔍 Deploying Prometheus..."
kubectl apply -f manifests/prometheus-configmap.yaml
kubectl apply -f manifests/prometheus-deployment.yaml

echo "📊 Deploying Grafana..."
kubectl apply -f manifests/grafana-deployment.yaml


echo "⏳ Waiting for pods to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/prometheus -n monitoring
kubectl wait --for=condition=available --timeout=300s deployment/grafana -n monitoring

echo "✅ Monitoring stack deployed successfully!"
echo ""
echo "📡 Access URLs (with minikube):"
echo "Prometheus: http://$(minikube ip):30090"
echo "Grafana: http://$(minikube ip):30030 (admin/admin)"
echo ""
echo "🔍 To check pod status: kubectl get pods -n monitoring"