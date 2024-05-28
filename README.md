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


### Apply manifests

    kubectl apply -f manifests/

## Test

```bash
curl -X 'GET' 'http://localhost:8080/restart-deployment/YourNAMESPACE_NAME/YourDEPLOYMENT_NAME?api_key=YourAPIKEY'
```

### or open in browser

```bash
http://localhost:8080/restart-deployment/YourNAMESPACE_NAME/YourDEPLOYMENT_NAME?api_key=YourAPIKEY
```

