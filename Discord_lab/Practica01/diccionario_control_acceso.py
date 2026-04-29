class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")
            return None

    def agregar_usuario(self, nueva_matricula, rol):
        if nueva_matricula in self.usuarios_autorizados:
            print("> El usuario ya existe.")
        else:
            self.usuarios_autorizados[nueva_matricula] = rol
            print("> Usuario agregado correctamente.")


def main():
    sistema = ControlAcceso()

    print("--- Sistema de Seguridad Laboratorio IA - UX ---")

    while True:
        try:
            matricula = input("\nIngrese su matrícula: ").strip()

            if not matricula:
                raise ValueError("El campo de matrícula no puede estar vacío.")

            rol = sistema.verificar_permisos(matricula)

            if rol == "Administrador":
                opcion = input("¿Desea agregar un nuevo usuario? (s/n): ").lower()

                if opcion == "s":
                    nueva_matricula = input("Ingrese la nueva matrícula: ").strip()
                    nuevo_rol = input("Ingrese el rol (Investigador/Estudiante): ").strip()

                    if not nueva_matricula or not nuevo_rol:
                        raise ValueError("Datos inválidos para el nuevo usuario.")

                    sistema.agregar_usuario(nueva_matricula, nuevo_rol)

        except ValueError as e:
            print(f"> Error: {e}")

        except Exception as e:
            print(f"> Error inesperado: {e}")

        finally:
            print("--- Intento de acceso registrado en el log del servidor ---")

if __name__ == "__main__":
    main()