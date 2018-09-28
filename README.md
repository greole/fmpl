# fmpl - Foam Mini Parsing Library

A python library to parse and write values to OpenFOAM dictionaries

# Usage


    import fmpl

    case = fmpl.Case("path/to/case")

    # Acces a generic value in a Dictionary stored in
    # the costant folder
    case.constant.myDictionary.get("name", dtype=int, default=None)





