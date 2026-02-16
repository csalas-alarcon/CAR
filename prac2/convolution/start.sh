#!/bin/bash
set -e

echo "Creating data directory..."
mkdir -p imgs
cd imgs

echo "Downloading Oxford Flowers dataset..."
curl -L -o flowers.tgz https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz

echo "Extracting dataset..."
tar -xzf flowers.tgz

echo "Cleaning up..."
rm flowers.tgz

cd ..
echo "Dataset ready in imgs/jpg/"
