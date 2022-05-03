NA_remaining, SA_remaining, E_remaining, AS_remaining, AF_remaining, AUS_remaining, all_remaining = [], [], [], [], [], \
                                                                                                    [], []
NORTHAMERICA_ORIGINAL, SOUTHAMERICA_ORIGINAL, EUROPE_ORIGINAL, ASIA_ORIGINAL, AFRICA_ORIGINAL, AUSTRALIA_ORIGINAL, \
                                                    ALL_ORIGINAL, ALL_countrycapital = [], [], [], [], [], [], [], []
score = 0
guessed = []


class North_America:
    country_num = 23
    countries = ['Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba',
                 'Dominica', 'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras',
                 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia',
                 'Saint Vincent and the Grenadines', 'Trinidad and Tobago', 'United States']

    capitals = ['Saint Johns', 'Nassau', 'Bridgetown', 'Belmopan', 'Ottawa', 'San Jose', 'Havana', 'Roseau',
                'Santo Domingo', 'San Salvador', 'Saint George', 'Guatemala City', 'Port-au-Prince',
                'Tegucigalpa', 'Kingston', 'Mexico City', 'Managua', 'Panama City', 'Basseterre', 'Castries',
                'Kingstown', 'Port of Spain', 'Washington, D.C.']

    country_capital = {x: y for x, y in zip(countries, capitals)}

    def __init__(self):
        global NA_remaining, NORTHAMERICA_ORIGINAL

        self.countries = North_America.countries
        self.capitals = North_America.capitals
        self.country_num = North_America.country_num
        self.co_cap = North_America.country_capital
        self.co_cap = {k.lower(): v for k, v in self.co_cap.items()}
        NORTHAMERICA_ORIGINAL = self.co_cap
        NA_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            print(f'{self.countries[i]}, {self.co_cap[North_America.countries[i]]} \n')


class South_America:
    country_num = 12
    countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay',
                 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

    capitals = ['Buenos Aires', 'Sucre', 'Brasilia', 'Santiago', 'Bogota', 'Quito', 'Georgetown', 'Asuncion',
                'Lima', 'Paramaribo', 'Montevideo', 'Caracas']

    country_capital = {x: y for x, y in zip(countries, capitals)}

    def __init__(self):
        global SA_remaining, SOUTHAMERICA_ORIGINAL

        self.countries = South_America.countries
        self.capitals = South_America.capitals
        self.country_num = South_America.country_num
        self.co_cap = South_America.country_capital
        self.co_cap = {k.lower(): v for k, v in self.co_cap.items()}
        SOUTHAMERICA_ORIGINAL = self.co_cap
        SA_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            print(f'{self.countries[i]}, {self.co_cap[South_America.countries[i]]} \n')


class Europe:
    country_num = 46
    countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
                 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
                 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta',
                 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal',
                 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
                 'Turkey', 'Ukraine', 'United Kingdom', 'Vatican City']

    capitals = ['Tirana', 'Andorra la Vella', 'Vienna', 'Minsk', 'Brussels', 'Sarajevo', 'Sofia', 'Zagreb', 'Nicosia',
                'Prague', 'Copenhagen', 'Tallinn', 'Helsinki', 'Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik',
                'Dublin', 'Rome', 'Riga', 'Vaduz', 'Vilnius', 'Luxembourg', 'Valletta', 'Chisinau', 'Monaco',
                'Podgorica', 'Amsterdam', 'Skopje', 'Oslo', 'Warsaw', 'Lisbon', 'Bucharest', 'Moscow', 'San Marino',
                'Belgrade', 'Bratislava', 'Ljubljana', 'Madrid', 'Stockholm', 'Bern', 'Ankara', 'Kiev', 'London',
                'Vatican City']

    country_capital = {x: y for x, y in zip(countries, capitals)}

    def __init__(self):
        global E_remaining, EUROPE_ORIGINAL

        self.countries = Europe.countries
        self.capitals = Europe.capitals
        self.country_num = Europe.country_num
        self.co_cap = Europe.country_capital
        self.co_cap = {k.lower(): v for k, v in self.co_cap.items()}
        EUROPE_ORIGINAL = self.co_cap
        E_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            print(f'{self.countries[i]}, {self.co_cap[Europe.countries[i]]} \n')


