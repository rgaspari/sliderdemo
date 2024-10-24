from ._anvil_designer import MainTemplate
from anvil import *

class Main(MainTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def slider_1_change(self, **event_args):
    self.label_4.text = self.slider_1.level

  def slider_2_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_3.text = self.slider_2.level

  def reset_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.slider_1.level = 1
    self.slider_2.level = 1
    self.label_4.text = 1
    self.label_3.text = 1



