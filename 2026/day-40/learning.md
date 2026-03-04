Faiz, GitHub Actions has **many variables (contexts + environment variables)**. Below is a **practical list of the most useful ones DevOps engineers actually use**, along with their purpose and example usage.

---

# 1️⃣ Repository & Project Variables

### `github.repository`

**What it does:**
Returns the repository name.

Example:

```yaml
run: echo "Repo: ${{ github.repository }}"
```

Output:

```
faizshaikh/90DaysOfDevOps
```

---

### `github.repository_owner`

**What it does:**
Shows the owner of the repository.

Example:

```yaml
run: echo "Owner: ${{ github.repository_owner }}"
```

Output:

```
faizshaikh
```

---

# 2️⃣ Branch & Commit Variables

### `github.ref_name`

**What it does:**
Branch or tag that triggered the workflow.

Example:

```yaml
run: echo "Branch: ${{ github.ref_name }}"
```

Output:

```
main
```

---

### `github.ref`

**What it does:**
Full Git reference.

Example output:

```
refs/heads/main
```

Example:

```yaml
run: echo "${{ github.ref }}"
```

---

### `github.sha`

**What it does:**
Commit SHA that triggered the workflow.

Example:

```yaml
run: echo "Commit: ${{ github.sha }}"
```

Use case (Docker tagging):

```yaml
docker build -t myapp:${{ github.sha }} .
```

---

### `github.head_ref`

**What it does:**
Source branch in pull requests.

Example:

```yaml
run: echo "${{ github.head_ref }}"
```

---

### `github.base_ref`

**What it does:**
Target branch in pull requests.

Example:

```
main
```

---

# 3️⃣ User / Trigger Variables

### `github.actor`

**What it does:**
User who triggered the workflow.

Example:

```yaml
run: echo "Triggered by ${{ github.actor }}"
```

---

### `github.event_name`

**What it does:**
Event that triggered the workflow.

Possible values:

```
push
pull_request
workflow_dispatch
schedule
```

Example:

```yaml
run: echo "${{ github.event_name }}"
```

---

# 4️⃣ Workflow Information

### `github.workflow`

**What it does:**
Workflow name.

Example:

```yaml
run: echo "${{ github.workflow }}"
```

Output:

```
CI Pipeline
```

---

### `github.run_id`

**What it does:**
Unique ID of the workflow run.

Example:

```yaml
run: echo "${{ github.run_id }}"
```

---

### `github.run_number`

**What it does:**
Sequential number of workflow runs.

Example:

```yaml
run: echo "${{ github.run_number }}"
```

---

# 5️⃣ Runner Variables

### `RUNNER_OS`

**What it does:**
Operating system of the runner.

Example:

```yaml
run: echo "Runner OS: $RUNNER_OS"
```

Possible values:

```
Linux
Windows
macOS
```

---

### `RUNNER_ARCH`

**What it does:**
CPU architecture.

Example:

```
X64
ARM64
```

Example:

```yaml
run: echo "$RUNNER_ARCH"
```

---

### `RUNNER_NAME`

**What it does:**
Name of the runner executing the job.

Example:

```yaml
run: echo "$RUNNER_NAME"
```

---

# 6️⃣ Job Variables

### `job.status`

**What it does:**
Status of the job.

Possible values:

```
success
failure
cancelled
```

Example:

```yaml
if: job.status == 'failure'
```

---

# 7️⃣ Environment Variables

### `env`

Used to define custom environment variables.

Example:

```yaml
env:
  APP_NAME: myapp
```

Use:

```yaml
run: echo "$APP_NAME"
```

---

# 8️⃣ Secrets Variables

Stored in **GitHub repository secrets**.

Example:

```
DOCKER_USERNAME
DOCKER_PASSWORD
AWS_ACCESS_KEY
```

Usage:

```yaml
run: echo "${{ secrets.DOCKER_USERNAME }}"
```

Important for:

* Docker login
* Cloud authentication
* API keys

---

# 9️⃣ Matrix Variables

Used in **parallel builds**.

Example:

```yaml
strategy:
  matrix:
    python: [3.8, 3.9, 3.10]
```

Usage:

```yaml
run: echo "Python version ${{ matrix.python }}"
```

---

# 10️⃣ Steps Variables

### `steps.<step_id>.outputs`

Used to pass outputs between steps.

Example:

```yaml
id: build
```

Then:

```yaml
${{ steps.build.outputs.version }}
```

---

# Example Real Pipeline Using Variables

```yaml
name: DevOps Demo

on: push

jobs:
  demo:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Repo Info
        run: echo "${{ github.repository }}"

      - name: Branch Name
        run: echo "${{ github.ref_name }}"

      - name: Commit
        run: echo "${{ github.sha }}"

      - name: Actor
        run: echo "${{ github.actor }}"

      - name: Runner OS
        run: echo "$RUNNER_OS"
```

---

# Variables DevOps Engineers Use the Most

These **7 are the most important**:

```
github.ref_name
github.sha
github.actor
github.repository
github.event_name
RUNNER_OS
secrets.*
```

---

If you want, I can also show you **10 powerful GitHub Actions tricks that make pipelines look like senior DevOps engineer pipelines** (matrix builds, caching, artifacts, conditional jobs). These are **very useful for interviews and real projects.** 🚀
