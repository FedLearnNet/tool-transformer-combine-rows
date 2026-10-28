from typing import Any

from pydantic.dataclasses import dataclass
from pyfedappwrap.transformation.base_transformer import BaseTransformerAPP
from pyfedappwrap.transformation.config.transformer_config import BaseTransformerConfig


@dataclass
class TransformerConfig(BaseTransformerConfig):
    delimiter: str = '|'


class TransformerCombineRows(BaseTransformerAPP[TransformerConfig]):
    def __init__(self):
        super().__init__()

    def transform(self, row) -> dict[str, str | Any]:
        """
           Combine two string values from the input row using the specified delimiter.

           Args:
               row (dict): Input dictionary containing 'a' and 'b' keys with values to combine

           Returns:
               dict: Dictionary containing the combined string with key 'value'

           Examples:
               >>> transform({'a': 'hello', 'b': 'world'})
               {'value': 'hello|world'}
           """
        a = row['a']
        b = row['b']
        value = f"{a}{self.config.delimiter}{b}"
        self.logger.debug("Combined Row")
        return {'value': value}
