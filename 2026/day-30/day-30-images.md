
# Day 30 – Docker Images & Container Lifecycle

## 🎯 Objective

Understand how Docker images and containers work internally, including image layers, lifecycle states, and cleanup operations.

---

# 🐳 Task 1: Docker Images

## 🔹 Pull Images from Docker Hub

```bash
docker pull nginx
docker pull ubuntu
docker pull alpine
```

Downloads images to the local system.

---

## 🔹 List All Images and Sizes

```bash
docker images
```

Example:

| Repository | Tag    | Size   |
| ---------- | ------ | ------ |
| nginx      | latest | ~180MB |
| ubuntu     | latest | ~70MB  |
| alpine     | latest | ~7MB   |

---

## 🔹 Ubuntu vs Alpine (Why is Alpine Smaller?)

**Alpine:**

* Minimal Linux distribution
* Uses musl libc instead of glibc
* Very small footprint
* Designed for containers

**Ubuntu:**

* Full-featured Linux distribution
* Includes more libraries and tools
* Larger base size

👉 Alpine is commonly used in production for lightweight deployments.

---

## 🔹 Inspect an Image

```bash
docker inspect nginx
```

Information visible:

* Image ID
* Creation time
* OS & Architecture
* Environment variables
* Default CMD
* Exposed ports
* Layer details

---

## 🔹 Remove an Image

```bash
docker rmi alpine
```

If image is in use:

```bash
docker rm <container_id>
docker rmi alpine
```

---

# 🧱 Task 2: Image Layers

## 🔹 View Image History

```bash
docker image history nginx
```

Each row represents a layer.

Some layers show sizes (e.g., 45MB).
Some layers show `0B`.

### Why 0B?

`0B` layers are metadata layers such as:

* CMD
* ENV
* EXPOSE
* LABEL

They do not add filesystem changes.

---

## 🔹 What Are Docker Layers?

* Each Dockerfile instruction creates a layer.
* Images are built layer-by-layer.
* Layers are read-only.

**Container = Image layers + Writable layer**

---

## 🔹 Why Docker Uses Layers

* Faster builds using caching
* Shared layers reduce storage
* Faster image pull/push
* Efficient storage management

---

# 🔄 Task 3: Container Lifecycle

## 🔹 Create (Without Starting)

```bash
docker create --name lifecycle-nginx nginx
docker ps -a
```

State: `Created`

---

## 🔹 Start

```bash
docker start lifecycle-nginx
docker ps -a
```

State: `Up`

---

## 🔹 Pause

```bash
docker pause lifecycle-nginx
docker ps
```

State: `Paused`

---

## 🔹 Unpause

```bash
docker unpause lifecycle-nginx
docker ps
```

State: `Up`

---

## 🔹 Stop

```bash
docker stop lifecycle-nginx
docker ps -a
```

State: `Exited`

---

## 🔹 Restart

```bash
docker restart lifecycle-nginx
```

Restart = Stop + Start

---

## 🔹 Kill (Force Stop)

```bash
docker kill lifecycle-nginx
```

Sends `SIGKILL`

---

## 🔹 Remove

```bash
docker rm lifecycle-nginx
```

Container removed.

---

# 🖥 Task 4: Working with Running Containers

## 🔹 Run Nginx in Detached Mode

```bash
docker run -d -p 8080:80 --name mynginx nginx
```

Access in browser:

```
http://localhost:8080
```

---

## 🔹 View Logs

```bash
docker logs mynginx
```

---

## 🔹 Follow Logs (Real-time)

```bash
docker logs -f mynginx
```

---

## 🔹 Exec into Container

```bash
docker exec -it mynginx sh
```

Explore filesystem:

```bash
ls
cd /usr/share/nginx/html
```

---

## 🔹 Run Single Command

```bash
docker exec mynginx ls /
```

---

## 🔹 Inspect Container

```bash
docker inspect mynginx
```

Look for:

* `"IPAddress"`
* `"HostPort"`
* `"Mounts"`

---

# 🧹 Task 5: Cleanup

## 🔹 Stop All Running Containers

```bash
docker stop $(docker ps -q)
```

---

## 🔹 Remove All Stopped Containers

```bash
docker container prune
```

---

## 🔹 Remove Unused Images

```bash
docker image prune -a
```

---

## 🔹 Check Docker Disk Usage

```bash
docker system df
```

Shows:

* Images usage
* Containers usage
* Volumes usage
* Build cache usage

---





