from matplotlib.path import Path as mpl_path
from galstreams import Track6D


class trackClass(): #borrow from galstreams?

class pawprintClass(dict):
    '''Dictionary class to store a "pawprint": polygons in multiple observational spaces that define an initial selection used for stream track modeling, membership calculation / density modeling, or background modeling.'''

    def __init__(self):
        self.skyprint = {} #polygon(s) in stream coordinates phi1, phi2? or angular width along track as fn of phi1?
        self.streamspec = {} #rotation matrix to transform from ??? to phi1/phi2
        self.cmdprint = {} #polygon(s) in cmd space
        self.cmdspec = {} #some kind of specification for which colors and mags?
        self.pmprint = {} #polygon(s) in proper-motion space
        self.pmspec = {} #some way to specify which PM coordinates the polygons are functions of

        #do we want to put tracks in here too? or have separate model for those?
        self.skytrack = {} #polynomial function returns phi2(phi1)
        self.cmdtrack = {} #polynomial function returns ??
        self.pmtrack = {} #polynomial functions return [pm1, pm2](phi1)
        self.distancetrack = {} #polynomial function returns distance(phi1)
        self.rvtrack = {} #polynomial function returns rv(phi1)
        
    def _inside_poly(data, vertices):
        '''This function takes a list of points (data) and returns a boolean mask that is True for all points inside the polygon defined by vertices'''
        return mpl_path(vertices).contains_points(data)

    def in_pawprint(self, data):
        '''take in some data and return masks for stuff in the pawprint (basically by successively applying _inside_poly)'''

    def save_pawprint(self):
        '''save as YAML (Eduardo)'''

