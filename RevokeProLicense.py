import fme
import fmeobjects
from arcgis.gis import GIS

gis = GIS(url="PortalURL",username="Username",password= 'Password')

def license_revoker(feature):
    try:
        pro_license = gis.admin.license.get('ArcGIS Pro')
        pro_license.assign(username=feature.getAttribute('baseusername'), entitlements=[])
    except Exception as e: 
        print(e)