from enum import Enum
from dataclasses import dataclass
from typing import List
from src.map.error_codes import invalid_station_code, invalid_station_name

@dataclass(frozen=True)
class TravelInfo:
    destination: str       # Enum name of the destination station
    time: int              # Travel time in minutes

@dataclass(frozen=True)
class StationInfo:
    name: str
    travel: List[TravelInfo]

class Station(Enum):
    pass
class EWStation(Station):
    EW1 = StationInfo(name="Pasir Ris",
        travel=[TravelInfo("EW2", 3)]
    )

    EW2 = StationInfo(name="Tampines",
        travel=[TravelInfo("EW1", 3), TravelInfo("EW3", 2), TravelInfo("DT32", 6)]
    )

    EW3 = StationInfo(name="Simei",
        travel=[TravelInfo("EW2", 2), TravelInfo("EW4", 3)]
    )

    EW4 = StationInfo(name="Tanah Merah",
        travel=[
            TravelInfo("EW3", 3),
            TravelInfo("EW5", 3),
            TravelInfo("CG", 0)
        ]
    )

    EW5 = StationInfo(name="Bedok",
        travel=[TravelInfo("EW4", 3), TravelInfo("EW6", 2)]
    )

    EW6 = StationInfo(name="Kembangan",
        travel=[TravelInfo("EW5", 2), TravelInfo("EW7", 2)]
    )

    EW7 = StationInfo(name="Eunos",
        travel=[TravelInfo("EW6", 2), TravelInfo("EW8", 2)]
    )

    EW8 = StationInfo(name="Paya Lebar",
        travel=[TravelInfo("EW7", 2), TravelInfo("EW9", 2), TravelInfo("CC9", 3)]
    )

    EW9 = StationInfo(name="Aljunied",
        travel=[TravelInfo("EW8", 2), TravelInfo("EW10", 2)]
    )

    EW10 = StationInfo(name="Kallang",
        travel=[TravelInfo("EW9", 2), TravelInfo("EW11", 2)]
    )

    EW11 = StationInfo(name="Lavender",
        travel=[TravelInfo("EW10", 2), TravelInfo("EW12", 2)]
    )

    EW12 = StationInfo(name="Bugis",
        travel=[
            TravelInfo("EW11", 2),
            TravelInfo("EW13", 2),
            TravelInfo("DT14", 4)
        ]
    )

    EW13 = StationInfo(name="City Hall",
        travel=[
            TravelInfo("EW12", 2),
            TravelInfo("EW14", 2),
            TravelInfo("NS25", 1)
        ]
    )

    EW14 = StationInfo(name="Raffles Place",
        travel=[
            TravelInfo("EW13", 2),
            TravelInfo("EW15", 2),
            TravelInfo("NS26", 1)
        ]
    )

    EW15 = StationInfo(name="Tanjong Pagar",
        travel=[TravelInfo("EW14", 2), TravelInfo("EW16", 2)]
    )

    EW16 = StationInfo(name="Outram Park",
        travel=[
            TravelInfo("EW15", 2),
            TravelInfo("EW17", 2),
            TravelInfo("TE17", 2),
            TravelInfo("NE3", 4)
        ]
    )

    EW17 = StationInfo(name="Tiong Bahru",
        travel=[TravelInfo("EW16", 2), TravelInfo("EW18", 2)]
    )

    EW18 = StationInfo(name="Redhill",
        travel=[TravelInfo("EW17", 2), TravelInfo("EW19", 2)]
    )

    EW19 = StationInfo(name="Queenstown",
        travel=[TravelInfo("EW18", 2), TravelInfo("EW20", 2)]
    )

    EW20 = StationInfo(name="Commonwealth",
        travel=[TravelInfo("EW19", 2), TravelInfo("EW21", 2)]
    )

    EW21 = StationInfo(name="Buona Vista",
        travel=[
            TravelInfo("EW20", 2),
            TravelInfo("EW22", 2),
            TravelInfo("CC22", 3)
        ]
    )

    EW22 = StationInfo(name="Dover",
        travel=[TravelInfo("EW21", 2), TravelInfo("EW23", 2)]
    )

    EW23 = StationInfo(name="Clementi",
        travel=[TravelInfo("EW22", 2), TravelInfo("EW24", 4)]
    )
    
    EW24 = StationInfo(name="Jurong East",
        travel=[
            TravelInfo("EW23", 4),
            TravelInfo("EW25", 2),
            TravelInfo("NS1", 1),
        ]
    )

    EW25 = StationInfo(name="Chinese Garden",
        travel=[TravelInfo("EW24", 2), TravelInfo("EW26", 3)]
    )

    EW26 = StationInfo(name="Lakeside",
        travel=[TravelInfo("EW25", 3), TravelInfo("EW27", 2)]
    )

    EW27 = StationInfo(name="Boon Lay",
        travel=[TravelInfo("EW26", 2), TravelInfo("EW28", 2)]
    )

    EW28 = StationInfo(name="Pioneer",
        travel=[TravelInfo("EW27", 2), TravelInfo("EW29", 4)]
    )

    EW29 = StationInfo(name="Joo Koon",
        travel=[TravelInfo("EW28", 4), TravelInfo("EW30", 3)]
    )

    EW30 = StationInfo(name="Gul Circle",
        travel=[TravelInfo("EW29", 3), TravelInfo("EW31", 3)]
    )

    EW31 = StationInfo(name="Tuas Crescent",
        travel=[TravelInfo("EW30", 3), TravelInfo("EW32", 2)]
    )

    EW32 = StationInfo(name="Tuas West Road",
        travel=[TravelInfo("EW31", 2), TravelInfo("EW33", 2)]
    )
    
    EW33 = StationInfo(name="Tuas Link",
        travel=[TravelInfo("EW32", 2)]
    )
    CG = StationInfo(name="Tanah Merah",
        travel=[
            TravelInfo("EW4", 0),
            TravelInfo("CG1", 3)
            ]
        )
    CG1 = StationInfo(name="Expo",
        travel=[
            TravelInfo("CG2", 5),
            TravelInfo("CG", 3),
            TravelInfo("DT35", 3)
            ]
        )
    CG2 = StationInfo(name="Changi Airport",
        travel=[
            TravelInfo("CG1", 5)
            ]
        )
    
