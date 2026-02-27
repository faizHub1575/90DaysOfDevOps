
Today’s goal was to solve two real-world problems:

1. **Data Persistence** – Containers lose data when removed.
2. **Container Communication** – Containers cannot communicate properly by default.

---

# 🧪 Task 1: The Problem – Ephemeral Containers

## Step 1: Run MySQL Container

```bash
docker run -d --name mysql-test \
-e MYSQL_ROOT_PASSWORD=root \
mysql
```

## Step 2: Create Data

Entered container and created:

* Database
* Table
* Inserted sample rows

## Step 3: Stop and Remove Container

```bash
docker stop mysql-test
docker rm mysql-test
```

## Step 4: Run New Container (Without Volume)

```bash
docker run -d --name mysql-test \
-e MYSQL_ROOT_PASSWORD=root \
mysql
```

## 🔍 Observation

❌ The data was **gone**.

## 💡 Why?

Containers are **ephemeral**.
When removed, the writable layer is deleted.

Docker stores container data inside the container filesystem, which is destroyed when the container is removed.

---

# 🧪 Task 2: Named Volumes

## Step 1: Create Volume

```bash
docker volume create mysql-data
```

Verify:

```bash
docker volume ls
```

## Step 2: Run MySQL with Volume

```bash
docker run -d --name mysql-vol \
-e MYSQL_ROOT_PASSWORD=root \
-v mysql-data:/var/lib/mysql \
mysql
```

## Step 3: Add Data

Created database and inserted rows.

## Step 4: Remove Container

```bash
docker stop mysql-vol
docker rm mysql-vol
```

## Step 5: Run New Container with SAME Volume

```bash
docker run -d --name mysql-new \
-e MYSQL_ROOT_PASSWORD=root \
-v mysql-data:/var/lib/mysql \
mysql
```

## 🔍 Observation

✅ The data was still there.

## Verify Volume

```bash
docker volume ls
docker volume inspect mysql-data
```

## 💡 Learning

Named volumes are stored outside container lifecycle.
Even if the container is deleted, volume data remains.

---

# 🧪 Task 3: Bind Mounts

## Step 1: Create Folder on Host

```bash
mkdir mysite
cd mysite
```

Create `index.html`:

```html
<h1>Hello from Faiz DevOps Lab 🚀</h1>
```

## Step 2: Run Nginx with Bind Mount

```bash
docker run -d --name web \
-p 8080:80 \
-v $(pwd):/usr/share/nginx/html \
nginx
```

Access:

```
http://localhost:8080
```

## Step 3: Edit index.html on Host

Changed content and refreshed browser.

## 🔍 Observation

✅ Changes reflected instantly.

---

## 📌 Difference Between Named Volume and Bind Mount

| Named Volume                        | Bind Mount                  |
| ----------------------------------- | --------------------------- |
| Managed by Docker                   | Managed by Host             |
| Stored in `/var/lib/docker/volumes` | Stored anywhere on host     |
| Better for production               | Better for development      |
| Less risk of permission issues      | May cause permission issues |
| Portable                            | Depends on host path        |

---

# 🌐 Task 4: Docker Networking Basics

## List Networks

```bash
docker network ls
```

Default networks:

* bridge
* host
* none

---

## Inspect Default Bridge

```bash
docker network inspect bridge
```

Observed:

* Subnet (172.17.0.0/16)
* Gateway
* Connected containers

---

## Run Two Containers on Default Bridge

```bash
docker run -dit --name c1 ubuntu
docker run -dit --name c2 ubuntu
```

Inside c1:

```bash
ping c2
```

❌ Failed (Name resolution does not work)

Ping by IP:

```bash
ping 172.x.x.x
```

✅ Worked

---

# 🧠 Why?

Default bridge does NOT enable embedded DNS.

Containers must communicate via IP.

---

# 🌐 Task 5: Custom Network

## Create Network

```bash
docker network create my-app-net
```

## Run Containers

```bash
docker run -dit --name app1 --network my-app-net ubuntu
docker run -dit --name app2 --network my-app-net ubuntu
```

Inside app1:

```bash
ping app2
```

✅ Worked

---

## 📌 Why Custom Network Works?

User-defined bridge networks include an embedded DNS server.

Docker automatically registers container names in its internal DNS.

So:

```
app2 → IP address
```

Default bridge does not provide this feature.

---

# 🔥 Task 6: Put It Together

## Step 1: Create Custom Network

```bash
docker network create app-network
```

## Step 2: Run MySQL with Volume on Network

```bash
docker volume create app-data

docker run -d --name db \
--network app-network \
-e MYSQL_ROOT_PASSWORD=root \
-v app-data:/var/lib/mysql \
mysql
```

## Step 3: Run App Container on Same Network

```bash
docker run -dit --name app \
--network app-network \
ubuntu
```

Inside app:

```bash
ping db
```


✔ Added to: `2026/day-32/`
✔ Committed and pushed to fork



Faiz 🔥
If you want, I’ll now:

* Write your LinkedIn “aha moment” post
* Give interview questions from Day 32
* Or move to Docker Compose (next logical step)
