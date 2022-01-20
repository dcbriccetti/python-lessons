'Give information about airports and their runways'

from os import mkdir, path

import pandas as pd
import requests

def run():
    DATA_DIR = 'https://github.com/davidmegginson/ourairports-data/raw/main'
    CACHE_DIR = 'aviation-cache'

    def cache_files_if_needed():
        try:
            mkdir(CACHE_DIR)
        except FileExistsError:
            pass
        for filename in ['airports.csv', 'runways.csv']:
            path_fn = f'{CACHE_DIR}/{filename}'
            if not path.exists(path_fn):
                print('fetching', path_fn)
                with open(path_fn, 'w') as f:
                    f.write(requests.get(f'{DATA_DIR}/{filename}').text)

    def create_airports_df():
        cols = 'name ident type latitude_deg longitude_deg elevation_ft iso_country iso_region municipality'.split()
        df = pd.read_csv(f'{CACHE_DIR}/airports.csv', index_col='ident', usecols=cols)
        df['type'] = df['type'].astype('category')
        return df

    def create_runways_df():
        cols = 'id airport_ref airport_ident length_ft width_ft surface closed le_ident he_ident'.split()
        return pd.read_csv(f'{CACHE_DIR}/runways.csv', index_col='id', usecols=cols)

    cache_files_if_needed()
    airports = create_airports_df()
    runways = create_runways_df()

    while True:
        if not (ident := input('\nWhat airport ID? ').strip().upper()):
            break
        if ident in airports.index:
            ap = airports.loc[ident]
            print(f"{ap['name']} is in {ap['iso_region']}, {ap['municipality']}, "
                  f"elev. {round(ap['elevation_ft'])} ft")
            print('Runways')
            airport_rws = runways[runways['airport_ident'] == ident]
            for row in airport_rws.itertuples():
                print(f"{row.le_ident}/{row.he_ident}: {round(row.length_ft)}×{round(row.width_ft)} ft")
        else:
            print('Can’t find that airport')

if __name__ == '__main__':
    run()
