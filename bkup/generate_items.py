import random, os

questionmarkposition = 0

def make_form_html(prompt,cardtext,target,amycondition,amy,bobcondition,bob,chriscondition,chris):
    return '''<table class="layout"><tr><td colspan="2"><h2 class="prompt">%s</h2></td></tr><tr><th rowspan="3"><div class="card"><p class="cardtext">%s</p>
<table class="bordered centered">
%s
</table>
</div>
</td>
<td>
<table>
<tr>
<td><input name="amy%s" id="amy" type="checkbox"></td>
<td><label for="amy"><img class="player-img" src="https://s14.postimg.org/hi8wahatr/player_1.png"><p class="playername">Amy</p></label></td>
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
<td><input name="bob%s" id="bob" type="checkbox"></td>
<td><label for="bob"><img class="player-img" src="https://s14.postimg.org/hi8wahatr/player_1.png"><p class="playername">Bob</p></label></td>

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
<td><input name="chris%s" id="chris" type="checkbox"></td>
<td><label for="chris"><img class="player-img" src="https://s14.postimg.org/hi8wahatr/player_1.png"><p class="playername">Chris</p></label></td>

<td>
<table class="bordered player">
%s
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>''' % (prompt,cardtext,target,amycondition,amy,bobcondition,bob,chriscondition,chris)

def make_card_html( symbols ):
    return '<tr class="bordered">%s%s</tr><tr>%s%s</tr>' % (make_symbol_div_html(symbols[0]),make_symbol_div_html(symbols[1]),make_symbol_div_html(symbols[2]),make_symbol_div_html(symbols[3]))



def make_symbol_div_html( symbol ):
    if symbol == 'triangle':
        return triangle_html
    if symbol == 'circle':
        return circle_html
    if symbol == 'star':
        return star_html
    if symbol == 'diamond':
        return diamond_html
    if symbol == 'square':
        return square_html
    if symbol == 'questionmark':
        return questionmark_html


symbols = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]

triangle_html = '<td class="bordered"><div class="cell"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/triangle.gif"></div></td>'
circle_html = '<td class="bordered tdStdSize"><div class="cell circle"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/circle.gif" height=50px; width=50px;></div></td>'
star_html = '<td class="bordered"><div class="cell"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/star.gif"></div></td>'
diamond_html = '<td class="bordered"><div class="cell"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/diamond.gif"></div></td>'
square_html = '<td class="bordered tdStdSize"><div class="cell square"><img  src="https://raw.githubusercontent.com/nahadine/IEintroExp/master/pics/square.gif" height=40px; width=40px;></div></td>'
questionmark_html = '<td class="bordered questionmark"><div class="cell">&#63;&#xFE0E;</div></td>'

cell_names = {0: 'upper left', 1: 'upper right', 2: 'lower left', 3:'lower right'}  


#i = random.randint(0,4)

def make_card():
    current_syms = random.sample(symbols,3)
    positions = [0,1,2,3]
    random.shuffle(positions)
    card = [0,0,0,0]
    card[positions[0]] = current_syms[0] # target1
    card[positions[1]] = current_syms[0] # target2
    card[positions[2]] = current_syms[1]
    card[positions[3]] = current_syms[2]
    target_positions = [positions[0], positions[1]]
    target_positions.sort()
    return card, target_positions

def make_card_three_targets():
    current_syms = random.sample(symbols,2)
    positions = [0,1,2,3]
    random.shuffle(positions)
    card = [0,0,0,0]
    card[positions[0]] = current_syms[0] # target1
    card[positions[1]] = current_syms[0] # target2
    card[positions[2]] = current_syms[0] # target3
    card[positions[3]] = current_syms[1]
    target_positions = [positions[0], positions[1], positions[2]]
    target_positions.sort()
    return card, target_positions

def od_player( card, target_positions ):
    [wrong_pos] = random.sample(target_positions, 1)
    target_sym = card[wrong_pos]
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(target_sym)
    [wrong_sym] = random.sample(rest_syms, 1)
    player = [ card[i] if i!=wrong_pos else wrong_sym for i in range(0,4) ]
    return player
    
