import random, os

questionmarkposition = 0

def make_form_html(prompt,cardtext,target,amycondition,amy,bobcondition,bob,chriscondition,chris):
    return '''<table class="layout"><tr><th rowspan="3"><div class="card"><p class="cardtext">%s</p>
<table class="bordered centered">
%s
</table>
</div>
</td>
<td>
<table>
<tr>
<td><img class="player-img" src="https://s14.postimg.org/hi8wahatr/player_1.png"><p class="playername">Amy</p></td>
<td>
<table class="bordered player">
%s
</table>
</td>

</tr>
</table>
</td>

<tr>
<td>
<table>
<tr>
<td><img class="player-img" src="https://s14.postimg.org/hi8wahatr/player_1.png"><p class="playername">Bob</p></td>

<td>
<table class="bordered player">
%s
</table>
</td>
</tr>
</table>
</td>
</tr>


<tr>
<td>
<table>
<tr>
<td><img class="player-img" src="https://s14.postimg.org/hi8wahatr/player_1.png"><p class="playername">Chris</p></td>

<td>
<table class="bordered player">
%s
</table>
</td>
</tr>
</table>
</td>
</tr>
  <tr><td colspan="2"><p class="prompt">%s</p></td></tr>
  <tr><td colspan="2"><table>
  <tr>
    <td class="CBanswer"><p class="playername"><input name="amy%s" id="amy" type="checkbox"><label for="amy">Amy</label></p></td>
    <td class="CBanswer"><p class="playername"><input name="bob%s" id="bob" type="checkbox"><label for="bob">Bob</label></p></td>
    <td class="CBanswer"><p class="playername"><input name="chris%s" id="chris" type="checkbox"><label for="chris">Chris</label></p></td>
  </td></tr>
</table></tr>
</table>''' % (cardtext,target,amy,bob,chris,prompt,amycondition,bobcondition,chriscondition)




symbols = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]


triangle_html = '<td class="bordered"><div class="cell"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/triangle.gif"></div></td>'
circle_html = '<td class="bordered tdStdSize"><div class="cell circle"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/circle.gif" height=50px; width=50px;></div></td>'
star_html = '<td class="bordered"><div class="cell"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/star.gif"></div></td>'
diamond_html = '<td class="bordered"><div class="cell"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/diamond.gif"></div></td>'
square_html = '<td class="bordered tdStdSize"><div class="cell square"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/square.gif" height=40px; width=40px;></div></td>'
questionmark_html = '<td class="bordered questionmark"><div class="cell">&#63;&#xFE0E;</div></td>'

symbol_div_html = {'triangle': triangle_html, 'circle': circle_html, 'star': star_html, 'diamond': diamond_html, 'square': square_html, 'questionmark': questionmark_html }


cell_names = {0: 'upper left', 1: 'upper right', 4: 'lower left', 5:'lower right'}  


def make_card_html( symbols ):
    return '<tr class="bordered">%s%s</tr><tr>%s%s</tr><tr>%s%s</tr>' % (symbol_div_html[symbols[0]],symbol_div_html[symbols[1]],symbol_div_html[symbols[2]],symbol_div_html[symbols[3]],symbol_div_html[symbols[4]],symbol_div_html[symbols[5]])


def make_card_2_target_syms():
    current_syms = random.sample(symbols,5)
    positions = [0,1,2,3,4,5]
    random.shuffle(positions)
    card = [0,0,0,0,0,0]
    card[positions[0]] = current_syms[0] # target1
    card[positions[1]] = current_syms[0] # target2
    card[positions[2]] = current_syms[1]
    card[positions[3]] = current_syms[1]
    card[positions[4]] = current_syms[2]
    card[positions[5]] = current_syms[3]
    target_positions = [positions[0], positions[1]]
    target_positions.sort()
    return card, target_positions

def make_card_3_target_syms():
    current_syms = random.sample(symbols,4)
    positions = [0,1,2,3,4,5]
    random.shuffle(positions)
    card = [0,0,0,0,0,0]
    card[positions[0]] = current_syms[0] # target1
    card[positions[1]] = current_syms[0] # target2
    card[positions[2]] = current_syms[0] # target3
    card[positions[3]] = current_syms[1]
    card[positions[4]] = current_syms[2]
    card[positions[5]] = current_syms[3]
    target_positions = [positions[0], positions[1], positions[2]]
    target_positions.sort()
    return card, target_positions


