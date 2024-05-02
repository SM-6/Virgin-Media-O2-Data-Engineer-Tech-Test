import apache_beam as beam
from datetime import datetime

class CheckTimestampYear(beam.DoFn):
    def process(self, element):
        timestamp_str = element.split(',')[0]  
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S %Z')
        if timestamp.year >= 2010:
            yield element

class ExtractDateAmount(beam.DoFn):
    def process(self, element):
        timestamp_str, _, _, amount_str = element.split(',')
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S %Z')
        amount = float(amount_str)
        date = timestamp.strftime('%Y-%m-%d')
        yield (date, amount)

class FormatOutput(beam.DoFn):
    def process(self, element):
        date, total_amount = element
        yield f'{date}, {total_amount}'

class SumAmountsByDate(beam.PTransform):
    def expand(self, pcoll):
        return (
            pcoll
            | 'Filter transactions for year' >> beam.ParDo(CheckTimestampYear())
            | 'Extract date and amount' >> beam.ParDo(ExtractDateAmount()) 
            | 'Sum amounts by date' >> beam.CombinePerKey(sum)  #GROUP BY 
            | 'Format output' >> beam.ParDo(FormatOutput())
        )

with beam.Pipeline() as pipeline:
    data = (
        pipeline
        | 'Read CSV file' >> beam.io.ReadFromText('/Users/Shehryar/Downloads/transactions.csv',  skip_header_lines=1)
        | 'Sum amounts by date' >> SumAmountsByDate()
        | 'Write to CSV file' >> beam.io.WriteToText('output/summed_amounts_v4', file_name_suffix='.csv', header='date, total_amount')
    )
