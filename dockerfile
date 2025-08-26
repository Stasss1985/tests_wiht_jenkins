# Используем официальный образ Python с явным указанием версии
FROM python:3.11-bookworm

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Установка Google Chrome через прямой .deb пакет (обход проблем с репозиторием)
RUN curl -L -o chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y --no-install-recommends ./chrome.deb \
    # Установка зависимостей Chrome
    libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 \
    libxtst6 libnss3 libcups2 libxss1 libxrandr2 libasound2 \
    libatk1.0-0 libatk-bridge2.0-0 libpangocairo-1.0-0 libgtk-3-0 \
    && rm chrome.deb && \
    rm -rf /var/lib/apt/lists/*

# Установка Java
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    openjdk-17-jre \
    && rm -rf /var/lib/apt/lists/*

# Установка Allure
RUN curl -L -o allure-2.30.0.tgz https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz && \
    tar -zxvf allure-2.30.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure && \
    rm allure-2.30.0.tgz

# Проверка установки
RUN google-chrome --version && \
    java --version && \
    allure --version