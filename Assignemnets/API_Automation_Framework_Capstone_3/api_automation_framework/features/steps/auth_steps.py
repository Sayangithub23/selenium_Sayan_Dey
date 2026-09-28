from behave import given, when, then
from config.config import USERNAME, PASSWORD
from utils.assertions import assert_status


@given("I have valid Booker credentials")
def step_valid_credentials(context):
    context.username = USERNAME
    context.password = PASSWORD


@when("I request an authentication token")
def step_request_token(context):
    context.response = context.api.create_token(
        context.username,
        context.password,
    )


@then("the authentication response status should be {status:d}")
def step_auth_status(context, status):
    assert_status(context.response, status)


@then("an authentication token should be generated")
def step_token_generated(context):
    body = context.response.json()
    assert body.get("token"), "Authentication token was not generated"
