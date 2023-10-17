import fme
import fmeobjects
from arcgis.gis import GIS
gis = GIS(url="PortalURL",username="Username",password= 'Password')

def groupRemover(feature):
    portaluser = gis.users.get(username = feature.getAttribute('baseusername'))
    try:
        if portaluser != None:
            user_groups = portaluser.groups
            for group in user_groups:
                targetgroup = gis.groups.get(group.id)
                targetgroup.remove_users([portaluser])
    except Exception as e:
        print(e)
    return feature