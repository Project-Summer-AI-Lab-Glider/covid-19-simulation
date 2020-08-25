populationFields = ["age", "gender", "race", "otherIllnesses", "BMI", "physicalActivity"]
from enum import Enum
class OtherIllnesses(Enum):
    hypertension = 0
    asthma = 1
    cancer = 2
    diabetes = 3
    depression = 4
    angina = 5
    myocardialInfraction = 6
    irritableBowelSyndrome = 7
    stroke = 8
    migraine = 9
#end class
testweights = [[56, 12.5],
            [["f","m"],0.52],
            [["white","black","rainbow"],[0.66, 0.22, 0.12]],
           [[OtherIllnesses.hypertension, OtherIllnesses.asthma, OtherIllnesses.cancer], [0.12, 0.08, 0.03]]]