#!/usr/bin/env pwsh

Set-StrictMode -Version latest
$ErrorActionPreference = "Stop"

# Get component metadata and set necessary variables
$component = Get-Content -Path "$PSScriptRoot/component.json" | ConvertFrom-Json
$rcImage = "$($component.registry)/$($component.name):$($component.version)-$($component.build)"
$container = $component.name

# Remove build files
if (Test-Path -Path "$PSScriptRoot/dist") {
    Remove-Item -Recurse -Force -Path "$PSScriptRoot/dist"
}

# Build docker image
docker build -f "$PSScriptRoot/docker/Dockerfile" -t $rcImage $PSScriptRoot

# Create and copy compiled files, then destroy
docker create --name $container $rcImage
docker cp "$($container):/app/dist" "$PSScriptRoot/dist"
docker rm $container

# Verify that obj folder was indeed created after build
if (-not (Test-Path -Path "$PSScriptRoot/dist")) {
    Write-Error "obj folder doesn't exist in root dir. Build failed. See logs above for more information."
}
