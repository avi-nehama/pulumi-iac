import pulumi
from pulumi_azure_native import resources, kubernetes

config = pulumi.Config()

RESOURCE_GROUP_NAME = "dev-RG" 
CLUSTER_NAME        = "dev-k8s-cluster"
PUBLIC_KEY_CERT     = "agent_public_key_certificate"
LOCATION            = "eastus"

resource_group = resources.ResourceGroup("",
    location=LOCATION, resource_group_name = RESOURCE_GROUP_NAME)

cluster = kubernetes.ConnectedCluster("connectedCluster",
    cluster_name=CLUSTER_NAME,
    agent_public_key_certificate=PUBLIC_KEY_CERT,
    identity=kubernetes.ConnectedClusterIdentityArgs(
        type="SystemAssigned",
    ),
    location=LOCATION,
    resource_group_name=RESOURCE_GROUP_NAME,
    tags={}
)
