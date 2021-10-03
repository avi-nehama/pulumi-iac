import pulumi
from pulumi_azure_native import resources, kubernetes

config = pulumi.Config()

resource_group = resources.ResourceGroup("myResourceGroup",
    location="eastus", resource_group_name="zure-native-py-aks")

cluster = kubernetes.ConnectedCluster("connectedCluster",
    cluster_name="testCluster",
    identity=kubernetes.ConnectedClusterIdentityArgs(
        type="SystemAssigned",
    ),
    location="East US",
    resource_group_name="k8sc-rg",
    tags={}
)
