# -*- coding: utf-8 -*-
# ---------------------------
# IMPORTACIÓN DE MÓDULOS
# ---------------------------
import json

# ---------------------------
# CLASES DE DATOS
# ---------------------------

# Clase para la información de medios de contacto
class Media:
    def __init__(self, email, cv, github, likedin):
        self.email = email
        self.cv = cv
        self.github = github
        self.likedin = likedin

# Clase para representar una tecnología con su nombre e ícono
class Technology:
    def __init__(self, name: str, icon: str):
        self.name = name
        self.icon = icon

    def __str__(self):
        return self.name  # Representación en cadena del nombre de la tecnología

# Clase para representar una entrada de experiencia, proyecto o formación
class Info:
    def __init__(self, icon, title, subtitle, description, date="", certificate="", technologies=[], image="", url="", github=""):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.technologies = [Technology(**tech) for tech in technologies]
        self.image = image
        self.url = url
        self.github = github

# Clase para representar recursos o enlaces adicionales (extras)
class Extra:
    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.url = url

# ---------------------------
# CLASE PRINCIPAL DE DATOS
# ---------------------------

# Clase principal que agrupa toda la información del portafolio
class Data:
    def __init__(
        self,
            title,
            description,
            image,
            avatar,
            name,
            skill,
            location,
            media,
            about,
            technologies,
            experience,
            projects,
            training,
            certification,
            extras
    ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.location = location
        self.media = Media(**media)
        self.about = about if isinstance(about, list) else about.split("\n\n")#Separa párrafos dobles
        self.technologies = [Technology(**tech) for tech in technologies]
        self.experience = [Info(**info) for info in experience]
        self.projects = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.certification = [Info(**info) for info in certification] #Modificacion
        self.extras = [Extra(**info) for info in extras]

# ---------------------------
# CARGA DE DATOS DESDE JSON
# ---------------------------

# Se abre el archivo JSON que contiene los datos del portafolio
with open("assets/data/data.json", encoding="utf-8") as file: # Se especifica codificación UTF-8
    json_data = json.load(file)

# Se instancia el objeto `Data` con la información cargada
data = Data(**json_data)
