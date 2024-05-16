import datetime
import os

from fastapi import FastAPI, HTTPException, Depends
from kubernetes import client, config

# Load Kubernetes config based on environment
config.load_kube_config(context="do-nyc3-hassnat-k8s") if os.getenv('KUBECONFIG') else config.load_incluster_config()

app = FastAPI()


def get_api_key(api_key: str):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=403, detail="Unauthorized. Please provide correct api_key")
    return api_key


@app.get("/restart-deployment/{namespace_name}/{deployment_name}")
async def restart_deployment(namespace_name: str, deployment_name: str, api_key: str = Depends(get_api_key)):
    apps_v1 = client.AppsV1Api()
    try:
        deployment = apps_v1.read_namespaced_deployment(
            name=deployment_name, namespace=namespace_name)
        if deployment:
            # Restart deployment
            deployment.spec.template.metadata.annotations = {
                "kubectl.kubernetes.io/restartedAt": datetime.datetime.now(datetime.UTC).isoformat()}
            res = apps_v1.patch_namespaced_deployment(
                name=deployment_name, namespace=namespace_name, body=deployment)
            return {"status": "success", "message": "Deployment restarted successfully"}
    except client.exceptions.ApiException as e:
        if e.status == 404:
            return {"status": "failure", "message": "Deployment not found"}
        else:
            raise HTTPException(status_code=e.status, detail=str(e))

    return {"status": "failure", "message": "Failed to restart deployment"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8081)
