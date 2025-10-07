Here’s a **professional, beginner-friendly `README.md`** written in clean Markdown format for your Streamlit project (the Food Lover App) — complete with setup, usage, and a detailed guide on using **`uv`** for environment management.

---


# 🍕 Food Lover App (Streamlit Project)
## 📘 Quick Summary
**Food Lover App** is a fun, interactive Streamlit web app where users can select and customize their favorite dishes — from Pizza and Momos to Chaap and Chinese.  
It uses modern Python tooling with **`uv`**, a fast package manager that combines the power of `pip` and `venv` into one seamless experience.

---

## ⚡ What is `uv`?

**uv** is a modern, fast tool that combines **package installation** and **environment management** — think **pip + venv**, but **faster** and with **better dependency & lock handling**.  
Use it to:
- Create isolated environments per project  
- Install dependencies  
- Generate lock files  
- Run Python scripts reproducibly

---

## 🧠 Beginner’s Guide — What You Need to Know

### 1️⃣ Install `uv`

If you don’t have it yet, install using pip (works on all systems):

```bash
python -m pip install --upgrade uv
````

> 💡 Tip: If Python is system-installed, use:
>
> ```bash
> python -m pip install --user --upgrade uv
> ```

---

### 2️⃣ Create a Virtual Environment

Create and manage your environment using `uv`:

```bash
uv venv env
```

This creates a virtual environment folder named `env` in your project directory.

**Activate the environment:**

* **Windows (PowerShell)**

  ```bash
  .\env\Scripts\Activate.ps1
  ```
* **Windows (CMD)**

  ```bash
  .\env\Scripts\activate.bat
  ```
* **macOS / Linux**

  ```bash
  source env/bin/activate
  ```

> 🧩 `uv venv` works just like `python -m venv env` — but with additional features.

---

### 3️⃣ Install Dependencies

Once your environment is active, install the required packages.

If you have a `requirements.txt` file:

```bash
uv pip install -r requirements.txt
```

or simply:

```bash
pip install -r requirements.txt
```

✅ `uv` uses fast installers and caching, so repeated installs are much quicker.

---

### 4️⃣ Run the Streamlit App

You can directly run your app inside the `uv` context — no need to manually activate the environment every time:

```bash
uv run streamlit run chapter-2.py
```

This guarantees your app runs using the correct Python interpreter and dependencies.

---

## 🚀 Intermediate — Recommended Workflow

### 📁 Recommended Project Structure

```
food-lover-app/
├─ env/                    # uv-created virtual environment (ignored in Git)
├─ main.py
│─ chapter-1.py 
│─ chapter-2.py
│─ chapter-3.py
|- chapter_4.py
|- chapter_5.py
|- localhost.py  
├─ project.py              # Streamlit launcher file
├─ requirements.txt
└─ README.md
```

> 🛑 Add `env/` to your `.gitignore` file — never commit your environment.

---

### 🧩 Sharing Your Environment with Others

To share the same environment setup with teammates:

1. **Create & lock your environment:**

   ```bash
   uv venv env
   uv pip install -r requirements.txt
   uv lock
   ```

   > If `uv lock` isn’t available, use:
   >
   > ```bash
   > pip freeze > requirements-lock.txt
   > ```

2. **Share with your teammate:**

   * Push your code to GitHub.
   * Tell them to run:

     ```bash
     git clone <repo-url>
     cd food-lover-app
     python -m pip install --upgrade uv
     uv venv env
     uv pip install --no-deps -r requirements-lock.txt
     ```
   * or simply:

     ```bash
     uv pip sync requirements-lock.txt
     ```

Using a **lock file** ensures everyone uses **identical package versions**, avoiding “works on my machine” problems.

---

## 📦 Understanding Requirements vs Lock Files

| File Type                            | Purpose                                                            | Example                        |
| ------------------------------------ | ------------------------------------------------------------------ | ------------------------------ |
| `requirements.txt`                   | Lists dependencies (e.g. `pandas>=1.5`) — flexible but not pinned. | ✅ Good for general use         |
| `requirements-lock.txt` or `uv.lock` | Captures exact versions for full reproducibility.                  | ✅ Best for deployment or CI/CD |

👉 Typical workflow:

1. Maintain a `requirements.in` (editable)
2. Generate a pinned file:

   ```bash
   uv lock
   ```

   or

   ```bash
   pip freeze > requirements-lock.txt
   ```

---

## ⚙️ Useful Commands Summary

| Command                              | Purpose                                    |
| ------------------------------------ | ------------------------------------------ |
| `uv venv env`                        | Create a virtual environment               |
| `uv pip install -r requirements.txt` | Install all dependencies                   |
| `uv run streamlit run app.py`        | Run the Streamlit app in isolated env      |
| `uv lock`                            | Create lock file for reproducible setup    |
| `uvx <tool>`                         | Run a Python tool/app without installation |
| `pip freeze > requirements.txt`      | Export current packages manually           |

---

## 💻 Running This Project (Quick Start)

1. Clone the repository

   ```bash
   git clone <repo-url>
   cd food-lover-app
   ```

2. Set up the environment

   ```bash
   python -m pip install --upgrade uv
   uv venv env
   uv pip install -r requirements.txt
   ```

3. Run the Streamlit app

   ```bash
   uv run streamlit run project.py
   ```

4. Visit the local URL shown (usually `http://localhost:8501`).

---

## 🧩 Troubleshooting

* **Port 8501 already in use**
  Run Streamlit on a different port:

  ```bash
  streamlit run project.py --server.port 8502
  ```

* **Session state warning**
  Make sure you’re running via:

  ```bash
  streamlit run project.py
  ```

  and **not** `python project.py`.

---

## 🧑‍💻 Author

**Jagan Pradhan**
B.Tech in Computer Science, LPU
Data Science & AI Enthusiast

> *This project demonstrates a modern, efficient, and reproducible workflow using `uv` and Streamlit for Python app development.*

---

```

---

Would you like me to make this README automatically detect all your `chapter-*.py` files and display them as clickable **Streamlit tabs** when viewed on Streamlit Cloud (like a small “project launcher”)? I can extend the `project.py` accordingly.
```
