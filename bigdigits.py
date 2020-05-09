import sys

Zero = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ']

One = [' * ',
       '** ',
       ' * ',
       ' * ',
       ' * ',
       ' * ',
       '***']


Two = [' **** ',
       '*    *',
       '*   * ',
       '   *  ',
       '  *   ',
       ' *    ',
       ' *****']

Eight = ['  ***  ',
         '*     *',
         '*     *',
         '  ***  ',
         '*     *',
         '*     *',
         '  ***  ']

Seven = ['***** ',
         '     *',
         '    * ',
         '   *  ',
         '   *  ',
         '   *  ',
         '   *  ',]

Four = ['   *  ',
        '  **  ',
        ' * *  ',
        '*  *  ',
        '***** ',
        '   *  ',
        '   *  ']

Five = ['*****',
        '*    ',
        '*     ',
        '*****',
        '    *',
        '    *',
        '*****']







Digits =[Zero,One,Seven,Eight]
digits = sys.argv[1]
row = 0
while row < 7:
    line=''
    column = 0
    while column < len(digits):
        number = int(digits[column])
        digit = Digits[number]
        line += digit[row] + '  '
        column +=1
    print(line)
    row += 1




# for i in Two:
#     print(i)