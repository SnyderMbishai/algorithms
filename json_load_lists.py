import json


def json_load_lists(arr):
    for key, value in arr.items():
        if (
            type(value) is str
            and '["' in value
            and '"]' in value
            and type(json.loads(value)) is list
        ):
            arr[key] = json.loads(value)
    return arr


if __name__ == "__main__":
    arr = {
        "city": "f[ds]a",
        "interest": '["a", "b", "c"]',
        "website": "jhgfds.com",
        "company_tax_id": "kjhgfdsa",
        "instagram_handle": "bgvcxz",
        "currently_selling_products_on_a_shopify_site": "bvcxz",
        "shopify_site": "bgvcxz",
        "description": "kjhfds",
        "registration_status": '["a", "b", "c"]',
        "business_classification": '["a", "b", "c"]',
        "current_sales_channels": '["a", "b", "c"]',
        "current_communication_channels_with_buyers": '["a", "b", "c"]',
        "average_wholesale_order_value_usd": 100,
        "minimum_order_value": 100,
        "year_business_was_founded": 1987,
        "year_started_exporting": 1999,
        "average_monthly_unit_capacity": 1234,
        "lead_times": "1236",
        "corporate_values": '["a", "b", "c"]',
        "regions_currently_exporting_to": '["a", "b", "c"]',
        "warehouse_location": '["a", "b", "c"]',
        "current_services_offered": '["a", "b", "c"]',
        "product": '["a", "b", "c"]',
        "number_of_artisans_in_your_network": 123,
        "percentage_of_artisans_women": 123,
        "percentage_of_artisans_fulltime": 123,
    }
    print(json_load_lists(arr))
