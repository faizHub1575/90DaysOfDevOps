
# 📄 day-31-dockerfile.md

# Day 31 – Dockerfile: Build Your Own Images

#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham

---

# 🚀 Objective

Today I learned how to:

* Write custom Dockerfiles
* Build images using `docker build`
* Understand Docker layers
* Use CMD vs ENTRYPOINT
* Build a static website with Nginx
* Optimize image build using cache
* Use `.dockerignore` properly

This is the skill that separates someone who uses Docker from someone who ships production containers.

---

# 🧩 Task 1 – My First Dockerfile

### 📁 Folder

```
my-first-image/
```

### 📄 Dockerfile

```dockerfile
FROM ubuntu

RUN apt update && apt install -y curl

CMD ["echo", "Hello from my custom image!"]
```

### 🏗 Build Command

```bash
docker build -t my-ubuntu:v1 .
```

### ▶️ Run Command

```bash
docker run my-ubuntu:v1
```

### ✅ Output

```
Hello from my custom image!
```

### 🧠 What I Learned

* `FROM` sets base OS
* `RUN` executes during build
* `CMD` runs when container starts
* Each RUN creates a layer

---

# 🧩 Task 2 – Dockerfile Instructions

### 📄 Dockerfile Using All Instructions

```dockerfile
FROM ubuntu

RUN apt update && apt install -y curl

WORKDIR /app

COPY . .

EXPOSE 8080

CMD ["echo", "Dockerfile instructions demo"]
```

### 🏗 Build

```bash
docker build -t docker-instructions:v1 .
```

### ▶️ Run

```bash
docker run docker-instructions:v1
```

---

## 🔍 Understanding Each Instruction

| Instruction | Purpose                      |
| ----------- | ---------------------------- |
| FROM        | Base image                   |
| RUN         | Execute command during build |
| COPY        | Copy files from host         |
| WORKDIR     | Set working directory        |
| EXPOSE      | Document container port      |
| CMD         | Default runtime command      |

---

# 🧩 Task 3 – CMD vs ENTRYPOINT

## 🐳 CMD Example

```dockerfile
FROM alpine
CMD ["echo", "hello"]
```

### Run normally:

```bash
docker run cmd-test
```

Output:

```
hello
```

### Run with custom command:

```bash
docker run cmd-test echo faiz
```

Output:

```
faiz
```

### 🔎 Observation:

CMD is overridden when custom command is passed.

---

## 🐳 ENTRYPOINT Example

```dockerfile
FROM alpine
ENTRYPOINT ["echo"]
```

### Run:

```bash
docker run entry-test hello faiz
```

Output:

```
hello faiz
```

### 🔎 Observation:

ENTRYPOINT is not replaced — arguments are appended.

---

## 🧠 When to Use What?

* Use CMD → when you want default command but allow override
* Use ENTRYPOINT → when container must always run a fixed executable
* Use both together → production best practice

---

# 🧩 Task 4 – Simple Web App (Nginx)

### 📄 index.html

```html
<h1>Welcome to My Docker Website 🚀</h1>
<p>Built during #90DaysOfDevOps</p>
```

### 📄 Dockerfile

```dockerfile
FROM nginx:alpine

COPY index.html /usr/share/nginx/html/

EXPOSE 80
```

### 🏗 Build

```bash
docker build -t my-website:v1 .
```

### ▶️ Run

```bash
docker run -d -p 8080:80 my-website:v1
```

Access in browser:

```
http://localhost:8080
```

---

## 🌐 Architecture

![Image](https://miro.medium.com/1%2AMzTETTz03awLfU9-fziOxA.png)

![Image](https://i.sstatic.net/EOIPV.png)

![Image](https://miro.medium.com/1%2AfkGIx_o9zG0ZeaqQJO_x8w.png)

![Image](https://linuxhandbook.com/content/images/2025/04/docker-port-mapping.png)

Browser → localhost:8080 → Docker → Nginx → index.html

---

# 🧩 Task 5 – .dockerignore

### 📄 .dockerignore

```
node_modules
.git
*.md
.env
```

### 🧠 What I Learned

* Prevents unnecessary files from going into image
* Reduces image size
* Improves build speed
* Protects secrets (.env)

---

# 🧩 Task 6 – Build Optimization & Cache

### 🔎 Experiment

1. Build image
2. Change last line
3. Rebuild

Docker reused cached layers for unchanged instructions.

### 🧠 Why Layer Order Matters?

Docker builds images layer by layer.

If an early layer changes:

* All layers after it rebuild

If frequently changing instructions are placed at bottom:

* Cache works better
* Faster builds

### ✅ Best Practice

Put:

* OS installs first
* Dependencies next
* Application code last

---

# 💡 Important Commands Used Today

```bash
docker build -t name:tag .
docker run image-name
docker run -d -p host:container image-name
docker images
docker ps
docker stop container-name
docker rm container-name
docker rmi image-name
```



