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

Five = ['***** ',
        '*     ',
        '*     ',
        '***** ',
        '    * ',
        '    * ',
        '***** ']

Three = ['*****',
         '    *',
         '    *',
         '*****',
         '    *',
         '    *',
         '*****']

Six = ['     *   ',
       '    *    ',
       '   *     ',
       ' * * * * ',
       '*       *',
       ' *     * ',
       '   * *   ']


Nine = [ '    * *   ',
         '  *     * ',
         ' *       *',
         '  * * * * ',
         '      *   ',
         '    *     ',
         '   *      ']







Digits =[Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]
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