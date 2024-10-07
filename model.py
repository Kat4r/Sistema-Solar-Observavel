from datetime import datetime
from astroquery.jplhorizons import Horizons
from mpl_toolkits.mplot3d import Axes3D

agora = datetime.now()
#ano = int(datetime.year)
marte = Horizons(499, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

terra = Horizons(399, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

mercurio = Horizons(199, location="500@10", epochs={'start':f"{agora}",
                                               'stop':f'2024-01-01',
                                               'step':'1y'}).ephemerides()

venus = Horizons(299, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

lua = Horizons(301, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

saturno = Horizons(699, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

urano = Horizons(799, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

pluto = Horizons(999, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

netuno = Horizons(899, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

jupiter = Horizons(599, location="500@10", epochs={'start':f"{agora}",
                                               'stop':'2024-01-01',
                                               'step':'1y'}).ephemerides()

