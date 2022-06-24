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
    return [aydin_denoise]  # [threshold, image_arithmetic]


# using Enums is a good way to get a dropdown menu.  Used here to select from np functions
class Operation(Enum):
    Noise2SelfFGR = noise2self_fgr
    Butterworth = classic_denoise


def aydin_denoise(
    layerA: "napari.types.ImageData", operation: Operation, layerB: "napari.types.ImageData"
) -> "napari.types.LayerDataTuple":
    """Adds, subtracts, multiplies, or divides two same-shaped image layers."""
    return (operation.value(layerA), {"colormap": "turbo"})
