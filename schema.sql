-- Database Schema for Post-Quantum Security Architecture Metrics
-- Author: Sania Shabbir

-- 1. Create the main table to store architectural evaluations
CREATE TABLE quantum_architectures (
    architecture_id INT PRIMARY KEY,
    architecture_name VARCHAR(100) NOT NULL,
    cryptographic_family VARCHAR(50) NOT NULL,
    security_score_l DECIMAL(4, 2),
    security_score_m DECIMAL(4, 2),
    security_score_u DECIMAL(4, 2),
    key_size_kb DECIMAL(8, 2),
    latency_ms DECIMAL(8, 2),
    vulnerability_index DECIMAL(4, 2)
);

-- 2. Insert simulated benchmark data matching the Python fuzzy matrix
INSERT INTO quantum_architectures (
    architecture_id, architecture_name, cryptographic_family, 
    security_score_l, security_score_m, security_score_u, 
    key_size_kb, latency_ms, vulnerability_index
) VALUES 
    (1, 'CRYSTALS-Kyber', 'Lattice-Based', 0.80, 0.90, 1.00, 1.18, 0.15, 0.12),
    (2, 'Classic McEliece', 'Code-Based', 0.90, 0.95, 1.00, 261.12, 0.30, 0.05),
    (3, 'SPHINCS+', 'Hash-Based', 0.85, 0.90, 0.95, 0.03, 0.85, 0.08),
    (4, 'Rainbow', 'Multivariate', 0.60, 0.70, 0.80, 161.60, 0.15, 0.45);

-- 3. Analytical query to retrieve metrics for Python processing
SELECT 
    architecture_name, 
    cryptographic_family,
    security_score_m AS expected_security, 
    key_size_kb, 
    latency_ms, 
    vulnerability_index
FROM quantum_architectures
WHERE vulnerability_index < 0.50
ORDER BY expected_security DESC;
