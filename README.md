
# MLOps Project – CI with Sentiment Analysis

This project is a minimal Sentiment Analysis app built with **Streamlit** and **TextBlob**, designed to **practice and demonstrate MLOps principles**, specifically **Continuous Integration (CI)** using **GitHub Actions**.

**Project URL:** [Repo](https://github.com/knight22-21/Mlops-project-ci)

---

## Project Focus

While the sentiment model itself is intentionally simple, the real goal of this project is to:

- Practice **CI** for machine learning projects
- Automate testing and linting with GitHub Actions
- Simulate real-world ML workflows with version control, testing, and quality checks

---

## Project Structure

```

.github/workflows/
│   └── ci.yaml          # GitHub Actions workflow for CI
.gitignore               # Ignored files
LICENSE                  # Open source license
README.md                # Project documentation
app.py                   # Streamlit app with sentiment analysis
requirements.txt         # Python dependencies
test_app.py              # Unit tests for sentiment logic

````

---

## CI Workflow Highlights

Implemented using **GitHub Actions**:

- Runs on every push and pull request to `main`
- Installs dependencies and runs `pytest`
- Lints code with `flake8`
- Prevents merging broken or unclean code into main

CI config file: `.github/workflows/ci.yaml`

---

## How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/knight22-21/Mlops-project-ci.git
   cd Mlops-project-ci
   ```


2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   streamlit run app.py
   ```

4. **Run tests**

   ```bash
   pytest test_app.py
   ```

---

## What I Learned

* How to set up **CI pipelines** for ML projects
* Importance of test coverage and code linting
* That **failures (like my first broken run)** are part of the process — and where the real learning happens

---

## Next Steps

* Add **Continuous Delivery (CD)** via Streamlit Cloud or Hugging Face Spaces
* Containerize with **Docker**
* Expand test coverage and model complexity gradually

---

## License


This project is licensed under the [MIT License](LICENSE).

---
