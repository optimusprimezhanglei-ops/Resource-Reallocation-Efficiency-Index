"""G20 country list + OECD extension + ISO codes"""
G20 = {
    'ARG': 'Argentina',   'AUS': 'Australia',  'BRA': 'Brazil',    'CAN': 'Canada',
    'CHN': 'China',       'FRA': 'France',     'DEU': 'Germany',   'IND': 'India',
    'IDN': 'Indonesia',   'ITA': 'Italy',      'JPN': 'Japan',     'KOR': 'South Korea',
    'MEX': 'Mexico',      'RUS': 'Russia',     'SAU': 'Saudi Arabia', 'ZAF': 'South Africa',
    'TUR': 'Türkiye',     'GBR': 'United Kingdom', 'USA': 'United States',
    # EU-27 as 20th member represented by its economic core
    'EUU': 'European Union',
}
# Note: EU-27 will be represented by GDP-weighted core (DE+FR+IT+ES+NL)
YEARS = list(range(2000, 2024))  # 24 years
print(f"G20 countries: {len(G20)}")
print(f"Years: {len(YEARS)} ({YEARS[0]}-{YEARS[-1]})")
print(f"Total country-year observations: {len(G20)*len(YEARS)}")
