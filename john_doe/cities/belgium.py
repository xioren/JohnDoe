cities = [
    'Brussels',
    'Antwerpen',
    'Gent',
    'Charleroi',
    'Liege',
    'Brugge',
    'Namur',
    'Leuven',
    'Mons',
    'Deurne',
    'Aalst',
    'Mechelen',
    'La Louviere',
    'Kortrijk',
    'Hasselt',
    'Ostend',
    'Sint-Niklaas',
    'Tournai',
    'Genk',
    'Seraing',
    'Roeselare',
    'Verviers',
    'Mouscron',
    'Beveren',
    'Dendermonde',
    'Beringen',
    'Turnhout',
    'Dilbeek',
    'Heist-op-den-Berg',
    'Sint-Truiden',
    'Lokeren',
    "Braine-l'Alleud",
    'Brasschaat',
    'Vilvoorde',
    'Herstal',
    'Maasmechelen',
    'Waregem',
    'Chatelet',
    'Ieper',
    'Ninove',
    'Geel',
    'Halle',
    'Hoboken',
    'Knokke-Heist',
    'Schoten',
    'Grimbergen',
    'Lier',
    'Mol',
    'Wavre',
    'Binche',
    'Lommel',
    'Menen',
    'Tienen',
    'Evergem',
    'Heusden',
    'Wevelgem',
    'Geraardsbergen',
    'Sint-Pieters-Leeuw',
    'Helchteren',
    'Houthalen',
    'Tongeren',
    'Deinze',
    'Waterloo',
    'Bilzen',
    'Louvain-la-Neuve',
    'Courcelles',
    'Asse',
    'Zaventem',
    'Oudenaarde',
    'Aarschot',
    'Ans',
    'Ath',
    'Kapellen',
    'Izegem',
    'Arlon',
    'Temse',
    'Harelbeke',
    'Herentals',
    'Brecht',
    'Flemalle-Haute',
    'Soignies',
    'Lanaken',
    'Mortsel',
    'Zottegem',
    'Ronse',
    'Nivelles',
    'Andenne',
    'Maaseik',
    'Oupeye',
    'Overijse',
    'Zwevegem',
    'Beersel',
    'Wetteren',
    'Hamme',
    'Willebroek',
    'Saint-Nicolas',
    'Westerlo',
    'Diest',
    'Saint-Ghislain',
    'Manage',
    'Maldegem',
    'Fleurus',
    'Merelbeke',
    'Zedelgem',
    'Tubize',
    'Edegem',
    'Gembloux',
    'Rixensart',
    'Oostkamp',
    'Zemst',
    'Koksijde',
    'Chaudfontaine',
    'Nijlen',
    'Zoersel',
    'Tervuren',
    'Frameries',
    'Schilde',
    'Kontich',
    'Zele',
    'Braine-le-Comte',
    'Boussu',
    'Bornem',
    'Balen',
    'Huy',
    'Colfontaine',
    'Zonhoven',
    'Lochristi',
    'Poperinge',
    'Sint-Katelijne-Waver',
    'Tielt',
    'Herent',
    'Eeklo',
    'Torhout',
    'Aalter',
    'Hoogstraten',
    'Meise',
    'Quaregnon',
    'Zwijndrecht',
    'Morlanwelz-Mariemont',
    'Blankenberge',
    'Wuustwezel',
    'Eupen',
    'Sint-Genesius-Rode',
    'Middelkerke',
    'Kortenberg',
    'Kasterlee',
    'Diepenbeek',
    'Lessines',
    'Sint-Gillis-Waas',
    'Walcourt',
    'Kalmthout',
    'Ranst',
    'Lebbeke',
    'Wervik',
    'Stabroek',
    'Londerzeel',
    'Haaltert',
    'Vise',
    'Stekene',
    'Denderleeuw',
    'Dour',
    'Marche-en-Famenne',
    'Destelbergen',
    'Lede',
    'Essen',
    'Peruwelz',
    'Tessenderlo',
    'Herve',
    'Herzele',
    'Beerse',
    'Neerpelt',
    'Duffel',
    'Sint-Kruis',
    'Fleron',
    'Puurs',
    'Pont-a-Celles',
    'Boom',
    'Riemst',
    'Peer',
    'Diksmuide',
    'Lille',
    'Putte',
    'Soumagne',
    'Rotselaar',
    'Aubange',
    'Bredene',
    'Ciney',
    'Kruibeke',
    'Thuin',
    'Zulte',
    'Merchtem',
    'Ternat',
    'Rumst',
    'Beernem',
    'Landen',
    'Wemmel',
    'Bastogne',
    'Bree',
    'Chapelle-lez-Herlaimont',
    'Eghezee',
    'Genappe',
    'Bonheiden',
    'Aartselaar',
    'Leopoldsburg',
    'Hannut',
    'Anzegem',
    'Basse Lasne',
    'Berlare',
    'Waremme',
    'Tremelo',
    'Lummen',
    'Dison',
    'Ichtegem',
    'Lubbeek',
    'Ravels',
    'Haacht',
    'Couvin',
    'Buggenhout',
    'Esneux',
    'Assenede',
    'Herselt',
    'Jabbeke',
    'Beloeil',
    'Overpelt',
    'Amay',
    'Wezembeek-Oppem',
    'Oosterzele',
    'Sprimont',
    'Wanze',
    'Wingene',
    'Dinant',
    'Kraainem',
    'Blegny',
    'Kuurne',
    'Grez-Doiceau',
    'Keerbergen',
    'Oud-Turnhout',
    'Bocholt',
    'Zandhoven',
    'Machelen',
    'Arendonk',
    'Boechout',
    'Opwijk',
    'Mettet',
    'Veurne',
    'Liedekerke',
    'Rochefort',
    'Gerpinnes',
    'Kinrooi',
    'Kortemark',
    'Jodoigne',
    'Wommelgem',
    'Zelzate',
    'Gavere',
    'De Haan',
    'Beyne-Heusay',
    'Laarne',
    'Anderlues',
    'Bernissart',
    'Theux',
    'Zonnebeke',
    'Boortmeerbeek',
    'Herk-de-Stad',
    'Malmedy',
    'Farciennes',
    'Profondeville',
    'Enghien',
    'Deerlijk',
    'Virton',
    'Nevele',
    'Gistel',
    'Olen',
    'Seneffe',
    'Wichelen',
    'Meulebeke',
    'Chaumont-Gistoux',
    'Frasnes-lez-Buissenal',
    'Alken',
    'Damme',
    'Aiseau',
    'Nazareth',
    'Nieuwpoort',
    'Staden',
    'Kampenhout',
    'Spa',
    'Grobbendonk',
    'Florennes',
    'Moorslede',
    'Melle',
    'Aywaille',
    'Rijkevorsel',
    'Ingelmunster',
    'Steenokkerzeel',
    'Oud-Heverlee',
    'Waasmunster',
    'Berlaar',
    'Borsbeek',
    'Vosselaar',
    'Hoeilaart',
    'Durbuy',
    'La Calamine',
    'Retie',
    'Rebecq-Rognon',
    'De Pinte',
    'Borgloon',
    'Raeren',
    'Hooglede',
    "Ecaussinnes-d'Enghien",
    'De Panne',
    'Chimay',
    'Braine-le-Chateau',
    'Plombieres',
    'Villers-la-Ville',
    'Ottignies',
    'Pepinster',
    'Hemiksem',
    'Jurbise',
    'Opglabbeek',
    'Erquelinnes',
    'Court-Saint-Etienne',
    'Meerhout',
    'Estaimpuis',
    'Lovendegem',
    'Hoeselt',
    'Bertem',
    'Hulshout',
    'Begijnendijk',
    'Ardooie',
    'Sint-Lievens-Houtem',
    'Huldenberg',
    'Saint-Vith',
    'Avelgem',
    'Ledegem',
    'Holsbeek',
    'Fosses-la-Ville',
    'Welkenraedt',
    'Bierbeek',
    'Gooik',
    'Houthulst',
    'Wijnegem',
    'Kapelle-op-den-Bos',
    'Wielsbeke',
    'Sint-Martens-Lennik',
    'Oudenburg',
    'Dessel',
    'Niel',
    'Awans',
    'Halen',
    'Oostduinkerke',
    'Ledeberg',
    'Herenthout',
    'Juprelle',
    'Koekelare',
    'Sint-Martens-Latem',
    'Beauraing',
    'La Bruyere',
    'Kruishoutem',
    'Lichtervelde',
    'Yvoir',
    'Zomergem',
    'Bassenge',
    'Bertrix',
    'Philippeville',
    'Kortessem',
    'Dentergem',
    'Lint',
    'Hove',
    'Roeulx',
    'Merksplas',
    'Galmaarden',
    'Gingelom',
    'Zoutleeuw',
    'Knesselare',
    'Silly',
    'Waarschoot',
    'Habay-la-Vieille',
    'Boutersem',
    'Quevy-le-Petit',
    'Jalhay',
    'Schelle',
    'Sint-Amands',
    'Brunehault',
    'Estinnes-au-Val',
    'Trooz',
    'Antoing',
    'Oostrozebeke',
    'Floreffe',
    'Sombreffe',
    'La Hulpe',
    'Kortenaken',
    'Perwez',
    'Vielsalm',
    'As',
    'Vorselaar',
    'Messancy',
    'Anhee',
    'Oostmalle',
    'Zutendaal',
    'Wachtebeke',
    'Wellen'
]