class NSStation(Station):
    NS1 = StationInfo(
        name="Jurong East",
        travel=[
            TravelInfo("NS2", 2),
            # Cross-platform (island) transfer to EW24 (East–West Line) ≈ 1 min
            TravelInfo("EW24", 1)
        ]
    )

    NS2 = StationInfo(
        name="Bukit Batok",
        travel=[
            TravelInfo("NS1", 2),
            TravelInfo("NS3", 1)
            ]
        )
    NS3 = StationInfo(
        name="Bukit Gombak",
        travel=[
            TravelInfo("NS2", 1),
            TravelInfo("NS4", 2)
            ]
        )
    NS4 = StationInfo(
        name="Choa Chu Kang",
        travel=[
            TravelInfo("NS3", 2),
            TravelInfo("NS5", 2),
            # Paid-link transfer to BP1 (Bukit Panjang LRT) ≈ 2 min
            TravelInfo("BP1", 2)
        ]
    )
    NS5 = StationInfo(
        name="Yew Tee",
        travel=[
            TravelInfo("NS4", 2),
            TravelInfo("NS7", 4)
        ]
    )
    NS7 = StationInfo(
        name="Kranji",
        travel=[
            TravelInfo("NS5", 4),
            TravelInfo("NS8", 3)
            ]
        )
    NS8 = StationInfo(
        name="Marsiling",
        travel=[
            TravelInfo("NS7", 3),
            TravelInfo("NS9", 2)
            ]
        )
    NS9 = StationInfo(
        name="Woodlands",
        travel=[
            TravelInfo("NS8", 2),
            TravelInfo("NS10", 2),
            TravelInfo("TE2", 4)
            ]
        )
    NS10 = StationInfo(
        name="Admiralty",
        travel=[
            TravelInfo("NS9", 2),
            TravelInfo("NS11", 3)
            ]
        )
    NS11 = StationInfo(
        name="Sembawang",
        travel=[
            TravelInfo("NS10", 3),
            TravelInfo("NS12", 2)
            ]
        )
    NS12 = StationInfo(
        name="Canberra",
        travel=[
            TravelInfo("NS11", 2),
                
           TravelInfo("NS13", 2)
            ]
        )
    NS13 = StationInfo(
        name="Yishun",
        travel=[
            TravelInfo("NS12", 2),
            TravelInfo("NS14", 2)
            ]
        )
    NS14 = StationInfo(
        name="Khatib",
        travel=[
            TravelInfo("NS13", 2),
            TravelInfo("NS15", 5)
            ]
        )
    NS15 = StationInfo(
        name="Yio Chu Kang",
        travel=[
            TravelInfo("NS14", 5),
            TravelInfo("NS16", 3)
            ]
        )
    NS16 = StationInfo(
        name="Ang Mo Kio",
        travel=[
            TravelInfo("NS15", 3),
            TravelInfo("NS17", 3)
            ]
        )
    NS17 = StationInfo(
        name="Bishan",
        travel=[
            TravelInfo("NS16", 3),
            TravelInfo("NS18", 2),
            TravelInfo("CC15", 3)
            ]
        )
    NS18 = StationInfo(
        name="Braddell",
        travel=[
            TravelInfo("NS17", 2),
            TravelInfo("NS19", 2)
            ]
        )
    NS19 = StationInfo(
        name="Toa Payoh",
        travel=[
            TravelInfo("NS18", 2),
            TravelInfo("NS20", 2)
            ]
        )
    NS20 = StationInfo(
        name="Novena",
        travel=[
            TravelInfo("NS19", 2),
            TravelInfo("NS21", 2)
            ]
        )
    NS21 = StationInfo(
        name="Newton",
        travel=[
            TravelInfo("NS20", 2),
            TravelInfo("NS22", 2),
            TravelInfo("DT11", 4)
            ]
        )
    NS22 = StationInfo(
        name="Orchard",
        travel=[
            TravelInfo("NS21", 2),
            TravelInfo("NS23", 2),
            TravelInfo("TE14", 3)
            ]
        )
    NS23 = StationInfo(
        name="Somerset",
        travel=[
            TravelInfo("NS22", 2),
            TravelInfo("NS24", 1)
            ]
        )
    NS24 = StationInfo(
        name="Dhoby Ghaut",
        travel=[
            TravelInfo("NS23", 1),
            TravelInfo("NS25", 2),
            TravelInfo("NE6", 3),
            TravelInfo("CC1", 2)
            ]
        )
    NS25 = StationInfo(
        name="City Hall",
        travel=[
            TravelInfo("NS24", 2),
            TravelInfo("NS26", 2),
            TravelInfo("EW13", 1)
            ]
        )
    NS26 = StationInfo(
        name="Raffles Place",
        travel=[
            TravelInfo("NS25", 2),
            TravelInfo("NS27", 2),
            TravelInfo("EW14", 1)
            ]
        )
    NS27 = StationInfo(
        name="Marina Bay",
        travel=[
            TravelInfo("NS26", 2),
            TravelInfo("NS28", 2),
            TravelInfo("TE20", 6),
            TravelInfo("CE2", 4)
            ]
        )
    NS28 = StationInfo(
        name="Marina South Pier",
        travel=[TravelInfo("NS27", 2)])
    
