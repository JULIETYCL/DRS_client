import json
import requests


base_url = "http://172.27.46.118:8080/ga4gh/drs/v1/objects"
base_info_url = "http://172.27.46.118:8080/ga4gh/drs/v1/service-info"


def post_function(
    access_url_headers=["string"],
    access_url="string",
    access_type="s3",
    aliases=["string"],
    checksum="string",
    checksum_type="sha-256",
    drs_uri=["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
    contents_id="string",
    contents_name="string",
    created_time="2023-04-16T18:56:55.077Z",
    description="string",
    mime_type="application/json",
    name="string",
    size=0,
    updated_time="2023-04-16T18:56:55.077Z",
    version="string",
):
    drs_object_register = {
        "access_methods": [
            {
                "access_url": {"headers": access_url_headers, "url": access_url},
                "region": "us-east-1",
                "type": access_type,
            }
        ],
        "aliases": aliases,
        "checksums": [{"checksum": checksum, "type": checksum_type}],
        "contents": [
            {
                "contents": [],
                "drs_uri": drs_uri,
                "id": contents_id,
                "name": contents_name,
            }
        ],
        "created_time": created_time,
        "description": description,
        "mime_type": mime_type,
        "name": name,
        "size": size,
        "updated_time": updated_time,
        "version": version,
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(
        base_url, data=json.dumps(drs_object_register), headers=headers
    )

    if response.status_code == 200:
        print("DrsObjectRegister created successfully!")
        res = print(json.loads(response.text))
    else:
        res = print(f"Error: {response.status_code} - {response.text}")
    return res


def get_function(id, expand):
    response = requests.get(f"{base_url}/{id}?expand={expand}")
    if response.status_code == 200:
        drs_object = response.json()
        print(drs_object)
        return drs_object


def delete_function(id):
    response = requests.delete(f"{base_url}/{id}")
    if response.status_code == 200:
        print("drs object is deleted")
        drs_object = response.json()
        print(drs_object)
        return drs_object


def put_function(
    id,
    access_url_headers=["string"],
    access_url="string",
    access_type="s3",
    aliases=["string"],
    checksum="string",
    checksum_type="sha-256",
    drs_uri=["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
    contents_name="string",
    created_time="2023-04-16T18:56:55.077Z",
    description="string",
    mime_type="application/json",
    name="string",
    size=0,
    updated_time="2023-04-16T18:56:55.077Z",
    version="string",
):
    drs_object_register = {
        "access_methods": [
            {
                "access_url": {"headers": access_url_headers, "url": access_url},
                "region": "us-east-1",
                "type": access_type,
            }
        ],
        "aliases": aliases,
        "checksums": [{"checksum": checksum, "type": checksum_type}],
        "contents": [
            {"contents": [], "drs_uri": drs_uri, "id": id, "name": contents_name}
        ],
        "created_time": created_time,
        "description": description,
        "mime_type": mime_type,
        "name": name,
        "size": size,
        "updated_time": updated_time,
        "version": version,
    }

    headers = {"Content-Type": "application/json"}

    response = requests.put(
        f"{base_url}/{id}", data=json.dumps(drs_object_register), headers=headers
    )

    if response.status_code == 200:
        print("DrsObject is updated successfully!")
        res = print(json.loads(response.text))
    else:
        res = print(f"Error: {response.status_code} - {response.text}")
    return res


def access_function(id, access_id):
    response = requests.get(f"{base_url}/{id}/access/{access_id}")
    if response.status_code == 200:
        obj_url = response.json()
        print(obj_url)
        return obj_url


def post_info_function(
    contactUrl="mailto:support@example.com",
    createdAt="2019-06-04T12:58:19Z",
    description="This service provides...",
):
    service_info = {
        "contactUrl": contactUrl,
        "createdAt": createdAt,
        "description": description,
        "documentationUrl": "https://docs.myservice.example.com",
        "environment": "test",
        "id": "org.ga4gh.myservice",
        "name": "My project",
        "organization": {"name": "My organization", "url": "https://example.com"},
        "type": {"artifact": "beacon", "group": "org.ga4gh", "version": "1.0.0"},
        "updatedAt": "2019-06-04T12:58:19Z",
        "version": "1.0.0",
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(
        base_info_url, data=json.dumps(service_info), headers=headers
    )

    if response.status_code == 201:
        res = print("Service information created successfully!")
    else:
        res = print(f"Error: {response.status_code} - {response.text}")
    return res


def get_info_function():
    response = requests.get(base_info_url)
    if response.status_code == 200:
        drs_object = response.json()
        print(drs_object)
        return drs_object


def delete_access_id(id, access_id):
    response = requests.delete(f"{base_url}/{id}/access/{access_id}")
    if response.status_code == 200:
        drs_response = response.json()
        print("drs object and access is deleted")
        return drs_response
    elif response.status_code == 400:
        drs_response = response.json()
        print("action is not successful, 400")
        return drs_response
    elif response.status_code == 401:
        drs_response = response.json()
        print("action is not successful,401")
        return drs_response
    elif response.status_code == 403:
        drs_response = response.json()
        print("action is not successful, 403")
        return drs_response
    elif response.status_code == 404:
        drs_response = response.json()
        print("action is not successful, 404")
        return drs_response
    elif response.status_code == 500:
        drs_response = response.json()
        print("action is not successful, 500")
        return drs_response
