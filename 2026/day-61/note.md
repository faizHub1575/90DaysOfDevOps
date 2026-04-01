# 🚀 Day 61 – Introduction to Terraform & First AWS Infrastructure

## 📌 What is Infrastructure as Code (IaC)?

Infrastructure as Code (IaC) is a way of managing and provisioning infrastructure using code instead of manually creating resources in the cloud console. It allows us to automate, version, and reuse infrastructure setups, making deployments faster and more consistent.

IaC is important in DevOps because it reduces human errors, ensures consistency across environments, and enables easy scaling and collaboration.

---

## ❗ Problems Solved by IaC

* Manual setup is slow and error-prone
* Difficult to track changes
* No version control
* Inconsistent environments (dev, test, prod)

👉 IaC solves this by:

* Automating infrastructure creation
* Maintaining consistency
* Enabling version control (Git)
* Making rollback easy

---

## ⚙️ Terraform vs Other Tools

| Tool           | Type        | Key Feature                |
| -------------- | ----------- | -------------------------- |
| Terraform      | Declarative | Cloud-agnostic             |
| CloudFormation | Declarative | AWS-specific               |
| Ansible        | Procedural  | Configuration management   |
| Pulumi         | Declarative | Uses programming languages |

---

## 🧠 Declarative & Cloud-Agnostic

* **Declarative** → You define *what* you want, Terraform decides *how* to achieve it
* **Cloud-agnostic** → Works across AWS, Azure, GCP, etc.

---

## 🛠️ Terraform Setup

### Installed Terraform

```bash
terraform -version
```

### Configured AWS CLI

```bash
aws configure
aws sts get-caller-identity
```

---

## ☁️ Resources Created

### ✅ S3 Bucket

* Created using Terraform
* Globally unique name

### ✅ EC2 Instance

* Instance type: `t2.micro`
* AMI: Amazon Linux 2
* Tag:

```hcl
Name = "TerraWeek-Modified"
```

---

## 🔁 Terraform Commands

| Command                | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| `terraform init`       | Downloads providers and initializes project |
| `terraform plan`       | Shows execution plan                        |
| `terraform apply`      | Creates/updates resources                   |
| `terraform destroy`    | Deletes all resources                       |
| `terraform show`       | Displays current state                      |
| `terraform state list` | Lists managed resources                     |

---

## 📦 What `terraform init` does

* Downloads AWS provider plugins
* Creates `.terraform/` directory
* Prepares environment for execution

---

## 📁 What `.terraform/` contains

* Provider binaries
* Module dependencies
* Internal Terraform data

---

## 🧾 Terraform State File

### What it stores:

* Resource IDs
* Metadata
* Current infrastructure state

### ⚠️ Important Rules:

* Never edit manually ❌
* Do not commit to Git ❌
* Can expose sensitive data ❌

---

## 🔄 Modification Task

Changed EC2 tag from:

```
TerraWeek-Day1 → TerraWeek-Modified
```

### Terraform Output Symbols:

* `~` → Modify existing resource
* `+` → Create new resource
* `-` → Destroy resource

👉 This change was an **in-place update (~)**

---

## 🔥 Key Learnings

* Terraform enables full automation of infrastructure
* State file is critical for tracking resources
* Always use unique names for S3 buckets
* Avoid hardcoding values (use variables/data sources)

---

## 🧹 Cleanup

```bash
terraform destroy
```

👉 Successfully removed:

* S3 bucket
* EC2 instance

---

## 💡 Final Thoughts

Terraform is a powerful DevOps tool that helps manage infrastructure efficiently using code. It improves consistency, scalability, and automation in cloud environments.

---
