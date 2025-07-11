import streamlit as st
import math

class BoscoGate:
    def __init__(self, r0, exotic_energy):
        self.r0 = r0
        self.exotic_energy = exotic_energy
    
    def timeline_divergence(self, q_state, t_now, t_target, lambda_decay=0.1):
        delta_t = t_now - t_target
        alpha = abs(hash(q_state) % 1000) / 1000
        divergence = alpha * math.exp(-lambda_decay * delta_t)
        return divergence
    
    def stability_index(self, divergence, delta_u=1):
        A = 4 * math.pi * (self.r0 ** 2)
        beta = (self.exotic_energy * A) / (delta_u ** 2)
        stable = beta > 0.5 and divergence > 0.1
        return stable, beta
    
    def open_gate(self, q_state, t_now, t_target):
        divergence = self.timeline_divergence(q_state, t_now, t_target)
        stable, beta = self.stability_index(divergence)
        if stable:
            st.success(f"Wormhole open to timeline '{q_state}' at time {t_target} with stability {beta:.2f}.")
            st.write(f"Timeline divergence factor: {divergence:.3f}")
            return True
        else:
            st.error(f"Failed to stabilize wormhole. Stability {beta:.2f}, divergence {divergence:.3f}.")
            return False

def main():
    st.title("Bosco Gate Simulator")
    r0 = st.slider("Throat radius (r0)", 0.001, 0.05, 0.01, 0.001)
    exotic_energy = st.slider("Exotic energy density", 10, 200, 100, 5)
    q_state = st.text_input("Quantum state label", "Q-Event-42")
    t_now = st.number_input("Current time (t_now)", 0, 10000, 1000)
    t_target = st.number_input("Target time (t_target)", 0, 10000, 900)
    
    gate = BoscoGate(r0, exotic_energy)
    if st.button("Open Gate"):
        gate.open_gate(q_state, t_now, t_target)

if __name__ == "__main__":
    main()
