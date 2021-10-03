import pulumi
from pulumi_azure_native import resources, containerservice
import pulumi_azuread as azuread

config = pulumi.Config()

RESOURCE_GROUP_NAME = "dev-RG" 
CLUSTER_NAME        = "dev-k8s-cluster"
PUBLIC_KEY_CERT     = "agent_public_key_certificate"
LOCATION            = "eastus"

resource_group = resources.ResourceGroup(RESOURCE_GROUP_NAME,
    location=LOCATION, resource_group_name = RESOURCE_GROUP_NAME)

# Create Azure AD Application for AKS
# app = azuread.Application(
#     "dev-aks-app",
#     display_name="dev-aks-app"
# )

cluster = containerservice.ManagedCluster("myCluster",
    location=LOCATION,
    resource_group_name=RESOURCE_GROUP_NAME
)
