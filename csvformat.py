import csv

input_file = '/run/media/x1nx3r/iniHaDeDe0/Mgodonf/ai/prediksi-pengangguran-keras/data_pengangguran_up_to_2023.csv'
output_file = '/run/media/x1nx3r/iniHaDeDe0/Mgodonf/ai/prediksi-pengangguran-keras/data_pengangguran_up_to_2023_modified.csv'

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    rows = [','.join(row).replace(' : ', ',') for row in reader]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
