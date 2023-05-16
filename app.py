import argparse

import functions


def main():
    # Create argument parser and subparsers for each action
    parser = argparse.ArgumentParser(description="Choose an action: post/get/delete")
    subparsers = parser.add_subparsers(dest="action")

    # DataRepositoryService
    # GET action arguments
    get_parser = subparsers.add_parser("get", help="Get an item")
    # Add arguments for the get action
    get_parser.add_argument("--id", type=str, required=True, help="ID of the item")
    get_parser.add_argument("--expand", help="true or false (default: false)", action="store_true", default=False)

    # ACCESS action arguments
    access_parser = subparsers.add_parser(
        "access", help="access the URL that can be used to fetch the bytes of a DrsObject"
    )
    # Add arguments for the access action
    access_parser.add_argument("--id", type=str, required=True, help="ID of the item")
    access_parser.add_argument("--access", type=str, required=True, help="ID of the item")

    # DRS-Filer
    # POST action arguments
    post_parser = subparsers.add_parser("post", help="Post an item")
    # Add arguments for the post action
    post_parser.add_argument(
        "--access_url_headers",
        type=str,
        nargs="+",
        default=["string"],
        help="List of access URL headers (default: ['string'])",
    )
    post_parser.add_argument("--access_url", type=str, default="string", help="Access URL (default: 'string')")
    post_parser.add_argument("--access_type", type=str, default="s3", help="Access type (default: 's3')")
    post_parser.add_argument(
        "--aliases", type=str, nargs="+", default=["string"], help="List of aliases (default: ['string'])"
    )
    post_parser.add_argument("--checksum", type=str, default="string", help="Checksum (default: 'string')")
    post_parser.add_argument("--checksum_type", type=str, default="sha-256", help="Checksum type (default: 'sha-256')")
    post_parser.add_argument(
        "--drs_uri",
        type=str,
        nargs="+",
        default=["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
        help="List of DRS URIs (default: ['drs://drs.example.org/314159', 'drs://drs.example.org/213512'])",
    )
    post_parser.add_argument("--contents_id", type=str, default="string", help="Contents ID (default: 'string')")
    post_parser.add_argument("--contents_name", type=str, default="string", help="Contents name (default: 'string')")
    post_parser.add_argument(
        "--created_time",
        type=str,
        default="2023-04-16T18:56:55.077Z",
        help="Created time in RFC3339 format (default: '2023-04-16T18:56:55.077Z')",
    )
    post_parser.add_argument("--description", type=str, default="string", help="Description (default: 'string')")
    post_parser.add_argument(
        "--mime_type", type=str, default="application/json", help="MIME type (default: 'application/json')"
    )
    post_parser.add_argument("--name", type=str, default="string", help="Name (default: 'string')")
    post_parser.add_argument("--size", type=int, default=0, help="Size (default: 0)")
    post_parser.add_argument(
        "--updated_time",
        type=str,
        default="2023-04-16T18:56:55.077Z",
        help="Updated time in RFC3339 format (default: '2023-04-16T18:56:55.077Z')",
    )
    post_parser.add_argument("--version", type=str, default="string", help="Version (default: 'string')")

    # DELETE action arguments
    delete_parser = subparsers.add_parser("delete", help="delete an item")
    delete_parser.add_argument("--id", type=str, required=True, help="ID of the item")

    # PUT action arguments
    put_parser = subparsers.add_parser("put", help="update an item")
    put_parser.add_argument("--id", type=str, required=True, help="ID of the item")
    put_parser.add_argument(
        "--access_url_headers",
        type=str,
        nargs="+",
        default=["string"],
        help="List of access URL headers (default: ['string'])",
    )
    put_parser.add_argument("--access_url", type=str, default="string", help="Access URL (default: 'string')")
    put_parser.add_argument("--access_type", type=str, default="s3", help="Access type (default: 's3')")
    put_parser.add_argument(
        "--aliases", type=str, nargs="+", default=["string"], help="List of aliases (default: ['string'])"
    )
    put_parser.add_argument("--checksum", type=str, default="string", help="Checksum (default: 'string')")
    put_parser.add_argument("--checksum_type", type=str, default="sha-256", help="Checksum type (default: 'sha-256')")
    put_parser.add_argument(
        "--drs_uri",
        type=str,
        nargs="+",
        default=["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
        help="List of DRS URIs (default: ['drs://drs.example.org/314159', 'drs://drs.example.org/213512'])",
    )
    put_parser.add_argument("--contents_name", type=str, default="string", help="Contents name (default: 'string')")
    put_parser.add_argument(
        "--created_time",
        type=str,
        default="2023-04-16T18:56:55.077Z",
        help="Created time in RFC3339 format (default: '2023-04-16T18:56:55.077Z')",
    )
    put_parser.add_argument("--description", type=str, default="string", help="Description (default: 'string')")
    put_parser.add_argument(
        "--mime_type", type=str, default="application/json", help="MIME type (default: 'application/json')"
    )
    put_parser.add_argument("--name", type=str, default="string", help="Name (default: 'string')")
    put_parser.add_argument("--size", type=int, default=0, help="Size (default: 0)")
    put_parser.add_argument(
        "--updated_time",
        type=str,
        default="2023-04-16T18:56:55.077Z",
        help="Updated time in RFC3339 format (default: '2023-04-16T18:56:55.077Z')",
    )
    put_parser.add_argument("--version", type=str, default="string", help="Version (default: 'string')")

    # Delete access url
    delete_access_parser = subparsers.add_parser("delete_access", help="Delete existing AccessMethod of DrsObject")
    delete_access_parser.add_argument("--id", type=str, required=True, help="id of the item")
    delete_access_parser.add_argument("--access_id", type=str, required=True, help="access id of the item")

    # POST SERVICE INFO action arguments
    post_info_parser = subparsers.add_parser("post_service_info", help="Post service information")
    post_info_parser.add_argument("--contact_url", type=str, default="string", help="contact URL (default: 'string')")
    post_info_parser.add_argument("--description", type=str, default="string", help="Description (default: 'string')")
    post_info_parser.add_argument(
        "--createdAt",
        type=str,
        default="2023-04-16T18:56:55.077Z",
        help="created time in RFC3339 format (default: '2023-04-16T18:56:55.077Z')",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the chosen action.
    if args.action == "post":
        functions.post_function(
            access_url_headers=args.access_url_headers,
            access_url=args.access_url,
            access_type=args.access_type,
            aliases=args.aliases,
            checksum=args.checksum,
            checksum_type=args.checksum_type,
            drs_uri=args.drs_uri,
            contents_id=args.contents_id,
            contents_name=args.contents_name,
            created_time=args.created_time,
            description=args.description,
            mime_type=args.mime_type,
            name=args.name,
            size=args.size,
            updated_time=args.updated_time,
            version=args.version,
        )
    elif args.action == "get":
        functions.get_function(id=args.id, expand=args.expand)
    elif args.action == "delete":
        functions.delete_function(id=args.id)
    elif args.action == "put":
        functions.put_function(
            id=args.id,
            access_url_headers=args.access_url_headers,
            access_url=args.access_url,
            access_type=args.access_type,
            aliases=args.aliases,
            checksum=args.checksum,
            checksum_type=args.checksum_type,
            drs_uri=args.drs_uri,
            contents_name=args.contents_name,
            created_time=args.created_time,
            description=args.description,
            mime_type=args.mime_type,
            name=args.name,
            size=args.size,
            updated_time=args.updated_time,
            version=args.version,
        )
    elif args.action == "access":
        functions.access_function(id=args.id, access_id=args.access)
    elif args.action == "post_service_info":
        functions.post_info_function(
            contactUrl=args.contact_url, createdAt=args.createdAt, description=args.description
        )
    elif args.action == "get_service_info":
        functions.get_info_function()
    elif args.action == "delete_access":
        functions.delete_access_id(id=args.id, access_id=args.access_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
