
# 🚀 Day 65 — Terraform Modules: Build Reusable Infrastructure

## 🧠 Why Modules?

Earlier, everything was written in one `main.tf` file → not scalable.

👉 Problem:

* Code duplication
* Hard to manage
* Not reusable

👉 Solution:
**Terraform Modules = Functions**

> Write once → reuse multiple times

---

# 📁 Module Structure

```bash
terraform-modules/
├── main.tf
├── variables.tf
├── outputs.tf
├── providers.tf
└── modules/
    ├── ec2-instance/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── security-group/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

---

## 🔑 Root vs Child Module

* **Root Module**

  * Entry point (`terraform apply`)
  * Calls other modules
  * Handles orchestration

* **Child Module**

  * Reusable component
  * Creates specific resources (EC2, SG)

---

# 💻 EC2 Module

## variables.tf

```hcl
variable "ami_id" { type = string }

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "subnet_id" { type = string }

variable "security_group_ids" {
  type = list(string)
}

variable "instance_name" { type = string }

variable "tags" {
  type    = map(string)
  default = {}
}
```

---

## main.tf

```hcl
resource "aws_instance" "this" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = var.security_group_ids

  tags = merge(
    { Name = var.instance_name },
    var.tags
  )
}
```

---

## outputs.tf

```hcl
output "instance_id"  { value = aws_instance.this.id }
output "public_ip"    { value = aws_instance.this.public_ip }
output "private_ip"   { value = aws_instance.this.private_ip }
```

---

# 🔐 Security Group Module

## Key Concept: Dynamic Block

```hcl
dynamic "ingress" {
  for_each = var.ingress_ports
```

👉 `ingress.value` = current port (22, 80, 443)

---

## main.tf

```hcl
resource "aws_security_group" "this" {
  name   = var.sg_name
  vpc_id = var.vpc_id

  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    { Name = var.sg_name },
    var.tags
  )
}
```

---

# 🔗 Root Module (Wiring Everything)

## Security Group

```hcl
module "web_sg" {
  source  = "./modules/security-group"
  vpc_id  = module.vpc.vpc_id
  sg_name = "terraweek-web-sg"
}
```

---

## EC2 (Reused Module)

```hcl
module "web_server" {
  source             = "./modules/ec2-instance"
  subnet_id          = module.vpc.public_subnets[0]
  security_group_ids = [module.web_sg.sg_id]
  instance_name      = "terraweek-web"
}

module "api_server" {
  source             = "./modules/ec2-instance"
  subnet_id          = module.vpc.public_subnets[1]
  security_group_ids = [module.web_sg.sg_id]
  instance_name      = "terraweek-api"
}
```

---

# 🌐 Registry Module (VPC)

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  cidr = "10.0.0.0/16"
  azs  = ["ap-south-1a", "ap-south-1b"]

  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]
}
```

---

# ⚖️ Comparison: Manual vs Registry VPC

| Feature          | Manual VPC | Registry Module |
| ---------------- | ---------- | --------------- |
| Resources        | 2–3        | 10–20+          |
| Internet Gateway | ❌          | ✅               |
| Route Tables     | ❌          | ✅               |
| Production Ready | ❌          | ✅               |

👉 Registry module = **real-world usage**

---

# 📦 Where Modules Are Stored

```bash
.terraform/modules/
```

👉 Terraform downloads registry modules here.

---

# 🔍 State Representation

```bash
terraform state list
```

Example:

```
module.vpc.aws_vpc.this
module.web_server.aws_instance.this
module.web_sg.aws_security_group.this
```

👉 Format:

```
module.<module_name>.<resource>
```

---

# 🔒 Module Versioning

```hcl
version = "5.1.0"         # exact
version = "~> 5.0"        # recommended
version = ">=5.0,<6.0"    # range
```

👉 Upgrade:

```bash
terraform init -upgrade
```

---

# 🧠 Key Learnings

* Modules = reusable infra
* Dynamic blocks = loops
* Outputs = connect modules
* Registry modules = production ready
* Terraform state tracks everything

---

# ✅ 5 Best Practices

1. Always pin module versions
2. Keep modules small (single responsibility)
3. Use variables — avoid hardcoding
4. Always define outputs
5. Add README.md for every module

---

# 💣 Cleanup (Important)

```bash
terraform destroy
```

👉 Avoid AWS billing

---

# 🧾 Final Summary

* Built custom EC2 module ✅
* Built security group module ✅
* Used dynamic blocks ✅
* Reused modules multiple times ✅
* Used registry VPC module ✅

👉 **Modules = Key to scalable Terraform**

---
