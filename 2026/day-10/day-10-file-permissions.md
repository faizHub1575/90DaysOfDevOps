# Day 10 – File Permissions & File Operations Challenge

## Task Overview

Master file permissions and basic file operations in Linux by creating, reading, and modifying files and directories using standard Linux commands.

---

## Files Created

* **devops.txt** – empty file created using `touch`
* **notes.txt** – file with content created using `cat` / `echo`
* **script.sh** – shell script created using `vim`

Command used to verify:

```bash
ls -l
```

---

## Task 1: Create Files

### Commands Used

```bash
touch devops.txt
echo "This is my DevOps notes" > notes.txt
vim script.sh
```

### Content of script.sh

```bash
echo "Hello DevOps"
```

### Verification

```bash
ls -l devops.txt notes.txt script.sh
```

---

## Task 2: Read Files

### Commands Used

```bash
cat notes.txt
vim -R script.sh
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```

---

## Task 3: Understand Permissions

### Permission Format

```
rwxrwxrwx
│││ │││ │││
│││ │││ │└─ Others
│││ │└─ Group
│└─ Owner
```

### Permission Values

* r = read (4)
* w = write (2)
* x = execute (1)

### Current Permissions

```bash
ls -l devops.txt notes.txt script.sh
```

**Observation:**

* Owner can read/write
* Group and others have read-only permissions
* script.sh initially not executable

---

## Task 4: Modify Permissions

### Make script.sh executable

```bash
chmod +x script.sh
./script.sh
```

### Set devops.txt to read-only

```bash
chmod 444 devops.txt
```

### Set notes.txt to 640

```bash
chmod 640 notes.txt
```

### Create project directory with 755 permissions

```bash
mkdir project
chmod 755 project
```

### Verification

```bash
ls -l
```

---

## Task 5: Test Permissions

### Writing to read-only file

```bash
echo "test" >> devops.txt
```

**Result:** Permission denied

### Executing file without execute permission

```bash
chmod -x script.sh
./script.sh
```

**Result:** Permission denied

---

## Commands Used (Summary)

```bash
touch
cat
echo
vim
ls -l
chmod
head
tail
mkdir
```

---

## What I Learned

1. Linux permissions control who can read, write, and execute files
2. `chmod` can be used with numeric and symbolic modes
3. Execute permission is mandatory to run scripts

---

## Submission Steps

```bash
cd 2026/day-10/
git add day-10-file-permissions.md
git commit -m "Day 10: File permissions and operations"
git push
```

---


