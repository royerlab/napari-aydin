"""
This module is an example of a barebones QWidget plugin for napari

It implements the ``napari_experimental_provide_dock_widget`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox
from qtpy.QtGui import QPixmap
from aydin.restoration.denoise.classic import classic_denoise
from aydin.restoration.denoise.noise2selffgr import noise2self_fgr


# class Aydin(QWidget):
#     """
#     Aydin is a user-friendly, feature-rich, and fast image denoising
#     tool that provides a number of self-supervised, auto-tuned, and
#     unsupervised image denoising algorithms. Aydin handles from the
#     get-go n-dimensional array-structured images with an arbitrary
#     number of batch dimensions, channel dimensions, and typically
#     up to 4 spatio-temporal dimensions.
#     """
#     # your QWidget.__init__ can optionally request the napari viewer instance
#     # in one of two ways:
#     # 1. use a parameter called `napari_viewer`, as done here
#     # 2. use a type annotation of 'napari.viewer.Viewer' for any parameter
#     def __init__(self, napari_viewer):
#         super().__init__()
#         self.setLayout(QVBoxLayout())
#
#         self.viewer = napari_viewer
#
#         # logo
#         logo_layout = QHBoxLayout()
#         logo_layout.setAlignment(Qt.AlignCenter)
#         pixmap = QPixmap('src/napari_aydin/resources/aydin_logo.png')
#         logo_label = QLabel()
#         logo_label.setPixmap(pixmap.scaled(pixmap.width() // 2, pixmap.height() // 2))
#
#         logo_layout.addWidget(logo_label)
#         self.layout().addLayout(logo_layout)
#
#         # description label
#         description_label = QLabel(self.__doc__)
#         description_label.setWordWrap(True)
#
#         self.layout().addWidget(description_label)
#
#         # variant selection
#         variant_selection_layout = QHBoxLayout()
#         variant_selection_layout.setAlignment(Qt.AlignLeft)
#         variant_label = QLabel("Variant: ")
#         variant_selection_layout.addWidget(variant_label)
#
#         self.variant_combobox = QComboBox()
#         self.available_variants = {
#             "Classic-Butterworth": classic_denoise,
#             "Noise2Self-FGR-Catboost": noise2self_fgr
#         }
#         self.variant_combobox.addItems(list(self.available_variants.keys()))
#         variant_selection_layout.addWidget(self.variant_combobox)
#
#         self.layout().addLayout(variant_selection_layout)
#
#         # denoise button
#         btn = QPushButton("Denoise")
#         btn.clicked.connect(self._on_click)
#
#         self.layout().addWidget(btn)
#
#         # for more and contact us
#         for_more_label = QLabel("For more information about Aydin: <a href='https://royerlab.github.io/aydin/'>https://royerlab.github.io/aydin/ </a>")
#         for_more_label.setTextFormat(Qt.RichText)
#         for_more_label.setOpenExternalLinks(True)
#
#         self.layout().addWidget(for_more_label)
#
#     def _on_click(self):
#         print("napari has", len(self.viewer.layers), "layers")
#
#         denoise_method = self.available_variants[self.variant_combobox.currentText()]
#
#         for layer_idx in range(len(self.viewer.layers)):
#             layer = self.viewer.layers[layer_idx]
#             print(layer.name, layer.data.shape)
#             denoised = denoise_method(layer.data)
#             self.viewer.add_image(denoised, name=layer.name + "_denoised")


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    # you can return either a single widget, or a sequence of widgets
    return []
