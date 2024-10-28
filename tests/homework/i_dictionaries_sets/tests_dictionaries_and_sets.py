import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        self.assertEqual
        (.4, get_p_distance(
            ['T','T','T','C','C','A','T','T','T','A'], 
            ['G','A','T','T','C','A','T','T','T','C']))

    def test_p_distance_matrix(self):

        input_dna = [['T','T','T','C','C','A','T','T','T','A'],
                     ['G','A','T','T','C','A','T','T','T','C'],
                     ['T','T','T','C','C','A','T','T','T','T'],
                     ['G','T','T','C','C','A','T','T','T','A']
        ]
        
        assertion = [[0.0, 0.4, 0.1, 0.1],
                     [0.4, 0.0, 0.4, 0.3],
                     [0.1, 0.4, 0.0, 0.2],
                     [0.1, 0.3, 0.2, 0.0]
        ]

        self.assertEqual(assertion, get_p_distance_matrix(input_dna, 4))