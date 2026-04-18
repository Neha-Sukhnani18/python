def solve_circuit(A, B, C):
    # Stage 1: Initial gates
    and_top = A & B
    or_mid = B | C
    and_bottom = B & C
    
    # Stage 2: Middle combination
    and_stage2 = or_mid & and_bottom
    
    # Final Stage: Output Q
    Q = and_top | and_stage2
    return Q

# Generate Truth Table
print("A B C | Q")
print("---------")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            Q = solve_circuit(A, B, C)
            print(f"{A} {B} {C} | {Q}")
