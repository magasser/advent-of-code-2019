def calc_required_fuel(mass_values):
    total_mass = 0
    for mass in mass_values:
        added_mass = (mass // 3) - 2
        if added_mass > 0:
            total_mass += calc_required_fuel([added_mass]) + added_mass

    return total_mass


print(calc_required_fuel([12, 14, 1969]))