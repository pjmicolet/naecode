from component import Component
from execute_engine import Engine

def testExample( a, b, c ):
    print( "Hey " + str( a ) + " " + str( b ) + " " + str( c ) )

def firstItem( a, b ):
    return [ a + 1, b +2, a + b]

def var( a ):
    return a

def if_func( lhs, rhs, expr, compExec : list ):
    val = {}
    exec( "val = ( {0} {1} {2} )".format(lhs,expr,rhs), {}, val )
    if val[ "val" ] == True:
        return compExec[0]
    elif len(compExec) == 2:
        return compExec[1]
    else
        return None

test = Component( testExample )
test2 = Component( firstItem )
engine = Engine( [ test2, test ] )

inputData = { "a" : 20, "b":30 }
engine.setInputParams( inputData )

engine.execute()

print( if_func( 20, 33, ">" ) )