class CCStation(Station):
    CC1 = StationInfo(
        name="Dhoby Ghaut",
        travel=[
            TravelInfo("CC2", 2),
            TravelInfo("NS24", 2),
            TravelInfo("NE6", 2)
        ]
    )

    CC2 = StationInfo(
        name="Bras Basah",
        travel=[
            TravelInfo("CC1", 2),
            TravelInfo("CC3", 2)
            ]
        )
    CC3 = StationInfo(
        name="Esplanade",
        travel=[
            TravelInfo("CC2", 2),
            TravelInfo("CC4", 2)
            ]
        )
    CC4 = StationInfo(
        name="Promenade",
        travel=[TravelInfo("CC3", 2), TravelInfo("CC5", 2), TravelInfo("CE1", 2), TravelInfo("DT15", 2)])
    CC5 = StationInfo(
        name="Nicoll Highway",
        travel=[TravelInfo("CC4", 2), TravelInfo("CC6", 2)])
    CC6 = StationInfo(
        name="Stadium",
        travel=[TravelInfo("CC5", 2), TravelInfo("CC7", 2)])
    CC7 = StationInfo(
        name="Mountbatten",
        travel=[TravelInfo("CC6", 2), TravelInfo("CC8", 2)])
    CC8 = StationInfo(
        name="Dakota", 
        travel=[TravelInfo("CC7", 2), TravelInfo("CC9", 2)])
    CC9 = StationInfo(
        name="Paya Lebar",
        travel=[TravelInfo("CC8", 2), TravelInfo("CC10", 2)])
    CC10 = StationInfo(
        name="MacPherson",
        travel=[TravelInfo("CC9", 2), TravelInfo("CC11", 2)])
    CC11 = StationInfo(
        name="Tai Seng",
        travel=[TravelInfo("CC10", 2), TravelInfo("CC12", 3)])
    CC12 = StationInfo(
        name="Bartley",  
        travel=[TravelInfo("CC11", 3), TravelInfo("CC13", 2)])
    CC13 = StationInfo(
        name="Serangoon",  
        travel=[TravelInfo("CC12", 2), TravelInfo("CC14", 2), TravelInfo("NE12", 3)])
    CC14 = StationInfo(
        name="Lorong Chuan",
        travel=[TravelInfo("CC13", 2), TravelInfo("CC15", 3)])

    CC15 = StationInfo(
        name="Bishan",
        travel=[
            TravelInfo("CC14", 3),
            TravelInfo("CC16", 2),
            TravelInfo("NS17", 3)
        ]
    )

    CC16 = StationInfo(
        name="Marymount",
        travel=[TravelInfo("CC15", 2), TravelInfo("CC17", 3)])

    CC17 = StationInfo(
        name="Caldecott",
        travel=[
            TravelInfo("CC16", 3),
            TravelInfo("CC19", 5),
            TravelInfo("TE9", 3)
        ]
    )

    CC19 = StationInfo(
        name="Botanic Gardens",
        travel=[
            TravelInfo("CC17", 5),
            TravelInfo("CC20", 2),
            TravelInfo("DT9", 3)
        ]
    )

    CC20 = StationInfo(
        name="Farrer Road", 
        travel=[TravelInfo("CC19", 2), TravelInfo("CC21", 2)])
    CC21 = StationInfo(
        name="Holland Village",
        travel=[TravelInfo("CC20", 2), TravelInfo("CC22", 2)])

    CC22 = StationInfo(
        name="Buona Vista",
        travel=[
            TravelInfo("CC21", 2),
            TravelInfo("CC23", 2),
            TravelInfo("EW21", 3)
        ]
    )

    CC23 = StationInfo(
        name="one-north", 
        travel=[TravelInfo("CC22", 2), TravelInfo("CC24", 2)])
    CC24 = StationInfo(
        name="Kent Ridge",  
        travel=[TravelInfo("CC23", 2), TravelInfo("CC25", 2)])
    CC25 = StationInfo(
        name="Haw Par Villa", 
        travel=[TravelInfo("CC24", 2), TravelInfo("CC26", 2)])
    CC26 = StationInfo(
        name="Pasir Panjang",
        travel=[TravelInfo("CC25", 2), TravelInfo("CC27", 2)])
    CC27 = StationInfo(
        name="Labrador Park",
        travel=[TravelInfo("CC26", 2), TravelInfo("CC28", 1)])
    CC28 = StationInfo(
        name="Telok Blangah",
        travel=[TravelInfo("CC27", 1), TravelInfo("CC29", 3)])
    CC29 = StationInfo(
        name="HarbourFront",
        travel=[
            TravelInfo("CC28", 3),
            TravelInfo("NE1", 2)
        ]
    )

    # Circle Line Extension
    CE1 = StationInfo(
        name="Bayfront",
        travel=[
            TravelInfo("CC4", 2),
            TravelInfo("CE2", 2),
            TravelInfo("DT16", 1)
            ]
        )
    CE2 = StationInfo(
        name="Marina Bay",
        travel=[
            TravelInfo("CE1", 2),
            TravelInfo("NS27", 4),
            TravelInfo("TE20", 6)
            ]
        )
       
