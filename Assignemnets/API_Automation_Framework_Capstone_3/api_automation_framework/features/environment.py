import allure
from utils.api_client import APIClient


def before_scenario(context, scenario):
    context.api = APIClient()
    context.response = None
    context.booking_id = None
    context.booking_data = {
        "firstname": "Sayan",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-10",
        },
        "additionalneeds": "Breakfast",
    }


def after_step(context, step):
    # Attach API response details to Allure after every step.
    if getattr(context, "response", None) is not None:
        response = context.response
        allure.attach(
            str(response.status_code),
            name="HTTP Status",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
            if "application/json" in response.headers.get("Content-Type", "")
            else allure.attachment_type.TEXT,
        )


def after_scenario(context, scenario):
    if getattr(context, "response", None) is not None:
        allure.attach(
            str(context.response.request.method),
            name="HTTP Method",
            attachment_type=allure.attachment_type.TEXT,
        )
        allure.attach(
            str(context.response.url),
            name="Request URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )
