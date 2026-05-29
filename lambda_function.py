def lambda_handler(event, context):
    ip_address = (
        event.get("requestContext", {}).get("http", {}).get("sourceIp", "unknown")
    )
    print(f"Received IP: {ip_address}")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain",
        },
        "body": f"Your IP address is: {ip_address}",
    }
