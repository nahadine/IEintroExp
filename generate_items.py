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
    <td class="CBanswer"><label for="amy"><p class="playername"><input name="amy%s" id="amy" type="checkbox">Amy</p></label></td>
    <td class="CBanswer"><label for="bob"><p class="playername"><input name="bob%s" id="bob" type="checkbox">Bob</p></label></td>
    <td class="CBanswer"><label for="chris"><p class="playername"><input name="chris%s" id="chris" type="checkbox">Chris</p></label></td>
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

def make_card_2_target_syms_3_non_target_syms():
    current_syms = random.sample(symbols,5)
    positions = [0,1,2,3,4,5]
    random.shuffle(positions)
    card = [0,0,0,0,0,0]
    card[positions[0]] = current_syms[0] # target1
    card[positions[1]] = current_syms[0] # target2
    card[positions[2]] = current_syms[1]
    card[positions[3]] = current_syms[1]
    card[positions[4]] = current_syms[1]
    card[positions[5]] = current_syms[2]
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
def ud_player_for_filler( card, target_positions, n ):
    #global questionmarkposition
    free_positions = set([0,1,2,3,4,5])-set(target_positions)
    try:
        free_positions.remove(n)
    except KeyError:
        pass
    [wrong_pos] = random.sample(free_positions,1)
    player = [ card[i] if i!=wrong_pos else 'questionmark' for i in range(0,6) ]
    #questionmarkposition = wrong_pos
    return player

def wrong_about_n_player(card,target_positions, n):
    rest_symbols = set(symbols) - set([card[n]])
    [wrong_sym] = random.sample(rest_symbols,1)
    player = [ card[i] if i!=n else wrong_sym for i in range(0,6) ]
    #print 'target sym', card[target_positions[0]]
    #print rest_symbols
    #print 'wrong sym', wrong_sym
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

def ud_player_2_target_symbols_3_qums( card, target_positions ):
    non_target_positions = list(set([0,1,2,3,4,5])-set(target_positions))
    player = [0,0,0,0,0,0]
    player[target_positions[0]] = card[target_positions[0]]
    player[target_positions[1]] = card[target_positions[1]]
    player[non_target_positions[0]] = 'questionmark'
    player[non_target_positions[1]] = 'questionmark'
    player[non_target_positions[2]] = 'questionmark'
    player[non_target_positions[3]] = card[non_target_positions[3]]
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

def se_player_for_filler( card, target_positions, n ):
    non_target_positions = set([0,1,2,3,4,5])-set(target_positions)
    try:
        non_target_positions.remove(n)
    except KeyError:
        pass
    #global wrong_pos1
    #global wrong_pos2
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


def certain_but_wrong_player( card, target_positions ):
    player = se_player(card, target_positions)
    random.shuffle(player)
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
#print wrong_about_n_player(c[0],c[1],1)
#print 'SE', se_player_for_filler(c[0],c[1])
#print 'certain', certain_but_wrong_player(c[0],c[1])
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
#print 'certain', certain_but_wrong_player(c[0],c[1])
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

# 20 target items (5 each, of which 3 w/ 2 target current_syms
# and 2 w/ 3 target syms)

# 5 UD items
# 2 with 2 target symbols and 2 non-target symbols
for i in range(0,2):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=UD_2targets_role=target_2qums', 'true':'_item=UD_2targets_role=truecontrol', 'false':'_item=UD_2targets_role=falsecontrol'}
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

# 1 with 2 target symbols and 3 non-target symbols
c = make_card_2_target_syms_3_non_target_syms()
c_html = make_card_html(c[0])
cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
conditions = {'ud':'_item=UD_2targets_role=target_2qums', 'true':'_item=UD_2targets_role=truecontrol', 'false':'_item=UD_2targets_role=falsecontrol'}
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
f = open('chunk_includes/ud2.html','w')
f.write(html)
f.close()

    
# 2 with 3 target symbols
for i in range(3,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=UD_3targets_role=target_2qums', 'true':'_item=UD_3targets_role=truecontrol', 'false':'_item=UD_3targets_role=falsecontrol'}
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

    
# 5 UA items
# 2 with 2 target symbols and 2 non-target symbols
for i in range(0,2):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ua': make_card_html(ua_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ua':'_item=UA_2targets_role=target_2qums', 'true':'_item=UA_2targets_role=truecontrol', 'false':'_item=UA_2targets_role=falsecontrol'}
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

