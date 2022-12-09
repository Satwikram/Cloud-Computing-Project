from simulation import Simulation
from window import Window

from curve import curve_road
sim = Simulation()


sim.create_roads([
    ((0, 100), (140, 100)),
    ((150, 110), (150, 200)),

    *curve_road((140, 100), (150, 110), (150, 100))
])

sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': [
        [1, {"path": [0, *range(2, 17), 1]}]
    ]
})


win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)