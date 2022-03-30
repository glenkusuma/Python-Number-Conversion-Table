# Function to calculate binary to decimal using Doubling Method
def b2d(bins=str,power=0,decs=list(),decimal=list()):
    bins=bins[::-1]
    total = 0
    for binary in bins:
        dec = 2**power*int(binary)
        decs.append(dec)
        total += dec
        decimal.append(total)
        power+=1
    return bins,decs,decimal

# Helper function to print binary to decimal table
def print_b2d(bins=list,decs=list,decimal=list):
    rown1 = '2ⁿ'
    rown2 = 'Binary'
    rown3 = '2ⁿ x Binary'
    rown4 = "Decimal"
    row1 = len(rown1)
    row2 = len(rown2)
    if len(rown3) >= len(str(decs[-1])):
        row3 = len(rown3)
    else:
        row3 = len(str(decs[-1]))
    if len(rown4) >= len(str(decimal[-1])):
        row4 = len(rown4)
    else:
        row4 = len(str(decimal[-1]))
    print("Binary to Decimal")
    table_cap = f"+-{''.center(row1,'-')}-+-{''.center(row2,'-')}-+-{''.center(row3,'-')}-+-{''.center(row4,'-')}-+"
    print(table_cap)
    print(f"| {rown1.ljust(row1)} | {rown2.ljust(row2)} | {rown3.ljust(row4)} | {rown4.ljust(row4)} |")
    print(table_cap)
    dec = 0
    for i in range(len(bins)):
        print(f"| {str(i).ljust(row1)} | {str(bins[i]).ljust(row2)} | {str(decs[i]).ljust(row3)} | {str(decimal[i]).ljust(row4)} |")
        dec += decs[i]
    print(table_cap)

    print(f"Binary  : {''.join(reversed(bins))}")
    print(f"Decimal : {dec}\n")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    print(f"Decimal Calculation Steps\n= ({''.join(reversed(bins))})₂\n",end="= ")

    for i in range(len(bins)-1,-1,-1):
        power = str(i).translate(SUP)
        print(end=f"2{power}.{bins[i]}")
        if i != 0:
            print(end=" + ")
        else:
            print()

    print(end="= ")
    for i in range(len(decs)-1,-1,-1):
        print(end=f"{decs[i]}")
        if i != 0:
            print(end=" + ")
        else:
            print()

    print(f"= ({dec})₁₀")

#  Wraper function binary to decimal
def binary_to_decimal(binary):
    bins,decs,decimal = b2d(binary)
    print_b2d(bins,decs,decimal)

if __name__ == "__main__":
    binary_to_decimal("10000111100101100")