c = make_card_2_target_syms_3_non_target_syms()
c_html = make_card_html(c[0])
cards = {'ua': make_card_html(ua_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
conditions = {'ua':'_item=UA_2targets_role=target', 'true':'_item=UA_2targets_role=truecontrol', 'false':'_item=UA_2targets_role=falsecontrol'}
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
f = open('chunk_includes/ua2.html','w')
f.write(html)
f.close()

# and 2 with 3 target symbols
for i in range(3,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ua': make_card_html(ua_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ua':'_item=UA_3targets_role=target', 'true':'_item=UA_3targets_role=truecontrol', 'false':'_item=UA_3targets_role=falsecontrol'}
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


# 5 OA items
# 2 with 2 target symbols and 2 non-target symbols
for i in range(0,2):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'oa': make_card_html(oa_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'oa':'_item=OA_2targets_role=target', 'true':'_item=OA_2targets_role=truecontrol', 'false':'_item=OA_2targets_role=falsecontrol'}
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


c = make_card_2_target_syms_3_non_target_syms()
c_html = make_card_html(c[0])
cards = {'oa': make_card_html(oa_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
conditions = {'oa':'_item=OA_2targets_role=target', 'true':'_item=OA_2targets_role=truecontrol', 'false':'_item=OA_2targets_role=falsecontrol'}
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
f = open('chunk_includes/oa2.html','w')
f.write(html)
f.close()

# and 2 with 3 target symbols
for i in range(3,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'oa': make_card_html(oa_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'oa':'_item=OA_3targets_role=target', 'true':'_item=OA_3targets_role=truecontrol', 'false':'_item=OA_3targets_role=falsecontrol'}
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

# 5 OD items
# 2 with 2 target symbols and 2 non-target symbols
for i in range(0,2):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'od': make_card_html(od_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'od':'_item=OD_2targets_role=target', 'true':'_item=OD_2targets_role=truecontrol', 'false':'_item=OD_2targets_role=falsecontrol'}
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

c = make_card_2_target_syms_3_non_target_syms()
c_html = make_card_html(c[0])
cards = {'od': make_card_html(od_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
conditions = {'od':'_item=OD_2targets_role=target', 'true':'_item=OD_2targets_role=truecontrol', 'false':'_item=OD_2targets_role=falsecontrol'}
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
f = open('chunk_includes/od2.html','w')
f.write(html)
f.close()

# and 2 with 3 target symbols
for i in range(3,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'od': make_card_html(od_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'od':'_item=OD_3targets_role=target', 'true':'_item=OD_3targets_role=truecontrol', 'false':'_item=OD_3targets_role=falsecontrol'}
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

# 5 PPF
# 2 SE PERFECT FALSE with 3 target symbols 
for i in range(0,2):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'perfect': c_html, 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player_three_targets(c[0],c[1]))}
    conditions = {'perfect':'_item=TrueTrueFalseFiller_3targets_role=truePerfect', 'true':'_item=TrueTrueFalseFiller_3targets_role=trueSE', 'false':'_item=TrueTrueFalseFiller_3targets_role=false'}
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

# 3 SE PERFECT FALSE with 2 target symbols 
for i in range(2,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'perfect': c_html, 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'perfect':'_item=TrueTrueFalseFiller_2targets_role=truePerfect', 'true':'_item=TrueTrueFalseFiller_2targets_role=trueSE', 'false':'_item=TrueTrueFalseFiller_2targets_role=false'}
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
    

# 10 win-fillers
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=winFiller_2targets_role=UDtarget_2qums', 'true':'_item=winFiller_2targets_role=truecontrol', 'false':'_item=winFiller_2targets_role=falsecontrol'}
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

for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=winFiller_3targets_role=UDtarget_2qums', 'true':'_item=winFiller_3targets_role=truecontrol', 'false':'_item=winFiller_3targets_role=falsecontrol'}
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



# 10 lose-fillers
for i in range(0,5):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols_3_qums(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=loseFiller_3targets_role=UDtarget_3qums', 'true':'_item=loseFiller_3targets_role=falsecontrolSE', 'false':'_item=loseFiller_3targets_role=truecontrol'}
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
    prompt = 'Who will lose 10 dollars in this round?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/lose'+str(i)+'.html','w')
    f.write(html)
    f.close()

for i in range(5,10):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_2_target_symbols_3_qums(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=loseFiller_2targets_role=UDtarget_3qums', 'true':'_item=loseFiller_2targets_role=falsecontrolSE', 'false':'_item=loseFiller_2targets_role=truecontrol'}
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
    prompt = 'Who will lose 10 dollars in this round?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/lose'+str(i)+'.html','w')
    f.write(html)
    f.close()



# 5 nth-sym fillers
# UD
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    [n] = random.sample([0,1,4,5],1)
    cards = {'ud': make_card_html(ud_player_for_filler(c[0],c[1],n)), 'true': make_card_html(se_player_for_filler(c[0],c[1],n)), 'false': make_card_html(wrong_about_n_player(c[0],c[1],n))}
    conditions = {'ud':'_item=whichSymbolFiller_2targets_role=UDtargetTrue_1qums', 'true':'_item=whichSymbolFiller_2targets_role=truecontrol', 'false':'_item=whichSymbolFiller_2targets_role=falsecontrol'}
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
    prompt = 'Who knows what the '+cell_names[n]+' symbol is?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/sym'+str(i)+'.html','w')
    f.write(html)
    f.close()


############################
# NEW FILLERS
############################

# 10 certain fillers, 
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(certain_but_wrong_player(c[0],c[1])), 'ua': make_card_html(ua_player(c[0],c[1]))}
    conditions = {'ud':'_item=certainFiller_2targets_role=UDtargetFalse_2qums', 'true':'_item=certainFiller_2targets_role=truecontrol', 'ua':'_item=certainFiller_2targets_role=falsecontrol'}
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
    prompt = 'Who is certain about which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/certain'+str(i)+'.html','w')
    f.write(html)
    f.close()

for i in range(5,10):
    c = make_card_3_target_syms()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player_3_target_symbols(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'ua': make_card_html(ua_player(c[0],c[1]))}
    conditions = {'ud':'_item=certainFiller_3targets_role=UDtargetFalse_2qums', 'true':'_item=certainFiller_3targets_role=truecontrol', 'ua':'_item=certainFiller_3targets_role=falsecontrol'}
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
    prompt = 'Who is certain about which of the shapes are '+target_sym_name+'s?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('chunk_includes/certain'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 10 forget fillers, false, UA, UD 
for i in range(0,5):
    c = make_card_2_target_syms()
    c_html = make_card_html(c[0])
    cards = {'perfect': c_html, 'ua': make_card_html(ua_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'perfect':'_item=forgetFiller_2targets_role=falsecontrol', 'false':'_item=forgetFiller_2targets_role=truecontrol', 'ua':'_item=forgetFiller_2targets_role=UAtarget'}
    players = ['perfect', 'false', 'ua']
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
    cards = {'perfect': c_html, 'ua': make_card_html(ua_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'perfect':'_item=forgetFiller_3targets_role=falsecontrol', 'false':'_item=forgetFiller_3targets_role=truecontrol', 'ua':'_item=forgetFiller_3targets_role=UAtarget'}
    players = ['perfect', 'false', 'ua']
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

