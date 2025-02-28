# Experimentos del projecto CP de la semana 6 y 7

This project the **compras** service.

## Project Structure

```
compras
├── src
│   ├── domain
│   │   ├── models.py
│   │   └── repositories.py
│   ├── infrastructure
│   │   ├── database.py
│   │   └── repositories_impl.py
│   └── service
│       ├── __init__.py
│       └── compras_service.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone <repository-url>
   cd experimentos
   ```

2. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   uvicorn main:app --reload
   ```

## Usage

- Access the API at `http://localhost:5001`.
- The following endpoints are available:
  - **Bodega Module**: Interact with the bodega-related functionalities.
  - **Ventas Module**: Access sales-related operations.
  - **Compras Module**: Manage purchase-related tasks.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
