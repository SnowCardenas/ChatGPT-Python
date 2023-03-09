import openai 
import config 
import typer
from rich import print
from rich.table import Table

def main(): 

    openai.api_key = config.api_key 

    print("[b yellow1]ChatGPT API en Python[/b yellow1] [blue1]By:[blue1] [b red1]SnowCardenas[/b red1] ⛄")

    table = Table("Comando", "Descipción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

# Contexto del Asistente
    context= {"role": "system", "content": "Eres un asistente muy útil."}
    messages=[context] 

    while True:

        content = __prompt()

        if content == "new":
             print("⭐ Nueva Conversación Creada ⭐")
             messages=[context]
             content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content}) 

        print(f"[b green1] > [/b green1] [green1]{response_content}[/green1]")

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre que quieres hablar?")

    if prompt == "exit":
        exit = typer.confirm("🚨 ¿Estas seguro de Salir? 🚨")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()
        return __prompt()
    
    return prompt

if __name__ == "__main__": 
        typer.run(main)