class NEStation(Station):
    NE1 = StationInfo(
        name="HarbourFront",
        travel=[
            TravelInfo("NE3", 4),
            TravelInfo("CC29", 2)
        ]
    )
    NE3 = StationInfo(
        name="Outram Park",
        travel=[
            TravelInfo("NE1", 4),
            TravelInfo("NE4", 2),
            TravelInfo("EW16", 4),
            TravelInfo("TE17", 3)
        ]
    )
    NE4 = StationInfo(
        name="Chinatown",
        travel=[
            TravelInfo("NE3", 2),
            TravelInfo("NE5", 1),
            TravelInfo("DT19", 2)
        ]
    )
    NE5 = StationInfo(
        name="Clarke Quay",
        travel=[TravelInfo("NE4", 1), TravelInfo("NE6", 3)])
    NE6 = StationInfo(
        name="Dhoby Ghaut",
        travel=[
            TravelInfo("NE5", 3),
            TravelInfo("NE7", 2),
            TravelInfo("CC1", 2),
            TravelInfo("NS24", 3)
        ]
    )

    NE7 = StationInfo(
        name="Little India",
        travel=[
            TravelInfo("NE6", 2),
            TravelInfo("NE8", 2),
            TravelInfo("DT12", 3)
        ]
    )
    NE8  = StationInfo(
        name="Farrer Park",
        travel=[TravelInfo("NE7", 2), TravelInfo("NE9", 2)])
    NE9  = StationInfo(
        name="Boon Keng",
        travel=[TravelInfo("NE8", 2), TravelInfo("NE10", 2)])
    NE10 = StationInfo(
        name="Potong Pasir",
        travel=[TravelInfo("NE9", 2), TravelInfo("NE11", 2)])
    NE11 = StationInfo(
        name="Woodleigh",
        travel=[TravelInfo("NE10", 2), TravelInfo("NE12", 1)])
    NE12 = StationInfo(
        name="Serangoon",
        travel=[
            TravelInfo("NE11", 1),
            TravelInfo("NE13", 2),
            TravelInfo("CC13", 3)
        ]
    )
    NE13 = StationInfo(
        name="Kovan",
        travel=[TravelInfo("NE12", 2), TravelInfo("NE14", 2)])
    NE14 = StationInfo(
        name="Hougang",
        travel=[TravelInfo("NE13", 2), TravelInfo("NE15", 3)])
    NE15 = StationInfo(
        name="Buangkok",
        travel=[TravelInfo("NE14", 3), TravelInfo("NE16", 2)])
    NE16 = StationInfo(
        name="Sengkang", 
        travel=[TravelInfo("NE15", 2), TravelInfo("NE17", 2)]) # add in the lrt if needed
    NE17 = StationInfo(
        name="Punggol",
        travel=[TravelInfo("NE16", 2), TravelInfo("NE18", 3)]) # add in the lrt if needed
    NE18 = StationInfo(
        name="Punggol Coast",
        travel=[TravelInfo("NE17", 3)])

