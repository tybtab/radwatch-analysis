import csv
import os

def csv_maker(dictionary):

    """
    This module makes the csv file for a specified spectrum that contains the
    identified isotopes along with their identified corresponding peak energies,
    branching rations, neat area, net area uncertainty, and fwhm.
    """
    csv_filename = dictionary['csv_filename']
    ordered_isotopes = dictionary['ordered_isotopes']
    ordered_energies = dictionary['ordered_energies']
    ordered_br = dictionary['ordered_br']
    ordered_net_area = dictionary['ordered_net_area']
    ordered_net_area_unc = dictionary['ordered_net_area_unc']
    ordered_peak_cps = dictionary['ordered_peak_cps']
    ordered_fwhm = dictionary['ordered_fwhm']

    if (csv_filename[-4:] == '.csv' or csv_filename[-4:] == '.CSV'):
        new_csv_filename = csv_filename[:-4] + '_identified_isotopes.csv'
    else:
        new_csv_filename = csv_filename + '_identified_isotopes.csv'

    returns_path = os.getcwd() + '/' + new_csv_filename
    file = open(returns_path,'w',newline='')
    writer = csv.writer(file)
    writer.writerow([new_csv_filename])
    writer.writerow(['Isotope','Energy (keV)','Branching Ratio','Net Area (Counts)','Net Area Uncertainty (Counts)','Peak CPS','FWHM (keV)'])

    for i in range(len(ordered_isotopes)):
        writer.writerow([ordered_isotopes[i]])
        for j in range(len(ordered_energies[i])):
            writer.writerow(['',ordered_energies[i][j],
                            ordered_br[i][j],ordered_net_area[i][j],
                            ordered_net_area_unc[i][j],ordered_peak_cps[i][j],
                            ordered_fwhm[i][j]])

    return(None)