# transformer-combine-rows

Combines two fields from each input row into one value using a configurable separator.

## Behavior

For each mapped row, the transformer reads `a` and `b` and returns
`{"value": "<a><delimiter><b>"}`. The `delimiter` hyperparameter defaults to `|`.

- `{"a": "hello", "b": "world"}` becomes `{"value": "hello|world"}`.
- Empty strings are retained, including the separator.
- Values are converted to strings using Python's string formatting.
- The number of input rows stays the same.

Configure row mappings with `input_mapping={"a": "first_column", "b": "second_column"}`
and `return_mapping={"value": "combined_column"}`. Leave `column` unset to use
row transformation mode.

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs in .env before connecting.
python main.py
```

The Docker base image provides the FL-Net API. `requirements.txt` contains only
additional runtime dependencies; `requirements-dev.txt` includes the API for local development.

Build with `docker build -t tool-transformer-combine-rows .`.
