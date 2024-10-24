terraform {
  required_version = ">= 1.5.7"
  backend "azurerm" {
    resource_group_name  = "rg1plopez-lab01"
    storage_account_name = "sta1plopez"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
 
provider "azurerm" {
  features {}
}

module "terraform_azure_workload" {
  source = "github.com/ploopez/terraform-weekly-exercise-ploopez/soluciones/modulo-weekly-exercise"

  resource_group_name = var.resource_group_name
  vnet_name           = var.vnet_name
  vnet_address_space  = var.vnet_address_space
  location            = var.location

  subnets             = var.subnets
  network_interface   = var.network_interface
  linux_virtual_machine = var.linux_virtual_machine
  load_balancer       = var.load_balancer
}


