'Give information about airports and their runways'

from os import mkdir, path

import pandas as pd
import requests
from requests import Response


def run():
    DATA_URL = 'https://github.com/davidmegginson/ourairports-data/raw/main'
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
                    full_url = f'{DATA_URL}/{filename}'
                    response: Response = requests.get(full_url)
                    if response.status_code == 200:
                        f.write(response.text)

    def create_airports_df():
        cols = 'name ident type latitude_deg longitude_deg elevation_ft iso_country iso_region municipality'.split()
        df = pd.read_csv(f'{CACHE_DIR}/airports.csv', index_col='ident', usecols=cols)
        df['type'] = df['type'].astype('category')
        df['elevation_ft'] = df['elevation_ft'].fillna(0).astype('int32')
        return df

    def create_runways_df():
        cols = 'id airport_ref airport_ident length_ft width_ft surface closed le_ident he_ident'.split()
        df = pd.read_csv(f'{CACHE_DIR}/runways.csv', index_col='id', usecols=cols)
        df['length_ft'] = df['length_ft'].fillna(0).astype('int16')
        df['width_ft' ] = df['width_ft' ].fillna(0).astype('int16')
        return df

    def print_airport_info(ident) -> None:
        ap = airports.loc[ident]
        print(f"{ap['name']} is in {ap.iso_region}, {ap.municipality}, elev. {ap.elevation_ft} ft")

    def print_runway_info(ident) -> None:
        print('Runways')
        airport_rws = runways[runways['airport_ident'] == ident]
        for row in airport_rws.itertuples():
            print(f"{row.le_ident}/{row.he_ident}: {row.length_ft}×{row.width_ft} ft")

    cache_files_if_needed()
    airports = create_airports_df()
    runways = create_runways_df()

    while True:
        if not (ident := input('\nWhat airport ID? ').strip().upper()):
            break
        if ident not in airports.index and ('K' + ident) in airports.index:
            ident = 'K' + ident  # Add the K automatically
        if ident in airports.index:
            print_airport_info(ident)
            print_runway_info(ident)
        else:
            print('Can’t find that airport')

if __name__ == '__main__':
    run()
