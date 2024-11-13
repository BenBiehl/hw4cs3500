token = ''
integers = '0123456789'
hexadecimals = 'ABCDEF'
keywords = ['PRINT', '.', ',', '[', ']', '(', ')', ';']
relations =  ['<', '>', '=', '#']
addoperators = ['+', '-', 'OR', '&']
muloperators = ['*', '/', 'AND']

def getToken():
    input(token)

def isInteger(word):
    state = 1
    i = 0
    acc = False
    while i < len(word):
        c = word[i]
        if state == 1:
            if c == '+' or c == '-':
                state = 2
                i += 1
            elif c in integers:
                state = 2
                i += 1
                acc = True
            else:
                return False
        elif state == 2:
            if c in integers:
                state = 2
                i += 1
                acc = True
            else:
                return False
    return acc

def isDecimal(word):
    state = 1
    i = 0
    acc = False
    while i < len(word):
        c = word[i]
        if state == 1:
            if c == '+' or c == '-' or c in integers:
                state = 2
                i += 1
            else:
                return False
        elif state == 2:
            if c in integers:
                state = 2
                i += 1
            elif c == '.':
                state = 3
                i += 1
            else:
               return False
        # State after '.' is detected
        elif state == 3:
            if c in integers:
                state = 3
                i += 1
                acc = True
            else:
                return False
    return acc

def isString(word):
    state = 1
    i = 0
    acc = False

    while i < len(word):
        c = word[i]
        if state == 1:
            if c == '\"':
                state = 2
                i += 1
            else:
                return False
        elif state == 2:
            if c != ' ' and c != '\"':
                state = 3
                i += 1
            else:
                return False
        elif state == 3:
            if c != ' ' and c != '\"':
                state = 3
                i += 1
            elif c == '\"':
                state = 4
                i += 1
                acc = True
            else:
                return False
        # If there's an closing '"', then if there are any more characters afterwards it's invalid
        elif state == 4:
            return False
    return acc

def isKeyword(word):
    if word in keywords:
        return True
    else:
        return False
    
def isRelation(word):
    if word in relations:
        return True
    else:
        return False
    
def isAddOperator(word):
    if word in addoperators;
        return True
    else:
        return False
    
def isMulOperator(word):
    if word in muloperators:
        return True
    else:
        return False
    
def isIdentifier(word):
    state = 1
    i = 0
    acc = False

    while i < len(word):
        c = word[i]
        if state == 1:
            if c.isalpha():
                state = 2
                i += 1
                acc = True
            else:
                return False
        elif state == 2:
            if c.isalpha() or c in integers or c == '_':
                state = 2
                i += 1
            else:
                return False
    return acc

def parseStatementSequence():
    parseStatement()
    while(token != "$"):
        parseStatement()

def parseStatement():
    if token == "PRINT":
        parsePrintStatement()
    else:
        parseAssignment()

def parsePrintStatement():
    if token == "PRINT":
        getToken()
        if token == "(":
            getToken()
            parseExpression()
            if token == ")":
                getToken()
                if token == ".":
                    getToken()
                else:
                    raise TypeError(". expected")
            else:
                raise TypeError(") expected")
        else:
            raise TypeError("( expected")
    else:
        raise TypeError("PRINT expected")

def parseAssignment():
    parseDesignator()
    if token == ":=":
        getToken()
        parseExpression()
        if token == ".":
            getToken()
        else:
            raise TypeError(". expected")
    else:
        raise TypeError(":= expected")

def parseSelector():
    if token == "^":
        getToken()
        if isIdentifier(token):
            getToken()
        else:
            raise TypeError("identifier expected")

def parseDesignator():
    notDone = True

def parseFactor():
    notDone = True

def parseTerm():
    notDone = True

def parseSimpleExpression():
    notDone = True

def parseExpression():
    notDone = True