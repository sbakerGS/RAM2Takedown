#--------------------------------------------------------------------------------------
#
#  Copyright: (c) 2020 Bentley Systems, Incorporated. All rights reserved. 
#
#--------------------------------------------------------------------------------------


from math import pi

from ram_concept.concrete import Concrete
from ram_concept.concretes import Concretes
from ram_concept.model import Model
from ram_concept.pt_system import PTSystem
from ram_concept.pt_system import PTSystemType
from ram_concept.pt_systems import PTSystems

def add_materials(model: Model):
    """Adds materials required for the structure."""

    # CONCRETE MIXES

    # add a 45 MPa concrete mix
    # note: adding a concrete mix with the name of an existing concrete mix will raise an exception
    concretes = model.concretes
    concrete_mix = concretes.add_concrete("45 MPa")
    concrete_mix.fc_final = 45000000
    concrete_mix.fc_initial = 30000000
    concrete_mix.poissons_ratio = 0.2
    concrete_mix.unit_mass = 2450
    concrete_mix.unit_unit_mass_for_loads = 2500
    concrete_mix.use_code_Ec = True

    # you can optionally delete the materials that come by default that you don't want
    # but you must leave at least 1 (attempting to delete the last one will raise an exception)
    all_concretes = concretes.concretes
    for concrete in all_concretes:
        if concrete.name != "45 MPa":
            concrete.delete()

    # PT SYSTEMS

    # add a PT System
    # note: adding a PT System with the name of an existing PT System will raise an exception
    pt_systems = model.pt_systems
    pt_system = pt_systems.add_pt_system("13mm Bonded")
    pt_system.Aps = 100e-6
    pt_system.Eps = 195000e6
    pt_system.Fse = 1100e6
    pt_system.Fpy = 1564e6
    pt_system.Fpu = 1840e6
    pt_system.duct_width = 70e-3
    pt_system.strands_per_duct = 4
    pt_system.min_curvature_radius = 2
    pt_system.system_type = PTSystemType.BONDED

    pt_system.anchor_friction = 0.02
    pt_system.angular_friction = 0.2 * (pi/180) # due to API consistent units this is per-degree, not per radian
    pt_system.jack_stress = 1564e6
    pt_system.seating_distance = 6e-3
    pt_system.long_term_losses = 150e6
    pt_system.wobble_friction = 0.005

    # you can optionally delete the materials that come by default that you don't want
    # but you must leave at least 1 (attempting to delete the last one will raise an exception)
    all_pt_systems = pt_systems.pt_systems
    for pt_system in all_pt_systems:
        if pt_system.name != "13mm Bonded":
            pt_system.delete()

