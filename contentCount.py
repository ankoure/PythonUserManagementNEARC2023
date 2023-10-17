import fme
import fmeobjects
from arcgis.gis import GIS
gis = GIS(url="PortalURL",username="Username",password= 'Password')

def contentCount(feature):
    qe = f"owner: {feature.getAttribute('baseusername')}"
    content_count = gis.content.advanced_search(query=qe,return_count=True)
    print(content_count)
    feature.setAttribute('contentOwned', content_count)
    return feature
