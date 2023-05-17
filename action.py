import json

import click
import requests

base_url = "http://172.27.46.118:8080/ga4gh/drs/v1/objects"
base_info_url = "http://172.27.46.118:8080/ga4gh/drs/v1/service-info"


@click.group()
def cli():
    """These are the commands for managing items"""
    pass


@click.command()
@click.help_option("-h", "--help")
@click.option("--access-url-headers", default=["string"], type=str, multiple=True, help="Access URL Headers")
@click.option("--access-url", default="string", help="Access URL")
@click.option("--access-type", default="s3", help="Access Type")
@click.option("--aliases", default=["string"], type=str, multiple=True, help="Aliases")
@click.option("--checksum", default="string", help="Checksum")
@click.option("--checksum-type", default="sha-256", help="Checksum Type")
@click.option(
    "--drs-uri",
    default=["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
    type=str,
    multiple=True,
    help="DRS URI",
)
@click.option("--contents-id", default="string", help="Contents ID")
@click.option("--contents-name", default="string", help="Contents Name")
@click.option("--created-time", default="2023-04-16T18:56:55.077Z", help="Created Time")
@click.option("--description", default="string", help="Description")
@click.option("--mime-type", default="application/json", help="MIME Type")
@click.option("--name", default="string", help="Name")
@click.option("--size", default=0, help="Size")
@click.option("--updated-time", default="2023-04-16T18:56:55.077Z", help="Updated Time")
@click.option("--version", default="string", help="Version")
def post(
    access_url_headers,
    access_url,
    access_type,
    aliases,
    checksum,
    checksum_type,
    drs_uri,
    contents_id,
    contents_name,
    created_time,
    description,
    mime_type,
    name,
    size,
    updated_time,
    version,
):
    """Post an item"""
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
        "contents": [{"contents": [], "drs_uri": drs_uri, "id": contents_id, "name": contents_name}],
        "created_time": created_time,
        "description": description,
        "mime_type": mime_type,
        "name": name,
        "size": size,
        "updated_time": updated_time,
        "version": version,
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(base_url, data=json.dumps(drs_object_register), headers=headers)

    if response.status_code == 200:
        print("DrsObjectRegister created successfully!")
        res = print(json.loads(response.text))
    else:
        res = print(f"Error: {response.status_code} - {response.text}")
    return res


@click.command()
@click.help_option("-h", "--help")
@click.option("--expand", default=False, help="true or false (default: false)")
@click.argument("id")
def get(id, expand):
    """Get an item"""
    response = requests.get(f"{base_url}/{id}?expand={expand}")
    if response.status_code == 200:
        drs_object = response.json()
        print(drs_object)
        return drs_object


@click.command()
@click.help_option("-h", "--help")
@click.argument("id", help="ID of the item")
def delete(id):
    """Get an item"""
    response = requests.delete(f"{base_url}/{id}")
    if response.status_code == 200:
        print("drs object is deleted")
        drs_object = response.json()
        print(drs_object)
        return drs_object


@click.command()
@click.help_option("-h", "--help")
@click.option("--access-url-headers", default=["string"], type=str, multiple=True, help="Access URL Headers")
@click.option("--access-url", default="string", help="Access URL")
@click.option("--access-type", default="s3", help="Access Type")
@click.option("--aliases", default=["string"], type=str, multiple=True, help="Aliases")
@click.option("--checksum", default="string", help="Checksum")
@click.option("--checksum-type", default="sha-256", help="Checksum Type")
@click.option(
    "--drs-uri",
    default=["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
    type=str,
    multiple=True,
    help="DRS URI",
)
@click.option("--contents-name", default="string", help="Contents Name")
@click.option("--created-time", default="2023-04-16T18:56:55.077Z", help="Created Time")
@click.option("--description", default="string", help="Description")
@click.option("--mime-type", default="application/json", help="MIME Type")
@click.option("--name", default="string", help="Name")
@click.option("--size", default=0, help="Size")
@click.option("--updated-time", default="2023-04-16T18:56:55.077Z", help="Updated Time")
@click.option("--version", default="string", help="Version")
@click.argument("id")
def put(
    id,
    access_url_headers,
    access_url,
    access_type,
    aliases,
    checksum,
    checksum_type,
    drs_uri,
    contents_name,
    created_time,
    description,
    mime_type,
    name,
    size,
    updated_time,
    version,
):
    """Update an item"""
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
        "contents": [{"contents": [], "drs_uri": drs_uri, "id": id, "name": contents_name}],
        "created_time": created_time,
        "description": description,
        "mime_type": mime_type,
        "name": name,
        "size": size,
        "updated_time": updated_time,
        "version": version,
    }

    headers = {"Content-Type": "application/json"}

    response = requests.put(f"{base_url}/{id}", data=json.dumps(drs_object_register), headers=headers)

    if response.status_code == 200:
        print("DrsObject is updated successfully!")
        res = print(json.loads(response.text))
    else:
        res = print(f"Error: {response.status_code} - {response.text}")
    return res


@click.command()
@click.help_option("-h", "--help")
@click.argument("id", type=str, help="ID of the item")
@click.argument("access_id", type=str, help="ID of the item")
def access(id, access_id):
    """access the URL that can be used to fetch the bytes of a DrsObject"""
    response = requests.get(f"{base_url}/{id}/access/{access_id}")
    if response.status_code == 200:
        obj_url = response.json()
        print(obj_url)
        return obj_url


@click.command()
@click.help_option("-h", "--help")
@click.option("--contact-url", default="mailto:support@example.com", help="Contact URL")
@click.option("--created-at", default="2019-06-04T12:58:19Z", help="Created At")
@click.option("--description", default="This service provides...", help="Description")
def post_info(contactUrl, createdAt, description):
    """post service information"""
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

    response = requests.post(base_info_url, data=json.dumps(service_info), headers=headers)

    if response.status_code == 201:
        res = print("Service information created successfully!")
    else:
        res = print(f"Error: {response.status_code} - {response.text}")
    return res


@click.command()
@click.help_option("-h", "--help")
def get_info():
    """Get service information"""
    response = requests.get(base_info_url)
    if response.status_code == 200:
        drs_object = response.json()
        print(drs_object)
        return drs_object


@click.command()
@click.help_option("-h", "--help")
@click.argument("id", type=str, help="id of the item")
@click.argument("access_id", type=str, help="access id of the item")
def delete_access_id(id, access_id):
    """Delete existing AccessMethod of DrsObject"""
    response = requests.delete(f"{base_url}/{id}/access/{access_id}")
    if response.status_code == 200:
        drs_response = response.json()
        print("drs object and access is deleted")
        return drs_response
    elif response.status_code in [400, 401, 403, 404, 500]:
        drs_response = response.json()
        print("action is not successful, 400")
        return drs_response
