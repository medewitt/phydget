
pkgreadme := 'phydget/README.md'
basereadme := 'README.md'

# List available recipes
default:
    just --list

# Compile python package
compile: updatereadme
    bash build.sh

# Update README
updatereadme:
    cp {{basereadme}} {{pkgreadme}}

cleanup:
    rm -rf phydget/dist;
    rm -rf phydget/PhyDGET.egg-info