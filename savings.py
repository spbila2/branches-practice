def total_savings(monthly, years, annual_rate=0.0):
    """Total saved, with interest compounded monthly.

    annual_rate is a fraction (0.04 means 4% per year).
    """
    months = years * 12
    if annual_rate == 0:
        return monthly * months
    r = annual_rate / 12
    return monthly * ((1 + r) ** months - 1) / r


def main():
    monthly = float(input("Monthly deposit: "))
    years = int(input("Number of years: "))
    rate = float(input("Annual interest rate in % (0 for none): ")) / 100
    print(f"Total saved: {total_savings(monthly, years, rate):,.2f}")


if __name__ == "__main__":
    main()