class DTStation(Station):
    DT1  = StationInfo(
        name="Bukit Panjang",
        travel=[TravelInfo("DT2", 2), TravelInfo("BP6", 5)])
    DT2  = StationInfo(
        name="Cashew",
        travel=[TravelInfo("DT1", 2), TravelInfo("DT3", 1)])
    DT3  = StationInfo(
        name="Hillview",
        travel=[TravelInfo("DT2", 1), TravelInfo("DT4", 1)])
    DT4  = StationInfo(
        name="Hume",
        travel=[TravelInfo("DT3", 1), TravelInfo("DT5", 2)])
    DT5  = StationInfo(
        name="Beauty World",
        travel=[TravelInfo("DT4", 2), TravelInfo("DT7", 2)])
    DT7  = StationInfo(
        name="Sixth Avenue",
        travel=[TravelInfo("DT5", 2), TravelInfo("DT8", 2)])
    DT8  = StationInfo(
        name="Tan Kah Kee", 
        travel=[TravelInfo("DT7", 2), TravelInfo("DT9", 2)])
    DT9  = StationInfo(
        name="Botanic Gardens",
        travel=[
            TravelInfo("DT8", 2),
            TravelInfo("DT10", 2),
            TravelInfo("CC19", 3)
        ]
    )
    DT10 = StationInfo(
        name="Stevens",
        travel=[
            TravelInfo("DT9", 2),
            TravelInfo("DT11", 3),
            TravelInfo("TE11", 2)
        ]
    )

    DT11 = StationInfo(
        name="Newton",
        travel=[
            TravelInfo("DT10", 3),
            TravelInfo("DT12", 2),
            TravelInfo("NS21", 4)
        ]
    )
    
    DT12 = StationInfo(
        name="Little India",
        travel=[
            TravelInfo("DT11", 2),
            TravelInfo("DT13", 2),
            TravelInfo("NE7", 3)
        ]
    )
    
    DT13 = StationInfo(
        name="Rochor", 
        travel=[TravelInfo("DT12", 2), TravelInfo("DT14", 2)])

    DT14 = StationInfo(
        name="Bugis",
        travel=[
            TravelInfo("DT13", 2),
            TravelInfo("DT15", 2),
            TravelInfo("EW12", 4)
        ]
    )

    DT15 = StationInfo(
        name="Promenade",
        travel=[
            TravelInfo("DT14", 2),
            TravelInfo("DT16", 2),
            TravelInfo("CC4", 2)
        ]
    )

    DT16 = StationInfo(
        name="Bayfront",
        travel=[
            TravelInfo("DT15", 2),
            TravelInfo("DT17", 2),
            TravelInfo("CE1", 1)
        ]
    )
    
    DT17 = StationInfo(
        name="Downtown",
        travel=[TravelInfo("DT16", 2), TravelInfo("DT18", 2)])
    DT18 = StationInfo(
        name="Telok Ayer",
        travel=[TravelInfo("DT17", 2), TravelInfo("DT19", 1)])

    DT19 = StationInfo(
        name="Chinatown",
        travel=[
            TravelInfo("DT18", 1),
            TravelInfo("DT20", 2),
            TravelInfo("NE4", 2)
        ]
    )
    
    DT20 = StationInfo(
        name="Fort Canning",
        travel=[TravelInfo("DT19", 2), TravelInfo("DT21", 2)])
    DT21 = StationInfo(
        name="Bencoolen", 
        travel=[TravelInfo("DT20", 2), TravelInfo("DT22", 2)])
    DT22 = StationInfo(
        name="Jalan Besar",
        travel=[TravelInfo("DT21", 2), TravelInfo("DT23", 2)])
    DT23 = StationInfo(
        name="Bendemeer", 
        travel=[TravelInfo("DT22", 2), TravelInfo("DT24", 2)])
    DT24 = StationInfo(
        name="Geylang Bahru",
        travel=[TravelInfo("DT23", 2), TravelInfo("DT25", 2)])
    DT25 = StationInfo(
        name="Mattar", 
        travel=[TravelInfo("DT24", 2), TravelInfo("DT26", 2)])
    DT26 = StationInfo(
        name="MacPherson",   
        travel=[TravelInfo("DT25", 2), TravelInfo("DT27", 2)])
    DT27 = StationInfo(
        name="Ubi",        
        travel=[TravelInfo("DT26", 2), TravelInfo("DT28", 2)])
    DT28 = StationInfo(
        name="Kaki Bukit",
        travel=[TravelInfo("DT27", 2), TravelInfo("DT29", 2)])
    DT29 = StationInfo(
        name="Bedok North",   
        travel=[TravelInfo("DT28", 2), TravelInfo("DT30", 2)])
    DT30 = StationInfo(
        name="Bedok Reservoir",
        travel=[TravelInfo("DT29", 2), TravelInfo("DT31", 2)])
    DT31 = StationInfo(
        name="Tampines West", 
        travel=[TravelInfo("DT30", 2), TravelInfo("DT32", 2)])
    DT32 = StationInfo(
        name="Tampines",
        travel=[
            TravelInfo("DT31", 2),
            TravelInfo("DT33", 2),
            TravelInfo("EW2", 6)
        ]
    )
    
    DT33 = StationInfo(
        name="Tampines East",
        travel=[TravelInfo("DT32", 2), TravelInfo("DT34", 3)])
    DT34 = StationInfo(
        name="Upper Changi",
        travel=[TravelInfo("DT33", 3), TravelInfo("DT35", 2)])
    DT35 = StationInfo(
        name="Expo",  
        travel=[TravelInfo("DT34", 2), TravelInfo("CG1", 3)])

