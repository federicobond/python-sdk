
from behave import given, when, then
from open_feature.open_feature_api import get_client, get_provider, set_provider


# Common step definitions

client = None
@given('a provider is registered with cache {cache_status}')
def step_given_provider_with_cache(context, cache_status):
    # Setup a provider with caching enabled, for now we do nothing as implementation doesn't exist.
    context.client = get_client(name="Default Provider", version="1.0")

@given('a {flag_type} flag with key "{key}" is evaluated with {eval_details} and default value "{default_value}"')
def step_given_flag_is_evaluated(context, flag_type, key, eval_details, default_value):
    raise NotImplementedError("Step definition not implemented yet")

@when('a boolean flag with key "{key}" is evaluated with {eval_details} and default value "{default_value}"')
def step_when_flag_is_evaluated(context, flag_type, key, eval_details, default_value):
    context.client.set_boolean()

@then('the resolved boolean details reason of flag with key "{key}" should be "{reason}"')
def step_then_flag_reason_should_be(context, flag_type, key, reason):


# Flag evaluation step definitions

@then('the resolved {flag_type} value should be "{expected_value}"')
@then('the resolved {flag_type} details value should be "{expected_value}", the variant should be "{variant}", and the reason should be "{reason}"')
def step_then_resolved_flag_details(context, flag_type, expected_value, variant=None, reason=None):
    if variant is None and reason is None:
        # Handle the case where only flag_type and expected_value are specified
        pass
    else:
        # Handle the case where flag_type, expected_value, variant, and reason are all specified
        pass
    raise NotImplementedError("Step definition not implemented yet")

@then('the resolved object value should be contain fields "{field1}", "{field2}", and "{field3}", with values "{val1}", "{val2}" and {val3}, respectively')
def step_then_resolved_object_value_should_contain_fields(context, field1, field2, field3, val1, val2, val3):
    raise NotImplementedError("Step definition not implemented yet")

@then('the resolved flag value is "{flag_value}" when the context is empty')
def step_then_resolved_flag_value_when_context_empty(context, flag_value):
    raise NotImplementedError("Step definition not implemented yet")

@then('the reason should indicate an error and the error code should indicate a missing flag with "{error_code}"')
def step_then_reason_should_indicate_missing_flag_error(context, error_code):
    raise NotImplementedError("Step definition not implemented yet")

@then('the default {flag_type} value should be returned')
def step_then_default_value_should_be_returned(context, flag_type):
    raise NotImplementedError("Step definition not implemented yet")

# Flag caching step definitions

@given('the flag\'s configuration with key "{key}" is updated to defaultVariant "{variant}"')
def step_given_flag_configuration_updated(context, key, variant):
    raise NotImplementedError("Step definition not implemented yet")

@given('sleep for {duration} milliseconds')
def step_given_sleep(context, duration):
    raise NotImplementedError("Step definition not implemented yet")

@then('the resolved string details reason should be "{reason}"')
def step_then_resolved_string_details_reason_should_be(context, reason):
    raise NotImplementedError("Step definition not implemented yet")
