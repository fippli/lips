import sys
import random
import os

state = {"paragraphs":[]}

def randomParagraphNumber( paragraphs ):
     return random.randint( 0, paragraphs )

def get_paragraphs( state, n ):
    s = "\n"
    return s.join( state["paragraphs"][:n] )

def get_paragraph( state ):
    return state["paragraphs"][randomParagraphNumber( len( state["paragraphs"] ))]

def get_words( state, n ):
    s = " "
    return s.join( state["words"][:n] )

def get_words_from_paragraph( paragraph, n ):
    s = " "
    return s.join( paragraph.split(" ")[:n] )

def get_sentence( paragraph, n ):
    s = "."
    return s.join( paragraph.split(".")[:n] ) + "."

# -- ----------------------------------------
def copy_to_clipboard( text ):
    os.system( "echo '%s' | pbcopy" % text )


if __name__=="__main__":
    # read the lorem ipsum file
    try:
        file = open( "./lorem-ipsum.txt", "r" )
        #p = 0
        paragraph = ""
        full_text = ""
        for line in file:
            paragraph = paragraph + line.strip("\n")
            full_text = full_text + line.strip("\n")
            if line == "\n":
                state[ "paragraphs" ].append( paragraph )
                paragraph = ""
        state["full_text"] = full_text
        state["words"] = full_text.split(" ")

    except Exception as e:
        print( "Could not read file", e )


    params = sys.argv[1:]
    if params[0] == "-w":
         copy_to_clipboard( get_words( state, int( params[1] )))

    if params[0] == "-p":
        copy_to_clipboard( get_paragraphs( state, int( params[1] )))

    if params[0] == "-t":
        n = random.randint( 2, 6 )
        copy_to_clipboard( get_words_from_paragraph( get_paragraph( state ), n ))

    if params[0] == "-s":
        copy_to_clipboard( get_sentence( get_paragraph( state ), int( params[1] )))
