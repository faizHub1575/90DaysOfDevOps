



# 🎯 Objective

Run multi-container applications using a single command with Docker Compose.

Understand:

* How Compose manages networks automatically
* How volumes are declared
* How services communicate using service names
* How environment variables work
* How to debug integration issues

---

# ✅ Task 1: Install & Verify Docker Compose

## 🔹 Commands Used

```bash
docker compose version
docker version
```

## 🔹 Observation

* Docker Compose V2 is included with Docker Desktop.
* `docker compose` (space) is modern syntax.
* Compose integrates directly with Docker CLI.

## 📘 Result

Compose is available and working on the system.

---

# ✅ Task 2: First Compose File (Single Container)

## 📁 Folder Created

```
compose-basics/
```

## 📄 docker-compose.yml

```yaml
version: "3.9"

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

## 🔹 Commands Used

```bash
docker compose up -d
docker ps
docker compose down
```

## 🌐 Browser Access

```
http://localhost:8080
```

## 📘 Result

* Nginx started successfully.
* Compose automatically created a network.
* `docker compose down` removed container and network.
* Multi-container orchestration simplified.

---

# ✅ Task 3: Two-Container Setup (WordPress + Database)

## 🎯 Goal

* WordPress container
* Database container (MariaDB)
* Shared network
* Named volume for persistence
* Service-name-based communication

---

## 📄 Final Working docker-compose.yml

```yaml
version: "3.9"

services:
  db:
    image: mariadb:10.6
    restart: always
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppassword
      MYSQL_ROOT_PASSWORD: rootpassword
    volumes:
      - mysql-data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    restart: always
    depends_on:
      - db
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppassword
      WORDPRESS_DB_NAME: wordpress

volumes:
  mysql-data:
```

---

## 🔹 Commands Used

```bash
docker compose up -d
docker compose logs -f
docker compose down
docker compose up -d
```

## 🌐 Browser

```
http://localhost:8080
```

---

## 📘 Result

* Compose automatically created network.
* WordPress connected to database using service name `db`.
* Named volume persisted database data.
* After `docker compose down` and restart → WordPress data remained.

---

# 🧠 Key Learning (Very Important)

* Service name = internal DNS hostname.
* Compose auto-creates network.
* Named volumes persist data.
* Environment variables configure containers at startup.
* Reset volume when debugging DB issues.

---

# ✅ Task 4: Compose Commands Practice

---

## 🔹 Start in Detached Mode

```bash
docker compose up -d
```

Runs containers in background.

---

## 🔹 View Running Services

```bash
docker ps
```

---

## 🔹 View Logs (All Services)

```bash
docker compose logs -f
```

---

## 🔹 View Logs (Specific Service)

```bash
docker compose logs db
docker compose logs wordpress
```

---

## 🔹 Stop Services (Without Removing)

```bash
docker compose stop
```

---

## 🔹 Remove Everything (Containers + Network)

```bash
docker compose down
```

---

## 🔹 Remove Volumes Also

```bash
docker compose down -v
```

---

## 🔹 Rebuild Images

```bash
docker compose up --build
```

---

# 📘 Result

Compose provides full lifecycle management of multi-container apps.

---

# ✅ Task 5: Environment Variables

---

## 🔹 Directly in YAML

```yaml
environment:
  MYSQL_USER: wpuser
```

Equivalent to:

```bash
docker run -e MYSQL_USER=wpuser
```

---

## 🔹 Using .env File

### Create `.env`

```
MYSQL_USER=wpuser
MYSQL_PASSWORD=wppassword
```

### Reference in docker-compose.yml

```yaml
environment:
  MYSQL_USER: ${MYSQL_USER}
  MYSQL_PASSWORD: ${MYSQL_PASSWORD}
```

---

## 🔹 Verify Variables

Inside container:

```bash
docker exec -it <container> env
```

---

## 📘 Result

* Environment variables configure containers dynamically.
* `.env` file improves security and maintainability.
* Variables are injected at container startup.

---

# 🔥 Mistakes Faced & Lessons Learned

* YAML indentation errors
* Ports must be arrays
* Named volumes must be declared globally
* WordPress generated wrong config when credentials were incorrect
* Volume reset required after DB initialization failure
* Service names enable container communication

---

# 🏗 Final Architecture

```
Browser
   ↓
WordPress Container
   ↓ (db:3306)
MariaDB Container
   ↓
Named Volume (Persistent Storage)
```

---

