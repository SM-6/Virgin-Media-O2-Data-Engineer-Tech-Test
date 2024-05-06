import unittest
import apache_beam as beam
from datetime import datetime
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that
from apache_beam.testing.util import equal_to
from composite_transform_pipeline_task2 import SumAmountsByDateCompositeTransform



class TestSumAmountsByDateCompositeTransform(unittest.TestCase):
    
    def test_transform(self):
        input_data = [
            '2010-01-01 00:00:00 UTC,wallet1,wallet2,1000.00',
            '2010-01-01 00:00:00 UTC,wallet2,wallet3,200.00',
            '2009-01-01 00:00:00 UTC,wallet3,wallet4,300.00',  
            '2011-01-01 00:00:00 UTC,wallet4,wallet5,400.00'
        ]

        expected_output = [
            '2010-01-01, 1200.0',
            '2011-01-01, 400.0'
        ]

        with TestPipeline() as p:
            input_pcoll = p | beam.Create(input_data)
            output_pcoll = input_pcoll | SumAmountsByDateCompositeTransform()
            assert_that(output_pcoll, equal_to(expected_output))

if __name__ == '__main__':
    unittest.main()
