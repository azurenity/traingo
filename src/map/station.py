from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Dict
import re

@dataclass(frozen=True)
class TravelInfo:
    destination: str       # Enum name of the destination station
    time: int              # Travel time in minutes

@dataclass(frozen=True)
class StationInfo:
    codes: List[str]       # One or more station codes, e.g. ["EW2", "DT32"]
    name: str
    travel: List[TravelInfo]

class Station(Enum):

    JURONG_EAST = StationInfo(
        codes=["NS1", "EW24"],
        name="Jurong East",
        travel=[
            TravelInfo("BUKIT_BATOK", 2), 
            TravelInfo("CLEMENTI", 2), 
            TravelInfo("CHINESE_GARDEN", 2)  
        ]
    )

    BUKIT_BATOK = StationInfo(
        codes=["NS2"],
        name="Bukit Batok",
        travel=[
            TravelInfo("JURONG_EAST", 2),
            TravelInfo("BUKIT_GOMBAK", 2)
        ]
    )

    BUKIT_GOMBAK = StationInfo(
        codes=["NS3"],
        name="Bukit Gombak",
        travel=[
            TravelInfo("BUKIT_BATOK", 2),
            TravelInfo("CHOA_CHU_KANG", 2)
        ]
    )

    CHOA_CHU_KANG = StationInfo(
        codes=["NS4"],
        name="Choa Chu Kang",
        travel=[
            TravelInfo("BUKIT_GOMBAK", 2),
            TravelInfo("YEW_TEE", 2), 
        ]
    )
    YEW_TEE = StationInfo(
        codes=["NS5"],
        name="Yew Tee",
        travel=[
            TravelInfo("CHOA_CHU_KANG", 2),
            TravelInfo("KRANJI", 2)
        ]
    )
    KRANJI = StationInfo(
        codes=["NS7"],
        name="Kranji",
        travel=[
            TravelInfo("YEW_TEE", 2),
            TravelInfo("MARSILING", 2)
        ]
    )
    MARSILING = StationInfo(
        codes=["NS8"],
        name="Marsiling",
        travel=[
            TravelInfo("KRANJI", 2),
            TravelInfo("WOODLANDS", 2)
        ]
    )

    WOODLANDS = StationInfo(
        codes=["NS9", "TE2"],
        name="Woodlands",
        travel=[
            TravelInfo("MARSILING", 2), 
            TravelInfo("ADMIRALTY", 2),
            TravelInfo("WOODLANDS_NORTH", 2), 
            TravelInfo("WOODLANDS_SOUTH", 2) 
        ]
    )
    ADMIRALTY = StationInfo(
        codes=["NS10"],
        name="Admiralty",
        travel=[
            TravelInfo("WOODLANDS", 2),
            TravelInfo("SEMBWANG", 2)
        ]
    )
    SEMBAWANG = StationInfo(
        codes=["NS11"],
        name="Sembawang",
        travel=[
            TravelInfo("ADMIRALTY", 2),
            TravelInfo("CANBERRA", 2)
        ]
    )
    CANBERRA = StationInfo(
        codes=["NS12"],
        name="Canberra",
        travel=[
            TravelInfo("SEMBWANG", 2),
            TravelInfo("YISHUN", 2)
        ]
    )
    YISHUN = StationInfo(
        codes=["NS13"],
        name="Yishun",
        travel=[
            TravelInfo("CANBERRA", 2),
            TravelInfo("KHATIB", 2)
        ]
    )
    KHATIB = StationInfo(
        codes=["NS14"],
        name="Khatib",
        travel=[
            TravelInfo("YISHUN", 2),
            TravelInfo("YIO_CHU_KANG", 2)
        ]
    )
    YIO_CHU_KANG = StationInfo(
        codes=["NS15"],
        name="Yio Chu Kang",
        travel=[
            TravelInfo("KHATIB", 2),
            TravelInfo("ANG_MO_KIO", 2)
        ]
    )
    ANG_MO_KIO = StationInfo(
        codes=["NS16"],
        name="Ang Mo Kio",
        travel=[
            TravelInfo("YIO_CHU_KANG", 2), 
            TravelInfo("BISHAN", 2),        
        ]
    )

    BISHAN = StationInfo(
        codes=["NS17", "CC15"],
        name="Bishan",
        travel=[
            TravelInfo("ANG_MO_KIO", 2), 
            TravelInfo("BRADDELL", 2),   
            TravelInfo("LORONG_CHUAN", 2),  
            TravelInfo("MARYMOUNT", 2)        
        ]
    )
    BRADDELL = StationInfo(
        codes=["NS18"],
        name="Braddell",
        travel=[
            TravelInfo("BISHAN", 2),
            TravelInfo("TOA_PAYOH", 2)
        ]
    )
    TOA_PAYOH = StationInfo(
        codes=["NS19"],
        name="Toa Payoh",
        travel=[
            TravelInfo("BRADDELL", 2),
            TravelInfo("NOVENA", 2)
        ]
    )
    NOVENA = StationInfo(
        codes=["NS20"],
        name="Novena",
        travel=[
            TravelInfo("TOA_PAYOH", 2),
            TravelInfo("NEWTON", 2)
        ]
    )

    NEWTON = StationInfo(
        codes=["NS21", "DT11"],
        name="Newton",
        travel=[
            TravelInfo("NOVENA", 2), 
            TravelInfo("ORCHARD", 2), 
            TravelInfo("STEVENS", 2),
            TravelInfo("LITTLE_INDIA", 2) 
        ]
    )

    ORCHARD = StationInfo(
        codes=["NS22", "TE14"],
        name="Orchard",
        travel=[
            TravelInfo("NEWTON", 2), 
            TravelInfo("SOMERSET", 2), 
            TravelInfo("ORCHARD_BOULEVARD", 2),
            TravelInfo("GREAT_WORLD", 2)   
        ]
    )

    SOMERSET = StationInfo(
        codes=["NS23"],
        name="Somerset",
        travel=[
            TravelInfo("ORCHARD", 2),
            TravelInfo("DHOBY_GHAUT", 2)
        ]
    )

    DHOBY_GHAUT = StationInfo(
        codes=["NS24", "NE6", "CC1"],
        name="Dhoby Ghaut",
        travel=[
            TravelInfo("SOMERSET", 2),   
            TravelInfo("CITY_HALL", 2),     
            TravelInfo("CLARKE_QUAY", 2),   
            TravelInfo("LITTLE_INDIA", 2),   
            TravelInfo("BRAS_BASAH", 2)       
        ]
    )

    CITY_HALL = StationInfo(
        codes=["NS25", "EW13"],
        name="City Hall",
        travel=[
            TravelInfo("DHOBY_GHAUT", 2), 
            TravelInfo("RAFFLES_PLACE", 2), 
            TravelInfo("BUGIS", 2),
            TravelInfo("RAFFLES_PLACE", 2)   
        ]
    )

    RAFFLES_PLACE = StationInfo(
        codes=["NS26", "EW14"],
        name="Raffles Place",
        travel=[
            TravelInfo("CITY_HALL", 2), 
            TravelInfo("MARINA_BAY", 2), 
            TravelInfo("CITY_HALL", 2),  
            TravelInfo("TANJONG_PAGAR", 2)   
        ]
    )

    MARINA_BAY = StationInfo(
        codes=["NS27", "CE2", "TE20"],
        name="Marina Bay",
        travel=[
            TravelInfo("RAFFLES_PLACE", 2),
            TravelInfo("MARINA_SOUTH_PIER", 2),
            TravelInfo("BAYFRONT", 2), 
            TravelInfo("SHENTON_WAY", 2), 
            TravelInfo("GARDENS_BY_THE_BAY", 2)
        ]
    )

    MARINA_SOUTH_PIER = StationInfo(
        codes=["NS28"],
        name="Marina South Pier",
        travel=[
            TravelInfo("MARINA_BAY", 2)
        ]
    )

    PASIR_RIS = StationInfo(codes=["EW1"], name="Pasir Ris", travel=[TravelInfo("TAMPINES", 2)])
    TAMPINES = StationInfo(codes=["EW2", "DT32"], name="Tampines", travel=[
        TravelInfo("PASIR_RIS", 2),
        TravelInfo("SIMEI", 2)
    ])
    SIMEI = StationInfo(codes=["EW3"], name="Simei", travel=[
        TravelInfo("TAMPINES", 2),
        TravelInfo("TANAH_MERAH", 2)
    ])
    TANAH_MERAH = StationInfo(codes=["EW4", "CG"], name="Tanah Merah", travel=[
        TravelInfo("SIMEI", 2),
        TravelInfo("BEDOK", 2),
        TravelInfo("EXPO", 3)
    ])
    BEDOK = StationInfo(codes=["EW5"], name="Bedok", travel=[
        TravelInfo("TANAH_MERAH", 2),
        TravelInfo("KEMBANGAN", 2)
    ])
    KEMBANGAN = StationInfo(codes=["EW6"], name="Kembangan", travel=[
        TravelInfo("BEDOK", 2),
        TravelInfo("EUNOS", 2)
    ])
    EUNOS = StationInfo(codes=["EW7"], name="Eunos", travel=[
        TravelInfo("KEMBANGAN", 2),
        TravelInfo("PAYA_LEBAR", 2)
    ])
    PAYA_LEBAR = StationInfo(codes=["EW8", "CC9"], name="Paya Lebar", travel=[
        TravelInfo("EUNOS", 2),
        TravelInfo("ALJUNIED", 2),
        TravelInfo("DAKOTA", 2),
        TravelInfo("MACPHERSON", 2)
    ])
    ALJUNIED = StationInfo(codes=["EW9"], name="Aljunied", travel=[
        TravelInfo("PAYA_LEBAR", 2),
        TravelInfo("KALLANG", 2)
    ])
    KALLANG = StationInfo(codes=["EW10"], name="Kallang", travel=[
        TravelInfo("ALJUNIED", 2),
        TravelInfo("LAVENDER", 2)
    ])
    LAVENDER = StationInfo(codes=["EW11"], name="Lavender", travel=[
        TravelInfo("KALLANG", 2),
        TravelInfo("BUGIS", 2)
    ])
    BUGIS = StationInfo(codes=["EW12", "DT14"], name="Bugis", travel=[
        TravelInfo("LAVENDER", 2),
        TravelInfo("CITY_HALL", 2),
        TravelInfo("ROCHOR", 2),
        TravelInfo("PROMENADE", 2)
    ])

    TANJONG_PAGAR = StationInfo(codes=["EW15"], name="Tanjong Pagar", travel=[
        TravelInfo("RAFFLES_PLACE", 2),
        TravelInfo("OUTRAM_PARK", 2)
    ])
    OUTRAM_PARK = StationInfo(codes=["EW16", "NE3", "TE17"], name="Outram Park", travel=[
        TravelInfo("TANJONG_PAGAR", 2),
        TravelInfo("TIONG_BAHRU", 2),
        TravelInfo("HARBOURFRONT", 4),
        TravelInfo("CHINATOWN", 2),
        TravelInfo("MAXWELL", 2),
        TravelInfo("HAVELOCK", 2)
    ])
    TIONG_BAHRU = StationInfo(codes=["EW17"], name="Tiong Bahru", travel=[
        TravelInfo("OUTRAM_PARK", 2),
        TravelInfo("REDHILL", 2)
    ])
    REDHILL = StationInfo(codes=["EW18"], name="Redhill", travel=[
        TravelInfo("TIONG_BAHRU", 2),
        TravelInfo("QUEENSWAY", 2)
    ])
    QUEENSWAY = StationInfo(codes=["EW19"], name="Queenstown", travel=[
        TravelInfo("REDHILL", 2),
        TravelInfo("COMMONWEALTH", 2)
    ])
    COMMONWEALTH = StationInfo(codes=["EW20"], name="Commonwealth", travel=[
        TravelInfo("QUEENSWAY", 2),
        TravelInfo("BUONA_VISTA", 2)
    ])
    BUONA_VISTA = StationInfo(codes=["EW21", "CC22"], name="Buona Vista", travel=[
        TravelInfo("COMMONWEALTH", 2),
        TravelInfo("DOVER", 2),
        TravelInfo("ONE_NORTH", 2),
        TravelInfo("HOLLAND_VILLAGE", 2)
    ])
    DOVER = StationInfo(codes=["EW22"], name="Dover", travel=[
        TravelInfo("BUONA_VISTA", 2),
        TravelInfo("CLEMENTI", 2)
    ])
    CLEMENTI = StationInfo(codes=["EW23"], name="Clementi", travel=[
        TravelInfo("DOVER", 2),
        TravelInfo("JURONG_EAST", 2)
    ])
    CHINESE_GARDEN = StationInfo(codes=["EW25"], name="Chinese Garden", travel=[
        TravelInfo("JURONG_EAST", 2),
        TravelInfo("LAKESIDE", 2)
    ])
    LAKESIDE = StationInfo(codes=["EW26"], name="Lakeside", travel=[
        TravelInfo("CHINESE_GARDEN", 2),
        TravelInfo("BOON_LAY", 2)
    ])
    BOON_LAY = StationInfo(codes=["EW27"], name="Boon Lay", travel=[
        TravelInfo("LAKESIDE", 2),
        TravelInfo("PIONEER", 2)
    ])
    PIONEER = StationInfo(codes=["EW28"], name="Pioneer", travel=[
        TravelInfo("BOON_LAY", 2),
        TravelInfo("JOO_KOON", 2)
    ])
    JOO_KOON = StationInfo(codes=["EW29"], name="Joo Koon", travel=[
        TravelInfo("PIONEER", 2),
        TravelInfo("GUL_CIRCLE", 2)
    ])
    GUL_CIRCLE = StationInfo(codes=["EW30"], name="Gul Circle", travel=[
        TravelInfo("JOO_KOON", 2),
        TravelInfo("TUAS_CRESCENT", 2)
    ])
    TUAS_CRESCENT = StationInfo(codes=["EW31"], name="Tuas Crescent", travel=[
        TravelInfo("GUL_CIRCLE", 2),
        TravelInfo("TUAS_WEST_ROAD", 2)
    ])
    TUAS_WEST_ROAD = StationInfo(codes=["EW32"], name="Tuas West Road", travel=[
        TravelInfo("TUAS_CRESCENT", 2),
        TravelInfo("TUAS_LINK", 2)
    ])
    TUAS_LINK = StationInfo(codes=["EW33"], name="Tuas Link", travel=[
        TravelInfo("TUAS_WEST_ROAD", 2)
    ])
 
    HARBOURFRONT = StationInfo(
        codes=["NE1", "CC29"],
        name="HarbourFront",
        travel=[
            TravelInfo("OUTRAM_PARK", 4),
            TravelInfo("TELOK_BLANGAH", 2)
        ]
    )
    CLARKE_QUAY = StationInfo(
        codes=["NE5"],
        name="Clarke Quay",
        travel=[TravelInfo("CHINATOWN", 2), TravelInfo("DHOBY GHAUT", 2)]
    )

    FARRER_PARK = StationInfo(
        codes=["NE8"],
        name="Farrer Park",
        travel=[TravelInfo("LITTLE_INDIA", 2), TravelInfo("BOON_KENG", 2)]
    )
    BOON_KENG = StationInfo(
        codes=["NE9"],
        name="Boon Keng",
        travel=[TravelInfo("FARRER_PARK", 2), TravelInfo("POTONG_PASIR", 2)]
    )
    POTONG_PASIR = StationInfo(
        codes=["NE10"],
        name="Potong Pasir",
        travel=[TravelInfo("BOON_KENG", 2), TravelInfo("WOODLEIGH", 2)]
    )
    WOODLEIGH = StationInfo(
        codes=["NE11"],
        name="Woodleigh",
        travel=[TravelInfo("POTONG_PASIR", 2), TravelInfo("SERANGOON", 2)]
    )
    SERANGOON = StationInfo(
        codes=["NE12", "CC13"],
        name="Serangoon",
        travel=[TravelInfo("WOODLEIGH", 2), TravelInfo("KOVAN", 2)]
    )
    KOVAN = StationInfo(
        codes=["NE13"],
        name="Kovan",
        travel=[TravelInfo("SERANGOON", 2), TravelInfo("HOUGANG", 2)]
    )
    HOUGANG = StationInfo(
        codes=["NE14"],
        name="Hougang",
        travel=[TravelInfo("KOVAN", 2), TravelInfo("BUANGKOK", 2)]
    )
    BUANGKOK = StationInfo(
        codes=["NE15"],
        name="Buangkok",
        travel=[TravelInfo("HOUGANG", 2), TravelInfo("SENGKANG", 2)]
    )
    SENGKANG = StationInfo(
        codes=["NE16"],
        name="Sengkang",
        travel=[TravelInfo("BUANGKOK", 2), TravelInfo("PUNGGOL", 2)]
    )
    PUNGGOL = StationInfo(
        codes=["NE17"],
        name="Punggol",
        travel=[TravelInfo("SENGKANG", 2), TravelInfo("PUNGGOL_COAST", 2)]
    )
    PUNGGOL_COAST = StationInfo(
        codes=["NE18"],
        name="Punggol Coast",
        travel=[TravelInfo("PUNGGOL", 2)]
    )

    BRAS_BASAH = StationInfo(
        codes=["CC2"],
        name="Bras Basah",
        travel=[
            TravelInfo("DHOBY_GHAUT", 2),
            TravelInfo("ESPLANADE", 2)
        ]
    )
    ESPLANADE = StationInfo(
        codes=["CC3"],
        name="Esplanade",
        travel=[
            TravelInfo("BRAS_BASAH", 2),
            TravelInfo("PROMENADE", 2)
        ]
    )
    PROMENADE = StationInfo(
        codes=["CC4", "DT15"],
        name="Promenade",
        travel=[
            TravelInfo("BUGIS", 2),
            TravelInfo("BAYFRONT", 2),
            TravelInfo("ESPLANADE", 2),
            TravelInfo("BAYFRONT", 2),
            TravelInfo("NICOLL_HIGHWAY", 2),
        ]
    )
    NICOLL_HIGHWAY = StationInfo(
        codes=["CC5"],
        name="Nicoll Highway",
        travel=[
            TravelInfo("PROMENADE", 2),
            TravelInfo("STADIUM", 2)
        ]
    )
    STADIUM = StationInfo(
        codes=["CC6"],
        name="Stadium",
        travel=[
            TravelInfo("NICOLL_HIGHWAY", 2),
            TravelInfo("MOUNTBATTEN", 2)
        ]
    )
    MOUNTBATTEN = StationInfo(
        codes=["CC7"],
        name="Mountbatten",
        travel=[
            TravelInfo("STADIUM", 2),
            TravelInfo("DAKOTA", 2)
        ]
    )
    DAKOTA = StationInfo(
        codes=["CC8"],
        name="Dakota",
        travel=[
            TravelInfo("MOUNTBATTEN", 2),
            TravelInfo("PAYA_LEBAR", 2)
        ]
    )
    MACPHERSON = StationInfo(
        codes=["CC10", "DT26"],
        name="MacPherson",
        travel=[
            TravelInfo("MATTAR", 2),
            TravelInfo("UBI", 2),
            TravelInfo("PAYA_LEBAR", 2),
            TravelInfo("TAI_SENG", 3)
        ]
    )
    TAI_SENG = StationInfo(
        codes=["CC11"],
        name="Tai Seng",
        travel=[
            TravelInfo("MACPHERSON", 2),
            TravelInfo("BARTLEY", 2)
        ]
    )
    BARTLEY = StationInfo(
        codes=["CC12"],
        name="Bartley",
        travel=[
            TravelInfo("TAI_SENG", 2),
            TravelInfo("SERANGOON", 2)
        ]
    )
    LORONG_CHUAN = StationInfo(
        codes=["CC14"],
        name="Lorong Chuan",
        travel=[
            TravelInfo("SERANGOON", 2),
            TravelInfo("BISHAN", 2)
        ]
    )
    MARYMOUNT = StationInfo(
        codes=["CC16"],
        name="Marymount",
        travel=[
            TravelInfo("BISHAN", 2),
            TravelInfo("CALDECOTT", 2)
        ]
    )
    CALDECOTT = StationInfo(
        codes=["CC17", "TE9"],
        name="Caldecott",
        travel=[
            TravelInfo("MARYMOUNT", 2),
            TravelInfo("BOTANIC_GARDENS", 2),
            TravelInfo("UPPER_THOMSON", 2), 
            TravelInfo("STEVENS", 2)
        ]
    )
    BOTANIC_GARDENS = StationInfo(
        codes=["CC19", "DT9"],
        name="Botanic Gardens",
        travel=[
            TravelInfo("TAN_KAH_KEE", 2),
            TravelInfo("STEVENS", 2),
            TravelInfo("CALDECOTT", 2),   
            TravelInfo("FARRER_ROAD", 2)  
        ]
    )
    FARRER_ROAD = StationInfo(
        codes=["CC20"],
        name="Farrer Road",
        travel=[
            TravelInfo("BOTANIC_GARDENS", 2),
            TravelInfo("HOLLAND_VILLAGE", 2)
        ]
    )
    HOLLAND_VILLAGE = StationInfo(
        codes=["CC21"],
        name="Holland Village",
        travel=[
            TravelInfo("FARRER_ROAD", 2),
            TravelInfo("BUONA_VISTA", 2)
        ]
    )
    ONE_NORTH = StationInfo(
        codes=["CC23"],
        name="one-north",
        travel=[
            TravelInfo("BUONA_VISTA", 2),
            TravelInfo("KENT_RIDGE", 2)
        ]
    )
    KENT_RIDGE = StationInfo(
        codes=["CC24"],
        name="Kent Ridge",
        travel=[
            TravelInfo("ONE_NORTH", 2),
            TravelInfo("HAW_PAR_VILLA", 2)
        ]
    )
    HAW_PAR_VILLA = StationInfo(
        codes=["CC25"],
        name="Haw Par Villa",
        travel=[
            TravelInfo("KENT_RIDGE", 2),
            TravelInfo("PASIR_PANJANG", 2)
        ]
    )
    PASIR_PANJANG = StationInfo(
        codes=["CC26"],
        name="Pasir Panjang",
        travel=[
            TravelInfo("HAW_PAR_VILLA", 2),
            TravelInfo("LABRADOR_PARK", 2)
        ]
    )
    LABRADOR_PARK = StationInfo(
        codes=["CC27"],
        name="Labrador Park",
        travel=[
            TravelInfo("PASIR_PANJANG", 2),
            TravelInfo("TELOK_BLANGAH", 2)
        ]
    )
    TELOK_BLANGAH = StationInfo(
        codes=["CC28"],
        name="Telok Blangah",
        travel=[
            TravelInfo("LABRADOR_PARK", 2),
            TravelInfo("HARBOURFRONT", 2)
        ]
    )

    BUKIT_PANJANG = StationInfo(
        codes=["DT1"],
        name="Bukit Panjang",
        travel=[TravelInfo("CASHEW", 2)]
    )
    CASHEW = StationInfo(
        codes=["DT2"],
        name="Cashew",
        travel=[TravelInfo("BUKIT_PANJANG", 2), TravelInfo("HILLVIEW", 2)]
    )
    HILLVIEW = StationInfo(
        codes=["DT3"],
        name="Hillview",
        travel=[TravelInfo("CASHEW", 2), TravelInfo("HUME", 2)]
    )
    HUME = StationInfo(
        codes=["DT4"],
        name="Hume",
        travel=[TravelInfo("HILLVIEW", 2), TravelInfo("BEAUTY_WORLD", 2)]
    )
    BEAUTY_WORLD = StationInfo(
        codes=["DT5"],
        name="Beauty World",
        travel=[TravelInfo("HUME", 2), TravelInfo("KING_ALBERT_PARK", 2)]
    )
    KING_ALBERT_PARK = StationInfo(
        codes=["DT6"],
        name="King Albert Park",
        travel=[TravelInfo("BEAUTY_WORLD", 2), TravelInfo("SIXTH_AVENUE", 2)]
    )
    SIXTH_AVENUE = StationInfo(
        codes=["DT7"],
        name="Sixth Avenue",
        travel=[TravelInfo("KING_ALBERT_PARK", 2), TravelInfo("TAN_KAH_KEE", 2)]
    )
    TAN_KAH_KEE = StationInfo(
        codes=["DT8"],
        name="Tan Kah Kee",
        travel=[TravelInfo("SIXTH_AVENUE", 2), TravelInfo("BOTANIC_GARDENS", 2)]
    )

    STEVENS = StationInfo(
        codes=["DT10", "TE11"],
        name="Stevens",
        travel=[
            TravelInfo("BOTANIC_GARDENS", 2),
            TravelInfo("NEWTON", 2),
            TravelInfo("CALDECOTT", 2), 
            TravelInfo("NAPIER", 2)        
        ]
    )

    LITTLE_INDIA = StationInfo(
        codes=["DT12", "NE7"],
        name="Little India",
        travel=[
            TravelInfo("NEWTON", 2),
            TravelInfo("ROCHOR", 2),
            TravelInfo("FARRER_PARK", 2), 
            TravelInfo("DHOBY GHAUT", 2)
        ]
    )
    ROCHOR = StationInfo(
        codes=["DT13"],
        name="Rochor",
        travel=[TravelInfo("LITTLE_INDIA", 2), TravelInfo("BUGIS", 2)]
    )

    BAYFRONT = StationInfo(
        codes=["DT16", "CE1"],
        name="Bayfront",
        travel=[
            TravelInfo("PROMENADE", 2),
            TravelInfo("DOWNTOWN", 2),
            TravelInfo("MARINA_BAY", 4), 
            TravelInfo("PROMENADE", 4)
        ]
    )
    DOWNTOWN = StationInfo(
        codes=["DT17"],
        name="Downtown",
        travel=[TravelInfo("BAYFRONT", 2), TravelInfo("TELOK_AYER", 2)]
    )
    TELOK_AYER = StationInfo(
        codes=["DT18"],
        name="Telok Ayer",
        travel=[TravelInfo("DOWNTOWN", 2), TravelInfo("CHINATOWN", 1)]
    )
    CHINATOWN = StationInfo(
        codes=["DT19", "NE4"],
        name="Chinatown",
        travel=[
            TravelInfo("TELOK_AYER", 2),
            TravelInfo("FORT_CANNING", 2),
            TravelInfo("OUTRAM_PARK", 2),
            TravelInfo("CLARKE_QUAY", 2)
        ]
    )
    FORT_CANNING = StationInfo(
        codes=["DT20"],
        name="Fort Canning",
        travel=[TravelInfo("CHINATOWN", 2), TravelInfo("BENCOOLEN", 2)]
    )
    BENCOOLEN = StationInfo(
        codes=["DT21"],
        name="BENCOOLEN",
        travel=[TravelInfo("FORT_CANNING", 2), TravelInfo("JALAN_BESAR", 2)]
    )
    JALAN_BESAR = StationInfo(
        codes=["DT22"],
        name="Jalan Besar",
        travel=[TravelInfo("BENCOOLEN", 2), TravelInfo("BENDEMEER", 2)]
    )
    BENDEMEER = StationInfo(
        codes=["DT23"],
        name="Bendemeer",
        travel=[TravelInfo("JALAN_BESAR", 2), TravelInfo("GEYLANG_BAHRU", 2)]
    )
    GEYLANG_BAHRU = StationInfo(
        codes=["DT24"],
        name="Geylang Bahru",
        travel=[TravelInfo("BENDEMEER", 2), TravelInfo("MATTAR", 2)]
    )
    MATTAR = StationInfo(
        codes=["DT25"],
        name="Mattar",
        travel=[TravelInfo("GEYLANG_BAHRU", 2), TravelInfo("MACPHERSON", 2)]
    )
    UBI = StationInfo(
        codes=["DT27"],
        name="Ubi",
        travel=[TravelInfo("MACPHERSON", 2), TravelInfo("KAKI_BUKIT", 2)]
    )
    KAKI_BUKIT = StationInfo(
        codes=["DT28"],
        name="Kaki Bukit",
        travel=[TravelInfo("UBI", 2), TravelInfo("BEDOK_NORTH", 2)]
    )
    BEDOK_NORTH = StationInfo(
        codes=["DT29"],
        name="Bedok North",
        travel=[TravelInfo("KAKI_BUKIT", 2), TravelInfo("BEDOK_RESERVOIR", 2)]
    )
    BEDOK_RESERVOIR = StationInfo(
        codes=["DT30"],
        name="Bedok Reservoir",
        travel=[TravelInfo("BEDOK_NORTH", 2), TravelInfo("TAMPINES_WEST", 2)]
    )
    TAMPINES_WEST = StationInfo(
        codes=["DT31"],
        name="Tampines West",
        travel=[TravelInfo("BEDOK_RESERVOIR", 2), TravelInfo("TAMPINES", 2)]
    )
    TAMPINES_EAST = StationInfo(
        codes=["DT33"],
        name="Tampines East",
        travel=[TravelInfo("TAMPINES", 2), TravelInfo("UPPER_CHANGI", 2)]
    )
    UPPER_CHANGI = StationInfo(
        codes=["DT34"],
        name="Upper Changi",
        travel=[TravelInfo("TAMPINES_EAST", 2), TravelInfo("EXPO", 2)]
    )
    EXPO = StationInfo(
        codes=["DT35", "CG1"],
        name="Expo",
        travel=[
            TravelInfo("UPPER_CHANGI", 2),
            TravelInfo("CHANGI_AIRPORT", 5) 
        ]
    )
    CHANGI_AIRPORT = StationInfo(
        codes=["CG2"],
        name="Changi Airport",
        travel=[
            TravelInfo("EXPO", 5) 
        ]
    )

    WOODLANDS_NORTH = StationInfo(
        codes=["TE1"],
        name="Woodlands North",
        travel=[TravelInfo("WOODLANDS", 2)]
    )
    WOODLANDS_SOUTH = StationInfo(
        codes=["TE3"],
        name="Woodlands South",
        travel=[TravelInfo("WOODLANDS", 2), TravelInfo("SPRINGLEAF", 2)]
    )
    SPRINGLEAF = StationInfo(
        codes=["TE4"],
        name="Springleaf",
        travel=[TravelInfo("WOODLANDS_SOUTH", 2), TravelInfo("LENTOR", 2)]
    )
    LENTOR = StationInfo(
        codes=["TE5"],
        name="Lentor",
        travel=[TravelInfo("SPRINGLEAF", 2), TravelInfo("MAYFLOWER", 2)]
    )
    MAYFLOWER = StationInfo(
        codes=["TE6"],
        name="Mayflower",
        travel=[TravelInfo("LENTOR", 2), TravelInfo("BRIGHT_HILL", 2)]
    )
    BRIGHT_HILL = StationInfo(
        codes=["TE7"],
        name="Bright Hill",
        travel=[TravelInfo("MAYFLOWER", 2), TravelInfo("UPPER_THOMSON", 2)]
    )
    UPPER_THOMSON = StationInfo(
        codes=["TE8"],
        name="Upper Thomson",
        travel=[TravelInfo("BRIGHT_HILL", 2), TravelInfo("CALDECOTT", 2)]
    )
    NAPIER = StationInfo(
        codes=["TE12"],
        name="Napier",
        travel=[TravelInfo("STEVENS", 2), TravelInfo("ORCHARD_BOULEVARD", 2)]
    )
    ORCHARD_BOULEVARD = StationInfo(
        codes=["TE13"],
        name="Orchard Boulevard",
        travel=[TravelInfo("NAPIER", 2), TravelInfo("ORCHARD", 2)]
    )
    GREAT_WORLD = StationInfo(
        codes=["TE15"],
        name="Great World",
        travel=[TravelInfo("ORCHARD", 2), TravelInfo("HAVELOCK", 2)]
    )
    HAVELOCK = StationInfo(
        codes=["TE16"],
        name="Havelock",
        travel=[TravelInfo("GREAT_WORLD", 2), TravelInfo("OUTRAM_PARK", 2)]
    )
    MAXWELL = StationInfo(
        codes=["TE18"],
        name="Maxwell",
        travel=[TravelInfo("OUTRAM_PARK", 2), TravelInfo("SHENTON_WAY", 2)]
    )
    SHENTON_WAY = StationInfo(
        codes=["TE19"],
        name="Shenton Way",
        travel=[TravelInfo("MAXWELL", 2), TravelInfo("MARINA_BAY", 2)]
    )
    GARDENS_BY_THE_BAY = StationInfo(
        codes=["TE22"],
        name="Gardens by the Bay",
        travel=[TravelInfo("MARINA_BAY", 2), TravelInfo("TANJONG_RHU", 2)]
    )
    TANJONG_RHU = StationInfo(
        codes=["TE23"],
        name="Tanjong Rhu",
        travel=[TravelInfo("GARDENS_BY_THE_BAY", 2), TravelInfo("KATONG_PARK", 2)]
    )
    KATONG_PARK = StationInfo(
        codes=["TE24"],
        name="Katong Park",
        travel=[TravelInfo("TANJONG_RHU", 2), TravelInfo("TANJONG_KATONG", 2)]
    )
    TANJONG_KATONG = StationInfo(
        codes=["TE25"],
        name="Tanjong Katong",
        travel=[TravelInfo("KATONG_PARK", 2), TravelInfo("MARINE_PARADE", 2)]
    )
    MARINE_PARADE = StationInfo(
        codes=["TE26"],
        name="Marine Parade",
        travel=[TravelInfo("TANJONG_KATONG", 2), TravelInfo("MARINE_TERRACE", 2)]
    )
    MARINE_TERRACE = StationInfo(
        codes=["TE27"],
        name="Marine Terrace",
        travel=[TravelInfo("MARINE_PARADE", 2), TravelInfo("SIGLAP", 2)]
    )
    SIGLAP = StationInfo(
        codes=["TE28"],
        name="Siglap",
        travel=[TravelInfo("MARINE_TERRACE", 2), TravelInfo("BAYSHORE", 2)]
    )
    BAYSHORE = StationInfo(
        codes=["TE29"],
        name="Bayshore",
        travel=[TravelInfo("SIGLAP", 2)]
    )
   
