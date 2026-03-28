# 📘 Day 58 – Metrics Server & Horizontal Pod Autoscaler (HPA)

## 🔹 Overview

Today I implemented **Metrics Server and Horizontal Pod Autoscaler (HPA)** in Kubernetes to enable automatic scaling of applications based on real-time resource usage.

---

## 🔹 What is Metrics Server?

* Metrics Server collects **CPU and Memory usage** from nodes and pods.
* It provides data to Kubernetes APIs.
* HPA depends on this data to make scaling decisions.

👉 Without Metrics Server:

```text
HPA will not work (TARGETS = <unknown>)
```

---

## 🔹 Verifying Metrics

Commands used:

```bash
kubectl top nodes
kubectl top pods -A
```

👉 These show **actual usage**, not configured requests/limits.

---

## 🔹 Deployment Setup

* Created a Deployment using `php-apache` image (CPU intensive)
* Set CPU request:

```yaml
resources:
  requests:
    cpu: 200m
```

👉 This is required for HPA to calculate utilization.

---

## 🔹 What is HPA?

Horizontal Pod Autoscaler automatically:

* Scales **UP** when load increases 📈
* Scales **DOWN** when load decreases 📉

---

## 🔹 HPA Formula

```text
desiredReplicas = ceil(currentReplicas * (currentUsage / targetUsage))
```

---

## 🔹 Imperative HPA

```bash
kubectl autoscale deployment php-apache --cpu=50% --min=1 --max=10
```

👉 Target:

* Maintain CPU at **50% of requested value**

---

## 🔹 Observations

* Initially:

  ```text
  TARGETS = 0% / 50%
  → No scaling
  ```

* After generating load:

  ```text
  CPU increased → Pods scaled automatically
  ```

---

## 🔹 Load Generation

Used BusyBox:

```bash
while true; do wget -q -O- http://php-apache; done
```

---

## 🔹 Declarative HPA (autoscaling/v2)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  minReplicas: 1
  maxReplicas: 10
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 0
    scaleDown:
      stabilizationWindowSeconds: 300
```

---

## 🔹 Behavior Section (Important)

Controls:

* **How fast scaling happens**

| Action     | Behavior            |
| ---------- | ------------------- |
| Scale Up   | Immediate           |
| Scale Down | Delayed (5 minutes) |

👉 Prevents **flapping (frequent scaling up/down)**

---

## 🔹 autoscaling/v1 vs v2

| Feature               | v1 | v2 |
| --------------------- | -- | -- |
| CPU scaling           | ✅  | ✅  |
| Memory/custom metrics | ❌  | ✅  |
| Behavior control      | ❌  | ✅  |

---

## 🔹 Key Learnings

* Metrics Server is required for HPA
* `kubectl top` shows real usage, not limits
* CPU requests are mandatory for autoscaling
* HPA reacts based on load, not instantly
* Scaling must be controlled to maintain stability

---

## 🎯 Final Takeaway

Kubernetes HPA enables systems to automatically adapt to changing traffic, ensuring optimal performance while avoiding over-provisioning.

👉 Autoscaling is about:

* Performance ⚡
* Cost optimization 💰
* System stability 🛡️

---