def oa_player( card, target_positions ):
    [wrong_pos] = random.sample(set([0,1,2,3])-set(target_positions), 1)
    target_sym = card[target_positions[0]]
    player = [ card[i] if i!=wrong_pos else target_sym for i in range(0,4) ]
    return player

def se_player( card, target_positions ):
    [wrong_pos] = random.sample(set([0,1,2,3])-set(target_positions), 1)
    target_sym = card[target_positions[0]]
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(target_sym)
    rest_syms.remove(card[wrong_pos])
    [wrong_sym] = random.sample(rest_syms, 1)
    player = [ card[i] if i!=wrong_pos else wrong_sym for i in range(0,4) ]
    return player


def ua_player( card, target_positions ):
    [wrong_pos] = random.sample(target_positions, 1)
    target_sym = card[wrong_pos]
    #rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    #rest_syms.remove(target_sym)
    wrong_sym = 'questionmark'
    player = [ card[i] if i!=wrong_pos else wrong_sym for i in range(0,4) ]
    return player

def ud_player( card, target_positions ):
    global questionmarkposition
    [wrong_pos] = random.sample(set([0,1,2,3])-set(target_positions), 1)
    wrong_sym = 'questionmark'
    player = [ card[i] if i!=wrong_pos else wrong_sym for i in range(0,4) ]
    questionmarkposition = wrong_pos
    #print wrong_pos
    return player

#def ud_player_pos( card, target_positions ):
    #[wrong_pos] = random.sample(set([0,1,2,3])-set(target_positions), 1)
    #wrong_sym = 'questionmark'
    #player = [ card[i] if i!=wrong_pos else wrong_sym for i in range(0,4) ]
    #return (player,wrong_pos)


def ud_player_double( card, target_positions ):
    non_target_positions = list(set([0,1,2,3])-set(target_positions))
    #wrong_sym = 'questionmark'
    player = [0,0,0,0]
    player[target_positions[0]] = card[target_positions[0]]
    player[target_positions[1]] = card[target_positions[1]]
    player[non_target_positions[0]] = 'questionmark'
    player[non_target_positions[1]] = 'questionmark'
    return player


def false_player( card, target_positions ):
    non_target_positions = [0,1,2,3]
    non_target_positions.remove(target_positions[0])    
    non_target_positions.remove(target_positions[1])    
    [new_target_pos] = random.sample(non_target_positions, 1)
    non_target_positions.remove(new_target_pos)
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(card[target_positions[0]])
    [wrong_sym1] = random.sample(rest_syms, 1)
    [wrong_sym2] = random.sample(rest_syms, 1)
    player = [0,0,0,0]
    player[target_positions[0]] = wrong_sym1
    player[target_positions[1]] = wrong_sym2
    player[new_target_pos] = card[target_positions[0]]
    [player[non_target_positions[0]]] = random.sample(rest_syms, 1)
    return player

def false_player_three_targets( card, target_positions ):
    rest_syms = [ 'star', 'circle', 'triangle', 'diamond', 'square' ]
    rest_syms.remove(card[target_positions[0]])
    [wrong_sym1] = random.sample(rest_syms, 1)
    [wrong_sym2] = random.sample(rest_syms, 1)
    [wrong_sym3] = random.sample(rest_syms, 1)
    non_target_pos = list(set([0,1,2,3])-set(target_positions))[0]
    player = [0,0,0,0]
    player[target_positions[0]] = wrong_sym1
    player[target_positions[1]] = wrong_sym2
    player[target_positions[2]] = wrong_sym2
    player[non_target_pos] = card[target_positions[0]]
    return player


c=make_card()
print c
##print 'SE', se_player(c[0],c[1])
##print 'OD', od_player(c[0],c[1])
##print 'OA', oa_player(c[0],c[1])
##print 'UA', ua_player(c[0],c[1])
#print 'UD', ud_player(c[0],c[1])
print 'UD-double', ud_player_double(c[0],c[1])
##print 'false', false_player_three_targets(c[0],c[1])