########

#UD with just one question mark for "nth symbol" fillers
def ud_player_for_filler( card, target_positions ):
    global questionmarkposition
    [wrong_pos] = random.sample(set([0,1,2,3,4,5])-set(target_positions), 1)
    player = [ card[i] if i!=wrong_pos else 'questionmark' for i in range(0,6) ]
    questionmarkposition = wrong_pos
    return player

#UD with two question marks, based on card with two target symbols
def ud_player( card, target_positions ):
    non_target_positions = list(set([0,1,2,3,4,5])-set(target_positions))
    player = [0,0,0,0,0,0]
    player[target_positions[0]] = card[target_positions[0]]
    player[target_positions[1]] = card[target_positions[1]]
    player[non_target_positions[0]] = 'questionmark'
    player[non_target_positions[1]] = 'questionmark'
    player[non_target_positions[2]] = card[non_target_positions[2]]
    player[non_target_positions[3]] = card[non_target_positions[3]]
    return player

#UD with two question marks, based on card with three target symbols
def ud_player_3_target_symbols( card, target_positions ):
    non_target_positions = list(set([0,1,2,3,4,5])-set(target_positions))
    player = [0,0,0,0,0,0]
    player[target_positions[0]] = card[target_positions[0]]
    player[target_positions[1]] = card[target_positions[1]]
    player[target_positions[2]] = card[target_positions[2]]
    player[non_target_positions[0]] = 'questionmark'
    player[non_target_positions[1]] = 'questionmark'
    player[non_target_positions[2]] = card[non_target_positions[2]]
    return player

#UD with three question marks, based on card with three target symbols
def ud_player_3_target_symbols_3_qums( card, target_positions ):
    non_target_positions = list(set([0,1,2,3,4,5])-set(target_positions))
    player = [0,0,0,0,0,0]
    player[target_positions[0]] = card[target_positions[0]]
    player[target_positions[1]] = card[target_positions[1]]
    player[target_positions[2]] = card[target_positions[2]]
    player[non_target_positions[0]] = 'questionmark'
    player[non_target_positions[1]] = 'questionmark'
    player[non_target_positions[2]] = 'questionmark'
    return player

########

def se_player( card, target_positions ):
    non_target_positions = set([0,1,2,3,4,5])-set(target_positions)
    [wrong_pos1] = random.sample(non_target_positions,1)
    [wrong_pos2] = random.sample(non_target_positions,1)
    target_sym = card[target_positions[0]]
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(target_sym)
    rest_syms.remove(card[wrong_pos1])
    try:
        rest_syms.remove(card[wrong_pos2])
    except ValueError:
        pass 
    [wrong_sym1] = random.sample(rest_syms, 1)
    [wrong_sym2] = random.sample(rest_syms, 1)
    player = [ card[i] for i in range(0,6) ]
    player[wrong_pos1] = wrong_sym1
    player[wrong_pos2] = wrong_sym2
    return player

########

def od_player( card, target_positions ):
    [wrong_pos] = random.sample(target_positions, 1)
    target_sym = card[wrong_pos]
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(target_sym)
    [wrong_sym] = random.sample(rest_syms, 1)
    player = [ card[i] if i!=wrong_pos else wrong_sym for i in range(0,6) ]
    return player
    
def oa_player( card, target_positions ):
    [wrong_pos] = random.sample(set([0,1,2,3,4,5])-set(target_positions), 1)
    target_sym = card[target_positions[0]]
    player = [ card[i] if i!=wrong_pos else target_sym for i in range(0,6) ]
    return player


def ua_player( card, target_positions ):
    [wrong_pos] = random.sample(target_positions, 1)
    target_sym = card[wrong_pos]
    player = [ card[i] if i!=wrong_pos else 'questionmark' for i in range(0,6) ]
    return player



def false_player( card, target_positions ):
    non_target_positions = [0,1,2,3,4,5]
    non_target_positions.remove(target_positions[0])    
    non_target_positions.remove(target_positions[1])    
    [new_target_pos] = random.sample(non_target_positions, 1)
    non_target_positions.remove(new_target_pos)
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(card[target_positions[0]])
    [wrong_sym1] = random.sample(rest_syms, 1)
    [wrong_sym2] = random.sample(rest_syms, 1)
    player = [0,0,0,0,0,0]
    player[target_positions[0]] = wrong_sym1
    player[target_positions[1]] = wrong_sym2
    player[new_target_pos] = card[target_positions[0]]
    [player[non_target_positions[0]]] = random.sample(rest_syms, 1)
    [player[non_target_positions[1]]] = random.sample(rest_syms, 1)
    [player[non_target_positions[2]]] = random.sample(rest_syms, 1)
    return player

