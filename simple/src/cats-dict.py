
cats = {}
cats['tabby'] = 'The tabby cat...'
cats['persian'] = 'This cat...'
cats['hairless'] = 'This type of cat, which horrifies most people, ...'

catType = input('What type of cat? ')

if catType not in cats:
    print('Does not compute!')
else:
    print(cats[catType])
