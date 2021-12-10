import os
import math
import asyncio
import discord as d
from discord.ext import commands
from discord.utils import get
import random
from datetime import date as dt
from urllib.request import Request, urlopen
import json
import nest_asyncio
import time
import aiohttp


nest_asyncio.apply()

##############################################################################Bot_Resources######################################################################################

skill = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
skills = ['combat','mining', 'smithing', 'woodcutting', 'crafting', 'fishing', 'cooking','total']

guilds_combat = {}
guilds_mining = {}
guilds_smithing = {}
guilds_woodcutting = {}
guilds_crafting = {}
guilds_fishing = {}
guilds_cooking = {}

guilds_counter  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                    'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                    'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                    'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                    'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                    'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                    'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                    0, 'ST': 0, '6T9': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                    'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                    'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                    'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                    'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                    'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                    'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                    'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                    'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                    'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                    'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                    'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                    'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                    'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                    'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                    'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                    'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                    'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                    'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                    'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                    'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_total  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                        0, 'ST': 0, '6T9': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_int  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 0,
                        'ST': 0, '6T9': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,
39431,45342,52132,59932,68892,79184,91006,104586,120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,1107128,1271805,
1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,
26857176,30850844,35438364,40708040,46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,246809111,283509271,325666684,
374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,
3948950932,4536153492,5210672106]

lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 
4480, 5146, 5911, 6790, 7800, 8960, 10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338, 94582, 108646, 124802, 143360, 
164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440, 658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 
3476690, 3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080, 21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 
48426151, 55627040, 63898689, 73400320, 84314826, 96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307, 387409211, 445016324, 
511189519, 587202560]



###############################################################################################################################################################################




######################################################################Bot_Funtctions##################################################################################        
        
        
        
def ToZero(dicc):
    for key in dicc:
        dicc[key]=0  
    
    
    
    
def tabfill(xp): 
    if xp>4536153492:
        lvl=120
        a=100
    else :   
        lvl=0
        a=0
        for l in range(120):
            if (xp > lvltab[l]):
                lvl = l+1
                a = round((((xp- lvltab[l]) / lvldef[l])*100),2)
    if a == 100:
        a = 0
        lvl += 1
    return lvl, a

def DictToList (dictio,listo):
    listo.clear()
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        listo.append(test)

def DictToList_alt (dictio):
    temporal = []
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        temporal.append(test)
    return temporal

def ResetDict(diction):
    diction = diction.fromkeys(diction, 0)
    return diction

def SortDict (di):
    temp = {}
    temp.clear()
    temp = {k: v for k, v in sorted(di.items(), key=lambda item: item[1],reverse=True)}
    return temp

def rankk (rank):
    rank_text = "**rank#"+str(rank)+"**"
    return rank_text

def get_tasks(session,skill_name):
    tasks = []
    for k in range(0,1000):  
        url='https://www.curseofaros.com/highscores'
        tasks.append(asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k))))
    return tasks
def get_tasks2(session,skill_name,limit):
    tasks = []
    for k in range(0,limit):  
        url='https://www.curseofaros.com/highscores'
        tasks.append(asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k))))
    return tasks

def get_tasks3(session,skill_name):
    tasks = []
    for k in range(0,2000):  
        url='https://www.curseofaros.com/highscores'
        tasks.append((k,asyncio.create_task(session.get(url+skill_name+'.json?p='+str(k)))))
    return tasks

owo_members=[]
members_list=[]
skill_xp=['combat_xp','mining_xp','smithing_xp','woodcutting_xp','crafting_xp','fishing_xp','cooking_xp']
member_templete={'member_name':'name_expml' ,'combat_xp':0 ,'mining_xp':0 ,'smithing_xp':0 ,'woodcutting_xp':0 ,'crafting_xp':0 ,'fishing_xp':0 ,'cooking_xp':0 }

