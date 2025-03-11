"""
Utility Functions Module
Provides helper functions for text processing, logging, and probability calculations.
"""

import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalize(value, min_val=0, max_val=1):
    """Normalizes a value to a given range."""
    return (value - min_val) / (max_val - min_val)

def log_event(message):
    """Logs an event in AI processing."""
    logging.info(message)

# Example Usage
if __name__ == "__main__":
    log_event("AI system initialized.")
    print("Normalized value:", normalize(0.75, 0, 1))
