# Usa a imagem base Ubuntu 24.04
FROM ubuntu:24.04

# Evita prompts interativos durante instalações
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza pacotes e instala utilitários básicos
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    curl \
    wget \
    git \
    vim \
    bash \
    ca-certificates \
    python3.12 \
    python3-pip \
    python3-dev \
    build-essential \
    gfortran \
    libatlas-base-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala pacotes Python necessários
RUN python3.12 -m pip install --no-cache-dir --break-system-packages\
    pandas \
    scikit-learn \
    jupyter


# Define o diretório de trabalho & faz cópia
WORKDIR /app
COPY . /app


CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]