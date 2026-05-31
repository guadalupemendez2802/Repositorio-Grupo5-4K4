from db import obtener_conexion
def data():
    con = obtener_conexion()
    cursor = con.cursor()

    cursor.execute("""
    INSERT INTO TipoPase
    (nombre, descripcion, precio)
    VALUES
    ('REGULAR','Pase Regular',10000)
    """)

    cursor.execute("""
    INSERT INTO TipoPase
    (nombre, descripcion, precio)
    VALUES
    ('VIP','Pase VIP',20000)
    """)

# Ejecutar esto cambiando el precio en base a lo que nos conteste el PO (para ya tenerlo en la base de datos) - Alan G.
# Esto se ejecuta con python src/database/init_db.py 