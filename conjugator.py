from verbs import * 

def present_eu(infinitive): 
    return verbs[infinitive][0]


def present_tu(infinitive): 
    return verbs[infinitive][1] 


def present_ele_ela_voce(infinitive):
    conjugated_form = verbs[infinitive][1][:-1] 
    return conjugated_form 

def present_nos(infinitive): 
    conjugated_form = verbs[infinitive][1][:-1] + 'mos' 
    return conjugated_form 
