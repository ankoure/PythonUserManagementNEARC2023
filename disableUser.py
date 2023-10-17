import fme
import fmeobjects
from arcgis.gis import GIS
gis = GIS(url="PortalURL",username="Username",password= 'Password')

def disableUser(feature):
    try:
        user = gis.users.get(username=feature.getAttribute('baseusername'))
        user.disable()
        return feature
    except Exception as e:
        print(e)