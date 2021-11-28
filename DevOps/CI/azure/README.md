### Azure Container Registry

    az login                                                                --> Login to Azure
    az group create -l <location> -n <rg_name>

    az acr create --name <name> --resource-group <rg_name> --sku Standard   --> Create Azure ACR
    az acr login --name <name>                                              --> Login to Azure ACR        
    docker tag <image_name> <name>.azurecr.io/<repo>/flask                  --> Tag image to Azure ACR
    docker push <name>.azurecr.io/<repo>/flask                              --> Push image to Azure ACR     

    az ad sp create-for-rbac -n <name> --role contributor 
    --scopes /subscriptions/<subscription_id> --sdk-auth                    --> Create Service Principal