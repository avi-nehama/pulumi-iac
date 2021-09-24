import pulumi
from pulumi_azure_native import resources, containerservice

resource_group = resources.ResourceGroup("azure-native-py-aks")