### 1. Authenticate with GCP
```bash
# Login to GCP
gcloud auth login

# Set application default credentials
gcloud auth application-default login

# Get your project ID
gcloud projects list
```

### 2. Enable Required APIs
```bash
# Replace YOUR_PROJECT_ID with your actual project ID
gcloud config set project YOUR_PROJECT_ID

# Enable Compute Engine and Storage APIs
gcloud services enable compute.googleapis.com
gcloud services enable storage.googleapis.com
```
