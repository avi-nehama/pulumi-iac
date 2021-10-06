import pulumi
from pulumi_azure_native import resources, containerservice, network
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

vnet = network.VirtualNetwork(
    f"avin-vnet",
    location=resource_group.location,
    resource_group_name=resource_group.name,
    address_space={
        "address_prefixes": ["10.0.0.0/16"],
    }
)

subnet = network.Subnet(
    f"avin-subnet",
    resource_group_name=resource_group.name,
    address_prefix="10.0.0.0/24",
    virtual_network_name=vnet.name
)

cluster = containerservice.ManagedCluster("myCluster",
    location=LOCATION,
    resource_group_name=resource_group.name,
    service_principal_profile={
        "client_id": "e2f89c57-2140-4d65-9270-1dfb7663c40d",
        "secret": "lnt2qwe~.fAXWVR5a8hVC5raq6QlBXYTAz"
    },
    agent_pool_profiles=[{
        "name": "type1",
        "mode": "System",
        "count": 2,
        "vm_size": "Standard_B2ms",
        "os_type": containerservice.OSType.LINUX,
        "max_pods": 110,
    }],
    dns_prefix="dns",
   
)
