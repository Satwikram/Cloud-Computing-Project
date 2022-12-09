from simulation import Simulation
from window import Window
from curve import *


sim = Simulation()

n = 15
a = 2
b = 12
l = 300

# Nodes
wrs = (-b-l, a)
wls =	(-b-l, -a)

srs = (a, b+l)
sls = (-a, b+l)

ers = (b+l, -a)
els = (b+l, a)

nrs = (-a, -b-l)
nls = (a, -b-l)


wr = (-b, a)
wl =	(-b, -a)

sr = (a, b)
sl = (-a, b)

er = (b, -a)
el = (b, a)

nr = (-a, -b)
nl = (a, -b)

# Roads
wi = (wrs, wr)
si = (srs, sr)
ei = (ers, er)
ni = (nrs, nr)

wq = (wl, wls)
sq = (sl, sls)
eq = (el, els)
nq = (nl, nls)

ws = (wr, el)
ss = (sr, nl)
es = (er, wl)
ns = (nr, sl)

wr_TURN = turn_road(wr, sl, TURN_RIGHT, n)
wl_TURN = turn_road(wr, nl, TURN_LEFT, n)

sr_TURN = turn_road(sr, el, TURN_RIGHT, n)
sl_TURN = turn_road(sr, wl, TURN_LEFT, n)

er_TURN = turn_road(er, nl, TURN_RIGHT, n)
el_TURN = turn_road(er, sl, TURN_LEFT, n)

nr_TURN = turn_road(nr, wl, TURN_RIGHT, n)
nl_TURN = turn_road(nr, el, TURN_LEFT, n)

sim.create_roads([
    wi,
    si,
    ei,
    ni,

    wq,
    sq,
    eq,
    nq,

    ws,
    ss,
    es,
    ns,

    *wr_TURN,
    *wl_TURN,

    *sr_TURN,
    *sl_TURN,

    *er_TURN,
    *el_TURN,

    *nr_TURN,
    *nl_TURN
])

def road(a): return range(a, a+n)

sim.create_gen({
'vehicle_rate': 30,
'vehicles':[
    [3, {'path': [0, 8, 6]}],
    [1, {'path': [0, *road(12), 5]}],
    [1, {'path': [0, *road(12+n), 7]}],

    [3, {'path': [1, 9, 7]}],
    [1, {'path': [1, *road(12+2*n), 6]}],
    [1, {'path': [1, *road(12+3*n), 4]}],


    [3, {'path': [2, 10, 4]}],
    [1, {'path': [2, *road(12+4*n), 7]}],
    [1, {'path': [2, *road(12+5*n), 5]}],

    [3, {'path': [3, 11, 5]}],
    [1, {'path': [3, *road(12+6*n), 4]}],
    [1, {'path': [3, *road(12+7*n), 6]}]
]})

sim.create_signal([[0, 2], [1, 3]])


# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=10)