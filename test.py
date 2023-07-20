from drs import (
    post_function,
    get_function,
    delete_function,
    put_function,
    access_function,
    post_info_function,
    get_info_function,
    delete_access_id_function
)
import unittest
from jsonschema import validate


class TestClick(unittest.TestCase):
    def test_post(self):
        post_return = post_function(
            "172.29.88.59",
            "8080",
            ["string"],
            "string",
            "s3",
            ["string"],
            "string",
            "sha-256",
            ["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
            "string",
            "string",
            "2023-04-16T18:56:55.077Z",
            "string",
            "application/json",
            "string",
            0,
            "2023-04-16T18:56:55.077Z",
            "string",
        )
        self.assertRegex(post_return, "\S", "The response is wrong")
        return post_return

    def test_get(self):
        get_return = get_function("172.29.88.59", "8080", "Uu4xZq", False)
        schema = {
            "type": "object",
            "properties": {
                "access_methods": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "access_id": {"type": "string"},
                                "access_url": {
                                    "type": "object",
                                    "properties": {
                                        "headers": {
                                            "type": "array",
                                            "items": [{"type": "string"}],
                                        },
                                        "url": {"type": "string"},
                                    },
                                    "required": ["headers", "url"],
                                },
                                "region": {"type": "string"},
                                "type": {"type": "string"},
                            },
                            "required": ["access_id", "access_url", "region", "type"],
                        }
                    ],
                },
                "aliases": {"type": "array", "items": [{"type": "string"}]},
                "checksums": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "checksum": {"type": "string"},
                                "type": {"type": "string"},
                            },
                            "required": ["checksum", "type"],
                        }
                    ],
                },
                "contents": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "contents": {"type": "array", "items": {}},
                                "drs_uri": {
                                    "type": "array",
                                    "items": [{"type": "string"}, {"type": "string"}],
                                },
                                "id": {"type": "string"},
                                "name": {"type": "string"},
                            },
                            "required": ["contents", "drs_uri", "id", "name"],
                        }
                    ],
                },
                "created_time": {"type": "string"},
                "description": {"type": "string"},
                "id": {"type": "string"},
                "mime_type": {"type": "string"},
                "name": {"type": "string"},
                "self_uri": {"type": "string"},
                "size": {"type": "integer"},
                "updated_time": {"type": "string"},
                "version": {"type": "string"},
            },
            "required": [
                "access_methods",
                "aliases",
                "checksums",
                "contents",
                "created_time",
                "description",
                "id",
                "mime_type",
                "name",
                "self_uri",
                "size",
                "updated_time",
                "version",
            ],
        }
        validate(instance=get_return, schema=schema)

    def test_delete(self):
        delete_return = delete_function("172.29.88.59", "8080", "0D~o6L")
        self.assertRegex(delete_return, "\S", "The response is wrong")

    def test_put(self):
        put_return = put_function(
            "172.29.88.59",
            "8080",
            "0D~o6L",
            ["string"],
            "string",
            "s3",
            ["string"],
            "string",
            "sha-256",
            ["drs://drs.example.org/314159", "drs://drs.example.org/213512"],
            "string",
            # "string",
            "2023-04-16T18:56:55.077Z",
            "string",
            "application/json",
            "string",
            0,
            "2023-04-16T18:56:55.077Z",
            "string",
        )
        self.assertRegex(put_return, "\S", "The response is wrong")

    def test_access(self):
        access_return = access_function("172.29.88.59", "8080", "Uu4xZq", "P1bu4x")
        accessSchema = {
            "type": "object",
            "properties": {
                "headers": {"type": "array", "items": [{"type": "string"}]},
                "url": {"type": "string"},
            },
            "required": ["headers", "url"],
        }
        validate(instance=access_return, schema=accessSchema)

    def test_post_info(self):
        post_info_return = post_info_function("172.29.88.59", "8080", "description")
        self.assertRegex(str(post_info_return), "\d", "the response is wrong")

    def test_get_info(self):
        get_info_return = get_info_function("172.29.88.59", "8080")
        info_schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "description": {"type": "string"},
                "documentationUrl": {"type": "string"},
                "environment": {"type": "string"},
                "id": {"type": "string"},
                "name": {"type": "string"},
                "organization": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "url": {"type": "string"},
                    },
                    "required": ["name", "url"],
                },
                "type": {
                    "type": "object",
                    "properties": {
                        "artifact": {"type": "string"},
                        "group": {"type": "string"},
                        "version": {"type": "string"},
                    },
                    "required": ["artifact", "group", "version"],
                },
                "updatedAt": {"type": "string"},
                "version": {"type": "string"},
            },
            "required": [
                "description",
                "documentationUrl",
                "environment",
                "id",
                "name",
                "organization",
                "type",
                "updatedAt",
                "version",
            ],
        }

        validate(instance=get_info_return, schema=info_schema)
    
    def test_delete_access_id(self):
        delete_access_id = delete_access_id_function("172.29.88.59", "8080", "Uu4xZq","P1bu4x")
        self.assertRegex(str(delete_access_id), "\d", "the response is wrong")
    
    

