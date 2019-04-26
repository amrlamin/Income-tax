#Income Tax
def main():
   incomeTax = int(input("Enter taxable income: $"))
   output = setTax(incomeTax)
   print(output)

def setTax(incomeTax):
   if incomeTax >= 0 and incomeTax <= 20000:
      setTax = .02 * incomeTax
      return("Income tax:${0:,.2f}".format(setTax))
   elif incomeTax >= 20001 and incomeTax <= 50000:
      setTax = 400 + .025 * (incomeTax - 20000)
      return("Income tax:${0:,.2f}".format(setTax))
   else:
      setTax = 1150 + .035 * (incomeTax - 50000)
      return("Income tax:${0:,.2f}".format(setTax))

main()
