from re import sub
from datetime import date
from random import choice as choose, randint
from countries import countries, country_alt_names
from importlib import import_module as import_this
from area_codes import world_area_codes, us_area_codes
from country_codes import iso_codes, iso_codes_reversed, country_codes


class Person:

    def __init__(self, country=None, sex=None, age:'range'=(18, 80)):
                 self.sex = sex
                 self.age = age
                 self.country = country
                 self.generate_identity()


    ############################################
    # dunders
    ############################################


    def __str__(self):
        return self.full_name


    ############################################
    # properties
    ############################################


    @property
    def identity(self):
        '''compiled identity information'''
        return f'NAME: {self.full_name}\n' \
               f'SEX: {self.sex}\nDOB: {self.dob} ' \
               f'AGE: {self.age}\nBIRTHPLACE: {self.birthplace}\n' \
               f'EMAIL: {self.email}\nPHONE: {self.phone_number}'

    @property
    def full_name(self):
        '''first last'''
        return f'{self.first_name} {self.last_name}'

    @property
    def birthplace(self):
        '''city[, state], country[, zip]'''
        if self.state:
            return f'{self.city}, {self.state}, {self.country}, {self.zip_code}'
        else:
            return f'{self.city}, {self.country}'


    ############################################
    # generators
    ############################################


    def generate_name(self):
        '''generate full name based on country and sex'''
        names_list = import_this('names.' + self.country.replace(' ', '_'))
        if self.sex == 'male':
            first_name = choose(names_list.male).lower()
        else:
            first_name = choose(names_list.female).lower()
        last_name = choose(names_list.last).lower()
        return first_name, last_name

    def generate_dob(self):
        '''generate age and d.o.b.'''
        days_in_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        if self.age[0] < 1 or self.age[1] < 1 or type(sum(self.age)) == float:
            raise ValueError('invalid age range')
        age = randint(self.age[0], self.age[1])
        month = randint(1, 12)
        day = randint(1, days_in_month[month])
        year = date.today().year - age
        return age, f'{day}-{month}-{year}'

    def generate_birthplace(self):
        '''generate a place of birth'''
        country_data = import_this('cities.' + self.country.replace(' ', '_'))
        if self.country == 'united states':
            state = choose(country_data.states).lower()
            zip = str(self.generate_zip(country_data.zip_codes[state])).zfill(5)
            cities_list = import_this('cities.us.' + state.replace(' ', '_'))
            city = choose(cities_list.cities).lower()
            return city, state, zip
        else:
            return choose(country_data.cities).lower(), None, None

    def generate_email(self):
        '''generate a (phoney) email'''
        # TODO: expand this
        first = sub(r" |'|\-", '', self.first_name)
        last = sub(r" |'|\-", '', self.last_name)
        number = randint(1, 999)
        separator = choose(('-', '_', '.', ''))
        format = (f'{first}{separator}{last}{number}',
                  f'{first[0]}{separator}{last}{number}',
                  f'{first}{separator}{last[0]}{number}')
        return choose(format) + '@mentiormail.{}'.format(iso_codes_reversed[self.country])

    def generate_sex(self):
        '''generates a sex'''
        abbreviated = {'m': 'male', 'f': 'female'}
        if self.sex:
            sex = self.sex.lower()
            if sex in abbreviated:
                sex = abbreviated[sex]
            if sex != 'male' and sex != 'female':
                raise ValueError('invalid sex')
        else:
            sex = choose(('male', 'female'))
        return sex

    def generate_country(self):
        '''generate a country'''
        if self.country:
            country = self.correct(self.country.lower())
            if country not in countries:
                raise ValueError('country not implemented')
        else:
            country = choose(countries)
        return country

    def generate_phone(self):
        '''generate (phony) phone number'''
        if self.country == 'united states':
            return '1-{}-{}-{}'.format(choose(us_area_codes[self.state]),
                                       ''.join(str(randint(1, 9)) for _ in range(3)),
                                       ''.join(str(randint(1, 9)) for _ in range(4)))
        else:
            return '{}-{}-{}-{}'.format(country_codes[self.country],
                                        choose(world_area_codes[self.country]),
                                        ''.join(str(randint(1, 9)) for _ in range(3)),
                                        ''.join(str(randint(1, 9)) for _ in range(4))).replace('--', '-')

    def generate_zip(self, range):
        '''generate a zip code (for u.s. states)'''
        return randint(range[0], range[1])

    def generate_social(self):
        '''generate (phony) social security number (for u.s.)'''
        return '{}-{}-{}'.format(''.join(str(randint(1, 9)) for _ in range(3)),
                                 ''.join(str(randint(1, 9)) for _ in range(2)),
                                 ''.join(str(randint(1, 9)) for _ in range(4)))

    def generate_identity(self):
        '''generate an identity'''
        self.country = self.generate_country()
        self.sex = self.generate_sex()
        self.first_name, self.last_name = self.generate_name()
        self.age, self.dob = self.generate_dob()
        self.city, self.state, self.zip_code = self.generate_birthplace()
        self.email = self.generate_email()
        self.phone_number = self.generate_phone()
        if self.country == 'united states':
            self.social = self.generate_social()


    ############################################
    # misc
    ############################################


    def correct(self, country):
        '''correct country name if entered in an alternate or abbreviated form'''
        if country in country_alt_names:
            return country_alt_names[country]
        if country in iso_codes:
            return iso_codes[country]
        return country
