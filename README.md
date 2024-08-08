# kubernetes-deployment-restarter-api

## Requirements

    Docker
    Python > 3.10
    kubectl

## Local setup

### Create a python virtual environment

```bash
python -m venv venv
activate venv `source venv/bin/activate
pip install -r requirements.txt
```

#### To run locally

```bash
export KUBECONFIG="~/.kube/config"
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

### or open in the browser

```bash
http://localhost:8080/restart-deployment/YourNAMESPACE_NAME/YourDEPLOYMENT_NAME?api_key=YourAPIKEY
```

