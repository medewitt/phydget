
pkgreadme := 'phydget/README.md'
basereadme := 'README.md'

pkgprogram := 'phydget/phydget/phydget.py'
baseprogram := 'phydget.py'

# List available recipes
default:
    just --list

# Compile python package
compile: updatereadme
    bash build.sh

# Update README
updatereadme:
    cp {{basereadme}} {{pkgreadme}}

# Update Program
updateprogram:
    cp {{baseprogram}} {{pkgprogram}}

# Clean up package
cleanup:
    rm -rf phydget/dist;
    rm -rf phydget/PhyDGET.egg-info