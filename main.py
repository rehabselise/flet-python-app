import flet as ft

def main(page: ft.Page):
    """Main Flet application entry point"""
    page.title = "My Flet App"
    page.window.width = 400
    page.window.height = 600
    
    # Create UI components
    title = ft.Text("Welcome to Flet!", size=24, weight="bold")
    
    input_field = ft.TextField(
        label="Enter text",
        width=300
    )
    
    result_text = ft.Text("", size=16)
    
    def on_click(e):
        """Handle button click"""
        if input_field.value:
            result_text.value = f"You entered: {input_field.value}"
        else:
            result_text.value = "Please enter some text!"
        page.update()
    
    submit_btn = ft.ElevatedButton(
        text="Submit",
        on_click=on_click,
        width=100
    )
    
    # Add components to the page
    page.add(
        title,
        ft.Divider(),
        input_field,
        submit_btn,
        result_text
    )

if __name__ == "__main__":
    ft.app(target=main)