class TEStation(Station): 
    TE1  = StationInfo(
        name="Woodlands North",
        travel=[TravelInfo("TE2", 3)])
    TE2  = StationInfo(
        name="Woodlands", 
        travel=[TravelInfo("TE1", 3), TravelInfo("TE3", 3), TravelInfo("NS9", 4)])
    TE3  = StationInfo(
        name="Woodlands South",
        travel=[TravelInfo("TE2", 3), TravelInfo("TE4", 5)])
    TE4  = StationInfo(
        name="Springleaf", 
        travel=[TravelInfo("TE3", 5), TravelInfo("TE5", 4)])
    TE5  = StationInfo(
        name="Lentor", 
        travel=[TravelInfo("TE4", 4), TravelInfo("TE6", 3)])
    TE6  = StationInfo(
        name="Mayflower",  
        travel=[TravelInfo("TE5", 3), TravelInfo("TE7", 3)])
    TE7  = StationInfo(
        name="Bright Hill",
        travel=[TravelInfo("TE6", 3), TravelInfo("TE8", 3)])
    TE8  = StationInfo(
        name="Upper Thomson", 
        travel=[TravelInfo("TE7", 3), TravelInfo("TE9", 3)])

    TE9  = StationInfo(
        name="Caldecott",
        travel=[
            TravelInfo("TE8", 3),
            TravelInfo("TE11", 5),
            TravelInfo("CC17", 3)
        ]
    )

    TE11 = StationInfo(
        name="Stevens",
        travel=[
            TravelInfo("TE9", 5),
            TravelInfo("TE12", 4),
            TravelInfo("DT10", 2)
        ]
    )
    TE12 = StationInfo(
        name="Napier",
        travel=[TravelInfo("TE11", 4), TravelInfo("TE13", 2)])
    TE13 = StationInfo(
        name="Orchard Boulevard",
        travel=[TravelInfo("TE12", 2), TravelInfo("TE14", 2)])
    TE14 = StationInfo(
        name="Orchard",
        travel=[
            TravelInfo("TE13", 2),
            TravelInfo("TE15", 3),
            TravelInfo("NS22", 3)
        ]
    )
    TE15 = StationInfo(
        name="Great World",
        travel=[TravelInfo("TE14", 3), TravelInfo("TE16", 2)])
    TE16 = StationInfo(
        name="Havelock",  
        travel=[TravelInfo("TE15", 2), TravelInfo("TE17", 2)])
    TE17 = StationInfo(
        name="Outram Park",
        travel=[
            TravelInfo("TE16", 2),
            TravelInfo("TE18", 2),
            TravelInfo("EW16", 2),
            TravelInfo("NE3", 4)
        ]
    )
    TE18 = StationInfo(   
        name="Maxwell", 
        travel=[TravelInfo("TE17", 2), TravelInfo("TE19", 2)])
    TE19 = StationInfo(
        name="Shenton Way", 
        travel=[TravelInfo("TE18", 2), TravelInfo("TE20", 2)])
    TE20 = StationInfo(
        name="Marina Bay",
        travel=[
            TravelInfo("TE19", 2),
            TravelInfo("TE22", 3),
            TravelInfo("NS27", 6),
            TravelInfo("CE2", 7)
        ]
    )
    TE22 = StationInfo(
        name="Gardens by the Bay",
        travel=[TravelInfo("TE20", 3), TravelInfo("TE23", 3)])
    TE23 = StationInfo(
        name="Tanjong Rhu", 
        travel=[TravelInfo("TE22", 3), TravelInfo("TE24", 4)])
    TE24 = StationInfo(
        name="Katong Park",    
        travel=[TravelInfo("TE23", 4), TravelInfo("TE25", 2)])
    TE25 = StationInfo(
        name="Tanjong Katong",  
        travel=[TravelInfo("TE24", 2), TravelInfo("TE26", 3)])
    TE26 = StationInfo(
        name="Marine Parade",   
        travel=[TravelInfo("TE25", 3), TravelInfo("TE27", 2)])
    TE27 = StationInfo(
        name="Marine Terrace", 
        travel=[TravelInfo("TE26", 2), TravelInfo("TE28", 2)])
    TE28 = StationInfo(
        name="Siglap",     
        travel=[TravelInfo("TE27", 2), TravelInfo("TE29", 3)])
    TE29 = StationInfo(
        name="Bayshore",     
        travel=[TravelInfo("TE28", 3)])
    
