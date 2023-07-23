# Hill Cipher Implementation in Python

![Hill Cipher](hill_cipher.jpg)

## Introduction

This repository contains a Python implementation of the **Hill Cipher** algorithm, a classical encryption technique used to secure messages. The Hill Cipher was developed by mathematician Lester S. Hill in 1929 and is a polygraphic substitution cipher based on linear algebra concepts.

## How the Hill Cipher Works

The Hill Cipher operates on blocks of plaintext letters and uses matrix multiplication for encryption and decryption. It employs an n x n matrix as the encryption key, where n is the dimension of the matrix. The encryption process involves dividing the plaintext into groups of n letters and converting each group into a numerical representation (A=0, B=1, ..., Z=25). Then, the matrix key is applied to each group of numbers to produce the encrypted ciphertext. Decryption is achieved by multiplying the ciphertext with the inverse of the matrix key.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/umar-bunu/hill-cipher-in-python
