def total_savings(monthly, years):
    """Total saved with no interest: monthly deposit times number of months."""
    return monthly * 12 * years


def main():
    monthly = float(input("Monthly deposit: "))
    years = int(input("Number of years: "))
    print(f"Total saved: {total_savings(monthly, years):,.2f}")


if __name__ == "__main__":
    main()
