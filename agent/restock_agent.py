def restock_decision(quantity, min_threshold):
    """
    Rule-Based Intelligent Agent
    """
    if quantity < min_threshold:
        return min_threshold * 2
    return 0
