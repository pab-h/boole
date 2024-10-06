def implication(p: bool, q: bool) -> bool:
    return not p or q

def biimplication(p: bool, q: bool) -> bool:
    return implication(p, q) and implication(q, p)

def __buildTrueTable(rowsLen, columsLen):
    rows = []
    for s in range(columsLen):
        row = [(i // (2 ** s) % 2) == 1 for i in range(rowsLen)]
        rows.append(row)
    return rows

def table(fn):
    def buildHeader(varnames):
        header = ""

        for var in varnames:
            header += f"{var} |\t"

        header += "fn\t\n"

        return header
    
    def buildOutput(trueTable, fn):
        output = ""

        columsLen = len(trueTable)
        rowsLen = len(trueTable[0])

        for i in range(rowsLen):
            values = []

            for k in range(columsLen):
                values.append(trueTable[k][i])

            for j in range(columsLen):
                output += f"{values[j]} |\t"

            output += f"{fn(*values)}\n"

        return output

    rowsLen = 2 ** fn.__code__.co_argcount
    columsLen = fn.__code__.co_argcount
    varnames = fn.__code__.co_varnames

    trueTable = __buildTrueTable(
        rowsLen,
        columsLen
    )

    header = buildHeader(varnames)
    output = buildOutput(trueTable,fn)
        
    print(header + output)

def graph(fn, *signs):
    def __buildTrueTable(rowsLen, columsLen):
        rows = []
        for s in range(columsLen):
            row = [(i // (2 ** s) % 2) == 1 for i in range(rowsLen)]
            rows.append(row)
        return rows
    
    varnames = fn.__code__.co_varnames

    output = ""

    if not signs:
        signs = __buildTrueTable(
            rowsLen = 2 ** fn.__code__.co_argcount,
            columsLen = fn.__code__.co_argcount
        )


    for varname, signal in zip(varnames, signs):
        output += f"{varname}:\t"
        for bit in signal:
            output += "-" if bit else "_"

        output += "\n"

    output += "fn:\t"

    for i in range(len(signs[0])):
        values = []

        for k in range(len(signs)):
            values.append(signs[k][i])

        output += "-" if fn(*values) else "_"

    print(output)

