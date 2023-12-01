Starting a Kubernetes Cluster
=============================

Create namespaces for pods and services


Get the list of namespaces in the cluster
```bash
kubectl ns pods
```
Switch to the namespace
```bash
kubectl config set-context --current --namespace=pods
```
Create a namespace
```bash
kubectl create ns pods
```
Get a namespace
```bash
kubectl get ns pods
```
Delete a namespace
```bash
kubectl delete ns pods
```

A group of nodes forms a cluster. A cluster is managed by a master node. 
The master node is responsible for managing:
- the state of the cluster. 
- scheduling the pods on the nodes. 
- scaling the cluster by adding or removing nodes. 
- upgrading the cluster. 
- managing the networking between the nodes. 
- managing the authentication and authorization of the users. 
- managing the logging and monitoring of the cluster. 
- managing the health of the cluster. 
- managing the storage of the cluster. 
- managing the networking of the cluster. 
- managing the security of the cluster. 

