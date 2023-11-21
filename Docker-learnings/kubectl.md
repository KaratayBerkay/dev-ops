
> Create a nginx deployment 
```bash
kubectl create deployment nginx --image=nginx-webserver
```

> list the pod 
```bash
kubectl get pods
```

> list the deployment 
```bash
kubectl get all
```

> delete the deployment 
```bash
kubectl delete deployment nginx
```

> upgrade spesific deployments name
```bash
kubectl set image deployment/nginx nginx=nginx:1.9.1
```

> describe the deployment 
```bash
kubectl describe deployment nginx  # kubectl describe <object type> <object name>
```

> get ip address of minikube
```bash
minikube ip  # this ip address will be used instead of localhost to reach any of the pods
```

> apply changes to the deployment
```bash
kubectl apply -f client-deployment.yaml
```

> Imperative commands to update the image
```bash
kubectl set image deployment/client-deployment client=stephengrider/multi-client:v5
# kubectl set image <object type>/<object name> <container name>=<new image to use>
```


client-node-port.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  ports:
    - port: 3050  # the port another container will use to access the service
      targetPort: 3000  # the port that is the targeted by the service
      nodePort: 31515  # the port on which user will access the service from browser
  selector:
    tier: frontend
```

client-pod.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: client-pod  # this name is used by the service to find the pod
  labels:
    tier: frontend  # this label is used by the service to find the pod
spec:
  containers:
    - name: client
      image: nginx
      ports:
        - containerPort: 3000
```
client-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: client-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: client
          image: nginx
          ports:
            - containerPort: 3000
```

client-cluster-ip-service.yaml
```yaml
apiVersion: v1
kind: Deployment
metadata:
  name: server-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      component: server
    template:
        metadata:
            labels:
            component: server
        spec:
          containers:
            - name: server
              image: multi-server
              ports:
                - containerPort: 5000
```

client-cluster-ip-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: server-cluster-ip-service
spec:
  type: ClusterIP
  selector:
    component: server
  ports:
    - port: 5000
      targetPort: 5000

```