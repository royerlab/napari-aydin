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

from aydin.restoration.denoise.classic import classic_denoise
from aydin.restoration.denoise.noise2selffgr import noise2self_fgr


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

def aydin_classic_denoise(input_image: "napari.types.ImageData"
) -> "napari.types.ImageData":
    return classic_denoise(input_image)

def aydin_noise2self_fgr(input_image: "napari.types.ImageData"
) -> "napari.types.ImageData":
    return noise2self_fgr(input_image)

