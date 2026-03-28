# 📘 Day 56 – Kubernetes StatefulSets (Hands-on Learning)

## 🔹 Task 1: Understanding the Problem

### Deployment Behavior

* Created a Deployment with 3 replicas (nginx)
* Observed pod names:

  ```
  app-xyz-abc (random)
  ```
* Deleted a pod → new pod created with **different random name**

👉 Works fine for stateless apps (web servers)
❌ Problem for databases → need **stable identity**

---

### 🔁 Deployment vs StatefulSet

| Feature          | Deployment | StatefulSet           |
| ---------------- | ---------- | --------------------- |
| Pod names        | Random     | Stable (web-0, web-1) |
| Startup order    | Parallel   | Ordered               |
| Storage          | Shared     | Per pod PVC           |
| Network identity | Dynamic    | Stable DNS            |

---

### ✅ Verification Answer

**Why random pod names are a problem for databases?**

Because databases require:

* Fixed identity (leader/follower roles)
* Stable connections between nodes
* Predictable hostnames

Random pod names break cluster communication.

---

## 🔹 Task 2: Headless Service

Created a Service with:

```yaml
clusterIP: None
```

👉 This creates a **Headless Service**

### Result:

```bash
kubectl get svc
```

Output:

```
CLUSTER-IP: None
```

---

### ✅ Verification Answer

**What does CLUSTER-IP show?**

👉 `None`

---

## 🔹 Task 3: StatefulSet Creation

* Created StatefulSet with:

  * 3 replicas
  * nginx image
  * volumeClaimTemplates (100Mi)

### Observations:

* Pods created in order:

  ```
  web-0 → web-1 → web-2
  ```

---

### PVCs Created:

```bash
kubectl get pvc
```

```
www-web-0
www-web-1
www-web-2
```

---

### ✅ Verification Answer

* Pod names:

  ```
  web-0, web-1, web-2
  ```
* PVC names:

  ```
  www-web-0, www-web-1, www-web-2
  ```

---

## 🔹 Task 4: Stable Network Identity

Each pod gets DNS:

```
<pod-name>.<service-name>.<namespace>.svc.cluster.local
```

### Example:

```
web-0.nginx.default.svc.cluster.local
```

---

### DNS Testing:

Used BusyBox:

```bash
nslookup web-0.nginx
```

Compared with:

```bash
kubectl get pods -o wide
```

---

### ✅ Verification Answer

👉 Yes — **nslookup IP matches Pod IP**

---

## 🔹 Task 5: Stable Storage

Added data:

```bash
kubectl exec web-0 -- sh -c "echo 'Data from web-0' > /usr/share/nginx/html/index.html"
```

Deleted pod:

```bash
kubectl delete pod web-0
```

👉 Pod recreated automatically

Checked data:

```bash
kubectl exec web-0 -- cat /usr/share/nginx/html/index.html
```

---

### ✅ Verification Answer

👉 Yes — **data remains same after pod recreation**

---

## 🔹 Task 6: Ordered Scaling

### Scale up:

```bash
kubectl scale statefulset web --replicas=5
```

Pods created:

```
web-3 → web-4
```

---

### Scale down:

```bash
kubectl scale statefulset web --replicas=3
```

Pods deleted:

```
web-4 → web-3
```

---

### PVC Check:

```bash
kubectl get pvc
```

👉 All 5 PVCs still exist

---

### ✅ Verification Answer

👉 PVC count after scale-down = **5**

---

## 🔹 Task 7: Cleanup

Deleted:

```bash
kubectl delete statefulset web
kubectl delete svc nginx
```

Checked:

```bash
kubectl get pvc
```

👉 PVCs still exist

---

### Manual cleanup:

```bash
kubectl delete pvc --all
```

---

### ✅ Verification Answer

👉 ❌ PVCs are NOT auto-deleted

---

## 🔹 Key Concepts Learned

* StatefulSets provide:

  * Stable identity
  * Persistent storage
  * Ordered deployment

* Headless Service:

  * Enables per-pod DNS
  * No load balancing

* PVC behavior:

  * One PVC per pod
  * Not deleted automatically

---

## 🎯 Final Takeaways

* Use **Deployment** → Stateless apps (web servers)
* Use **StatefulSet** → Stateful apps (databases)

👉 Real-world examples:

* MySQL cluster
* MongoDB
* Kafka

---

## 🚀 Learning Outcome

Today I learned:

* Difference between Deployment and StatefulSet
* How Kubernetes handles storage and identity
* How to debug real issues (Pending pods, PVC binding)
* How DNS works inside Kubernetes

---
