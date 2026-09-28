from behave import given, when, then
from utils.assertions import assert_status, assert_json_response, assert_has_keys


@given("I authenticate with the Booker API")
def step_authenticate(context):
    context.response = context.api.create_token(
        context.username,
        context.password,
    )
    assert_status(context.response, 200)
    assert context.api.token, "Authentication token was not created"


@when("I create a booking")
def step_create_booking(context):
    context.response = context.api.post(
        "/booking",
        json=context.booking_data,
    )


@then("the booking response status should be {status:d}")
def step_booking_status(context, status):
    assert_status(context.response, status)


@then("the response should contain a booking ID")
def step_booking_id(context):
    body = context.response.json()
    assert "bookingid" in body
    context.booking_id = body["bookingid"]


@then('the booking details should contain "{firstname}" as firstname')
def step_booking_firstname(context, firstname):
    body = context.response.json()
    assert body["booking"]["firstname"] == firstname


@given("I have created a booking")
def step_create_booking_for_scenario(context):
    step_create_booking(context)
    assert_status(context.response, 200)
    context.booking_id = context.response.json()["bookingid"]


@when("I request the created booking")
def step_get_booking(context):
    context.response = context.api.get(
        f"/booking/{context.booking_id}"
    )


@then("the response should contain booking details")
def step_booking_details(context):
    assert_json_response(context.response)
    body = context.response.json()
    assert_has_keys(
        body,
        ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"],
    )


@when('I update the booking firstname to "{firstname}"')
def step_update_booking(context, firstname):
    updated_data = dict(context.booking_data)
    updated_data["firstname"] = firstname

    context.response = context.api.put(
        f"/booking/{context.booking_id}",
        json=updated_data,
    )


@then('the booking firstname should be "{firstname}"')
def step_updated_firstname(context, firstname):
    body = context.response.json()
    assert body["firstname"] == firstname


@when("I delete the created booking")
def step_delete_booking(context):
    context.response = context.api.delete(
        f"/booking/{context.booking_id}"
    )
