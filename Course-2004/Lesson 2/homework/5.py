class InputCollector:
    def getSpecialNum(self):
        while 1:
            try:
                num = float(eval(input('Enter a number > 10: ')))
                if num > 10:
                    break
                
                print('That is not > 10')
                    
            except (ValueError):
                print('That is not a number')
    
        print('Thank you')

inputCollector = InputCollector()
inputCollector.getSpecialNum()
