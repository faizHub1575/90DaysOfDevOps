Docker is the foundation of modern deployment. Every CI/CD pipeline, Kubernetes cluster, and microservice architecture starts with containers. Today you took the first step.

...............................................................................................................................................................................

TASK 1: WHAT IS DOCKER?

1. WHAT IS DOCKER?

Docker is a containerization platform used to package applications along with their dependencies so that they run consistently across different environments.

It solves the problem:
"It works on my machine but not on the server."

Docker ensures:

* Environment consistency
* Fast deployment
* Lightweight execution
* Easy scaling

---

2. WHAT IS A CONTAINER AND WHY DO WE NEED THEM?

What is a Container?

A container is a lightweight, standalone package that contains:

* Application code
* Runtime
* Libraries
* Dependencies
* Configuration

Containers share the host operating system kernel but run in isolation.

Why do we need containers?

Before containers:

* Applications failed in production
* Dependency conflicts
* Different OS versions
* Hard to scale

Containers solve:

* Environment consistency
* Faster startup
* Better resource utilization
* Easy portability
* Support for microservices architecture

---

3. CONTAINERS VS VIRTUAL MACHINES

Virtual Machine (VM):

Architecture:
Hardware
→ Hypervisor
→ Guest OS
→ Application

Each VM has its own full operating system.

Problems with VM:

* Heavy (GB size)
* Slow boot time
* High RAM usage

Container:

Architecture:
Hardware
→ Host OS
→ Docker Engine
→ Containers

Containers share the host OS kernel.

Benefits:

* Lightweight (MB size)
* Starts in seconds
* Low RAM usage
* Better performance

Main Difference:

VM:

* Full OS inside each VM
* Slower and heavy

Container:

* Share host OS
* Faster and lightweight

---

4. DOCKER ARCHITECTURE

Docker uses a Client-Server architecture.

Main Components:

1. Docker Client
2. Docker Daemon
3. Docker Images
4. Docker Containers
5. Docker Registry

Docker Client:
The command line tool (docker command).
Example:
docker run
docker build
docker pull

It sends commands to Docker Daemon.

Docker Daemon:
Runs in background.
Responsible for:

* Building images
* Running containers
* Managing networks
* Managing volumes

Docker Image:

* Blueprint of a container
* Read-only template
* Created using Dockerfile

Docker Container:

* Running instance of Docker image
* Isolated process on host machine

Docker Registry:

* Stores Docker images
* Public registry example: Docker Hub
* Used to pull and push images

---

5. DOCKER ARCHITECTURE FLOW (IN SIMPLE WORDS)

Step 1:
Developer runs command:
docker run nginx

Step 2:
Docker Client sends request to Docker Daemon.

Step 3:
Daemon checks if image exists locally.
If not, it pulls from Docker Registry.

Step 4:
Daemon creates container from image.

Step 5:
Container runs as isolated process on host OS.

---

INTERVIEW SHORT SUMMARY

* Docker is a containerization platform.
* Containers are lightweight and share host OS.
* Virtual machines have full OS; containers do not.
* Docker architecture includes:
  Client, Daemon, Images, Containers, Registry.
* Docker follows client-server architecture.

...............................................................

Task 2: Install Docker
Install Docker on your machine (or use a cloud instance)
Verify the installation
Run the hello-world container
Read the output carefully — it explains what just happened

docker ps -a 




WHAT HAPPENS WHEN YOU RUN IT?

When you run:

docker run hello-world

This is what happens internally:

Step 1:
Docker Client sends request to Docker Daemon.

Step 2:
Daemon checks if hello-world image exists locally.

Step 3:
If image is not found, Docker pulls it from Docker Hub.

Step 4:
Docker creates a container from that image.

Step 5:
Container runs and prints a message.

Step 6:
Container stops after execution.


................................................................
TASK 3: RUN REAL CONTAINERS

RUN NGINX CONTAINER AND ACCESS IN BROWSER

Command:
docker run -d -p 8080:80 --name mynginx nginx

Explanation:
-d means run in background
-p 8080:80 means map host port 8080 to container port 80
--name assigns a container name
nginx is the image name

Open browser and type:
http://localhost:8080

If running on EC2:
http://<Public-IP>:8080

You should see: Welcome to nginx

RUN UBUNTU CONTAINER IN INTERACTIVE MODE

Command:
docker run -it --name myubuntu ubuntu

Explanation:
-i keeps interactive input open
-t allocates terminal
ubuntu is the image

Now you are inside a mini Linux machine.

Try commands:
ls
pwd
whoami

To exit container:
exit

LIST ALL RUNNING CONTAINERS

Command:
docker ps

Shows only running containers.

LIST ALL CONTAINERS (INCLUDING STOPPED)

Command:
docker ps -a

Shows running and stopped containers.

STOP A CONTAINER

Command:
docker stop mynginx

Stops the running container.

REMOVE A CONTAINER

Command:
docker rm mynginx

Removes stopped container.


....................................................


Force remove if running:
docker rm -f mynginx



