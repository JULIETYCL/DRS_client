import click
import json
import requests

@click.group("cli")
@click.option("--url",default = "172.19.99.130", help = "IP address of the Ubuntu instance")
@click.option("--port", default = "8080", help = "Port number of the server")
@click.pass_context
def cli(ctx, url, port):
    """These are the commands for managing items"""
    ctx.ensure_object(dict)
    base_url = f"http://{url}:{port}/ga4gh/drs/v1/objects"
    ctx.obj["BASE_URL"] = base_url
    ctx.obj["BASE_INFO_URL"] = base_url.replace("object", "service-info")


@cli.command("post")
@click.pass_context
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
def post( ctx,
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
    print("Script is running")
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

    base_url = ctx.obj["BASE_URL"]
    response = requests.post(base_url, data=json.dumps(drs_object_register), headers=headers)
    if response.status_code == 200:
        click.secho("DrsObjectRegister created successfully!", fg = "red")
        res = click.echo(json.loads(response.text))
    else:
        res = click.secho(f"Error: {response.status_code} - {response.text}", fg = "red")
    return res


@cli.command("get")
@click.pass_context
@click.option("--expand", default=False, help="true or false (default: false)")
@click.argument("id")
def get(ctx, id, expand):
    """Get an item"""
    base_url = ctx.obj["BASE_URL"]
    response = requests.get(f"{base_url}/{id}?expand={expand}")
    if response.status_code == 200:
        drs_object = response.json()
        for key, value in drs_object.items():
            click.secho(f'{key}:', fg = 'green',nl = False)
            click.secho(f'{value}',fg = 'yellow')
        return drs_object


@cli.command("delete")
@click.pass_context
@click.argument("id")
def delete(ctx, id):
    """Delete an item"""
    base_url= ctx.obj["BASE_URL"]
    response = requests.delete(f"{base_url}/{id}")
    if response.status_code == 200:
        click.secho("drs object is deleted",fg = "red")
        drs_object = response.json()
        click.secho(f'{drs_object}',fg ="white")
        return drs_object


@cli.command("put")
@click.pass_context
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
def put(ctx,
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

    base_url = ctx.obj["BASE_URL"]

    response = requests.put(f"{base_url}/{id}", data=json.dumps(drs_object_register), headers=headers)

    if response.status_code == 200:
        click.secho("DrsObject is updated successfully!",fg ="green")
        res = click.echo(json.loads(response.text))
    else:
        res = click.secho(f"Error: {response.status_code} - {response.text}", fg = "red")
    return res


@cli.command("access")
@click.pass_context
@click.argument("id", type=str)
@click.argument("access_id", type=str)
def access(ctx, id, access_id):
    """access the URL that can be used to fetch the bytes of a DrsObject"""
    base_url = ctx.obj["BASE_URL"]
    response = requests.get(f"{base_url}/{id}/access/{access_id}")
    if response.status_code == 200:
        obj_url = response.json()
        click.secho(f'{obj_url}', fg = "yellow")
        return obj_url


@cli.command("post_info")
@click.pass_context
@click.option("--contact-url", default="mailto:support@example.com", help="Contact URL")
@click.option("--created-at", default="2019-06-04T12:58:19Z", help="Created At")
@click.argument("description", default="This service provides...")
def post_info(ctx, contactUrl, createdAt, description):
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

    base_info_url = ctx.obj["BASE_INFO_URL"]

    response = requests.post(base_info_url, data=json.dumps(service_info), headers=headers)

    if response.status_code == 201:
        res = click.secho("Service information created successfully!", fg = "green")
    else:
        res = click.secho(f"Error: {response.status_code} - {response.text}", fg = "red")
    return res


@cli.command("get_info")
@click.pass_context
def get_info(ctx):
    """Get service information"""
    base_info_url = ctx.object["BASE_INFO_URL"]
    response = requests.get(base_info_url)
    if response.status_code == 200:
        drs_object = response.json()
        click.echo(drs_object)
        return drs_object


@cli.command("delete_access_id")
@click.pass_context
@click.argument("id", type=str)
@click.argument("access_id", type=str)
def delete_access_id(ctx, id, access_id):
    """Delete existing AccessMethod of DrsObject"""
    base_url = ctx.obj["BASE_URL"]
    response = requests.delete(f"{base_url}/{id}/access/{access_id}")
    if response.status_code == 200:
        drs_response = response.json()
        click.secho("drs object and access is deleted", fg = "red")
        return drs_response
    elif response.status_code in [400, 401, 403, 404, 500]:
        drs_response = response.json()
        click.secho("action is not successful, 400", fg = "red")
        return drs_response

def main():
   cli(prog_name="cli")
 
if __name__ == '__main__':
   main()
