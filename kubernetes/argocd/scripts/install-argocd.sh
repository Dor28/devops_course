#!/bin/bash

echo "🚀 ArgoCD o'rnatilmoqda..."

# Namespace yaratish
kubectl apply -f manifests/namespace.yaml

# ArgoCD o'rnatish
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

echo "⏳ ArgoCD podlar tayyor bo'lishini kutmoqda..."
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=argocd-server -n argocd --timeout=300s

echo "✅ ArgoCD muvaffaqiyatli o'rnatildi!"

# Admin parol olish
echo "🔑 Admin parol:"
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
echo ""
echo ""

echo "📋 ArgoCD ga kirish:"
echo "1. Port forwarding ishga tushirish:"
echo "   kubectl port-forward svc/argocd-server -n argocd 8080:443"
echo ""
echo "2. Browser da ochish: https://localhost:8080"
echo "   Username: admin"
echo "   Password: yuqoridagi parol"
echo ""
echo "3. FastAPI ilovasini deploy qilish:"
echo "   kubectl apply -f applications/fastapi-app.yaml"