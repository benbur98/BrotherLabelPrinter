# Brother Printer API

## Config

The Configuration is managed by Environment Variables.

| EnvVar        | Description                          | Required | Options                                          |
|---------------|--------------------------------------|----------|--------------------------------------------------|
| BACKEND       | Backend Type for Printer Connection  | True     | usb, bluetooth, wifi                             |
| PRINTER       | Printer Model                        | True     | PTP_700, PTP_750W, PTP_H500, PTP_E500, PTP_E550W |
| MEDIA         | Printer Media (Tape) Inserted        | False    | W3_5, W6, W9, W12, W18, W24                      |
| FONT          | Truetype Font Path to use by Default | False    |                                                  |

## API

`fastapi run` - Starts the FastAPI server

## Endpoints

### Print

`POST /print`

#### Request Body:

```json
{
  "text": "Hello World",
  "height": 50,
  "font": "font.ttf",
  "padding": {
    "top": 0,
    "right": 0,
    "bottom": 0,
    "left": 0
  }
}
```
