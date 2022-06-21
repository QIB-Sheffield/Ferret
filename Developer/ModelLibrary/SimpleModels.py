import numpy as np
from SupportModules.Model import Model, ModelParameter, ModelConstant, ModelVariable 
from SupportModules.GraphSupport import LineColours

#*********************************************************************************
#** Models
#*********************************************************************************
def quadraticModel(inputData, a, b, constantsString):
    #y = ax^2 + bx + c
    constantsDict = eval(constantsString) 
    c = float(constantsDict['c'])
    return np.multiply((inputData*inputData),a) + np.multiply(inputData, b) + c


def straightLineModel(inputData, m, constantsString):
    constantsDict = eval(constantsString) 
    c = float(constantsDict['c'])
    return np.multiply(inputData,m) + c


def linearModel(inputData, a, b, constantsString=None):
    return np.multiply(inputData,a) + b

#*******************************************************************************
#** Define parameters for the model
#*******************************************************************************
def setUpParameterForStraightLineModel():
    """
    This optional function returns a list of parameter objects.

    An object is created for each parameter using the ModelParameter class 
    and added to the list, that is returned by this function.

    In the returnModelList function, this function is used to 
    populate the parameterList argument. 
    """
    paramList = []
    m = ModelParameter(shortName='m',
                        longName='m',
                        units='s-1', 
                        defaultValue=1.0, 
                        stepSize=1, 
                        precision=1, 
                        minValue=1, 
                        maxValue=100.0)
    paramList.append(m)    
    return paramList

def setUpParametersForLinearModel():
    """
    This optional function returns a list of parameter objects.

    An object is created for each parameter using the ModelParameter class 
    and added to the list, that is returned by this function.

    In the returnModelList function, this function is used to 
    populate the parameterList argument. 
    """
    paramList = []
    a = ModelParameter(shortName='a',
                        longName='a',
                        units='mL/min/mL', 
                        defaultValue=1.0, 
                        stepSize=1, 
                        precision=1, 
                        minValue=1, 
                        maxValue=100.0)
    paramList.append(a)    
    b = ModelParameter(shortName='b',
                        longName='b',
                        units='mL/min/mL', 
                        defaultValue=2, 
                        stepSize=1, 
                        precision=1, 
                        minValue=1, 
                        maxValue=100.0)
    paramList.append(b)    
    return paramList

def setUpParametersForQuadraticModel():
    """
    This optional function returns a list of parameter objects.

    An object is created for each parameter using the ModelParameter class 
    and added to the list, that is returned by this function.

    In the returnModelList function, this function is used to 
    populate the parameterList argument. 
    """
    paramList = []
    a = ModelParameter(shortName='a',
                        longName='a',
                        units='mL/min/mL', 
                        defaultValue=4.0, 
                        stepSize=1, 
                        precision=1, 
                        minValue=1, 
                        maxValue=100.0)
    paramList.append(a)    
    b = ModelParameter(shortName='b',
                        longName='b',
                        units='mL/min/mL', 
                        defaultValue=2, 
                        stepSize=1, 
                        precision=1, 
                        minValue=1, 
                        maxValue=100.0)
    paramList.append(b)    
    return paramList

#*******************************************************************************
#** Define constants for  models
#*******************************************************************************
def setUpConstantForYAxisIntersection():
    """
    This optional function returns a list of constant objects.

    An object is created for each constant using the ModelConstant class 
    and added to the list, that is returned by this function.

    In the returnModelList function, this function is used to 
    populate the constantList argument. 
    """
    constantList = []
    c = ModelConstant(shortName='c', longName='Y Axis Intersection', defaultValue=1.0, stepSize=10.0,
                       precision=1, units = None, minValue=0, maxValue=10000, listValues=[])
    constantList.append(c)
    return constantList

#*******************************************************************************
# Define variables for both models
#*******************************************************************************
def setUpVariablesForAllModels():
    """
    This optional function returns a list of variable objects.

    An object is created for each variable using the ModelVariable class 
    and added to the list, that is returned by this function.

    In the returnModelList function, this function is used to 
    populate the variablesList argument. 
    """
    variablesList = []
    X = ModelVariable('X', 'X', LineColours.blueLine, False, True)
    variablesList.append(X)

    X2 = ModelVariable('X2', 'X2', LineColours.redLine, True, False)
    variablesList.append(X2)
    return variablesList


def returnModelList():
    """
    This mandatory function returns a list of Model objects.

    Every model library module must contain an implementation of this function.

    An object is created for each mathematic model using the Model class 
    and added to the list, that is returned by this function.
    """
    linear = Model(shortName='Linear', 
                     longName ='Linear', 
                     xDataInputOnly = True,
                     modelFunction = linearModel,
                     parameterList = setUpParametersForLinearModel(), 
                     variablesList = setUpVariablesForAllModels()
                     )

    straightLine = Model(shortName='Straight Line',
                         longName='Straight Line',
                         xDataInputOnly = True,
                         modelFunction = straightLineModel,
                         parameterList = setUpParameterForStraightLineModel(), 
                         variablesList = setUpVariablesForAllModels(),
                         constantsList = setUpConstantForYAxisIntersection())

    quadratic = Model(shortName='Quadratic',
                         longName='Quadratic',
                         xDataInputOnly = True,
                         modelFunction = quadraticModel,
                         parameterList = setUpParametersForQuadraticModel(), 
                         variablesList = setUpVariablesForAllModels(),
                         constantsList = setUpConstantForYAxisIntersection())
   
    return[linear, straightLine, quadratic]


def returnDataFileFolder():
    """
    An optional function that returns the file path to the folder containing 
    CSV data files that form the input to Ferret.
    """
    return 'FerretData'