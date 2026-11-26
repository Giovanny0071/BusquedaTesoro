# Búsqueda del tesoro

Juego de consola en Python. El jugador inicia sesión, elige una dificultad e introduce coordenadas para encontrar un diamante oculto. El administrador puede consultar el historial de las partidas finalizadas, las estadísticas de la sesión y los gráficos.

## Instalación

Necesitas Python 3.10 o posterior. Descarga el proyecto o clona el repositorio desde GitHub:

```bash
git clone https://github.com/Giovanny0071/BusquedaTesoro.git
cd BusquedaTesoro
```

Si vas a ejecutar la versión de desarrollo, cambia a la rama `Dev`:

```bash
git switch Dev
```

Instala Matplotlib, la biblioteca que utiliza el programa para mostrar los gráficos:

```bash
python -m pip install matplotlib
```

En Windows, si `python` no se reconoce, usa `py` en los comandos.

## Configuración

Crea o edita `usuarios.txt` en la misma carpeta que `main.py`. Cada línea contiene el nombre, la contraseña y el rol, separados por punto y coma. Usa una línea por cuenta y deja el fichero sin encabezado.

Estas cuentas sirven para probar ambos perfiles:

```text
ana;AnaPrueba23;Usuario
admin;AdminPrueba59;Administrador
```

Escribe `Usuario` con mayúscula inicial para las cuentas de jugador.

## Ejecución

Abre una terminal en la carpeta que contiene `main.py` y ejecuta:

```bash
python main.py
```

Selecciona **Iniciar sesión** e introduce una cuenta de `usuarios.txt`. Para jugar, elige una dificultad y un máximo de intentos.

| Dificultad | Tamaño del tablero |
| --- | --- |
| Fácil | 5 × 5 |
| Normal | 8 × 8 |
| Difícil | 10 × 10 |

Las coordenadas empiezan en `0`. Por ejemplo, en el tablero fácil, las filas y columnas van del `0` al `4`. Tras cuatro intentos fallidos, el juego ofrece una pista de cercanía.

## Historial, estadísticas y registro

Desde el menú de administrador puedes consultar el historial y abrir las estadísticas con sus gráficos. Las partidas y las estadísticas se guardan en memoria durante la ejecución y se reinician al volver a arrancar el programa.

Los eventos se guardan en `registro.log`, en la carpeta desde la que ejecutas el programa.
