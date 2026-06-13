def calculate_discount(total_purchase, current_order=0):
    if total_purchase + current_order >= 50000000:
        return 0.1
    return 0