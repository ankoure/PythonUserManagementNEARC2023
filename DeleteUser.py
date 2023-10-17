import fme
import fmeobjects
from arcgis.gis import GIS

gis = GIS(url="PortalURL",username="Username",password= 'Password')

def deleteUser(feature):
    try:
        portaluser = gis.users.get(username = feature.getAttribute('baseusername'))
        portaluser.delete()
    except Exception as e:
        print(e)
       
    