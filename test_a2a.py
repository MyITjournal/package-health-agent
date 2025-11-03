import requests
import json

# Test A2A endpoint
url = "http://localhost:8000/a2a"

# Test 1: Help message
print("Test 1: Asking for help...")
request_data = {
    "jsonrpc": "2.0",
    "id": "test-1",
    "method": "message/send",
    "params": {
        "message": {
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": "help"
                }
            ]
        },
        "configuration": {
            "blocking": True
        }
    }
}

response = requests.post(url, json=request_data)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# Test 2: Analyze Python packages
print("Test 2: Analyzing Python packages...")
request_data = {
    "jsonrpc": "2.0",
    "id": "test-2",
    "method": "message/send",
    "params": {
        "message": {
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": "Check these Python packages: flask==2.0.1, requests==2.25.0"
                }
            ]
        },
        "configuration": {
            "blocking": True
        }
    }
}

response = requests.post(url, json=request_data)
print(f"Status: {response.status_code}")
result = response.json()
if "result" in result and "status" in result["result"]:
    message_text = result["result"]["status"]["message"]["parts"][0]["text"]
    print(f"Agent Response:\n{message_text}\n")

# Test 3: Analyze npm packages
print("Test 3: Analyzing npm packages...")
request_data = {
    "jsonrpc": "2.0",
    "id": "test-3",
    "method": "message/send",
    "params": {
        "message": {
            "role": "user",
            "parts": [
                {
                    "kind": "text",
                    "text": "Analyze npm: express@4.17.1, axios@0.21.1"
                }
            ]
        },
        "configuration": {
            "blocking": True
        }
    }
}

response = requests.post(url, json=request_data)
print(f"Status: {response.status_code}")
result = response.json()
if "result" in result and "status" in result["result"]:
    message_text = result["result"]["status"]["message"]["parts"][0]["text"]
    print(f"Agent Response:\n{message_text}\n")
