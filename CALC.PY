import flet as ft 

def build(page : ft.Page):
        result = ft.Text("0",size=20)
        def button_click(e):
                if e.control.text == 'C':
                    result.value = ""
                    result.update()
                elif result.value == '0':
                    result.value = e.control.text
                    result.update()
                elif e.control.text == '=':
                    try:
                        result.value = str(eval(result.value))
                        result.update()
                    except:
                        result.value = "Error"
                        result.update()
                elif e.control.text == '+/-':
                    result.value = f"-{result.value}"
                    result.update()
                elif e.control.text == '()':
                    result.value = f"({result.value})"
                    result.update()
                else:
                    result.value += e.control.text
                    result.update()
        page.add(
        ft.Container(
            width=1000,
            bgcolor="black",
            border_radius=ft.border_radius.all(20),
            padding=20,
            content= ft.Column(
                controls=[
                ft.Row(controls= [result],alignment="end"),
                ft.Row(controls=[
                    ft.IconButton(icon=ft.icons.HISTORY,icon_color="Grey",expand=1,),
                    ft.IconButton(icon=ft.icons.LINEAR_SCALE,icon_color="Grey",expand=1),
                    ft.IconButton(icon=ft.icons.CALCULATE,icon_color="Grey",expand=1),
                    ]),
                    ft.Row(controls=[
                    ft.ElevatedButton(text="C",color="Red",bgcolor="DarkGrey",expand=1,on_click=button_click),
                    ft.ElevatedButton(text="()",color="Green",bgcolor="DarkGrey",expand=1,on_click=button_click),
                    ft.ElevatedButton(text="%",color="Green",bgcolor="DarkGrey",expand=1,on_click=button_click),
                    ft.ElevatedButton(text="/",color="Green",bgcolor="DarkGrey",expand=1,on_click=button_click),
                    ]),
                    ft.Row(controls=[
                        ft.ElevatedButton(text="7",color="white",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="8",color="white",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="9",color="white",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="*",color="Green",bgcolor="DarkGrey",expand=1,on_click=button_click),
                    ]),
                    ft.Row(controls=[
                        ft.ElevatedButton(text="4",color="white",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="5",color="white",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="6",color="white",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="-",color="Green",bgcolor="DarkGrey",expand=1,on_click=button_click)
                        ]),
                    ft.Row(controls=[
                        ft.ElevatedButton(text="1",color="white",bgcolor="black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="2",color="white",bgcolor="black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="3",color="White",bgcolor="Black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="+",color="Green",bgcolor="DarkGrey",expand=1,on_click=button_click)
                    ]),
                    ft.Row(controls=[
                        ft.ElevatedButton(text="+/-",color="white",bgcolor="black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="0",color="white",bgcolor="black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text=".",color="white",bgcolor="black",expand=1,on_click=button_click),
                        ft.ElevatedButton(text="=",color="white",bgcolor="Green",expand=1,on_click=button_click)
                    ])
                    ]
                )
        )
    )
    
ft.app(target=build)

