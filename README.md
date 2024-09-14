# Parcel Management System

A Django-based parcel management system that tracks and manages parcels from reception to delivery.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)


## Installation

### Prerequisites
- Python 3.x
- pip
- Django

### Steps

1. **Clone the repositor**
   ```bash
   git clone https://github.com/username/parcel-management-system.git
2. **Navigate to the project directory**
   cd parcel-management-system
3.**Create and activate a virtual environment**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4.**Install dependencies**
   pip install -r requirements.txt
5.**Apply migrations**
   python manage.py migrate
6.**Create a superuser**
   python manage.py createsuperuser
7.**Run the development server**
   python manage.py runserver
   
### Usage

**Accessing the Application**
  Navigate to http://127.0.0.1:8000/login in your browser.
  
**Admin Interface**
  Access the admin interface at http://127.0.0.1:8000/admin/.

**Key Features**
  Create Parcels
  Track Parcels
  Update Parcel status
  Generate reports

**Login and Navigation Instructions**

**Login**:

Log in using the super-admin credentials created.
Upon successful login, you will be redirected to the Order Details page, where detailed information about the order will be displayed on the side.

**Create Order**:

To create a new order, click on the "Create Parcel" option in the navbar.
After creating the order, you will be redirected to the Order Details page where you can view the details of the newly created order.

**Update Order Status**:

On the Order Details page, you can update the status of an order by clicking the relevant button associated with the order.

**Search Orders**:

The Order Details page includes a search functionality that allows you to find orders by name or by the order tracking number.

**View Reports**:

To view all orders, navigate to the "Report" page by clicking on the "Report" option in the navbar.

**Update Report Details**:

On the Report page, you can update the details of a report by clicking on the three dots in the "Action" column of the report.

**Download Report**:

You can download the report as an Excel file by clicking on the provided button on the Report page.

 
  


