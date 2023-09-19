import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
import requests


# Obtenção dos dados meteorológicos:
def Recebe_Dados(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data


# Função para exibir os dados meteorológicos na janela
def display_weather_in_gui(data):
    if data["cod"] != "404":
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        termic_sense = data["main"]["feels_like"]
        t_min = data["main"]["temp_min"]
        t_max = data["main"]["temp_max"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Traduzindo o campo desccrição para o português
        description_pt = translator.translate(description, src="en", dest="pt").text

        # Atualize o rótulo de saída com os dados traduzidos
        output_label.config(
            text=f"Clima em {city}, {country}:\n"
            f"Temperatura: {temperature}°C\n"
            f"Sensação térmica: {termic_sense}°C\n"
            f"Temperatura mínima: {t_min}°C\n"
            f"Temperatura máxima: {t_max}°C\n"
            f"Descrição: {description_pt}\n"
            f"Umidade: {humidity}%\n"
            f"Velocidade do Vento: {wind_speed} km/h"
        )
    else:
        messagebox.showerror(
            "Erro", "Cidade não encontrada. Por favor, tente novamente."
        )


# Função para obter os dados meteorológicos e exibi-los na janela
def get_and_display_weather():
    city = city_entry.get()

    if not city:
        messagebox.showerror("Erro", "Por favor, insira o nome da cidade.")
        return

    try:
        # Obtenha os dados meteorológicos usando a função interna
        weather_data = Recebe_Dados(api_key, city)

        # Exiba os dados traduzidos na janela
        display_weather_in_gui(weather_data)
    except Exception as e:
        messagebox.showerror(
            "Erro", f"Ocorreu um erro ao buscar dados meteorológicos: {str(e)}"
        )


# Configuração inicial
api_key = "9e40882d49c9fbd3c949c345aa42701f"
translator = Translator()

# Configuração da janela
window = tk.Tk()
window.title("Previsão do Tempo")
window.geometry("400x300")
window.iconbitmap(
    "D:\Pablinho & Nanda\Documents\Programação\Previsão do tempo\icon_previsao.ico"
)
# Rótulo e entrada para o nome da cidade
city_label = tk.Label(window, text="Digite o nome da cidade:")
city_label.pack(pady=10)
city_entry = tk.Entry(window)
city_entry.pack()

# Botão para obter os dados meteorológicos
get_weather_button = tk.Button(
    window, text="Obter Previsão", command=get_and_display_weather
)
get_weather_button.pack()

# Rótulo para exibir os dados meteorológicos
output_label = tk.Label(window, text="")
output_label.pack(pady=10)

# Inicie a interface gráfica
window.mainloop()
