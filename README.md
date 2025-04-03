## 🛒 Django DRF eCommerce API

A simple e-commerce platform built with Django.

## Features
User authentication (register, login, logout)

Product management with categories and images

Shopping cart management

Admin panel for managing products


### 📌 Project Overview  
This is a RESTful API for an eCommerce platform built with Django Rest Framework (DRF).
 It provides user authentication, product management, and cart functionality.  
 Users can browse products and add them to their cart.
 Admins can manage products and categories
---

## 🚀 Tech Stack  
- **Backend:** Django, Django Rest Framework (DRF)  
- **Database:** SQLite  

---------------------------------------------------------------------------------

## ⚙️ Installation & Setup  

### Prerequisites  
- Python (>= 3.13.1)  
- Django (>= 5.1.6)  
- Virtual environment tool (e.g., `venv` or `pipenv`)  

### Steps to Set Up Locally  

1. **Clone the repository:**  
   ```
   git clone https://github.com/Ahmedhassan1990ali/Capstone-project.git
   ```

2. **Create and activate a virtual environment:**  
   ```
   python -m venv venv  
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**  
   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**  
   ```
   python manage.py migrate
   ```

5. **Create a superuser (optional):**  
   ```
   python manage.py createsuperuser
   ```

6. **Run the server:**  
   ```
   python manage.py runserver
   ```

---------------------------------------------------------------------------------

## 🔐 Authentication & Security  

- The API uses **TokenAuthentication** for user authentication.  
- Obtain a token by sending a POST request to `/api/users/register/` or `/api/users/login/`
- Include the token in the `Authorization` header for protected endpoints:  
  ```
  Authorization: Token your_token_here
  ```

---------------------------------------------------------------------------------

## 📌 API Endpoints  

### **User Authentication**  
| Method | Endpoint               | Description                                         |
|--------|------------------------|-----------------------------------------------------|
| POST   | `/api/users/register/` | Register a new user and obtain authentication token |
| POST   | `/api/users/login/`    | Login and obtain authentication token               |
| GET    | `/api/users/profile/`  | Retrieve user profile                               |
| PATCH  | `/api/users/profile/`  | Update user profile                                |
| POST   | `/api/users/logout/`   | Logout and delete authentication token              |

### **Products**  
| Method | Endpoint                          | Description                              |
|--------|-----------------------------------|------------------------------------------|
| GET    | `/api/products/products/`         | List all products                        |
| POST   | `/api/products/products/`         | Add new product (Admins only)            |
| GET    | `/api/products/products/<id>/`    | Retrieve a product                       |
| PUT    | `/api/products/products/<id>/`    | Update a product (Admins only)           |
| PATCH  | `/api/products/products/<id>/`    | Partialy update a product (Admins only)  |
| DELETE | `/api/products/products/<id>/`    | Delete a product (Admins only)          |

| GET    | `/api/products/categories/`       | List all categories                      |
| POST   | `/api/products/categories/`       | Add new category (Admins only)           |
| GET    | `/api/products/categories/<id>/`  | Retrieve a category                      |
| PUT    | `/api/products/categories/<id>/`  | Update a category (Admins only)          |
| PATCH  | `/api/products/categories/<id>/`  | Partialy update a category (Admins only) |
| DELETE | `/api/products/categories/<id>/`  | Delete a category (Admins only)         |

### **Carts**  
| Method | Endpoint                          | Description                                      |
|--------|-----------------------------------|--------------------------------------------------|
| GET    | `/api/carts/user/carts/`          | View current user's carts                        |
| POST   | `/api/carts/user/carts/`          | Add new current user's cart                      |
| GET    | `/api/carts/user/carts/<id>/`     | Retrieve a specific cart for the user            |
| PUT    | `/api/carts/user/carts/<id>/`     | Update a specific cart for the user              |
| PATCH  | `/api/carts/user/carts/<id>/`     | Partialy update a specific cart for the user     |
| DELETE | `/api/carts/user/carts/<id>/`     | Delete a specific cart for the user              |

| GET    | `/api/carts/user/cartitems/`      | View cart items of the user                      |
| POST   | `/api/carts/user/cartitems/`      | Add new cart item of the user                    |
| GET    | `/api/carts/user/cartitems/<id>/` | Retrieve a specific cart item for the user       |
| PUT    | `/api/carts/user/cartitems/<id>/` | Update a specific cart item for the user         |
| PATCH  | `/api/carts/user/cartitems/<id>/` | Partialy update a specific cart item for the user|
| DELETE | `/api/carts/user/cartitems/<id>/` | Delete a specific cart item for the user         |

| GET    | `/api/carts/admin/carts/`         | View all carts (admin)                           |
| GET    | `/api/carts/admin/carts/<id>/`    | Retrieve a specific cart (admin)                 |
| GET    | `/api/carts/admin/cartitems/`     | View all cart items (admin)                      |
| GET    | `/api/carts/admin/cartitems/<id>/`| Retrieve a specific cart item (admin)            |


---------------------------------------------------------------------------------

## 📞 Contact  
For support, contact:  
💎 Email: drahmedhassan.1990@gmail.com 
🐙 GitHub: [Ahmedhassan1990ali](https://github.com/Ahmedhassan1990ali)  
