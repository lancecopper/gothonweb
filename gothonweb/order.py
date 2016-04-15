from gothonweb import lexicon
from gothonweb import parser

def order_transfer(user_input):
    lex = lexicon.scan(user_input)
    if len(lex) == 0:
        return None
    elif len(lex) == 1:
        if lex[0][0] == 'number':
            if lex[0][1] in ('0132', '2'):
                return lex[0][1]
            else:
                return '*'
        else:
            return lex[0][1]
    else:
        sentence = parser.parse_sentence(lex)
        return sentence.verb + " " + sentence.object
