# Terraform State Management (Detailed Notes)

---

## 📌 1. What is Terraform State?

Terraform state is a **JSON file** that stores information about:
- Resources created by Terraform
- Their current attributes (IDs, IPs, etc.)
- Dependency relationships

### Example:
If you create an EC2 instance:
- Terraform stores its ID, IP, etc. in state

👉 This helps Terraform understand:
- What already exists
- What needs to be created, updated, or destroyed

---

## 📌 2. Types of State

### 🔹 Local State
- Stored in: `terraform.tfstate`
- Exists on your machine
- Not suitable for teams ❌

### 🔹 Remote State
- Stored in S3 (or other backend)
- Used with DynamoDB for locking
- Suitable for teams ✅

---

## 📌 3. Why State is Important

Terraform uses state to:
- Track resources
- Detect changes (drift)
- Plan updates efficiently

Without state:
👉 Terraform cannot manage infrastructure properly

---

## 📌 4. Importing Existing Resources

### 🔹 Problem:
Resources already exist in AWS but not in Terraform

### 🔹 Solution:
Use `terraform import`

### Command:
terraform import <resource_type>.<name> <resource_id>

### Example:
terraform import aws_s3_bucket.imported terraweek-import-test-faiz

---

### 🔹 Steps:
1. Write resource block in `.tf`
2. Run import command
3. Run `terraform plan`
4. Fix differences until:
   👉 "No changes"

---

### 🔹 Important:
- Import only updates **state**
- It does NOT generate configuration

---

## 📌 5. Desired State vs Actual State

Terraform compares:

Desired State (your .tf code)
VS
Actual State (AWS resources)

👉 Goal:
Both should match

---

## 📌 6. State Drift

### 🔹 Definition:
Drift occurs when:
Terraform state ≠ actual infrastructure

---

### 🔹 Example:
1. Terraform creates EC2
2. You manually change it in AWS
3. Terraform detects mismatch

---

### 🔹 Detect Drift:
terraform plan

---

### 🔹 Fix Drift:
Option 1: Update code  
Option 2: Run terraform apply  

---

## 📌 7. terraform state mv

### 🔹 Purpose:
Move or rename a resource in state

---

### 🔹 Syntax:
terraform state mv <old> <new>

---

### 🔹 Example:
terraform state mv aws_s3_bucket.imported aws_s3_bucket.logs_bucket

---

### 🔹 Use Cases:
- Renaming resource
- Moving resource to module
- Refactoring Terraform code

---

### 🔹 Benefit:
✔ No resource destruction  
✔ No downtime  

---

## 📌 8. terraform state rm

### 🔹 Purpose:
Remove resource from state without deleting it in AWS

---

### 🔹 Syntax:
terraform state rm <resource>

---

### 🔹 Example:
terraform state rm aws_s3_bucket.logs_bucket

---

### 🔹 Use Cases:
- Stop managing resource via Terraform
- Fix incorrect state
- Prepare for re-import

---

### 🔹 Important:
Resource still exists in AWS ✅  
Only removed from Terraform ❗  

---

## 📌 9. terraform import

### 🔹 Purpose:
Bring existing AWS resource under Terraform

---

### 🔹 Syntax:
terraform import <resource> <id>

---

### 🔹 Example:
terraform import aws_s3_bucket.logs_bucket terraweek-import-test-faiz

---

---

## 📌 10. Remote Backend (S3 + DynamoDB)

### 🔹 S3 Bucket:
- Stores Terraform state file
- Enables remote access

---

### 🔹 Versioning:
- Keeps history of state
- Allows rollback

---

### 🔹 DynamoDB:
- Used for state locking

---

## 📌 11. State Locking

### 🔹 Problem:
Two people running Terraform at same time

---

### 🔹 Solution:
DynamoDB lock

---

### 🔹 Behavior:
- One user runs `apply` → lock created
- Second user → blocked

---

### 🔹 Test:
Run in 2 terminals:
- Terminal 1: terraform apply
- Terminal 2: terraform plan

👉 You will see lock error

---

## 📌 12. State File Contents (High Level)

State contains:
- Resource IDs
- Attributes (IP, ARN)
- Dependencies
- Metadata

---

## 📌 13. Common Mistakes

❌ Hardcoding values  
❌ Not using remote backend  
❌ Ignoring drift  
❌ Editing state manually  

---

## 📌 14. Best Practices

✔ Use remote backend (S3 + DynamoDB)  
✔ Enable versioning  
✔ Use tagging  
✔ Avoid manual changes in AWS  
✔ Use modules  

---

## 📌 15. Key Commands Summary

terraform plan      → Preview changes  
terraform apply     → Apply changes  
terraform import    → Import resource  
terraform state mv  → Move resource  
terraform state rm  → Remove from state  

---

## 🎯 Interview Questions

### Q1: What is Terraform state?
A: A file that tracks all managed resources and their attributes.

---

### Q2: What is drift?
A: Difference between Terraform state and actual infrastructure.

---

### Q3: When to use state mv?
A: When renaming or restructuring resources.

---

### Q4: When to use state rm?
A: When removing resource from Terraform without deleting it.

---

### Q5: Why use DynamoDB?
A: To enable state locking and prevent concurrent changes.

---

## 💡 Final Insight

Terraform is not just about creating infrastructure.

👉 It is about:
- Managing state
- Ensuring consistency
- Preventing conflicts
- Enabling team collaboration
