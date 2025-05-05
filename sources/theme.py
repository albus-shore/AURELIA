from gradio.themes.soft import Soft
from gradio.themes.utils import colors, fonts, sizes
from typing import Iterable

class AURELIA(Soft):
    '''The class is defined for create AURELIA theme.'''
    def __init__(self):
        super().__init__()
        super().set(background_fill_primary='#0C1628',
                    background_fill_primary_dark='#0C1628')