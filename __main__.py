import pulumi
from pulumi_azure_native import resources, containerservice

config = pulumi.Config()

resource_group = resources.ResourceGroup("azure-native-py-aks")