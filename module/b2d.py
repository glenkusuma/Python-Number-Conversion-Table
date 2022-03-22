# function to calculate binary to decimal using Doubling Method
def b2d(binaries=str,i=0,decimals=list()):
    binaries=binaries[::-1]
    for binary in binaries:
        decimal = 2**i*int(binary)
        decimals.append(decimal)
        i+=1
    return binaries,decimals

# helper function to print binery to decimal tables
def print_b2d(binaries=list,decimals=list):
    rown1 = '2ⁿ'
    rown2 = 'Binary'
    rown3 = 'Result'
    row1 = len(rown1)
    row2 = len(rown2)
    if len(rown3) != len(str(decimals[-1])):
        row3 = len(rown3)
    else:
        row3 = len(str(decimals[-1]))
    print("Binary to Decimal")
    table_cap = f"+-{''.center(row1,'-')}-+-{''.center(row2,'-')}-+-{''.center(row3,'-')}-+"
    print(table_cap)
    print(f"| {rown1.ljust(row1)} | {rown2.ljust(row2)} | {rown3.ljust(row3)} |")
    print(table_cap)
    decimal = 0
    for i in range(len(binaries)):
        print(f"| {str(i).ljust(row1)} | {str(binaries[i]).ljust(row2)} | {str(decimals[i]).ljust(row3)} |")
        decimal += decimals[i]
    print(table_cap)

    print(f"Binary  : {''.join(reversed(binaries))}")
    print(f"Decimal : {decimal}\n")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    print(end="= ")
    for i in range(len(binaries)):
        power = str(i).translate(SUP)
        print(end=f"2{power}.{binaries[i]}")
        if i != len(binaries)-1:
            print(end=" + ")
        else:
            print()

    print(end="= ")
    for i in range(len(decimals)):
        print(end=f"{decimals[i]}")
        if i != len(binaries)-1:
            print(end=" + ")
        else:
            print()

    print("=",decimal)

#  
def binary_to_decimal(binary):
    binaries,decimals = b2d(binary)
    print_b2d(binaries,decimals)

if __name__ == "__main__":
    binary_to_decimal("10000111100101100")