def false_player_three_targets( card, target_positions ):
    non_target_positions = [0,1,2,3,4,5]
    non_target_positions.remove(target_positions[0])    
    non_target_positions.remove(target_positions[1])    
    non_target_positions.remove(target_positions[2])    
    [new_target_pos] = random.sample(non_target_positions, 1)
    non_target_positions.remove(new_target_pos)
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(card[target_positions[0]])
    [wrong_sym1] = random.sample(rest_syms, 1)
    [wrong_sym2] = random.sample(rest_syms, 1)
    [wrong_sym3] = random.sample(rest_syms, 1)
    #non_target_pos = list(set([0,1,2,3,4,5])-set(target_positions))[0]
    player = [0,0,0,0,0,0]
    player[target_positions[0]] = wrong_sym1
    player[target_positions[1]] = wrong_sym2
    player[target_positions[2]] = wrong_sym2
    player[new_target_pos] = card[target_positions[0]]
    [player[non_target_positions[0]]] = random.sample(rest_syms, 1)
    [player[non_target_positions[1]]] = random.sample(rest_syms, 1)
    return player


#c=make_card_2_target_syms()
#print c
#print 'SE', se_player(c[0],c[1])
#print 'OD', od_player(c[0],c[1])
#print 'OA', oa_player(c[0],c[1])
#print 'UA', ua_player(c[0],c[1])
#print 'UD', ud_player(c[0],c[1])
#print 'UD for filler', ud_player_for_filler(c[0],c[1])
#print 'false', false_player(c[0],c[1])

#print
#print
#c=make_card_3_target_syms()
#print c
#print 'SE', se_player(c[0],c[1])
#print 'OD', od_player(c[0],c[1])
#print 'OA', oa_player(c[0],c[1])
#print 'UA', ua_player(c[0],c[1])
##print 'UD', ud_player(c[0],c[1])
#print 'UD for filler', ud_player_for_filler(c[0],c[1])
#print 'false', false_player_three_targets(c[0],c[1])

############################################
############################################
############################################

# generating the items

# 40 target items
# 20 of them with 2 target symbols, 20 with 3 target symbols

