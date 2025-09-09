#!/bin/bash

echo "🌐 ArgoCD UI ga kirish uchun port forwarding ishga tushirilmoqda..."
echo "Browser da ochish: https://localhost:8080"
echo "Username: admin"
echo ""
echo "🔑 Parolni olish uchun:"
echo "kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d"
echo ""
echo "To'xtatish uchun Ctrl+C bosing"
echo ""

kubectl port-forward svc/argocd-server -n argocd 8080:443