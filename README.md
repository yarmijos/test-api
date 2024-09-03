# test-api

# Inicia el proyecto
1. git clone https://github.com/yarmijos/test-api.git
2. pip install -r requirements.txt
3. python api-test.py

# realizar pruebas en postman
1. En la barra url de postman coloca lo siguiente: http://127.0.0.1:5000/get-subarreglo
2. En el header añade Content-Type: application/json
3. En el body selecciona la opcion raw
4. Copia el siguiente JSON
   {
      "array": [-2, -2, -2, -3, -4, -1, -1],
      "target":-5
   }

5. Debes recibir una respuesta como:
    "subarray": [-2,-3]



