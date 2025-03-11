"""
Test Cases for Self-Correcting AI Framework
Validates deception detection, narrative tracking, and ethical decision-making.
"""

from src.deception_analysis import deception_entropy
from src.narrative_tracking import NarrativeTracker
from src.hermetic_decision import apply_hermetic_principles

# Sample test case functions
def test_deception_entropy():
    text = "Everyone knows that this product is the best."
    score = deception_entropy(text)
    print("Deception Entropy Test Score:", score)

def test_narrative_tracking():
    tracker = NarrativeTracker()
    tracker.track_claim("The economy is strong", "News Channel 1", "2023-06-01")
    print("Tracked Narrative:", tracker.get_claim_history("The economy is strong"))

def test_hermetic_decision():
    text = "Science always changes our understanding of reality."
    score = apply_hermetic_principles(text, 0.4)
    print("Hermetic Decision Test Score:", score)

# Run tests
if __name__ == "__main__":
    test_deception_entropy()
    test_narrative_tracking()
    test_hermetic_decision()
