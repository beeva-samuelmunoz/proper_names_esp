# -*- coding: utf-8 -*-

from codecs import open
import re

from data.hombres import HOMBRES
from data.mujeres import MUJERES
# from data.lemario import LEMARIO
# pedro, juan, jorge, también son nombres comunes
LEMARIO = {}

class ProperNames(object):

    def __init__(self, threshold=3):
        self.regexfemale=re.compile("[^\w]"+"[^\w]|[^\w]".join(
            [x for x in MUJERES.difference(LEMARIO) if len(x)>threshold]
        )+"[^\w]")
        self.regexmale=re.compile("[^\w]"+"[^\w]|[^\w]".join(
            [x for x in HOMBRES.difference(LEMARIO) if len(x)>threshold]
        )+"[^\w]")
        self.regexfm = re.compile(" mujer hombre ")
        self.regexmf = re.compile(" hombre mujer ")

    def filter_names(self, txt):
        retval = ' '+txt.lower()+' '  # Ñapa por regexp
        retval = self.regexmale.sub(" hombre ", retval)
        retval = self.regexfemale.sub(" mujer ", retval)
        retval = self.regexfm.sub(" mujer ", retval)
        retval = self.regexfm.sub(" hombre ", retval)
        return retval.strip()