# 10 UD items
# 5 with 2 target symbols
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=UD_role=target', 'true':'_item=UD_role=truecontrol', 'false':'_item=UD_role=falsecontrol'}
    players = ['ud', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/ud'+str(i)+'.html','w')
    f.write(html)
    f.close()
    
# 5 with 3 target symbols
for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=UD_role=target', 'true':'_item=UD_role=truecontrol', 'false':'_item=UD_role=falsecontrol'}
    players = ['ud', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/ud'+str(i)+'.html','w')
    f.write(html)
    f.close()

    
# 10 UA items
# 5 with 2 target symbols
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ua': make_card_html(ua_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ua':'_item=UA_role=target', 'true':'_item=UA_role=truecontrol', 'false':'_item=UA_role=falsecontrol'}
    players = ['ua', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/ua'+str(i)+'.html','w')
    f.write(html)
    f.close()

# and 5 with 3 target symbols
for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ua': make_card_html(ua_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ua':'_item=UA_role=target', 'true':'_item=UA_role=truecontrol', 'false':'_item=UA_role=falsecontrol'}
    players = ['ua', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/ua'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 10 OA items
# 5 with 2 target symbols
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'oa': make_card_html(oa_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'oa':'_item=OA_role=target', 'true':'_item=OA_role=truecontrol', 'false':'_item=OA_role=falsecontrol'}
    players = ['oa', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/oa'+str(i)+'.html','w')
    f.write(html)
    f.close()

# and 5 with 3 target symbols
for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'oa': make_card_html(oa_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'oa':'_item=OA_role=target', 'true':'_item=OA_role=truecontrol', 'false':'_item=OA_role=falsecontrol'}
    players = ['oa', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/oa'+str(i)+'.html','w')
    f.write(html)
    f.close()

# 10 OD items
# 5 with 2 target symbols
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'od': make_card_html(od_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'od':'_item=OD_role=target', 'true':'_item=OD_role=truecontrol', 'false':'_item=OD_role=falsecontrol'}
    players = ['od', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/od'+str(i)+'.html','w')
    f.write(html)
    f.close()

# and 5 with 3 target symbols
for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'od': make_card_html(od_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'od':'_item=OD_role=target', 'true':'_item=OD_role=truecontrol', 'false':'_item=OD_role=falsecontrol'}
    players = ['od', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/od'+str(i)+'.html','w')
    f.write(html)
    f.close()

##################################################################

# 50 fillers

# 5 SE PERFECT FALSE with 3 target symbols 
for i in range(0,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'perfect': c_html, 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player_three_targets(c[0],c[1]))}
    conditions = {'perfect':'_item=TrueTrueFalseFiller_role=truePerfect', 'true':'_item=TrueTrueFalseFiller_role=trueSE', 'false':'_item=TrueTrueFalseFiller_role=false'}
    players = ['perfect', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/ppf'+str(i)+'.html','w')
    f.write(html)
    f.close()

# 5 SE PERFECT FALSE with 2 target symbols 
# used to be 15
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'perfect': c_html, 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'perfect':'_item=TrueTrueFalseFiller_role=truePerfect', 'true':'_item=TrueTrueFalseFiller_role=trueSE', 'false':'_item=TrueTrueFalseFiller_role=false'}
    players = ['perfect', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who knows which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/ppf'+str(i+5)+'.html','w')
    f.write(html)
    f.close()
    

# 5 win-fillers
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=winFiller_role=UDtarget', 'true':'_item=winFiller_role=truecontrol', 'false':'_item=winFiller_role=falsecontrol'}
    players = ['ud', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who will win 5 dollars in this round?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/win'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 5 lose-fillers
for i in range(0,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols_3_qums(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=winFiller_role=UDtarget', 'true':'_item=winFiller_role=falsecontrolSE', 'false':'_item=winFiller_role=truecontrol'}
    players = ['ud', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who will lose 5 dollars in this round?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/lose'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 10 nth-sym fillers
# UD
for i in range(0,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_for_filler(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=whichSymbolFiller_role=UDtargetTrue', 'true':'_item=whichSymbolFiller_role=truecontrol', 'false':'_item=whichSymbolFiller_role=falsecontrol'}
    players = ['ud', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    positions = [0,1,4,5]
    try:
        positions.remove(questionmarkposition)
    except ValueError:
        pass 
    [j] = random.sample(positions,1)
    #print j, cell_names[j]
    prompt = 'Who knows what the '+cell_names[j]+' symbol is?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/sym'+str(i)+'.html','w')
    f.write(html)
    f.close()


############################
# NEW FILLERS
############################

# 10 certain fillers, UD SE UA?
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'ua': make_card_html(ua_player(c[0],c[1]))}
    conditions = {'ud':'_item=certainFiller_role=UDtargetFalse', 'true':'_item=certainFiller_role=truecontrol', 'ua':'_item=certainFiller_role=falsecontrol'}
    players = ['ud', 'true', 'ua']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who is certain which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/certain'+str(i)+'.html','w')
    f.write(html)
    f.close()

for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'ua': make_card_html(ua_player(c[0],c[1]))}
    conditions = {'ud':'_item=certainFiller_role=UDtargetFalse', 'true':'_item=certainFiller_role=truecontrol', 'ua':'_item=certainFiller_role=falsecontrol'}
    players = ['ud', 'true', 'ua']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who is certain which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/certain'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 10 forget fillers, false, UA, UD 
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'ua': make_card_html(ua_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=forgetFiller_role=falsecontrol', 'false':'_item=forgetFiller_role=truecontrol', 'ua':'_item=forgetFiller_role=UAtarget'}
    players = ['ud', 'false', 'ua']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who forgot which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/forget'+str(i)+'.html','w')
    f.write(html)
    f.close()
    
for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_for_filler(c[0],c[1])), 'ua': make_card_html(ua_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=forgetFiller_role=falsecontrol', 'false':'_item=forgetFiller_role=truecontrol', 'ua':'_item=forgetFiller_role=UAtarget'}
    players = ['ud', 'false', 'ua']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who forgot which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/forget'+str(i)+'.html','w')
    f.write(html)
    f.close()

