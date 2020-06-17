def tax(cent=None, income=None):
    value = cent / 100 * income
    return round(value)


def calculate_tax(income=None):
    if 0 <= income <= 15527:
        percent = 0
        calculated_tax = tax(percent, income)
    elif 15528 <= income <= 42707:
        percent = 15
        calculated_tax = tax(percent, income)
    elif 42708 <= income <= 132406:
        percent = 25
        calculated_tax = tax(percent, income)
    elif income >= 132407:
        percent = 28
        calculated_tax = tax(percent, income)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
    pass


nv = int(input())
calculate_tax(nv)
