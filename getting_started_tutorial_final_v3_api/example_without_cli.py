# Example code for how to create a new expectation suite without the CLI, using the V3 (Batch Request) API.
# See corresponding documentation at https://docs.greatexpectations.io/en/latest/guides/how_to_guides/creating_and_editing_expectations/how_to_create_a_new_expectation_suite_without_the_cli.html

import great_expectations as ge
from great_expectations.core.batch import BatchRequest

context = ge.data_context.DataContext()
suite = context.create_expectation_suite(
    "my_suite_name", overwrite_existing=True # Configure these parameters for your needs
)

batch_request = BatchRequest(
    datasource_name="data__dir",
    data_connector_name="data__dir_example_data_connector",
    data_asset_name="data_asset_name"
)
validator = context.get_validator(batch_request=batch_request, expectation_suite=suite)

# Start creating Expectations here
validator.expect_column_values_to_not_be_null('passenger_count')

# And save the final state to JSON
validator.save_expectation_suite(discard_failed_expectations=False)
