

from datetime import datetime

class Carro:

    def __init__(self, marca, modelo, num_de_asientos, color, tipo, precio, años_de_garantia, fecha):
        self.marca = marca
        self.modelo = modelo
        self.num_de_asientos = num_de_asientos
        self.color = color
        self.tipo = tipo
        self.precio = precio
        self.años_de_garantia = años_de_garantia
        self.fecha = fecha

    def info_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Asientos: {self.num_de_asientos}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio: ${self.precio}")
        print(f"Garantía: {self.años_de_garantia} años")
        print(f"Fecha: {self.fecha.strftime('%d-%B-%Y')}")
        print()

# Crear instancias de la clase Carro para diferentes marcas
mitsubishi = Carro("Mitsubishi", "Outlander", 7, "Gris", "SUV", 30000, 5, datetime(2023, 1, 1))
nissan = Carro("Nissan", "Altima", 5, "Negro", "Sedán", 28000, 4, datetime(2022, 8, 20))
kia = Carro("Kia", "Sportage", 5, "Blanco", "SUV", 26000, 3, datetime(2023, 2, 10))
toyota = Carro("Toyota", "Rav4", 5, "Plateado", "SUV", 32000, 6, datetime(2022, 6, 5))
hyundai = Carro("Hyundai", "Elantra", 5, "Azul", "Sedán", 24000, 5, datetime(2022, 12, 15))

# Obtener información de los carros
mitsubishi.info_carro()
nissan.info_carro()
kia.info_carro()
toyota.info_carro()
hyundai.info_carro()