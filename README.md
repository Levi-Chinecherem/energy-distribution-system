# Energy Distribution Management System


The **Energy Distribution Management System** is a digitalized system designed to efficiently manage energy distribution, including data processing, information storage, and decision-making support. It provides a comprehensive solution for tracking energy products, consumer data, and generating reports and insights.

![Energy Consumption by Product](https://your-image-hosting-url.com/energy_report.png)

![Monthly Consumption Trends](https://your-image-hosting-url.com/monthly_consumption.png)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Data Management**: The system handles data for energy products, consumer information, and energy consumption.
- **Reports and Insights**: Generate various reports, including energy consumption by product, monthly consumption trends, and more.
- **User Authentication**: Secure user authentication and authorization for system access.
- **Database Integration**: Utilizes a SQLite database to store data efficiently.
- **Web Interface**: A web-based user interface for easy interaction and data visualization.
- **Monthly Consumption Analysis**: Charts showing monthly energy consumption trends.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python 3.6 or higher installed.
- **Django**: Install Django using `pip install Django`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Levi-Chinecherem/energy-distribution-system.git
   ```
2. Navigate to the project directory:

   ```bash
   cd energy-distribution-system
   ```
3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
7. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```
8. Run the development server:

   ```bash
   python manage.py runserver
   ```
9. Access the system in your web browser at `http://localhost:8000`.

## Configuration

- **Database**: By default, the system uses SQLite as the database. You can change this in the project's settings.
- **Static Files**: Ensure that your static files are properly configured in `settings.py` to serve CSS, JavaScript, and images.
- **Additional Configuration**: Customize the system further by editing `settings.py` and `urls.py`.

## Usage

1. Log in with the superuser account created during installation.
2. Use the system to manage energy products, consumer data, and energy consumption records.
3. Explore the available reports, including energy consumption by product and monthly consumption trends.

## Customization

The system can be customized and extended in various ways:

- **Additional Features**: You can add more features, such as data validation, export functionality, or user roles.
- **Styling**: Customize the appearance by modifying the CSS stylesheets.
- **Database**: Replace the default SQLite database with a more robust database system, if needed.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please follow the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