############################################
############################################
############################################

# generating the items

# 40 target items
if not os.path.exists('items'):
    os.makedirs('items')

# 10 UD items
for i in range(0,10):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=UD_role=target', 'true':'_item=UD_role=truecontrolSE', 'false':'_item=UD_role=falsecontrol'}
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
    f = open('items/ud'+str(i)+'.html','w')
    f.write(html)
    f.close()
    
# 10 UA items
for i in range(0,10):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'ua': make_card_html(ua_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ua':'_item=UA_role=target', 'true':'_item=UA_role=truecontrolSE', 'false':'_item=UA_role=falsecontrol'}
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
    f = open('items/ua'+str(i)+'.html','w')
    f.write(html)
    f.close()

# 10 OA items
for i in range(0,10):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'oa': make_card_html(oa_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'oa':'_item=OA_role=target', 'true':'_item=OA_role=truecontrolSE', 'false':'_item=OA_role=falsecontrol'}
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
    f = open('items/oa'+str(i)+'.html','w')
    f.write(html)
    f.close()

# 10 OD items
for i in range(0,10):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'od': make_card_html(od_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'od':'_item=OD_role=target', 'true':'_item=OD_role=truecontrolSE', 'false':'_item=OD_role=falsecontrol'}
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
    f = open('items/od'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 40 fillers
if not os.path.exists('fillers'):
    os.makedirs('fillers')

# 5 SE PERFECT FALSE with 3 target symbols 
for i in range(0,5):
    c = make_card_three_targets()
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
    f = open('fillers/ppf'+str(i)+'.html','w')
    f.write(html)
    f.close()

# 15 SE PERFECT FALSE with 2 target symbols 
for i in range(0,15):
    c = make_card()
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
    f = open('fillers/ppf'+str(i+5)+'.html','w')
    f.write(html)
    f.close()
    

# 5 win-fillers
for i in range(0,5):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=winFiller_role=UDtarget', 'true':'_item=winFiller_role=truecontrolSE', 'false':'_item=winFiller_role=falsecontrol'}
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
    prompt = 'Who will win 2 points in this round?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('fillers/win'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 5 lose-fillers
for i in range(0,5):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'ud_double': make_card_html(ud_player_double(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud_double':'_item=winFiller_role=UDtarget', 'true':'_item=winFiller_role=falsecontrolSE', 'false':'_item=winFiller_role=truecontrol'}
    players = ['ud_double', 'true', 'false']
    random.shuffle(players)
    amy = cards[players[0]]
    amycondition = conditions[players[0]]
    bob = cards[players[1]]
    bobcondition = conditions[players[1]]
    chris = cards[players[2]]
    chriscondition = conditions[players[2]]
    target_sym_name = c[0][c[1][0]]
    cardtext = 'Remember the<br>'+target_sym_name+'s'
    prompt = 'Who will lose 1 point in this round?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('fillers/lose'+str(i)+'.html','w')
    f.write(html)
    f.close()


# 10 first-sym select 2 fillers
# 10 UD items
for i in range(0,10):
    c = make_card()
    c_html = make_card_html(c[0])
    cards = {'ud': make_card_html(ud_player(c[0],c[1])), 'true': make_card_html(se_player(c[0],c[1])), 'false': make_card_html(false_player(c[0],c[1]))}
    conditions = {'ud':'_item=whichSymbolFiller_role=UDtargetTrue', 'true':'_item=whichSymbolFiller_role=truecontrolSE', 'false':'_item=whichSymbolFiller_role=falsecontrol'}
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
    positions = [0,1,2,3]
    positions.remove(questionmarkposition)
    [j] = random.sample(positions,1)
    #print j, cell_names[j]
    prompt = 'Who knows what the '+cell_names[j]+' symbol is?'
    html = make_form_html(prompt,cardtext,c_html,amycondition,amy,bobcondition,bob,chriscondition,chris)
    f = open('fillers/sym'+str(i)+'.html','w')
    f.write(html)
    f.close()

