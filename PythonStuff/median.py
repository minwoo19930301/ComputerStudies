def getMedian(numericValues):
   theValues = sorted(numericValues)

   if len(theValues) % 2 == 1:      
     return theValues[(len(theValues)+1)/2-1]
   else:
     lower = theValues[len(theValues)/2-1]
     upper = theValues[len(theValues)/2]

     return (float(lower + upper)) / 2  

def validate(valueShouldBe, valueIs):
   print ("Value Should Be: %.6f, Value Is: %.6f, Correct: %s" % (valueShouldBe, valueIs, valueShouldBe==valueIs) )

validate(2.5, getMedian([0,1,2,3,4,5]))
validate(2, getMedian([0,1,2,3,4]))
validate(2, getMedian([3,1,2]))
validate(3, getMedian([3,2,3]))
validate(1.234, getMedian([1.234, 3.678, -2.467]))
validate(1.345, getMedian([1.234, 3.678, 1.456, -2.467]))
