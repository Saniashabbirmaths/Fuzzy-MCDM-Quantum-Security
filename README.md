# Fuzzy-MCDM-Quantum-Security
Mathematical framework for evaluating post-quantum software security architectures
# Fuzzy-MCDM Quantum Security Evaluator

An open-source mathematical framework built in Python and SQL to evaluate and rank Post-Quantum Cryptography (PQC) and Software Security Architectures under ambient uncertainty. This project is a practical implementation based on my MPhil thesis in Mathematics.

## 🔬 Project Overview
As quantum computing evolves, traditional encryption methods will break. This tool utilizes **Fuzzy Multi-Criteria Decision-Making (MCDM)** to rank next-generation security architectures based on conflicting performance criteria (e.g., encryption speed, key size, power consumption, and adversarial attack resistance).

## 🧮 Mathematical Framework

This system models uncertainty using triangular fuzzy numbers $\tilde{A} = (l, m, u)$ to handle imprecise engineering metrics. 

### 1. Vector Normalization
To normalize conflicting criteria (where higher is better for security, but lower is better for latency), we apply:

$$\tilde{r}_{ij} = \left( \frac{l_{ij}}{u_j^+}, \frac{m_{ij}}{u_j^+}, \frac{u_{ij}}{u_j^+} \right) \quad \text{(For Benefit Criteria)}$$

$$\tilde{r}_{ij} = \left( \frac{l_j^-}{u_{ij}}, \frac{l_j^-}{m_{ij}}, \frac{l_j^-}{l_{ij}} \right) \quad \text{(For Cost/Latency Criteria)}$$

### 2. Closeness Coefficient
The final ranking is determined by calculating the closeness coefficient ($CC_i$) to the ideal mathematical solution:

$$CC_i = \frac{d^-(\tilde{A}_i, \tilde{A}^-)}{d^+(\tilde{A}_i, \tilde{A}^+) + d^-(\tilde{A}_i, \tilde{A}^-)}$$

---

## 🛠️ Tech Stack & Architecture

*   **Database (SQL):** PostgreSQL / SQLite database storing architectural vulnerability scores, key sizes, and simulated benchmark records.
*   **Mathematical Processing (Python):** NumPy and Pandas are used to construct vectors, build the fuzzy decision matrix, and compute Euclidean distances.

## 🚀 How to Run the Code

### 1. Database Setup
Run the included SQL script to initialize the security metrics database:
```sql
-- Example schema used to pull metrics
SELECT architecture_name, encryption_speed, key_size, vulnerability_index 
FROM quantum_architectures;
```

### 2. Compute Rankings
Execute the primary python script to calculate the mathematical matrix:
```bash
python compute_fuzzy_mcdm.py
```

---

## 📨 Contact & Academic Research
*   **Author**: Sania Shabbir
*   **Degree**: MPhil in Mathematics (CGPA: 3.83/4.00)
*   **Target**: Fully Funded PhD Candidate (2027 Intake)
*   **Email** : [saniashabbir241@gmail.com]
