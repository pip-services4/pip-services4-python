#!/usr/bin/env pwsh

Set-StrictMode -Version latest
$ErrorActionPreference = "Stop"

# Get component data and set necessary variables
$component = Get-Content -Path "component.json" | ConvertFrom-Json
$imageName = If ([bool]$component.psobject.Properties["product"] -and $component.product -ne "") `
                {"$($component.product)-$($component.name)"} Else {"$($component.name)"}
$protoImage = "$($component.registry)/$imageName`:$($component.version)-$($component.build)-proto"
$container=$component.name
$packageName=$component.name.replace('-', '_')

# Remove old generate files
if (Test-Path "$PSScriptRoot/$($packageName)/protos") {
    Remove-Item -Path "$PSScriptRoot/$($packageName)/protos/*" -Force -Include *.py -Exclude __init__.py
}

if (Test-Path "$PSScriptRoot/test/protos") {
    Remove-Item -Path "test/protos/*" -Force -Include *.py -Exclude __init__.py
}

# Build docker image
docker build --build-arg PACKAGE_NAME="$($packageName)" -f "$PSScriptRoot/docker/Dockerfile.proto" -t $protoImage $PSScriptRoot

# Create and copy compiled files, then destroy
docker create --name $container $protoImage
docker cp "$($container):/app/$($packageName)/protos" "$PSScriptRoot/$($packageName)/"
# docker cp "$($container):/app/test/protos" "$PSScriptRoot/test/"
docker rm $container

# Verify that protos folder was indeed created after generating proto files
if (-not (Test-Path "$PSScriptRoot/$($packageName)/protos")) {
    Write-Error "protos folder doesn't exist in $($packageName) dir. Build failed. See logs above for more information."
}