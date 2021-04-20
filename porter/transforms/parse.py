import apache_beam as beam
from apache_beam import DoFn, PTransform


class Parse(PTransform):

    def expand(self, pcoll):
        import logging
        return pcoll | "Parse" >> beam.Map(self.parse_fields)
    
    def parse_fields(self, element, created_timestamp=DoFn.TimestampParam):
        from datetime import datetime
        import logging
        parsed_element = element.decode('utf-8')
        created_datetime = datetime.utcfromtimestamp(float(created_timestamp))
        logging.info(f'timestamp: {created_datetime} \nelement: {parsed_element}')
        return parsed_element