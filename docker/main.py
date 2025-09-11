from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import os
import sys
import time
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Docker Demo API", version="1.0.0")

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')
ACTIVE_REQUESTS = Gauge('http_requests_active', 'Active HTTP requests')

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        ACTIVE_REQUESTS.inc()
        start_time = time.time()
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        REQUEST_DURATION.observe(duration)
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()
        ACTIVE_REQUESTS.dec()
        
        return response

app.add_middleware(MetricsMiddleware)

@app.get("/", response_class=HTMLResponse)
def read_root():
    hostname = os.environ.get("HOSTNAME", "unknown")
    timestamp = datetime.now().isoformat()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI Docker Demo</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }}
            
            .container {{
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
                padding: 40px;
                text-align: center;
                max-width: 600px;
                width: 100%;
                animation: slideUp 0.6s ease-out;
            }}
            
            @keyframes slideUp {{
                from {{
                    opacity: 0;
                    transform: translateY(30px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            .docker-icon {{
                font-size: 4rem;
                margin-bottom: 20px;
                color: #2496ed;
                animation: pulse 2s infinite;
            }}
            
            @keyframes pulse {{
                0%, 100% {{ transform: scale(1); }}
                50% {{ transform: scale(1.05); }}
            }}
            
            h1 {{
                color: #2c3e50;
                font-size: 2.5rem;
                margin-bottom: 10px;
                font-weight: 300;
            }}
            
            .subtitle {{
                color: #7f8c8d;
                font-size: 1.2rem;
                margin-bottom: 30px;
            }}
            
            .status-card {{
                background: linear-gradient(45deg, #27ae60, #2ecc71);
                color: white;
                padding: 20px;
                border-radius: 15px;
                margin: 20px 0;
                box-shadow: 0 10px 20px rgba(46, 204, 113, 0.3);
            }}
            
            .info-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }}
            
            .info-card {{
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                border-left: 4px solid #3498db;
                transition: transform 0.3s ease;
            }}
            
            .info-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            }}
            
            .info-label {{
                font-weight: bold;
                color: #2c3e50;
                font-size: 0.9rem;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-bottom: 5px;
            }}
            
            .info-value {{
                color: #34495e;
                font-family: 'Courier New', monospace;
                font-size: 0.95rem;
                word-break: break-all;
            }}
            
            .endpoints {{
                margin-top: 30px;
                text-align: left;
            }}
            
            .endpoints h3 {{
                color: #2c3e50;
                margin-bottom: 15px;
                text-align: center;
            }}
            
            .endpoint {{
                background: #ecf0f1;
                padding: 12px 15px;
                margin: 8px 0;
                border-radius: 8px;
                border-left: 4px solid #e74c3c;
                font-family: 'Courier New', monospace;
                transition: all 0.3s ease;
            }}
            
            .endpoint:hover {{
                background: #d5dbdb;
                border-left-color: #c0392b;
                transform: translateX(5px);
            }}
            
            .endpoint a {{
                text-decoration: none;
                color: #2c3e50;
            }}
            
            .footer {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #ecf0f1;
                color: #7f8c8d;
                font-size: 0.9rem;
            }}
            
            .badge {{
                display: inline-block;
                background: #e74c3c;
                color: white;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: bold;
                margin: 0 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="docker-icon">🐳</div>
            <h1>FastAPI + Docker</h1>
            <p class="subtitle">Container is running successfully!</p>
            
            <div class="status-card">
                <strong>✅ Status: HEALTHY</strong><br>
                <small>All systems operational</small>
            </div>
            
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-label">Hostname</div>
                    <div class="info-value">{hostname}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Timestamp</div>
                    <div class="info-value">{timestamp}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Environment</div>
                    <div class="info-value">{os.environ.get("ENVIRONMENT", "development")}</div>
                </div>
                <div class="info-card">
                    <div class="info-label">Python Version</div>
                    <div class="info-value">{sys.version.split()[0]}</div>
                </div>
            </div>
            
            <div class="endpoints">
                <h3>🔗 Available Endpoints</h3>
                <div class="endpoint">
                    <a href="/api">GET /api</a> - JSON API endpoint
                </div>
                <div class="endpoint">
                    <a href="/health">GET /health</a> - Health check endpoint
                </div>
                <div class="endpoint">
                    <a href="/info">GET /info</a> - Application information
                </div>
                <div class="endpoint">
                    <a href="/docs">GET /docs</a> - Interactive API documentation
                </div>
            </div>
            
            <div class="footer">
                <span class="badge">FastAPI</span>
                <span class="badge">Docker</span>
                <span class="badge">v1.0.0</span>
                <br><br>
                🚀 Perfect for demonstrating Docker build, run & push commands!
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.get("/api")
def api_root():
    """JSON API endpoint (original functionality)"""
    return {
        "message": "Hello World from Docker!",
        "timestamp": datetime.now().isoformat(),
        "hostname": os.environ.get("HOSTNAME", "unknown")
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "fastapi-demo"
    }

@app.get("/info")
def get_info():
    return {
        "app": "FastAPI Docker Demo",
        "version": "1.0.0",
        "python_version": sys.version,
        "environment": os.environ.get("ENVIRONMENT", "development")
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)