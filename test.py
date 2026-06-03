from lambda_function import lambda_handler

event = {
    "name": "Mercy"
}

output = lambda_handler(event, None)

print(output)
