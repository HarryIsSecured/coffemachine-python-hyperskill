spin = input()
charge = input()
spin_half = '1/2'
#  spin_one = '1'  isn't required but can be implemented
charge_minus_one = '-1'
charge_minus_third = '-1/3'
charge_two_thirds = '2/3'
charge_zero = '0'


if spin == spin_half and charge == charge_minus_third:
    print('Strange Quark')
elif spin == spin_half and charge == charge_two_thirds:
    print('Charm Quark')
elif spin == spin_half and charge == charge_minus_one:
    print('Electron Lepton')
elif spin == spin_half and charge == charge_zero:
    print('Neutrino Lepton')
else:
    print('Photon Boson')
