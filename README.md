# k8s-deployment-restarter

## Requirements
    docker
    python > 3.10
    kubectl

## Local setup

### create a python virtual environement 
```bash
python -m venv venv
activate ven `source venv/bin/activate
pip install -r requirements.txt
```
#### To run locally
```bash
export KUBECONFIG="/Users/hassnat/.kube/config"
export API_KEY="secret"
python main.py
```
## Run in Kubernetes

**make sure you have built and pushed docker image to docker registery to build**
```bash
docker buildx build --platform linux/amd64 -t k8s-deployment-restarter:latest .
```

#### push image to docker registry e.g hassnat/k8s-deployment-restarter:latest

#### add image and tag to manifests/app.yaml

### Apply manifests
    kubectl apply -f manifests/


## Test
```bash
curl -X 'POST' \
  'http://0.0.0.0:8080/restart-deployment/?api_key_header=secret' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "namespace": "edyou-dev-apps",
  "deployment": "notification-worker-deployment"
}'
```

