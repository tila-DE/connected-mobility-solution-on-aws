# -*- coding: utf-8 -*-
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Standard Library
import os

# AWS Libraries
import boto3

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.environ.get("AWS_SESSION_TOKEN")
PROFILE = None

if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN]):
    PROFILE = os.environ.get(
        "AWS_PROFILE",
        input(f"Which AWS profile {boto3.session.Session().available_profiles}: "),
    )

session = boto3.Session(profile_name=PROFILE)
s3 = session.resource("s3")


for bucket in s3.buckets.all():
    if (
        bucket.name.startswith("acdp")
        or bucket.name.startswith("cms-")
        or bucket.name.startswith("backstage")
    ):
        print(bucket.name)
        bucket.object_versions.delete()
        bucket.objects.delete()
        bucket.delete()