class BPStation(Station):
    BP1  = StationInfo(name="Choa Chu Kang", travel=[TravelInfo("BP2", 2), TravelInfo("NS4", 2)])
    BP2  = StationInfo(name="South View", travel=[TravelInfo("BP1", 2), TravelInfo("BP3", 2)])
    BP3  = StationInfo(name="Keat Hong", travel=[TravelInfo("BP2", 2), TravelInfo("BP4", 2)])
    BP4  = StationInfo(name="Teck Whye", travel=[TravelInfo("BP3", 2), TravelInfo("BP5", 2)])
    BP5  = StationInfo(name="Phoenix", travel=[TravelInfo("BP4", 2), TravelInfo("BP6", 2)])
    BP6  = StationInfo(name="Bukit Panjang", travel=[TravelInfo("BP5", 2), TravelInfo("BP7", 2), TravelInfo("BP13", 2), TravelInfo("DT1", 5)])
    BP7  = StationInfo(name="Petir", travel=[TravelInfo("BP6", 2), TravelInfo("BP8", 2)])
    BP8  = StationInfo(name="Pending", travel=[TravelInfo("BP7", 2), TravelInfo("BP9", 2)])
    BP9  = StationInfo(name="Bangkit", travel=[TravelInfo("BP8", 2), TravelInfo("BP10", 2)])
    BP10 = StationInfo(name="Fajar", travel=[TravelInfo("BP9", 2), TravelInfo("BP11", 2)])
    BP11 = StationInfo(name="Segar", travel=[TravelInfo("BP10", 2), TravelInfo("BP12", 2)])
    BP12 = StationInfo(name="Jelapang", travel=[TravelInfo("BP11", 2), TravelInfo("BP13", 2)])
    BP13 = StationInfo(name="Senja", travel=[TravelInfo("BP12", 2), TravelInfo("BP6", 2)])






