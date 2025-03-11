"""
Narrative Tracking Module
Tracks how claims evolve over time and compares them with historical records.
"""

import datetime

class NarrativeTracker:
    def __init__(self):
        self.claim_history = {}
    
    def track_claim(self, claim, source, date=None):
        """Tracks a claim and its source over time."""
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        if claim not in self.claim_history:
            self.claim_history[claim] = []
        self.claim_history[claim].append({"source": source, "date": date})
    
    def get_claim_history(self, claim):
        """Returns the historical timeline of a claim."""
        return self.claim_history.get(claim, [])

# Example Usage
if __name__ == "__main__":
    tracker = NarrativeTracker()
    tracker.track_claim("AI will replace all jobs", "Tech News", "2023-01-15")
    tracker.track_claim("AI will create new jobs", "Business Weekly", "2024-05-10")
    print("Claim History:", tracker.get_claim_history("AI will replace all jobs"))
