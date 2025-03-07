{"filter":false,"title":"calc_weight_json.py","tooltip":"/calc_weight_json.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":22,"column":35},"action":"insert","lines":["import jsonFileHandler","data = jsonFileHandler.readJsonFile('insulin.json')","if data != \"\":","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","    # Calculating the molecular weight of insulin  ","    # Getting a list of the amino acid (AA) weights  ","    aaWeights = data['weights']","    # Count the number of each amino acids  ","    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  ","    # Multiply the count by the weights  ","    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in","    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  ","    print(\"The rough molecular weight of insulin: \" +","    str(molecularWeightInsulin))","    print(\"Percent error: \" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))","else:","    print(\"Error. Exiting program\")"],"id":2}],[{"start":{"row":0,"column":22},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":2,"column":51},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":11,"column":79},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":21},"end":{"row":0,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1741353899778,"hash":"86569e231a9de130c23b325487ab474a7f09a9a7"}