class Asia:
    country_num = 49
    countries = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia',
                 'China', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan',
                 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal',
                 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Russia', 'Saudi Arabia',
                 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste',
                 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']

    capitals = ['Kabul', 'Yerevan', 'Baku', 'Manama', 'Dhaka', 'Thimphu', 'Bandar Seri Begawan', 'Phnom Penh',
                'Beijing', 'Tbilisi', 'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Jerusalem', 'Tokyo', 'Amman',
                'Nur-Sultan', 'Kuwait City', 'Bishkek', 'Vientiane', 'Beirut', 'Kuala Lumpur', 'Male', 'Ulaanbaatar',
                'Naypyidaw', 'Kathmandu', 'Pyongyang', 'Muscat', 'Islamabad', 'East Jerusalem', 'Manila', 'Doha',
                'Moscow', 'Riyadh', 'Singapore', 'Seoul', 'Colombo', 'Damascus', 'Taipei', 'Dushanbe', 'Bangkok',
                'Dili', 'Ankara', 'Ashgabat', 'Abu Dhabi', 'Tashkent', 'Hanoi', 'Sanaa']

    country_capital = {x: y for x, y in zip(countries, capitals)}

    def __init__(self):
        global AS_remaining, ASIA_ORIGINAL

        self.countries = Asia.countries
        self.capitals = Asia.capitals
        self.country_num = Asia.country_num
        self.co_cap = Asia.country_capital
        self.co_cap = {k.lower(): v for k, v in self.co_cap.items()}

        ASIA_ORIGINAL = self.co_cap
        AS_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            print(f'{self.countries[i]}, {self.co_cap[Asia.countries[i]]} \n')


class Africa:
    country_num = 54
    countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon',
                 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of Congo', 'Republic of Congo',
                 'Ivory Coast', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon',
                 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar',
                 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
                 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa',
                 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

    capitals = ['Algiers', 'Luanda', 'Porto-Novo', 'Gaborone', 'Ouagadougou', 'Gitega', 'Praia', 'Yaounde', 'Bangui',
                'NDjamena', 'Moroni', 'Kinshasa', 'Brazzaville', 'Yamoussoukro', 'Djibouti', 'Cairo', 'Malabo',
                'Asmara', 'Mbabane', 'Addis Aba', 'Libreville', 'Banjul', 'Accra', 'Conakry', 'Bissau', 'Nairobi',
                'Maseru', 'Monrovia', 'Tripoli', 'Antananarivo', 'Lilongwe', 'Bamako', 'Nouakchott', 'Port Louis',
                'Rabat', 'Maputo', 'Windhoek', 'Niamey', 'Abuja', 'Kigali', 'Sao Tome', 'Dakar', 'Victoria', 'Freetown',
                'Mogadishu', 'Cape Town', 'Juba', 'Khartoum', 'Dodoma', 'Lome', 'Tunis', 'Kampala', 'Lusaka', 'Harare']

    country_capital = {x: y for x, y in zip(countries, capitals)}

    def __init__(self):
        global AF_remaining, AFRICA_ORIGINAL

        self.countries = Africa.countries
        self.capitals = Africa.capitals
        self.country_num = Africa.country_num
        self.co_cap = Africa.country_capital
        self.co_cap = {k.lower(): v for k, v in self.co_cap.items()}

        AFRICA_ORIGINAL = self.co_cap
        AF_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            print(f'{self.countries[i]}, {self.co_cap[Africa.countries[i]]} \n')


class Australia:
    country_num = 14
    countries = ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau',
                 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

    capitals = ['Canberra', 'Suva', 'Tarawa', 'Majuro', 'Palikir', 'Yaren', 'Wellington', 'Ngerulmud',
                'Port Moresby', 'Apia', 'Honiara', 'Nukualofa', 'Funafuti', 'Port Vila']

    country_capital = {x: y for x, y in zip(countries, capitals)}

    def __init__(self):
        global AUS_remaining, AUSTRALIA_ORIGINAL

        self.countries = Australia.countries
        self.capitals = Australia.capitals
        self.country_num = Australia.country_num
        self.co_cap = Australia.country_capital
        self.co_cap = {k.lower(): v for k, v in self.co_cap.items()}

        AUSTRALIA_ORIGINAL = self.co_cap
        AUS_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            print(f'{self.countries[i]}, {self.co_cap[Australia.countries[i]]} \n')


class Countries:
    def __init__(self):
        self.country_capital = {**North_America.country_capital, **South_America.country_capital,
                                **Europe.country_capital, **Asia.country_capital, **Africa.country_capital,
                                **Australia.country_capital}
        self.country_capital = dict(sorted(self.country_capital.items()))
        self.country_num = len(self.country_capital)  # 196 countries
        self.co_cap = {k.lower(): v for k, v in self.country_capital.items()}

        global all_remaining, ALL_ORIGINAL, ALL_countrycapital
        ALL_countrycapital = self.co_cap
        ALL_ORIGINAL = self.co_cap
        all_remaining = self.co_cap

    def __str__(self):
        for i in range(self.country_num):
            return f'{self.country_capital} \n'


