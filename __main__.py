import pulumi
from pulumi_azure_native import resources, containerservice

config = pulumi.Config()

resource_group = resources.ResourceGroup(location="eastus", resource_group_name="zure-native-py-aks")