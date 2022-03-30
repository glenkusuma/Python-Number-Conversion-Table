# Function to calculate hexadecimal to decimal 
def hex2d(hexadesimal=str,decs=list(),hexs=list(),rdec=list(),decimals=list()):
    power = 0
    total = 0
    for char in reversed(hexadesimal):
        hexs.append(char)
        if ord(char) >= 48 and ord(char) <= 57:
            decs.append(char)
            rdec.append(int(char)*16**power)
        elif ord(char) >= 65 and ord(char) <=70:
            decs.append(10 + int(chr(ord(char)-17)))
            rdec.append((10 + int(chr(ord(char)-17)))*16**power)
        total += rdec[-1]
        decimals.append(total)
        power += 1
    return hexs,decs,rdec,decimals

# Helper function to print hexadecimal to decimal table
def print_hex2d(hexs=list,decs=list,rdec=list,decimals=list):
    rown1 = 'Hex'
    rown2 = 'Dec'
    rown3 = '16ⁿ'
    rown4 = 'Dec x 16ⁿ'
    rown5 = 'Decimals'

    row1 = len(rown1)
    row2 = len(rown2)
    row3 = len(rown3)
    if len(rown4) >= len(str(rdec[-1])):
        row4 = len(rown4)
    else:
        row4 = len(str(rdec[-1]))
    if len(rown5) >= len(str(rdec[-1])):
        row5 = len(rown5)
    else:
        row5 = len(str(rdec[-1]))
    print("Hexadecimal to Decimal")
    table_cap = f"+-{''.center(row1,'-')}-+-{''.center(row2,'-')}-+-{''.center(row3,'-')}-+-{''.center(row4,'-')}-+-{''.center(row5,'-')}-+"
    print(table_cap)
    print(f"| {rown1.ljust(row1)} | {rown2.ljust(row1)} | {rown3.ljust(row3)} | {rown4.ljust(row4)} | {rown5.ljust(row5)} |")
    print(table_cap)
    for i in range(len(hexs)):
        print(f"| {str(hexs[i]).ljust(row1)} | {str(decs[i]).ljust(row2)} | {str(i).ljust(row3)} | {str(rdec[i]).ljust(row4)} | {str(decimals[i]).ljust(row5)} |")
    print(table_cap)

    print(f"Hexadecimal  : {''.join(reversed(hexs))}")
    print(f"Decimal      : {decimals[-1]}\n")
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    
    print(f"Decimal Calcutaion Steps\n= ({''.join(reversed(hexs))})₁₆\n",end= "= ")
    for i in range(len(hexs)-1,-1,-1):
        power = str(i).translate(SUP)
        print(end=f"16{power}.{decs[i]}")
        if i != 0:
            print(end=" + ")
        else:
            print()

    print(end="= ")
    for i in range(len(rdec)-1,-1,-1):
        print(end=f"{rdec[i]}")
        if i != 0:
            print(end=" + ")
        else:
            print()

    print(f"= ({decimals[-1]})₁₀")

# Wraper function hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal=str):
    hexs,decs,rdec,decimals = hex2d(hexadecimal)
    print_hex2d(hexs,decs,rdec,decimals)
    
if __name__ == "__main__":
    hexadecimal_to_decimal("10F2C")