def check_guess(s, game_type):
    global score, NA_remaining, SA_remaining, E_remaining, AS_remaining, AF_remaining, AUS_remaining, guessed
    current_score = score

    if game_type == 'North America':
        remaining1 = [char for char in list(list(NA_remaining)) if char != ' ']
        x = [True for i in remaining1 if s.lower() == str(i)]
        try:
            if x:
                guessed += [s.lower()]
                del NA_remaining[s.lower()]
                print(NA_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score

    if game_type == 'South America':
        remaining2 = [char for char in list(list(SA_remaining)) if char != ' ']
        x = [True for i in remaining2 if s.lower() == str(i)]
        try:
            if x:
                guessed += [s.lower()]
                del SA_remaining[s]
                print(SA_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score

    if game_type == 'Europe':
        remaining3 = [char for char in list(list(E_remaining)) if char != ' ']
        x = [True for i in remaining3 if s.lower() == str(i)]
        try:
            if x:
                guessed += [s.lower()]
                del E_remaining[s]
                print(E_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score

    if game_type == 'Asia':
        remaining4 = [char for char in list(list(AS_remaining)) if char != ' ']
        x = [True for i in remaining4 if s.lower() == str(i)]
        try:
            if x:
                guessed += [s.lower()]
                del AS_remaining[s]
                print(AS_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score

    if game_type == 'Africa':
        remaining5 = [char for char in list(list(AF_remaining)) if char != ' ']
        x = [True for i in remaining5 if s.lower() == str(i)]
        try:
            if x:
                guessed += [s.lower()]
                del AF_remaining[s]
                print(AF_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score

    if game_type == 'Australia':
        remaining6 = [char for char in list(list(AUS_remaining)) if char != ' ']
        x = [True for i in remaining6 if s.lower() == str(i)]
        try:
            if x:
                guessed += [s.lower()]
                del AUS_remaining[s]
                print(AUS_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score

    if game_type == 'All':
        remaining7 = [char for char in list(list(all_remaining)) if char != ' ']
        x = [True for i in remaining7 if s.lower() == str(i)]
        print(x)
        try:
            if x:
                guessed += [s.lower()]
                del all_remaining[s.lower()]
                print(all_remaining)
                current_score += 1
                score = current_score
                return True, score
        except KeyError:
            print('Invalid')
            return False, score


def get_remaining(s):
    if s == 'North America':
        return NA_remaining
    if s == 'South America':
        return SA_remaining
    if s == 'Europe':
        return E_remaining
    if s == 'Asia':
        return AS_remaining
    if s == 'Africa':
        return AF_remaining
    if s == 'Australia':
        return AUS_remaining
    if s == 'All':
        return all_remaining


def get_country_capital(s):
    if s == 'North America':
        return North_America.country_capital
    if s == 'South America':
        return South_America.country_capital
    if s == 'Europe':
        return Europe.country_capital
    if s == 'Asia':
        return Asia.country_capital
    if s == 'Africa':
        return Africa.country_capital
    if s == 'Australia':
        return Australia.country_capital
    if s == 'All':
        return ALL_countrycapital


def reset_cntrylst():
    global NA_remaining, NORTHAMERICA_ORIGINAL
    if len(NA_remaining) < len(NORTHAMERICA_ORIGINAL):
        NA_remaining = NORTHAMERICA_ORIGINAL
        print(NA_remaining)
        return NA_remaining

    global SA_remaining, SOUTHAMERICA_ORIGINAL
    if len(SA_remaining) < len(SOUTHAMERICA_ORIGINAL):
        SA_remaining = SOUTHAMERICA_ORIGINAL
        return SA_remaining

    global E_remaining, EUROPE_ORIGINAL
    if len(E_remaining) < len(EUROPE_ORIGINAL):
        E_remaining = EUROPE_ORIGINAL
        return E_remaining

    global AS_remaining, ASIA_ORIGINAL
    if len(AS_remaining) < len(ASIA_ORIGINAL):
        AS_remaining = ASIA_ORIGINAL
        return AS_remaining

    global AF_remaining, AFRICA_ORIGINAL
    if len(AF_remaining) < len(AFRICA_ORIGINAL):
        AF_remaining = AFRICA_ORIGINAL
        return AF_remaining

    global AUS_remaining, AUSTRALIA_ORIGINAL
    if len(AUS_remaining) < len(AUSTRALIA_ORIGINAL):
        AUS_remaining = AUSTRALIA_ORIGINAL
        return AUS_remaining

    global all_remaining, ALL_ORIGINAL
    if len(all_remaining) < len(ALL_ORIGINAL):
        all_remaining = ALL_ORIGINAL
        return all_remaining


def get_guessed():
    print(guessed)
    return guessed


def reset_guessed_score():
    global guessed, score
    guessed = []
    score = 0
    return guessed, score
