def tax_calculator(subtotal, sales_tax=.06):
    """the fuunction takes in a subtotal and tax rate and returns tax and the total (tax inclusive)

    Args:
        subtotal(float): cost of items
        tax_rate (float, optional): tax rate. Default is set to .06

    Returns:
        list: list containing subtotal, total, and tax
    """
    
    tax = round(subtotal * sales_tax, 2)
    
    total = round(subtotal + tax, 2)

    return [subtotal, tax, total]
