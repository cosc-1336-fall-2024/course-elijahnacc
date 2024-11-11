import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
       
       test_values : list = [10, 25, -10]
       expected_value : int = 0
       
       test_dictionary : dict = {}
       widget_name : str = "Widget1"
       
       for i in range(len(test_values)):

        expected_value += test_values[i]
        quantity : int = test_values[i]
        
        add_inventory(test_dictionary, widget_name, quantity)

        self.assertEqual({widget_name : expected_value}, test_dictionary)

    def test_remove_inventory_widget(self):
       
       widget_inventory : dict = {"Widget1" : 7, "Widget2" : 12}
       remove_inventory_widget(widget_inventory, "Widget1")
       self.assertEqual(1, len(widget_inventory))
       self.assertEqual(True, "Widget2" in widget_inventory)