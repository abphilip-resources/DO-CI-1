param([string]$subID = '')

az ad sp create-for-rbac --name "githubActions" --role contributor `
                         --scopes /subscriptions/$subID --sdk-auth