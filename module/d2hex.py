# recursive function to calculate decimal to hexadecimal using division method
def d2hex(num=int,rdec=list(),rhex=list(),quotient=list(),division=list()):
    if num == 0:
        return rdec,rhex,quotient,division
    rdec.append(num%16)
    division.append(num)
    num //= 16
    quotient.append(num)
    if rdec[-1] > 9:
        rhex.append(str(chr(65 + rdec[-1] - 10)))
    else:
        rhex.append(str(rdec[-1]))
    d2hex(num,rdec,rhex,quotient,division)
    return rdec,rhex,quotient,division

# helper function to print decimal to hexadecimal tables
def print_d2hex(num,rdec,rhex,quotient,division):
    rown1 = 'Divison by 16'
    rown2 = 'Quotient'
    rown3 = 'Remainder Dec'
    rown4 = 'Hexadecimal'
    rown5 = '#'
    if len(str(division[0]))+3 <= len(rown1):
        row1 = len(rown1)
    else:
        row1 = len(str(division[0]))+3
    if len(str(quotient[0])) <= len(rown2):
        row2 = len(rown2)
    else:
        row2 = len(str(quotient[0]))+1
    row3 = len(rown3)
    row4 = len(rown4)
    row5 = len(str(len(rdec)))
    table_cap = f"+-{''.center(row1,'-')}-+-{''.center(row2,'-')}-+-{''.center(row3,'-')}-+-{''.center(row4,'-')}-+-{''.center(row5,'-')}-+"
    print(f"Decimal to Hexadecimal")
    print(table_cap)
    print(f"| {rown1.ljust(row1)} | {rown2.ljust(row2)} | {rown3.ljust(row3)} | {rown4.ljust(row4)} | {rown5.ljust(row5)} |")
    print(table_cap)
    for i in range(0,len(rdec)):
        print(f"| {(f'{str(division[i])}/16').ljust(row1)} | {str(quotient[i]).ljust(row2)} | {str(rdec[i]).ljust(row3)} | {str(rhex[i]).ljust(row4)} | {str(i).ljust(row5)} |")
    print(table_cap)
    rhex.reverse()
    print(f"Decimal     : {num}\nHexadecimal : {''.join(rhex)}")

# wraper function decimal to hexadecimal
def decimal_to_hexadecimal(decimal=int):
    rdec,rhex,quotient,division = d2hex(decimal)
    print_d2hex(decimal,rdec,rhex,quotient,division)

if __name__ == "__main__":
    decimal_to_hexadecimal(69420)