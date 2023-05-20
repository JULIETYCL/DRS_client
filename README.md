# Drs Client
The DRS Client is a command-line tool designed for interaction with the Data Repository Service (DRS) Server. While there exists a SwaggerUI client for the DRS server, this tool stands out as a command-line client intended for use on Linux systems. It facilitates a host of actions, including creating, retrieving, updating, and deleting DrsObjects, as well as accessing their associated URLs and posting or retrieving service information. This simplified DRS client code forms a part of my CRYPT4GH internship project. Please note that any sensitive or unauthorized information has been purposely omitted for security purposes.

## How To Use
1. **Setting Up the Environment**: The DRS client runs on Ubuntu. Ensure that your machine has Ubuntu installed. I have utilized Ubuntu (20.04) on WSL2 within a Windows 11 environment. If you're operating a different version of Ubuntu, you may need to modify the relevant files to suit your setup.
2. **Downloading the DRS Server Code**: Access the DRS server code at **_https://github.com/elixir-cloud-aai/drs-filer_**
3. **Running the Server Code**: Execute the server code on your Ubuntu (20.04) using the following command:

```
docker-compose up -d –-build
```

Once the Docker container is constructed, you can verify the container's status using:

```
docker ps

```

If successful, ascertain the IP address for the WSL2 instance with:

```
ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}' 
```

In my case, the IP address is 172.27.46.118, leading to base_url and base_info_url in the functions.py file as shown below. Replace the IP address with your own:

```
base_url = "http://172.27.46.118:8080/ga4gh/drs/v1/objects"
base_info_url = "http://172.27.46.118:8080/ga4gh/drs/v1/service-info"
```

For different versions of Ubuntu, you might face version or port mapping issues, which can be resolved as follows:
 - Modify the base image in the Dockerfile, updating the image tag from 20201114 to a newer version:

 ```
 FROM elixircloud/foca:20201114`
 ```

 - Alter the port mapping in docker-compose.yaml to:

```
 ports:
            - "8081:8080"
```

Consequently, the base URL would change to
`base_url = "http://172.27.46.118:8081/ga4gh/drs/v1/objects"`

4. Once the server is up and running, you can start using the app. For ease of testing, follow these steps: 

(1) post call: `action post` (this call will return a drs object id, e.g. 12345)

(2) get call: `python3 app.py get --id 12345` (you can find the access id from this call, e.g. 0000)

(3) access call: `python3 app.py access --id 12345, --access_id 0000` (this will return an access url)

(4)put call: `python3 app.py put --id 1234 --(any argument you would like to update)`

(5) delete call:`python3 app.py delete --id 1234`

(6) delete_access call: `python3 app.py delete --id 1234 --access_id 0000` (Note: this call does not work on the server side)

(7) post_service_info: `python3 app.py post_service_info --description your info`

(8) get_service_info: `python3 app.py get_service_info`

## Usage 
Below is a description of all the actions available in the command-line client:

`post` - Register metadata of a data object.

`get` - Returns object metadata, and a list of access methods that can be used to fetch object bytes

`delete` - Delete existing DrsObject

`delete_access` - Delete existing AccessMethod of DrsObject.

`put` - Create a DRS object with a predefined ID. Overwrites any existing DRS object with the same ID.

`access` - Returns a URL that can be used to fetch the bytes of a DrsObject. This method only needs to be called when using an AccessMethod that contains an access_id (e.g., for servers that use signed URLs for fetching object bytes).

`post_service_info` - Delete existing AccessMethod of DrsObject.

`get_service_info` - A successful operation to request the service information about this running service.

The development is ongoing, with more functions and features being added. Therefore, this README is also a work in progress. 

