# Smart Weather Station

A comprehensive environmental monitoring system built on Raspberry Pi that collects, stores, and visualizes real-time weather and air quality data.

## Overview

This project implements a complete IoT solution for environmental monitoring. The Smart Weather Station captures temperature, humidity, pressure, and air quality metrics, stores them in a database, and makes them accessible through a responsive web interface and API.

## Features

- **Real-time Environmental Monitoring**
  - Temperature, humidity, and barometric pressure monitoring (GY-BME280)
  - Air quality measurement (MQ135 sensor for CO2, NH3, NOx)
  - Day/night cycle detection using Light Dependent Resistor (LDR)
  - Real-time clock (RTC) support for reliable timestamps

- **Data Management**
  - Local data storage using SQLite database
  - Time-stamped entries for historical data analysis

- **Visualization & Remote Access**
  - Interactive charts and graphs for data visualization
  - Responsive web interface built with MudBlazor
  - API for data access
  - Secure HTTPS access through Nginx and Let's Encrypt

- **Alerts & Notifications**
  - Automated alerts for poor air quality conditions
  - Configurable threshold alerts for temperature and humidity extremes

## Technology Stack

### Hardware Components
- Raspberry Pi (central controller)
- GY-BME280 sensor (temperature, humidity, pressure)
- MQ135 sensor (air quality)
- LDR (light detection)
- RTC module (optional, for offline time tracking)

### Software & Technologies
- **Backend**
  - Python (sensor data collection)
  - C# (API and application logic)
  - SQLite (data storage)
  - Raspbian OS (operating system)

- **Frontend**
  - MudBlazor (UI component library)
  - HTML/CSS3 (web interface styling)

- **Infrastructure**
  - Nginx (reverse proxy)
  - Let's Encrypt (SSL certificates)