def get_station_name_by_code(code):
    """
    Return the station name corresponding to a given station code.
    If not found, returns None.
    """
    for subclasses in Station.__subclasses__():
        for member in subclasses:
            if code.lower() in str(member).lower():
                return member.value.name
    return invalid_station_code


def get_codes_by_station_name(name):
    """
    Return the list of codes corresponding to a given station name.
    If not found, returns None.
    """
    temp = []
    for subclasses in Station.__subclasses__():
        for member in subclasses:
            if member.value.name.lower() == name.lower():
                temp.append(member.name)
                
    if temp == []:
        return invalid_station_name
    else:
        return ', '.join(temp)

    
def get_line(station_name):
    Flag = True
    temp = []
    for subclasses in Station.__subclasses__():
        for member in subclasses:
            if member.value.name.lower() == station_name.lower():
                Flag = False
                ture = member.value.name
                temp.append(f'{member.name}')

    if Flag:
        return "Please give a correct Station name"
    for name in range(len(temp)):
        temp[name] = temp[name][:2] + "L" 
        
    return f"{ture} belongs to the following lines: {', '.join(temp)}" 

def name_dict():
    graph = {}
    for subclasses in Station.__subclasses__():  # iterates thru the subclasses
        for member in subclasses: # iterates thru the stations in the subclasses
            name = get_station_name_by_code(member.name)     
            graph.setdefault(name, set()) # adds an empty set if it is not inside the dict
            for travel in member.value.travel: # accesses the travel info of the stations
                dst, t = get_station_name_by_code(travel.destination), travel.time # takes the destination, time
                if dst == name:
                    continue
                graph[name].add((dst, t)) 
                graph.setdefault(dst, set())  # adds the an empty set when its not inside the dict for the dst
                graph[dst].add((name, t)) # Add reverse neighbor for dst
                
    for subclasses in Station.__subclasses__():  # iterates thru the subclasses
        for member in subclasses: 
            graph[name] = list(graph[name]) # converts the elements in the graph back into lists for better accessibility for the algo
    return graph


def build_adjacency_dict():
    graph = {}
    for subclasses in Station.__subclasses__():  # iterates thru the subclasses
        for member in subclasses: # iterates thru the stations in the subclasses     
            graph.setdefault(member.name, set()) # adds an empty set if it is not inside the dict 
            for travel in member.value.travel: # accesses the travel info of the stations
                dst, t = travel.destination, travel.time # takes the destination, time
                graph[member.name].add((dst, t))
                graph.setdefault(dst, set())  # adds the an empty set when its not inside the dict for the dst
                graph[dst].add((member.name, t)) # Add reverse neighbor for dst
                
    for subclasses in Station.__subclasses__():  # iterates thru the subclasses
        for member in subclasses: 
            graph[member.name] = list(graph[member.name]) # converts the elements in the graph back into lists for better accessibility for the algo
    return graph
    