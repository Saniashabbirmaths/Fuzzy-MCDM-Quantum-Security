import numpy as np
import pandas as pd

# 1. Simulated Quantum-Era Security Architectures Data
# Metrics:
# - Security_Score (Benefit: Higher is better)
# - Key_Size_KB (Cost: Lower is better)
# - Latency_ms (Cost: Lower is better)
architectures = ["Lattice-Based (Kyber)", "Code-Based (McEliece)", "Hash-Based (SPHINCS+)", "Multivariate (Rainbow)"]

# Triangular Fuzzy Numbers (l, m, u) representing expert evaluations under uncertainty
# Shape: (4 architectures, 3 criteria, 3 fuzzy bounds)
fuzzy_matrix = np.array([
    # Lattice-Based: High security, very small key size, ultra-low latency
    [[0.8, 0.9, 1.0], [0.1, 0.2, 0.3], [0.1, 0.15, 0.2]],
    # Code-Based: Ultra-high security, massive key size, low latency
    [[0.9, 0.95, 1.0], [0.8, 0.9, 1.0], [0.2, 0.3, 0.4]],
    # Hash-Based: High security, tiny key size, very high latency
    [[0.85, 0.9, 0.95], [0.05, 0.1, 0.15], [0.7, 0.85, 1.0]],
    # Multivariate: Moderate security, medium key size, ultra-low latency
    [[0.6, 0.7, 0.8], [0.4, 0.5, 0.6], [0.1, 0.15, 0.2]]
])

# Criteria Weights (Importance of Security, Key Size, Latency)
weights = np.array([0.50, 0.25, 0.25])

# Criteria Types: 'benefit' (higher is better) or 'cost' (lower is better)
criteria_types = ['benefit', 'cost', 'cost']

def normalize_fuzzy_matrix(matrix, types):
    """Applies vector normalization to the fuzzy decision matrix."""
    norm_matrix = np.zeros_like(matrix, dtype=float)
    num_criteria = matrix.shape[1]
    
    for j in range(num_criteria):
        if types[j] == 'benefit':
            u_max = np.max(matrix[:, j, 2])
            norm_matrix[:, j, :] = matrix[:, j, :] / u_max
        elif types[j] == 'cost':
            l_min = np.min(matrix[:, j, 0])
            # Invert bounds for cost criteria: (l_min/u, l_min/m, l_min/l)
            norm_matrix[:, j, 0] = l_min / matrix[:, j, 2]
            norm_matrix[:, j, 1] = l_min / matrix[:, j, 1]
            norm_matrix[:, j, 2] = l_min / matrix[:, j, 0]
            
    return norm_matrix

def fuzzy_euclidean_distance(a, b):
    """Calculates vertex distance between two triangular fuzzy numbers."""
    return np.sqrt((1/3) * np.sum((a - b) ** 2, axis=-1))

def compute_mcdm_rankings():
    # Step 1: Normalize
    norm_matrix = normalize_fuzzy_matrix(fuzzy_matrix, criteria_types)
    
    # Step 2: Apply Weights
    weighted_matrix = norm_matrix * weights[np.newaxis, :, np.newaxis]
    
    # Step 3: Define Fuzzy Positive Ideal Solution (FPIS) and Negative Ideal Solution (FNIS)
    fpis = np.max(weighted_matrix, axis=0)
    fnis = np.min(weighted_matrix, axis=0)
    
    # Step 4: Calculate Distances (d+ and d-)
    d_plus = np.sum(fuzzy_euclidean_distance(weighted_matrix, fpis), axis=1)
    d_minus = np.sum(fuzzy_euclidean_distance(weighted_matrix, fnis), axis=1)
    
    # Step 5: Compute Closeness Coefficient (CC_i)
    closeness_coeff = d_minus / (d_plus + d_minus)
    
    # Format results into a clean DataFrame
    results = pd.DataFrame({
        'Architecture': architectures,
        'Distance_to_Ideal (d+)': np.round(d_plus, 4),
        'Distance_to_Anti_Ideal (d-)': np.round(d_minus, 4),
        'Closeness_Coefficient (CC_i)': np.round(closeness_coeff, 4)
    })
    
    results['Rank'] = results['Closeness_Coefficient (CC_i)'].rank(ascending=False).astype(int)
    return results.sort_values(by='Rank')

if __name__ == "__main__":
    print("--- Fuzzy MCDM Post-Quantum Security Architecture Evaluation ---\n")
    ranking_df = compute_mcdm_rankings()
    print(ranking_df.to_string(index=False))
