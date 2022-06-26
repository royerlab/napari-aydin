"""
This module is an example of a barebones function plugin for napari

It implements the ``napari_experimental_provide_function`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation

from napari_tools_menu import register_function


if TYPE_CHECKING:
    import napari


# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    # we can return a single function
    # or a tuple of (function, magicgui_options)
    # or a list of multiple functions with or without options, as shown here:
    return [aydin_classic_denoise, aydin_noise2self_fgr]


@register_function(menu="Filtering / noise removal > Classic denoise (aydin)")
def aydin_classic_denoise(input_image: "napari.types.ImageData"
) -> "napari.types.ImageData":
    from aydin.restoration.denoise.classic import classic_denoise
    return classic_denoise(input_image, variant='butterworth')


@register_function(menu="Filtering / noise removal > noise2self (fgr, aydin)")
def aydin_noise2self_fgr(input_image: "napari.types.ImageData"
) -> "napari.types.ImageData":
    from aydin.restoration.denoise.noise2selffgr import noise2self_fgr
    return noise2self_fgr(input_image)