async def set_init():
    start = time.time()
    members_sorted = []
    guildreg = {}
    x=0
    for skill_name in skill :
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20):
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    
                    if tag == 'OWO':
                        if player_name in members_list :
                            order = members_list.index(player_name)
                            owo_members[order][skill_xp[x]]=xp
                            continue
                        else:
                            member_list.append(player_name)
                            owo_member_temp=member_templete
                            owo_member_temp[member_name]=player_ame
                            owo_member_temp[skill_xp[x]]=xp
                            owo_members.append(owo_member_temp)
                            continue
        x=x+1 
    end = time.time()
    total_time = end - start
    return owo_members, total_time


##############################################################################
#get guild members rankings in a certain skill (20000)    
async def searchtag(skill_name,guildtag):
    start = time.time()
    members_sorted = []
    guildreg_names = {}
    guildreg_ranks = {}
    async with aiohttp.ClientSession() as session:
        to_do = get_tasks(session,skill_name)
        responses = await asyncio.gather(*to_do)
        for response in responses:
            fdata = await response.json()
            for i in range(0,20): 
                #check names get rank
                #player_rank = 20 * k + i + 1
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                if tag == guildtag.upper():
                    if player_name in guildreg_names :
                        continue
                    else:
                        guildreg_names[player_name]=xp
                        #guildreg_ranks[player_name]=player_rank
                        continue
    temp_dic = {k: v for k, v in sorted(guildreg_names.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    for key, value in temp_dic.items():
        test = key + " -- " + "{:,}".format(value) +"\n [Lv."+str(tabfill(value)[0])+" ("+str(tabfill(value)[1])+"%)]"
        members_sorted.append(test)
    mini_list = []
    for i in range(len(members_sorted)):
        mini_list.append(members_sorted[i])
    members_sorted.clear()
    temp_dic = {}
    end = time.time()
    total_time = end - start
    #print(mini_list)
    #print(total_time)
    return mini_list, total_time

#get guilds members rankings in total xp (20000)
async def searchtagtotal(guildtag):
    start = time.time()
    members_sorted = []
    guildreg = {}
    
    for skill_name in skill :
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20): 
                    #check names get rank
                    #player_rank = 20 * k + i + 1
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    
                    if tag == guildtag.upper():
                        if player_name in guildreg :
                            guildreg[player_name]+=xp
                            continue
                        else:
                            guildreg[player_name]=xp
                            continue
    temp_dic = {k: v for k, v in sorted(guildreg.items(), key=lambda item: item[1],reverse=True)}
    members_sorted.clear()
    for key, value in temp_dic.items():
        test = key + " -- " + "{:,}".format(value)
        members_sorted.append(test)
    mini_list = []
    for i in range(len(members_sorted)):
        mini_list.append(members_sorted[i])
    members_sorted.clear()
    temp_dic = {}
    end = time.time()
    total_time = end - start
    return mini_list, total_time

#get guilds ranking in a certain skill (5000)
async def search(skill_name):
    start = time.time()
    list_guilds_stred = []
    d_test = ResetDict(guilds_counter_int)
    async with aiohttp.ClientSession() as session:
        to_do = get_tasks(session,skill_name)
        responses = await asyncio.gather(*to_do)
        for response in responses:
            fdata = await response.json()
            for i in range(0,20): 
                #check names get rank
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()
                
                if tag in d_test :
                    d_test[tag] += xp
                elif "Immortal" in player_name :
                    d_test["IMMORTAL"] += xp
                else :                
                    continue
            
    temp_guilds = {k: v for k, v in sorted(d_test.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_guilds,list_guilds_stred)
    
    mini_list = []
    for i in range(len(list_guilds_stred)):
        mini_list.append(list_guilds_stred[i])
    list_guilds_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    end = time.time()
    total_time = end - start
    return mini_list , total_time
    
    
#get guilds ranking in total xp (5000)
async def searchTotal():
    start = time.time()
    list_guilds_total_stred = []
    dd_test = ResetDict(guilds_counter_int)
    for skill_name in skill:
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20): 
                    #check names
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    
                    if tag in dd_test :
                        dd_test[tag] += xp
                    elif "Immortal" in player_name :
                        dd_test["IMMORTAL"] += xp
                    else :                
                        continue
            
    temp_guilds = {k: v for k, v in sorted(dd_test.items(), key=lambda item: item[1],reverse=True)}
    
    DictToList(temp_guilds,list_guilds_total_stred)
        
    mini_list = []
    for i in range(len(list_guilds_total_stred)):
            mini_list.append(list_guilds_total_stred[i])
    list_guilds_total_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    end = time.time()
    total_time = end - start
    return mini_list, total_time


#get guilds overall ranking (20000)
async def LeaderBoard():
    start = time.time()
    all_xp = ResetDict(guilds_counter_int)
    skill_0 = ResetDict(guilds_counter_int)
    skill_1 = ResetDict(guilds_counter_int)
    skill_2 = ResetDict(guilds_counter_int)
    skill_3 = ResetDict(guilds_counter_int)
    skill_4 = ResetDict(guilds_counter_int)
    skill_5 = ResetDict(guilds_counter_int)
    skill_6 = ResetDict(guilds_counter_int)
    skills_dict_list = [skill_0,skill_1,skill_2,skill_3,skill_4,skill_5,skill_6,all_xp]

    list_empty = []
    list_empty.clear()
    list_0 = list_empty
    list_1 = list_empty
    list_2 = list_empty
    list_3 = list_empty
    list_4 = list_empty
    list_5 = list_empty
    list_6 = list_empty
    list_all = list_empty
    list_lists = [list_0, list_1, list_2, list_3, list_4, list_5, list_6, list_all ]
    m=0
    for skill_name in skill:
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks(session,skill_name)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
                for i in range(0,20): 
                    player_name = fdata[i]["name"]
                    xp = fdata[i]["xp"]
                    tag = player_name.split()[0]
                    tag = tag.upper()
                    n = player_name.lower()
                    
                    if tag in skills_dict_list[m] :
                        skills_dict_list[m][tag] += xp
                        all_xp[tag] += xp
                    elif "immortal" in n :
                        skills_dict_list[m]["IMMORTAL"] += xp
                        all_xp["IMMORTAL"] += xp
                    else :                
                        continue
        m +=1
        
    for j in range(0,8):
        tempo = SortDict(skills_dict_list[j])
        list_lists[j] = DictToList_alt(tempo)
        tempo.clear()
        
    end = time.time()
    total_time = end - start
    return list_lists ,total_time
#show members counts and lists of a certain guild in a certain range (rnk)
async def SearchMembers(guildtag,rnk):
    start = time.time()
    members_names = []
    limit = (rnk // 20) +1
    for skill_name in skill:
        async with aiohttp.ClientSession() as session:
            to_do = get_tasks2(session,skill_name,limit)
            responses = await asyncio.gather(*to_do)
            for response in responses:
                fdata = await response.json()
            for i in range(0,20): 
                player_name = fdata[i]["name"]
                tag = player_name.split()[0]
                tag = tag.upper()
                if tag == guildtag.upper():
                    if player_name in members_names :
                        continue
                    else:
                        members_names.append(player_name)
                        continue
    end = time.time()
    total_time = end - start
    return members_names, total_time

#############################################################################Bot_Main_Code##############################################################################


bot = commands.Bot(command_prefix='!')

bot.remove_command("help")
bot.remove_command("date")
bot.remove_command('random')
@bot.event
async def on_ready():
    print('Logging in as {0.user}'.format(bot))
    await bot.change_presence(activity=d.Activity(type=d.ActivityType.watching, name="LeaderBoard"))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

    


@bot.command()
async def hello(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Hello {username}!")

@bot.command()
async def wussup(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"Nothing much, hbu {username} ?")

@bot.command()
async def bye(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.send(f"See you later {username}!")

@bot.command(name="OwO",aliases=["owo","Owo","oWo"])
async def OwO(ctx):
    await ctx.send(f"Numba Wan !!")

@bot.command(name='dc',aliases=['disconnect','logout'])
async def dc(ctx):
    await bot.logout()

@bot.command()
async def date(ctx):
    d1 = dt.today().strftime("%d/%m/%Y")
    await ctx.send(f'Today is : {d1}')

@bot.command()
async def getlist(ctx):
    await ctx.send('getting init members xp')
    list = set_init()
    a = asyncio.run(list)
    members_xp_list = a[0]
    time_taken = a[1]
    await ctx.send(members_xp_list)
    await ctx.send(f'time taken {time_taken}')


@bot.command(name='combat',aliases=['melee','sw','silent'])
async def combat(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Combat Data ... ")
        combatlb_srch = search("")
        a = asyncio.run(combatlb_srch)
        test_list_1 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar1 = d.Embed(title="Top Guilds: Combat (20,000)", color=0x669999)
        for i in range(int(rank)):
            embedVar1.add_field(name=rankk(i+1), value= test_list_1[i] , inline=False)
        embedVar1.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar1)
        test_list_1.clear()

@bot.command(name='mining',aliases=['mine','rocky','pick','krieger'])
async def mining(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Mining Data ... ")
        mininglb_srch = search("-mining")
        a = asyncio.run(mininglb_srch)
        test_list_2 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar2 = d.Embed(title="Top Guilds: Mining (20,000)", color=0x333300)
        for i in range(int(rank)):
            embedVar2.add_field(name=rankk(i+1), value= test_list_2[i] , inline=False)
        embedVar2.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar2)
        test_list_2.clear()

@bot.command(name='smithing',aliases=['smith','ember','hammer'])
async def smithing(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Smithing Data ... ")
        smithinglb_srch = search("-smithing")
        a = asyncio.run(smithinglb_srch)
        test_list_3 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar3 = d.Embed(title="Top Guilds: Smithing (20,000)", color=0xff0000)
        for i in range(int(rank)):
            embedVar3.add_field(name=rankk(i+1), value= test_list_3[i] , inline=False)
        embedVar3.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar3)
        test_list_3.clear()

@bot.command(name='woodcutting',aliases=['wc','pecker','axe','matt'])
async def woodcutting(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Woodcutting Data ... ")
        woodcuttinglb_srch = search("-woodcutting")
        a = asyncio.run(woodcuttinglb_srch)
        test_list_4 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar4 = d.Embed(title="Top Guilds: Woodcutting (20,000)", color=0x00cc00)
        for i in range(int(rank)):
            embedVar4.add_field(name=rankk(i+1), value= test_list_4[i] , inline=False)
        embedVar4.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar4)
        test_list_4.clear()

@bot.command(name='crafting',aliases=['craft','woody','yekzer'])
async def crafting(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Crafting Data ... ")
        craftinglb_srch = search("-crafting")
        a = asyncio.run(craftinglb_srch)
        test_list_5 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar5 = d.Embed(title="Top Guilds: Crafting (20,000)", color=0x996633)
        for i in range(int(rank)):
            embedVar5.add_field(name=rankk(i+1), value= test_list_5[i] , inline=False)
        embedVar5.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar5)
        test_list_5.clear()

@bot.command(name='fishing',aliases=['fish','tantrid','tant'])
async def fishing(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Fishing Data ... ")
        fishinglb_srch = search("-fishing")
        a = asyncio.run(fishinglb_srch)
        test_list_6 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar6 = d.Embed(title="Top Guilds: Fishing (20,000)", color=0x0066ff)
        for i in range(int(rank)):
            embedVar6.add_field(name=rankk(i+1), value= test_list_6[i] , inline=False)
        embedVar6.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar6)
        test_list_6.clear()

@bot.command(name='cooking',aliases=['cook','food'])
async def cooking(ctx,rank="25"):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Cooking Data ... ")
        cookinglb_srch = search("-cooking")
        a = asyncio.run(cookinglb_srch)
        test_list_7 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar7 = d.Embed(title="Top Guilds: Cooking (20,000)", color=0x800000)
        for i in range(int(rank)):
            embedVar7.add_field(name=rankk(i+1), value= test_list_7[i] , inline=False)
        embedVar7.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar7)
        test_list_7.clear()

@bot.command(name='total',aliases=['totalxp'])
async def total(ctx,rank='25'):
    if ((int(rank)<=0) or (int(rank)>25)):
        await ctx.send("Ranks must be between 1 and 25")
    else:
        await ctx.send("Fetching Data ... ")
        totallb_srch = searchTotal()
        a = asyncio.run(totallb_srch)
        test_list_0 = a[0]
        time_taken = a[1]
        cmd_time = int(time_taken) 
        embedVar0 = d.Embed(title="Top Guilds: Total XP (20,000)", color=0x6600ff)
        for i in range(int(rank)):
            embedVar0.add_field(name=rankk(i+1), value= test_list_0[i] , inline=False)
        embedVar0.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embedVar0)
        test_list_0.clear()
        
@bot.command()
async def test(ctx):
    embedVar = d.Embed(title="TEST", color=0x6600ff)
    embedVar.add_field(name="test", value= "testtesttest" , inline=False)
                        
    embedVarr = d.Embed(title="TEST1", color=0x6600ff)
    embedVarr.add_field(name="test1", value= "testtesttest1" , inline=False)
                    
    await ctx.send(embed=embedVar)
    await ctx.send(embed=embedVarr)

@bot.command(name='all',aliases=['overall','ranking'])
async def all(ctx):
    mining = get(ctx.guild.emojis, name="mining")
    wc = get(ctx.guild.emojis, name="woodcutting")
    fishing = get(ctx.guild.emojis, name="fishing")
    smithing = get(ctx.guild.emojis, name="smithing")
    crafting = get(ctx.guild.emojis, name="crafting")
    cooking = get(ctx.guild.emojis, name="cooking")
    combat = get(ctx.guild.emojis, name="combat")
    
    field_header = [f' {mining} Top Guilds Mining \n',f' {wc} Top Guilds Woodcutting\n',f' {fishing} Top Guilds Fishing\n',f' {smithing} Top Guilds Smithing\n',
                        f' {crafting} Top Guilds Crafting\n',f' {cooking} Top Guilds Cooking\n',f' {combat} Top Guilds Combat\n',"Top Guilds Total XP\n"]
    await ctx.send("Fetching Data ... ")
    embedVar1 = d.Embed(title="Top Guilds (20,000)", color=0x669999)
    
    alllb_srch = LeaderBoard()
    a = asyncio.run(alllb_srch)
    listed = a[0]
    time_taken = a[1]
    cmd_time = int(time_taken) 
    wierd_order = [1,3,5,2,4,6,0,7]
    for i in range(8) :
        msg = ""
        for j in range(10):
            msg = msg + rankk(j+1) + ' ' + listed[wierd_order[i]][j]+'\n'
        embedVar1.add_field(name= field_header[i], value= msg , inline=True)
    embedVar1.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
    await ctx.send(embed=embedVar1)
    listed.clear()



@bot.command(name='guildlb',aliases=['glb','guildboard'])
async def guildlb(ctx,skill_name,guildtag):
    guild_name = guildtag.upper()
    await ctx.send(f"Getting {guild_name}'s {skill_name} Leaderboard ... ")
    x = skills.index(skill_name.lower())

    guildlb_srch = searchtag(skill[x],guildtag)
    #loop = asyncio.get_event_loop()
    #future = await asyncio.ensure_future(guildlb_srch)
    #a = loop.run_until_complete(future)
    a = asyncio.run(guildlb_srch)
    test_list_8 = a[0]
    
    tag = guildtag.upper()
    time_taken = a[1]
    cmd_time = int(time_taken) 

    guildlb_msg = f"Top "+tag+": "+skill_name.capitalize()+"(20,000)"
    embedVar = d.Embed(title= guildlb_msg , color=0x0066ff)
    embedVar.add_field(name="Skillers count", value= str(len(test_list_8)) , inline=False)
    await ctx.send(embed=embedVar)
    
    counter_int = len(test_list_8)
    embeds_int = math.ceil(counter_int / 15)
    fields_int = embeds_int
    

    embed0 = d.Embed(title="\u200b", color=0x6600ff)
    embed1 = d.Embed(title="\u200b", color=0x6600ff)
    embed2 = d.Embed(title="\u200b", color=0x6600ff)
    embed3 = d.Embed(title="\u200b", color=0x6600ff)
    embed4 = d.Embed(title="\u200b", color=0x6600ff)
    embed5 = d.Embed(title="\u200b", color=0x6600ff)
    embed6 = d.Embed(title="\u200b", color=0x6600ff)
    embed7 = d.Embed(title="\u200b", color=0x6600ff)
    embed8 = d.Embed(title="\u200b", color=0x6600ff)
    embed9 = d.Embed(title="\u200b", color=0x6600ff)
    embed10 = d.Embed(title="\u200b", color=0x6600ff)
    embed11 = d.Embed(title="\u200b", color=0x6600ff)
    embed12 = d.Embed(title="\u200b", color=0x6600ff)
    embed13 = d.Embed(title="\u200b", color=0x6600ff)
    embed14 = d.Embed(title="\u200b", color=0x6600ff)
    embed15 = d.Embed(title="\u200b", color=0x6600ff)
    embed16 = d.Embed(title="\u200b", color=0x6600ff)
    embed17 = d.Embed(title="\u200b", color=0x6600ff)
    embeds_list = [embed0,embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,embed11,embed12,embed13,embed14,embed15,embed16,embed17]
    
    members_msg0 = ""
    
    for i in range(embeds_int):
        members_msg0 = ""
        loop_list = []
        for j in range(fields_int):
            loop_list.append(j*15)
        loop_list.append(counter_int)
        
        for k in range(loop_list[i],loop_list[i+1]):
            members_msg0 = members_msg0 + rankk(k+1) + "\n" + test_list_8[k] + '\n'
        embeds_list[i].add_field(name='\u200b', value= members_msg0 , inline=False)
        members_msg0=""
        if i == embeds_int-1:
            embeds_list[i].set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embeds_list[i])
    test_list_8.clear()    












"""@bot.command()
async def event(ctx):

    await ctx.send(f"Getting Combat Grinders Leaderboard ... ")
    results_list = []
    results_list = CombatEvent()
    temp_msg = ""
    for i in range(len(results_list)-1):
        temp_msg = temp_msg + results_list[i] + '\n'
    await ctx.send(f"{temp_msg}")
    temp_msg0 = "Total Guild Gained Xp"+' -- '+"{:,}".format(results_list[len(results_list)-1])
    await ctx.send(f"{temp_msg0}")
    results_list.clear()"""


    
@bot.command(name='guildlbT',aliases=['glbt','guildranks'])
async def guildlbT(ctx,guildtag):
    guild_name = guildtag.upper()
    await ctx.send(f"Getting {guild_name}'s Leaderboard ... ")
    

    guildlbT_srch = searchtagtotal(guildtag)
    #loop = asyncio.get_event_loop()
    #future = await asyncio.ensure_future(guildlb_srch)
    #a = loop.run_until_complete(future)
    temp_result_T = asyncio.run(guildlbT_srch)
    test_list_10 = temp_result_T[0]


    tag = guildtag.upper()
    time_taken = temp_result_T[1]
    time_take = int(time_taken) 

    guildlb_msg = f"Top "+tag+": "+"[Total XP](20,000)"
    embedVar = d.Embed(title= guildlb_msg , color=0x0066ff)
    embedVar.add_field(name="Players Count", value= str(len(test_list_10)) , inline=False)
    await ctx.send(embed=embedVar)
    
    counter_int = len(test_list_10)
    embeds_int = math.ceil(counter_int / 15)
    fields_int = embeds_int
    
    embed0 = d.Embed(title="\u200b", color=0x6600ff)
    embed1 = d.Embed(title="\u200b", color=0x6600ff)
    embed2 = d.Embed(title="\u200b", color=0x6600ff)
    embed3 = d.Embed(title="\u200b", color=0x6600ff)
    embed4 = d.Embed(title="\u200b", color=0x6600ff)
    embed5 = d.Embed(title="\u200b", color=0x6600ff)
    embed6 = d.Embed(title="\u200b", color=0x6600ff)
    embed7 = d.Embed(title="\u200b", color=0x6600ff)
    embed8 = d.Embed(title="\u200b", color=0x6600ff)
    embed9 = d.Embed(title="\u200b", color=0x6600ff)
    embed10 = d.Embed(title="\u200b", color=0x6600ff)
    embed11 = d.Embed(title="\u200b", color=0x6600ff)
    embed12 = d.Embed(title="\u200b", color=0x6600ff)
    embed13 = d.Embed(title="\u200b", color=0x6600ff)
    embed14 = d.Embed(title="\u200b", color=0x6600ff)
    embed15 = d.Embed(title="\u200b", color=0x6600ff)
    embed16 = d.Embed(title="\u200b", color=0x6600ff)
    embed17 = d.Embed(title="\u200b", color=0x6600ff)
    embeds_list = [embed0,embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,embed11,embed12,embed13,embed14,embed15,embed16,embed17]
    
    members_msg0 = ""
    
    for i in range(embeds_int):
        members_msg0 = ""
        loop_list = []
        for j in range(embeds_int):
            loop_list.append(j*15)
        loop_list.append(counter_int)
        
        for k in range(loop_list[i],loop_list[i+1]):
            members_msg0 = members_msg0 + rankk(k+1) + "\n" + test_list_10[k] + '\n'
        embeds_list[i].add_field(name='\u200b', value= members_msg0 , inline=False)
        members_msg0=""
        if i == embeds_int-1:
            embeds_list[i].set_footer(text="time taken : "+str(time_take)+" seconds.")
        await ctx.send(embed=embeds_list[i])
    test_list_10.clear()                  




    
@bot.command(name="guildcount",aliases=['gc','count','howmany','hm'])
async def guildcount(ctx,guildtag,rank):
    guild_name = guildtag.upper()
    await ctx.send(f"Countings {guild_name}'s members")
    count_srch = SearchMembers(guild_name,int(rank))
    a = asyncio.run(count_srch)
    y = a[0]
    time_taken = a[1]
    cmd_time = int(time_taken)
    counter_int = len(y)
    counter_msg = f"{guild_name}'s Members at Top {rank}"
    embedVar8 = d.Embed(title= counter_msg , color=0x0066ff)
    embedVar8.add_field(name="Count", value= str(counter_int) , inline=False)
    await ctx.send(embed=embedVar8)
    members_msg = ""
    members_msg0 = ""
    ###############################Guilds_Less_Than_65_members###############################################
    if (counter_int<=65):
        if (guild_name == "OWO"):
            embed = d.Embed(title="Legends", inline=False)
        else:
            embed = d.Embed(title="Members", inline=False)
        for i in range(counter_int):
            members_msg = members_msg + y[i] + '\n'
        embed.add_field(name="\u200b", value= members_msg , inline=False)
        embed.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
        await ctx.send(embed=embed)      
    ###############################Guilds_Between_65_And_325_members###############################################
    elif ((counter_int>65) and (counter_int<325)):
        fields_int =  math.ceil(counter_int / 65)
        loop_list = []
        for i in range(fields_int):
            loop_list.append(i*65)
        loop_list.append(counter_int)
        if (guild_name == "OWO"):
            embed = d.Embed(title="Legends", inline=False)
        else:
            embed = d.Embed(title="Members", inline=False)
            
        for i in range(fields_int):
            for j in range(loop_list[i],loop_list[i+1]):
                members_msg0 = members_msg0 + y[j] + '\n'
            embed.add_field(name='\u200b', value= members_msg0 , inline=False)
            if i == fields_int-1:
                embed.set_footer(text="time taken : "+str(cmd_time)+" seconds.")
            members_msg0=""
            await ctx.send(embed=embed)
    ##################################Guilds_Between_325_And_1625_members############################################
    elif ((counter_int>=325) and (counter_int<1625)):
        embed0 = d.Embed(title="\u200b", color=0x6600ff)
        embed1 = d.Embed(title="\u200b", color=0x6600ff)
        embed2 = d.Embed(title="\u200b", color=0x6600ff)
        embed3 = d.Embed(title="\u200b", color=0x6600ff)
        embed4 = d.Embed(title="\u200b", color=0x6600ff)
        embed5 = d.Embed(title="\u200b", color=0x6600ff)
        embed6 = d.Embed(title="\u200b", color=0x6600ff)
        embed7 = d.Embed(title="\u200b", color=0x6600ff)
        embed8 = d.Embed(title="\u200b", color=0x6600ff)
        embed9 = d.Embed(title="\u200b", color=0x6600ff)
        embed10 = d.Embed(title="\u200b", color=0x6600ff)
        embed11 = d.Embed(title="\u200b", color=0x6600ff)
        embed12 = d.Embed(title="\u200b", color=0x6600ff)
        embed13 = d.Embed(title="\u200b", color=0x6600ff)
        embed14 = d.Embed(title="\u200b", color=0x6600ff)
        embed15 = d.Embed(title="\u200b", color=0x6600ff)

        embeds_list = [embed0,embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10,embed11,embed12,embed13,embed14,embed15]
        exf = math.ceil(counter_int / 65)
        embeds_int = exf
        fields_int = exf

        if (guild_name == "OWO"):
            embed = d.Embed(title="Legends", inline=False)
            embed.add_field(name="\u200b",value="\u200b")
        else:
            embed = d.Embed(title="Members", inline=False)
            embed.add_field(name="\u200b",value="\u200b")
        await ctx.send(embed=embed)

        for i in range(embeds_int):
            loop_list = []
            embeds_list[i] = d.Embed(title="\u200b", inline=False)
            for j in range(fields_int):
                loop_list.append(j*65)
            loop_list.append(counter_int)
                
            for k in range(loop_list[i],loop_list[(i)+1]):
                members_msg0 = members_msg0 + y[k] + '\n'
            embeds_list[i].add_field(name='\u200b', value= members_msg0 , inline=False)
            members_msg0=""
            await ctx.send(embed=embeds_list[i])
    y.clear()








@bot.command(name='help',aliases=['help?','helpme','commands?','command?','cmd'])
async def help(ctx):
    embedVar9 = d.Embed(title="Guilds Commands", color=0x669999)
    embedVar9.add_field(name="-----skills ranking-----", value= "!{Skill's Command} {How Many Guilds to Display(max 25)}" , inline=False)
    embedVar9.add_field(name="!combat or !melee or !sw", value= "Show Top Guilds in Combat (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!mining or !mine or !pick or !rocky or !krieger", value= "Show Top Guilds in Mining (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!smithing or !smith or !hammer or !ember", value= "Show Top Guilds in Smithing (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!woodcutting or !wc or !pecker or !matt", value= "Show Top Guilds in Woodcutting (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!crafting or !craft or !woody or !yekzer", value= "Show Top Guilds in Crafting (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!fishing or !fish or !tantrid or !tant", value= "Show Top Guilds in Fishing (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!cooking or !cook or !food", value= "Show Top Guilds in Cooking (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!total or !totalxp", value= "Show Top Guilds in Total XP (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!all or !overall or !ranking", value= "Show an Overall Leaderboard (From Top 20,000 players)" , inline=False)
    embedVar9.add_field(name="!guildlb or !glb or !guildboard", value= "Show The Leaderboard of a Guild in a Skill (From Top 20,000 players)\n !guildlb {skill name} {guild tag}" , inline=False)
    embedVar9.add_field(name="!guildlbT or !glbT or !guildboardT", value= "Show The Leaderboard of a Guild in Total XP (From Top 20,000 players)\n !guildlbT {guild tag}" , inline=False)
    embedVar9.add_field(name="!guildcount or !gc or !count or !howmany or !hm", value= "Show The Members of a Guilds in a Certain Range \n !counter {guild tag} {Search Range}" , inline=False)
    embedVar9.add_field(name="!date", value= "Show Today Date" , inline=False)
    embedVar9.add_field(name="!help or !help? or !helpme or !commands?", value= "Show  This Menu" , inline=False)
    embedVar9.add_field(name="!test", value= "Test The Current Command In Developement" , inline=False)
    embedVar9.add_field(name="!ping", value= "Show The Bot ping" , inline=False)
    embedVar9.add_field(name="!dc or !disconnect or !logout", value= "Disconnect The Bot For a While To Reset Himself" , inline=False)
    embedVar9.add_field(name="!hello , !wussup , !bye", value= "Interract With The Bot" , inline=False)
    await ctx.send(embed=embedVar9)   



bot.run(os.getenv('TOKEN'))

