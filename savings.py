def total_savings(monthly, years):
    """Total saved with no interest: monthly deposit times number of months."""
    return monthly * 12 * years


def real_value(amount, years, inflation):
    """Today's purchasing power of an amount received after `years`.

    inflation is a fraction (0.03 means 3% per year).
    """
    return amount / (1 + inflation) ** years


def main():
    monthly = float(input("Monthly deposit: "))
    years = int(input("Number of years: "))
    inflation = float(input("Expected yearly inflation in %: ")) / 100
    total = total_savings(monthly, years)
    print(f"Total saved: {total:,.2f}")
    print(f"Value in today's money: {real_value(total, years, inflation):,.2f}")


if __name__ == "__main__":
    main()
