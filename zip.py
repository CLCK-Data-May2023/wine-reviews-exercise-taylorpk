from zipfile import ZipFile

with ZipFile('/home/taylor/code_louisville/data_science/wine-reviews-exercise-taylorpk/data/winemag-data-130k-v2.csv.zip', 'r') as file:
    file.extractall('/home/taylor/code_louisville/data_science/wine-reviews-exercise-taylorpk/data')