# Access station name
print(Station.PASIR_RIS.value.name)  # Output: Pasir Ris

# Access code
print(Station.PASIR_RIS.value.codes)  # Output: EW1

# Print travel destinations and times
for travel in Station.PASIR_RIS.value.travel:
    print(f"To {Station[travel.destination].value.name} in {travel.time} mins")





# To start instantiating things:
    # for each trainline:
    #     Initialize graph from TR1 to TR x 


# Helper functions

def get_station_name_by_code(code):
    """
    Return the station name corresponding to a given station code.
    If not found, returns None.
    """
    for station in Station:
        if code in station.value.codes:
            return station.value.name
    return None


def get_codes_by_station_name(name):
    """
    Return the list of codes corresponding to a given station name.
    If not found, returns None.
    """
    for station in Station:
        if station.value.name.lower() == name.lower():
            return station.value.codes
    return None
    
# Example usage
if __name__ == "__main__":
    print(get_station_name_by_code("DT32"))  # input: any station code / Output: station name
    print(get_codes_by_station_name("changi airport"))  # User input: any station name / Output: station code

def build_adjacency_dict():
    graph = {}
    for station in Station:
        src = station.name
        # Ensure every station appears in the graph
        graph.setdefault(src, set()) # adds an empty set if it is not inside the dict 
        for travel in station.value.travel:
            dst, t = travel.destination, travel.time
            # Add neighbor for src
            graph[src].add((dst, t))
            # Add reverse neighbor for dst
            graph.setdefault(dst, set()) 
            graph[dst].add((src, t))
    # Convert sets back to lists if needed
    for station in graph:
        graph[station] = list(graph[station])
    return graph

if __name__ == "__main__":
    adj_dict = build_adjacency_dict()
    # Example: see all neighbours of CASHEW
    print("Neighbours of BUKIT_GOMBAK:", adj_dict["BUKIT_GOMBAK"])