df = pd.read_hdf('all_of_them_clean.h5')

df[['kadencja','nr_posiedzenia']] = df[['kadencja','nr_posiedzenia']].astype('uint8')
df['nr_glos'] = df['nr_glos'].astype('uint16')

df['partia'] = df['partia'].astype('category')
df['osoba'] = df['osoba'].astype('category')
df['glos'] = df['glos'].astype('category')
df['opis'] = df['opis'].astype('category')

df.to_hdf('votings.h5', 'votings', complevel=9, format='table')
